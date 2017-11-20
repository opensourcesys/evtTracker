# Event Tracker

* Author: Joseph Lee

This add-on outputs information about objects for which events were fired.

Notes:

* This add-on is designed for developers needing to track events coming from apps and various controls.
* In order to use the add-on, NVDA must be run with debug logging enabled (restart NVDA with this option).

## Events and their information
The following events are tracked and recorded:

* Focus manipulation: gainFocus, loseFocus, focusEntered, foreground
* Changes: nameChange, valueChange, stateChange, liveRegionChange
* UIA events: itemSelected, controllerFor.

For each event, the following informatoi nwill be recorded:

* Event name
* Object
* Object name* Role
* App module and app information* Additional informatoin based on API

