# NVDA Event Tracker/Investigator
# Copyright 2017-2022 Joseph Lee, released under GPL.

from comtypes import COMError
import globalPluginHandler
import globalVars
from logHandler import log
from NVDAObjects.IAccessible import IAccessible
from NVDAObjects.UIA import UIA


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		# Do not activate this from secure screens.
		# And do not activate the add-on if log level is not debug.
		if globalVars.appArgs.secure or not log.isEnabledFor(log.DEBUG):
			return

	# Record info about events and objects.
	def evtDebugLogging(self, obj, event=None):
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
		info.append(f"window class name: {obj.windowClassName}")
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
		self.evtDebugLogging(obj, "UIA_notification")
		if isinstance(obj, UIA) and log.isEnabledFor(log.DEBUG):
			log.debug(
				"EvtTracker: UIA notification: "
				f"sender: {obj.UIAElement}, "
				f"notification kind: {notificationKind}, "
				f"notification processing: {notificationProcessing}, "
				f"display string: {displayString}, "
				f"activity Id: {activityId}"
			)
		nextHandler()

	def event_UIA_toolTipOpened(self, obj, nextHandler):
		self.evtDebugLogging(obj, "UIA_toolTipOpened")
		nextHandler()

	def event_UIA_itemStatus(self, obj, nextHandler):
		self.evtDebugLogging(obj, "UIA_itemStatus")
		nextHandler()

	def event_textChange(self, obj, nextHandler):
		self.evtDebugLogging(obj, "textChange")
		nextHandler()

	def event_UIA_layoutInvalidated(self, obj, nextHandler):
		self.evtDebugLogging(obj, "layoutInvalidated")
		if log.isEnabledFor(log.DEBUG):
			log.debug(f"EvtTracker: list item count: {obj.childCount}")
		nextHandler()
