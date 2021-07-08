# NVDA Event Tracker/Investigator
# Copyright 2017-2021 Joseph Lee, released under GPL.

import globalPluginHandler
from NVDAObjects.UIA import UIA
import globalVars
from logHandler import log

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		# #20: don't even think about proceeding in secure screens (especially add-on updates).
		if globalVars.appArgs.secure: return

	# Record info about events and objects.
	def evtDebugLogging(self, obj, event=None):
		if isinstance(obj, UIA) and globalVars.appArgs.debugLogging:
			element = obj.UIAElement
			if not obj.name:
				obj.name = "unavailable"
			automationID = element.cachedAutomationID
			if not automationID: automationID = "unavailable"
			className = element.cachedClassName
			if not className: className = "unavailable"
			if not event:
				event = "no event specified"
			if event != "controllerFor":
				log.debug("W10: UIA object name: %s, event: %s, app module: %s, automation Id: %s, class name: %s"%(obj.name, event, obj.appModule, automationID, className))
			else:
				log.debug("Event Tracker: UIA object name: %s, event: %s, app module: %s, automation Id: %s, class name: %s, controller for count: %s"%(obj.name, event, obj.appModule, automationID, className, len(obj.controllerFor)))

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
