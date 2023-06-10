# NVDA Event Tracker/Investigator
# Copyright 2017-2023 Joseph Lee, Thiago Seus, 2023 Luke Davis and Open Source Systems, Ltd., all rights reserved.
# Released under GPL V2.

from comtypes import COMError
from collections import deque
from typing import Optional, List

from gui.dpiScalingHelper import DpiScalingHelperMixinWithoutInit
import gui
import globalPluginHandler
import globalVars
from logHandler import log
from NVDAObjects.IAccessible import IAccessible
from NVDAObjects.UIA import UIA
import NVDAObjects
from scriptHandler import script
import wx


# Security: disable the global plugin altogether in secure mode.
def disableInSecureMode(cls):
	return globalPluginHandler.GlobalPlugin if globalVars.appArgs.secure else cls


class Event(object):

	def __init__(self, type: str, info: List[str]) -> None:
		self.type = type
		self.info = info


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self, *args, **kw):
		super().__init__(*args, **kw)
		self.eventHistory = deque([], 100)

	# Record info about events and objects.
	def evtDebugLogging(
			self,
			obj: NVDAObjects.NVDAObject,
			event: Optional[str] = None,
			additionalInfo: Optional[str] = None
	) -> None:
		info: List[str] = [f"object: {repr(obj)}"]
		info.append(f"name: {obj.name}")
		# Use a friendly name for role (credit: NV Access).
		info.append("role: %s" % obj.role)
		if not event:
			event = "no event specified"
		info.append(f"event: {event}")
		if event == "valueChange":
			info.append(f"value: {obj.value}")
		elif event == "stateChange":
			# Parts copied from NVDA Core's default navigator object dev info's state retriever (credit: NV Access).
			try:
				ret = ", ".join(str(state) for state in obj.states)
			except Exception as e:
				ret = "exception: %s" % e
			info.append("states: %s" % ret)
		info.append(f"app module: {obj.appModule}")
		# Some objects do not define window class name such as secure desktop object.
		try:
			ret = obj.windowClassName
		except Exception as e:
			ret = "exception: %s" % e
		info.append("window class name: %s" % ret)
		if isinstance(obj, IAccessible):
			# Bulk comes from dev info for IAccessible object (credit: NV Access).
			IAccessibleObject = obj.IAccessibleObject
			childID = obj.IAccessibleChildID
			try:
				ret = obj._formatLongDevInfoString(IAccessibleObject.accName(childID))
			except Exception as e:
				ret = "exception: %s" % e
			info.append("IAccessible accName: %s" % ret)
			info.append("IAccessibleChildID: %r" % childID)
		elif isinstance(obj, UIA):
			element = obj.UIAElement
			# Sometimes due to timing errors, COM error is thrown
			# when trying to obtain Automation Id from the underlying UIA element.
			# To keep an eye on this, use cached Automation Id
			# rather than fetching UIAAutomationId property directly.
			try:
				info.append(f"UIA Automation Id: {element.cachedAutomationId}")
			except COMError:
				info.append("UIA Automation Id: not found")
			info.append(f"class name: {element.cachedClassName}")
		if additionalInfo:
			info.append(additionalInfo)
		log.debug(u"EvtTracker: {debuginfo}".format(debuginfo="\n".join(info)))
		self.eventHistory.append(Event(event, info))

	# Record object properties when events are fired.
	# General dev info for base object, followed by API specific ones such as UIA properties.

	def event_gainFocus(self, obj, nextHandler):
		self.evtDebugLogging(obj, "gainFocus")
		nextHandler()

	def event_loseFocus(self, obj, nextHandler):
		self.evtDebugLogging(obj, "loseFocus")
		nextHandler()

	def event_focusEntered(self, obj, nextHandler):
		self.evtDebugLogging(obj, "focusEntered")
		nextHandler()

	def event_foreground(self, obj, nextHandler):
		self.evtDebugLogging(obj, "foreground")
		nextHandler()

	def event_nameChange(self, obj, nextHandler):
		self.evtDebugLogging(obj, "nameChange")
		nextHandler()

	def event_valueChange(self, obj, nextHandler):
		self.evtDebugLogging(obj, "valueChange")
		nextHandler()

	def event_stateChange(self, obj, nextHandler):
		self.evtDebugLogging(obj, "stateChange")
		nextHandler()

	def event_descriptionChange(self, obj, nextHandler):
		self.evtDebugLogging(obj, "descriptionChange")
		nextHandler()

	def event_UIA_controllerFor(self, obj, nextHandler):
		self.evtDebugLogging(obj, "UIA_controllerFor")
		nextHandler()

	def event_liveRegionChange(self, obj, nextHandler):
		self.evtDebugLogging(obj, "liveRegionChange")
		nextHandler()

	def event_UIA_elementSelected(self, obj, nextHandler):
		self.evtDebugLogging(obj, "UIA_elementSelected")
		nextHandler()

	def event_UIA_systemAlert(self, obj, nextHandler):
		self.evtDebugLogging(obj, "UIA_systemAlert")
		nextHandler()

	def event_UIA_window_windowOpen(self, obj, nextHandler):
		self.evtDebugLogging(obj, "UIA_window_windowOpen")
		nextHandler()

	def event_UIA_notification(
			self, obj, nextHandler,
			notificationKind=None, notificationProcessing=None, displayString=None, activityId=None
	):
		# Introduced in Windows 10 1709 (Fall Creators Update), to be treated as a notification event.
		notificationInfo = [
			f"sender: {obj.UIAElement}",
			f"notification kind: {notificationKind}",
			f"notification processing: {notificationProcessing}",
			f"display string: {displayString}",
			f"activity Id: {activityId}"
		]
		self.evtDebugLogging(obj, "UIA_notification", additionalInfo="\n".join(notificationInfo))
		nextHandler()

	def event_UIA_toolTipOpened(self, obj, nextHandler):
		self.evtDebugLogging(obj, "UIA_toolTipOpened")
		nextHandler()

	def event_UIA_itemStatus(self, obj, nextHandler):
		self.evtDebugLogging(
			obj, "UIA_itemStatus",
			additionalInfo=f"item status: {obj.UIAElement.currentItemStatus}"
		)
		nextHandler()

	def event_textChange(self, obj, nextHandler):
		self.evtDebugLogging(obj, "textChange")
		nextHandler()

	def event_UIA_layoutInvalidated(self, obj, nextHandler):
		self.evtDebugLogging(
			obj, "layoutInvalidated",
			additionalInfo=f"list item count: {obj.childCount}"
		)
		nextHandler()

	def event_UIA_dragDropEffect(self, obj, nextHandler):
		UIA_DragDropEffectPropertyId = 30139
		dragDropEffect = obj._getUIACacheablePropertyValue(UIA_DragDropEffectPropertyId)
		self.evtDebugLogging(
			obj, "dragDropEffect",
			additionalInfo=f"drag drop effect: {dragDropEffect}"
		)
		nextHandler()

	def event_UIA_dropTargetEffect(self, obj, nextHandler):
		UIA_DropTargetDropTargetEffectPropertyId = 30142
		dropTargetEffect = obj._getUIACacheablePropertyValue(UIA_DropTargetDropTargetEffectPropertyId)
		self.evtDebugLogging(
			obj, "dropTargetEffect",
			additionalInfo=f"drop target effect: {dropTargetEffect}"
		)
		nextHandler()

	def event_alert(self, obj, nextHandler):
		self.evtDebugLogging(obj, "alert")
		nextHandler()

	@script(
		# Translators: input help message for a command in Event Tracker add-on.
		description=_("Shows the list of processed events"),
		category="Event Tracker"
	)
	def script_displayEventsList(self, gesture):
		# We need this to be a modal dialog, but it mustn't block this script.
		def run():
			gui.mainFrame.prePopup()
			d = EventsListDialog(self.eventHistory)
			d.ShowModal()
			d.Destroy()
			gui.mainFrame.postPopup()
		wx.CallAfter(run)


