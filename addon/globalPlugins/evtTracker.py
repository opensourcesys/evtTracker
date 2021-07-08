# NVDA Event Tracker/Investigator
# Copyright 2017-2021 Joseph Lee, released under GPL.

from comtypes import COMError
import globalPluginHandler
from NVDAObjects.UIA import UIA
import globalVars
from logHandler import log


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

	# Focus announcement hacks.
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
		# Specifically in order to debug multiple toast announcements.
		self.evtDebugLogging(obj, "windowOpen")
		nextHandler()
