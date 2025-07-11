# Event-Tracker #

* Autoren: Joseph Lee, Thiago Seus

Diese Erweiterung gibt Informationen zu Objekten aus, für die Ereignisse
ausgelöst wurden. Zu den im Debug-Protokollmodus aufgezeichneten
Eigenschaften gehören Objekttyp, Name, Rolle, Ereignis, App-Modul und
API-spezifische Informationen zur Barrierefreiheit wie accName für
IAccessible-Objekte und Automatisierungs-ID für UIA-Objekte.

Anmerkungen:

* Diese Erweiterung wurde für Entwickler und Power-User entwickelt, die
  Ereignisse verfolgen müssen, die von Apps und verschiedenen
  Steuerelementen stammen.
* Um die Erweiterung verwenden zu können, muss sich NVDA im Debug-Modus
  befinden (konfiguriert über das NVDA-Menü, Optionen, Einstellungen,
  Allgemein und dort Protokollierungsstufen oder Neustart mit aktivierter
  Debug-Protokollierung).
* Es ist möglich, dass Erweiterungen, die früher als Event-Tracker geladen
  wurden, das Ereignis möglicherweise nicht an andere Erweiterungen
  weitergeben, einschließlich Event-Tracker. In diesem Fall kann
  Event-Tracker keine Ereignisse protokollieren.
* Ereignisse werden von globalen Plugins, App-Modulen, Baum-Interceptors und
  NVDA-Objekten in dieser Reihenfolge verarbeitet.

## Events und deren Informationen

Die folgenden Ereignisse werden verfolgt und protokolliert:

* Fokusmanipulation: Fokus gewinnen, Fokus verlieren, Fokus eingegeben,
  Vordergrund
* Änderungen: Name, Wert, Status, Beschreibung, Live-Region
* Andere Ereignisse: Alarm
* UIA-Ereignisse: Controller für, Drag-Drop- und Drop-Zieleffekte, Element
  ausgewählt, Elementstatus, Layout ungültig, Benachrichtigung,
  Systemwarnung, Textänderung, Tooltip geöffnet, Fenster geöffnet

Für jedes Event werden folgende Informationen protokolliert:

* Name des Events
* Objekt
* Name des Objekts
* Rolle des Objekt
* Wert oder Zustand des Objekts, abhängig von Ereignissen
* App-Module
* Für IAccessible-Objekte: Acc-Name, Child-ID
* Für UIA-Objekte: Automatisierungs-ID, Klassenname,
  Benachrichtigungseigenschaften, wenn Informationen zum
  Benachrichtigungsereignis aufgezeichnet werden, Anzahl der Unterobjekte
  für das Ereignis "Layout ungültig", Eigenschaften für den Elementstatus,
  Drag-Drop und Drop-Ziel-Effekt, falls definiert

Sie können auch einen Tastenbefehl zuweisen, um die Ereignisse in einer
Liste anzuzeigen (NVDA-Menü/Einstellungen/Tastenbefehle, Kategorie
"Ereignis-Tracker"). Die Liste speichert bis zu 100 zuletzt verarbeitete
Ereignisse.

If you find this add-on useful, please [review it][1] in the NVDA Add-on
Store.

## Version 25.1.0

* NVDA 2025.1 compatibility.
* NVDA 2024.1 or later is required due to Python 3.11 upgrade.
* Restored limited support for Windows 8.1.
* Made the add-on code more robust with help from Pyright (a Python static
  type checker).
* NVDA will record actual control role name instead of integers when
  reporting events.

## Version 24.1.0

* Kompatibilität für NVDA 2024.1.
* opensourcesys/evtTracker #4: the first event's description no longer
  missing when first opening the event viewer. Contributed by: WangFeng
  Huang (hwf1324)

## Version 23.02

* NVDA 2022.4 oder neuer wird benötigt.
* Windows 10 Version 21H2 (November 2021 Update bzw. Build 19044) oder neuer
  wird benötigt.
* Benachrichtigungen für Ereignisse (meist für IAccessible-Objekte) werden
  verfolgt.

## Version 23.01

* NVDA 2022.3 oder neuer wird benötigt.
* Windows 10 oder neuer ist erforderlich, da Windows 7, 8 und 8.1 seit
  Januar 2023 nicht mehr von Microsoft unterstützt werden.

## Version 22.12

* Dialogfeld zur Ereignisliste hinzugefügt (Befehl nicht zugewiesen), um bis
  zu 100 Ereignisse aufzulisten, die von der NVDA-Erweiterung aufgezeichnet
  wurden (Thiago Seus).
* Zusätzliche Ereignisinformationen, wie z. B. die Eigenschaften von
  UIA-Benachrichtigungen, werden gleichzeitig mit den Ereignissen
  aufgezeichnet.

## Version 22.10

* NVDA 2022.2 oder neuer wird auf Grund von Änderungen an NVDA benötigt, die
  diese Erweiterung betreffen.
* Die folgenden UIA-Eigenschaftsänderungen werden nachverfolgt:
  Drag-Drop-Effekt, Drop-Ziel-Effekt.
* Der UIA-Eigenschaftstext für den Elementstatus wird protokolliert.
* NVDA gibt keinen Fehler als Signalton mehr aus oder scheint nichts zu tun,
  wenn in einem Objekt keinen Fensterklassennamen definiert wurde.

## Version 22.06

* NVDA 2021.3 oder neuer wird auf Grund von Änderungen an NVDA benötigt, die
  diese Erweiterung betreffen.

## Version 21.10

* NVDA 2021.2 oder neuer wird auf Grund von Änderungen an NVDA benötigt, die
  diese Erweiterung betreffen.
* Ungültiges UIA-Layout-Ereignis wird verfolgt.
* Die Informationen zu Objektrollen und -status ähneln den
  Entwicklerinformationen aus neueren NVDA-Versionen.

## Version 21.07

* Erstveröffentlichung.

[1]: https://github.com/nvaccess/addon-datastore/discussions/2717
