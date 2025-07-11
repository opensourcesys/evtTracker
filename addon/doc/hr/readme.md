# Praćenje događaja (Event Tracker) #

* Autor: Joseph Lee, Thiago Seus

Ovaj dodatak daje informacije o objektima za koje su pokrenuti
događaji. Svojstva zabilježena u načinu dnevnika otklanjanja grešaka
uključuju vrstu objekta, naziv, ulogu, događaj, modul aplikacije i
informacije specifične za API pristupačnosti kao što su accName za
IAccessible objekt i Automation Id za UIA objekte.

Zabilješke:

* Ovaj je dodatak dizajniran za programere i napredne korisnike koji trebaju
  mogućnost praćenja događaja koji dolaze iz aplikacija i raznih kontrola.
* Za korištenje dodatka, NVDA mora biti prijavljivanje u načinu ispravljanja
  grešaka (konfigurirano u općim postavkama / razini prijave ili s ponovnim
  pokretnjem s aktiviranim zapisivanjem ispravljanja grešaka).
* Moguće je da dodaci koji su učitani prije dodatka „Praćenja događaja” ne
  proslijede događaj drugim dodacima, uključujući dodatak „Praćenje
  događaja”. Ako se to dogodi, dodatak „Praćenje događaja” neće moći
  zabilježiti događaje.
* Događajima se upravlja iz globalnih dodataka, modula aplikacija,
  presretača stabla i NVDA objekata, tim redoslijedom.

## Događaji i njihove informacije

Sljedeći događaji se prate i snimaju:

* Manipulacija fokusom: dobivanje fokusa, gubljenje fokusa, unesen fokus,
  prvi plan
* Promjene: naziv, vrijednost, stanje, opis, regija uživo
* Ostali događaji: upozorenje
* UIA događaji: kontroler za, efekte povlačenja i ispuštanja cilja, odabran
  element, stanje stavke, poništen raspored, obavijest, upozorenje sustava,
  promjena teksta, otvoren opis alata, otvoren prozor

Za svaki događaj zabilježit će se sljedeće informacije:

* Naziv događaja
* Objekt
* Naziv objekta
* Uloga objekta
* Vrijednost ili stanje objekta ovisno o događaju
* Modul aplikacije
* Za IAccessible objekte: ime računa, ID podređenog
* Za UIA objekte: ID automatizacije, ime klase, svojstva obavijesti ako se
  snimaju informacije obavijesti događaja, broj podređenih za izgled
  nevažećeg događaja, svojstva za stanje stavke, povuci-i-ispusti, te
  ispuštanje efekta cilja ako je definiran

Možeš dodijeliti i gestu za pregled događaja na popisu (NVDA
izbornik/Postavke/Geste unosa, kategorija „Praćenje događaja”). Popis sprema
do 100 najnovijih obrađenih događaja.

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

## Verzija 24.10

* Kompatibilnost s NVDA 2024.1.
* opensourcesys/evtTracker #4: the first event's description no longer
  missing when first opening the event viewer. Contributed by: WangFeng
  Huang (hwf1324)

## Verzija 23.02

* Potrebna je NVDA verzija 2022.4 ili novija.
* Potreban je sustav Windows 10 21H2 (aktualizirana verzija iz studenog
  2021./izgradnja 19044) ili novija verzija.
* Događaji upozorenja (uglavnom za IAccessible objekte) će se pratiti.

## Verzija 23.01

* Potrebna je NVDA verzija 2022.3 ili novija.
* Zahtijeva Windows 10 ili noviju verziju, jer od siječnja 2023. Microsoft
  više ne pordržava Windows 7, 8 i 8.1.

## Verzija 22.12

* Added events list dialog (command unassigned) to list up to 100 recent
  events recorded by the add-on (Thiago Seus).
* Additional event information such as UIA notification properties are
  recorded at the same time as events.

## Verzija 22.10

* Iz sigurnosnih razloga je potrebna je NVDA verzija 2022.2 ili novija.
* The following UIA property changes are tracked: drag drop effect, drop
  target effect.
* UIA item status property text is logged.
* NVDA will no longer play error tones or appear to do nothing if an object
  does not define a window class name.

## Verzija 22.06

* Iz sigurnosnih razloga je potrebna je NVDA verzija 2021.3 ili novija.

## Verzija 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this
  add-on.
* UIA layout invalidated event will be tracked.
* Object role and states information will resemble developer info found in
  more recent NVDA releases.

## Verzija 21.07

* Prvo izdanje.

[1]: https://github.com/nvaccess/addon-datastore/discussions/2717
