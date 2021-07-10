# Event Tracker

* Author: Joseph Lee
* Download [stable version][1]
* NVDA compatibility: 2021.1 and beyond

This add-on outputs information about objects for which events were fired. Properties recorded in debug log mode include object type, name, event, app module, and accessibility API specific information such as accName for IAccessible object and Automation Id for UIA objects.

Notes:

* This add-on is designed for developers and power users needing to track events coming from apps and various controls.
* In order to use the add-on, NVDA must be logging in debug mode (configured from general settings/logging level, or restart with debug logging enabled).
* It might be possible that add-ons loaded earlier than Event Tracker may not pass on the event to other add-ons, including Event Tracker. If this happens, Event Tracker will not be able to log events.
* Events are handled from global plugins, app modules, tree interceptors, and NVDA objects, in that order.

## Events and their information

The following events are tracked and recorded:

* Focus manipulation: gain focus, lose focus, focus entered, foreground
* Changes: name, value, state, description, live region
* UIA events: element selected, item status, controller for, notification, tooltip open, window open, text change

For each event, the following information will be recorded:

* Event name
* Object
* Object name
* Object value or state depending on events
* App module
* For IAccessible objects: acc name, child ID
* For UIA objects: Automation Id, class name, notification properties if recording notification event information

## Version 21.07

* Initial release.

[1]: https://addons.nvda-project.org/files/get.php?file=evttracker
