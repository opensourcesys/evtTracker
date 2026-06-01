# Event Tracker Add-on Changelog

This page lists the complete changelog for Event Tracker add-on releases.

## Version 26.3.0

* Removed add-on changelog from add-on help (readme) file.

## Version 26.2.0

* NVDA 2025.3.3 or later is required.

## Version 26.1.0

* The events list dialog will no longer show confusing information for the last event description when left open for an extended time.
* UIA drop target effect text is fetched from the focus ancestor object if the UIA object raising this event does not record this information.

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
