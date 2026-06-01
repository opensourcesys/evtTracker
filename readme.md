# Event Tracker

* Author: Joseph Lee, Thiago Seus

This add-on outputs information about objects for which events were fired. Properties recorded in debug log mode include object type, name, role, event, app module, and accessibility API specific information such as accName for IAccessible object and Automation Id for UIA objects.

Notes:

* This add-on is designed for developers and power users needing to track events coming from apps and various controls.
* In order to use the add-on, NVDA must be logging in debug mode (configured from general settings (Privacy and Security in NVDA 2026.1 and later)/logging level, or restart with debug logging enabled).
* It might be possible that add-ons loaded earlier than Event Tracker may not pass on the event to other add-ons, including Event Tracker. If this happens, Event Tracker will not be able to log events.
* Events are handled from global plugins, app modules, tree interceptors, and NVDA objects, in that order.

## Events and their information

The following events are tracked and recorded:

* Focus manipulation: gain focus, lose focus, focus entered, foreground
* Changes: name, value, state, description, live region
* Other events: alert
* UIA events: controller for, drag drop and drop target effects, element selected, item status, layout invalidated, notification, system alert, text change, tooltip open, window open

For each event, the following information will be recorded:

* Event name
* Object
* Object name
* Object role
* Object value or state depending on events
* App module
* For IAccessible objects: acc name, child ID
* For UIA objects: Automation Id, class name, notification properties if recording notification event information, child count for layout invalidated event, properties for item status, drag drop, and drop target effect if defined

You can also assign a gesture to view the events on a list (NVDA menu/Preferences/Input gestures, Event Tracker category). The list saves up to 100 latest events processed prior to opening the dialog.

If you find this add-on useful, please [review it][1] in the NVDA Add-on Store.

[1]: https://github.com/nvaccess/addon-datastore/discussions/2717
