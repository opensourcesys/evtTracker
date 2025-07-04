# Event Tracker

* Author: Joseph Lee, Thiago Seus

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

You can also assign a gesture to view the events on a list (NVDA menu/Preferences/Input gestures, Event Tracker category). The list saves up to 100 latest events processed.

If you find this add-on useful, please [review it][1] in the NVDA Add-on Store.

## Version 25.1.0

* NVDA 2025.1 compatibility.
* NVDA 2024.1 or later is required due to Python 3.11 upgrade.
* Restored limited support for Windows 8.1.
* Made the add-on code more robust with help from Pyright (a Python static type checker).
* NVDA will record actual control role name instead of integers when reporting events.

## Version 24.1.0

* NVDA 2024.1 compatibility.
* opensourcesys/evtTracker #4: the first event's description no longer missing when first opening the event viewer. Contributed by: WangFeng Huang (hwf1324)

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.
* Alert event (mostly for IAccessible objects) will be tracked.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer supported by Microsoft as of January 2023.

## Version 22.12

* Added events list dialog (command unassigned) to list up to 100 recent events recorded by the add-on (Thiago Seus).
* Additional event information such as UIA notification properties are recorded at the same time as events.

## Version 22.10

* NVDA 2022.2 or later is required due to security.
* The following UIA property changes are tracked: drag drop effect, drop target effect.
* UIA item status property text is logged.
* NVDA will no longer play error tones or appear to do nothing if an object does not define a window class name.

## Version 22.06

* NVDA 2021.3 or later is required due to security.

## Version 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this add-on.
* UIA layout invalidated event will be tracked.
* Object role and states information will resemble developer info found in more recent NVDA releases.

## Version 21.07

* Initial release.

[1]: https://github.com/nvaccess/addon-datastore/discussions/2717
