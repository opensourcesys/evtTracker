# Event-Tracker

* Autoren: Joseph Lee, Thiago Seus

Diese Erweiterung gibt Informationen zu Objekten aus, für die Ereignisse ausgelöst wurden. Zu den im Debug-Protokollmodus aufgezeichneten Eigenschaften gehören Objekttyp, Name, Rolle, Ereignis, App-Modul und API-spezifische Informationen zur Barrierefreiheit wie accName für IAccessible-Objekte und Automatisierungs-ID für UIA-Objekte.

Anmerkungen:

* Diese Erweiterung wurde für Entwickler und Power-User entwickelt, die Ereignisse verfolgen müssen, die von Apps und verschiedenen Steuerelementen stammen.
* Um die Erweiterung verwenden zu können, muss sich NVDA im Debug-Modus befinden (konfiguriert über das NVDA-Menü, Optionen, Einstellungen, Allgemein und dort Protokollierungsstufen oder Neustart mit aktivierter Debug-Protokollierung).
* Es ist möglich, dass Erweiterungen, die früher als Event-Tracker geladen wurden, das Ereignis möglicherweise nicht an andere Erweiterungen weitergeben, einschließlich Event-Tracker. In diesem Fall kann Event-Tracker keine Ereignisse protokollieren.
* Ereignisse werden von globalen Plugins, App-Modulen, Baum-Interceptors und NVDA-Objekten in dieser Reihenfolge verarbeitet.

## Events und deren Informationen

Die folgenden Ereignisse werden verfolgt und protokolliert:

* Fokusmanipulation: Fokus gewinnen, Fokus verlieren, Fokus eingegeben, Vordergrund
* Änderungen: Name, Wert, Status, Beschreibung, Live-Region
* Andere Ereignisse: Alarm
* UIA-Ereignisse: Controller für, Drag-Drop- und Drop-Zieleffekte, Element ausgewählt, Elementstatus, Layout ungültig, Benachrichtigung, Systemwarnung, Textänderung, Tooltip geöffnet, Fenster geöffnet

Für jedes Event werden folgende Informationen protokolliert:

* Name des Events
* Objekt
* Name des Objekts
* Rolle des Objekt
* Wert oder Zustand des Objekts, abhängig von Ereignissen
* App-Module
* Für IAccessible-Objekte: Acc-Name, Child-ID
* Für UIA-Objekte: Automatisierungs-ID, Klassenname, Benachrichtigungseigenschaften, wenn Informationen zum Benachrichtigungsereignis aufgezeichnet werden, Anzahl der Unterobjekte für das Ereignis "Layout ungültig", Eigenschaften für den Elementstatus, Drag-Drop und Drop-Ziel-Effekt, falls definiert

Sie können auch einen Tastenbefehl zuweisen, um die Ereignisse in einer Liste anzuzeigen (NVDA-Menü/Einstellungen/Tastenbefehle, Kategorie "Ereignis-Tracker"). Die Liste speichert bis zu 100 zuletzt verarbeitete Ereignisse.

If you find this add-on useful, please [review it][1] in the NVDA Add-on Store.

[1]: https://github.com/nvaccess/addon-datastore/discussions/2717
