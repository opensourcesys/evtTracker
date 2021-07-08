# NVDA Event Tracker/Investigator
# Copyright 2017-2021 Joseph Lee, released under GPL.

from comtypes import COMError
import globalPluginHandler
import controlTypes
from NVDAObjects.UIA import UIA
import globalVars
from logHandler import log


# Object states constants for use when tracking events.
# Copied from NVDA Core's default navigator object dev info's state retriever (credit: NV Access).
# State constants in control types were rearranged in control types refactor (enumeration) in NVDA.
# Support control types refactor (both before (2021.1) and after (2021.2) for a time).
if hasattr(controlTypes, "State"):
	stateConsts = dict(
		(state.value, state.name) for state in controlTypes.State
	)
else:
	stateConsts = dict(
		(const, name) for name, const in controlTypes.__dict__.items() if name.startswith("STATE_")
	)


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		# Do not activate this from secure screens.
		if globalVars.appArgs.secure:
			return

	# Record info about events and objects.
	def evtDebugLogging(self, obj, event=None):
		if isinstance(obj, UIA) and globalVars.appArgs.debugLogging:
			info = [f"object: {repr(obj)}"]
			info.append(f"name: {obj.name}")
			if not event:
				event = "no event specified"
			info.append(f"event: {event}")
			if event == "valueChange":
				info.append(f"value: {obj.value}")
			elif event == "stateChange":
				# Parts copied from NVDA Core's default navigator object dev info's state retriever (credit: NV Access).
				try:
					ret = ", ".join(
						stateConsts.get(state) or str(state)
						for state in obj.states)
				except Exception as e:
					ret = "exception: %s" % e
				info.append(f"states: {ret}")
			info.append(f"app module: {obj.appModule}")
			element = obj.UIAElement
			# Sometimes due to timing errors, COM error is thrown
			# when trying to obtain Automation Id from the underlying UIA element.
			# To keep an eye on this, use cached Automation Id
			# rather than fetching UIAAutomationId property directly.
			try:
				info.append(f"Automation Id: {element.cachedAutomationId}")
			except COMError:
				info.append("Automation Id: not found")
			info.append(f"class name: {element.cachedClassName}")
			log.debug(u"EvtTracker: UIA {debuginfo}".format(debuginfo=", ".join(info)))

	# Record object properties when events are fired.
	# General dev info for base object, followed by API specific ones such as UIA properties.

	def event_gainFocus(self, obj, nextHandler):
		self.evtDebugLogging(obj, "gainFocus")
		nextHandler()

	def event_loseFocus(self, obj, nextHandler):
		self.evtDebugLogging(obj, "loseFocus")
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
		self.evtDebugLogging(obj, "controllerFor")
		nextHandler()

	def event_liveRegionChange(self, obj, nextHandler):
		self.evtDebugLogging(obj, "liveRegionChange")
		nextHandler()

	def event_UIA_elementSelected(self, obj, nextHandler):
		self.evtDebugLogging(obj, "elementSelected")
		nextHandler()

	def event_UIA_systemAlert(self, obj, nextHandler):
		self.evtDebugLogging(obj, "systemAlert")
		nextHandler()

	def event_UIA_window_windowOpen(self, obj, nextHandler):
		self.evtDebugLogging(obj, "windowOpen")
		nextHandler()

	def event_UIA_notification(
			self, obj, nextHandler,
			notificationKind=None, notificationProcessing=None, displayString=None, activityId=None
	):
		# Introduced in Windows 10 1709, to be treated as a notification event.
		self.evtDebugLogging(obj, "notification")
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
		self.evtDebugLogging(obj, "tooltipOpened")
		nextHandler()

	def event_UIA_itemStatus(self, obj, nextHandler):
		self.evtDebugLogging(obj, "itemStatus")
		nextHandler()

	def event_textChange(self, obj, nextHandler):
		self.evtDebugLogging(obj, "textChange")
		nextHandler()
