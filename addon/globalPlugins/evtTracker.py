# NVDA Event Tracker/Investigator
# Copyright 2017-2022 Joseph Lee, released under GPL.

from comtypes import COMError
import globalPluginHandler
import globalVars
from logHandler import log
from NVDAObjects.IAccessible import IAccessible
from NVDAObjects.UIA import UIA


# Security: disable the global plugin altogether in secure mode.
def disableInSecureMode(cls):
	return globalPluginHandler.GlobalPlugin if globalVars.appArgs.secure else cls


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Record info about events and objects.
	def evtDebugLogging(self, obj, event=None, additionalInfo=None):
		info = [f"object: {repr(obj)}"]
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
		self.evtDebugLogging(obj, "dragDropEffect")
		if log.isEnabledFor(log.DEBUG):
			UIA_DragDropEffectPropertyId = 30139
			dragDropEffect = obj._getUIACacheablePropertyValue(UIA_DragDropEffectPropertyId)
			log.debug(f"EvtTracker: drag drop effect: {dragDropEffect}")
		nextHandler()

	def event_UIA_dropTargetEffect(self, obj, nextHandler):
		self.evtDebugLogging(obj, "dropTargetEffect")
		if log.isEnabledFor(log.DEBUG):
			UIA_DropTargetDropTargetEffectPropertyId = 30142
			dropTargetEffect = obj._getUIACacheablePropertyValue(UIA_DropTargetDropTargetEffectPropertyId)
			log.debug(f"EvtTracker: drop target effect: {dropTargetEffect}")
		nextHandler()
