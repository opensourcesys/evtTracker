# Event Tracker

* Author: Joseph Lee
* Download [stable version][1]
* NVDA compatibility: 2022.2 and later

This add-on outputs information about objects for which events were fired. Properties recorded in debug log mode include object type, name, role, event, app module, and accessibility API specific information such as accName for IAccessible object and Automation Id for UIA objects.

Notes:

* This add-on is designed for developers and power users needing to track events coming from apps and various controls.
* In order to use the add-on, NVDA must be logging in debug mode (configured from general settings/logging level, or restart with debug logging enabled).
* It might be possible that add-ons loaded earlier than Event Tracker may not pass on the event to other add-ons, including Event Tracker. If this happens, Event Tracker will not be able to log events.
* Events are handled from global plugins, app modules, tree interceptors, and NVDA objects, in that order.

## Events and their information

The following events are tracked and recorded:

* Focus manipulation: gain focus, lose focus, focus entered, foreground
* Changes: name, value, state, description, live region
* UIA events: controller for, element selected, item status, layout invalidated, notification, text change, tooltip open, window open

For each event, the following information will be recorded:

* Event name
* Object
* Object name
* Object role
* Object value or state depending on events
* App module
* For IAccessible objects: acc name, child ID
* For UIA objects: Automation Id, class name, notification properties if recording notification event information, child count for layout invalidated event

## Version 22.09

* NVDA 2022.2 or later is required due to security.
* NVDA will no longer play error tones or appear to do nothing if an object does not define a window class name.

## Version 22.06

* NVDA 2021.3 or later is required due to security.

## Version 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this add-on.
* UIA layout invalidated event will be tracked.
* Object role and states information will resemble developer info found in more recent NVDA releases.

## Version 21.07

* Initial release.

[1]: https://addons.nvda-project.org/files/get.php?file=evttracker