class EventsListDialog(
		DpiScalingHelperMixinWithoutInit,
		wx.Dialog
):
	def __init__(self, eventHistory):
		super().__init__(
			parent=gui.mainFrame,
			# Translators: title of a dialog displaying recent events.
			title=_("Events List")
		)
		self.eventHistory = eventHistory
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		contentsSizer = wx.BoxSizer(wx.VERTICAL)
		self.list = wx.ListBox(
			self,
			size=self.scaleSize((500, 300)),  # height is chosen to ensure the dialog will fit on an 800x600 screen,
			style=wx.LB_SINGLE
		)
		self.list.Bind(wx.EVT_LISTBOX, self.onListItemSelected)
		contentsSizer.Add(self.list, flag=wx.EXPAND)
		contentsSizer.AddSpacer(gui.guiHelper.SPACE_BETWEEN_VERTICAL_DIALOG_ITEMS)
		self.description = gui.guiHelper.LabeledControlHelper(
			self,
			# Translators: label for a read-only edit field displaying event properties.
			_("Event &description"),
			wx.TextCtrl,
			style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_DONTWRAP
		)
		contentsSizer.Add(self.description.sizer)

		mainSizer.Add(contentsSizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.CentreOnScreen()
		self._createEventsList()

	def _createEventsList(self):
		if self.eventHistory:
			for event in self.eventHistory:
				eventType = event.type
				# Copy event info removing the event object and type for readability
				eventInfo = ";\n".join([event.info[1], event.info[2]] + event.info[4:])
				self.list.Append(f"{eventType}; {eventInfo}")
			self.list.SetSelection(0)

	def onListItemSelected(self, event):
		index = event.GetSelection()
		nvdaEvent = self.eventHistory[index] if index >= 0 else None
		if nvdaEvent:
			self.description.control.Value = "\n".join(nvdaEvent.info)
