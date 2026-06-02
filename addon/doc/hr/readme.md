# Praćenje događaja (Event Tracker)

* Autor: Joseph Lee, Thiago Seus

Ovaj dodatak daje informacije o objektima za koje su pokrenuti događaji. Svojstva zabilježena u načinu dnevnika otklanjanja grešaka uključuju vrstu objekta, naziv, ulogu, događaj, modul aplikacije i informacije specifične za API pristupačnosti kao što su accName za IAccessible objekt i Automation Id za UIA objekte.

Zabilješke:

* Ovaj je dodatak dizajniran za programere i napredne korisnike koji trebaju mogućnost praćenja događaja koji dolaze iz aplikacija i raznih kontrola.
* Za korištenje dodatka, NVDA mora biti prijavljivanje u načinu ispravljanja grešaka (konfigurirano u općim postavkama / razini prijave ili s ponovnim pokretnjem s aktiviranim zapisivanjem ispravljanja grešaka).
* Moguće je da dodaci koji su učitani prije dodatka „Praćenja događaja” ne proslijede događaj drugim dodacima, uključujući dodatak „Praćenje događaja”. Ako se to dogodi, dodatak „Praćenje događaja” neće moći zabilježiti događaje.
* Događajima se upravlja iz globalnih dodataka, modula aplikacija, presretača stabla i NVDA objekata, tim redoslijedom.

## Događaji i njihove informacije

Sljedeći događaji se prate i snimaju:

* Manipulacija fokusom: dobivanje fokusa, gubljenje fokusa, unesen fokus, prvi plan
* Promjene: naziv, vrijednost, stanje, opis, regija uživo
* Ostali događaji: upozorenje
* UIA događaji: kontroler za, efekte povlačenja i ispuštanja cilja, odabran element, stanje stavke, poništen raspored, obavijest, upozorenje sustava, promjena teksta, otvoren opis alata, otvoren prozor

Za svaki događaj zabilježit će se sljedeće informacije:

* Naziv događaja
* Objekt
* Naziv objekta
* Uloga objekta
* Vrijednost ili stanje objekta ovisno o događaju
* Modul aplikacije
* Za IAccessible objekte: ime računa, ID podređenog
* Za UIA objekte: ID automatizacije, ime klase, svojstva obavijesti ako se snimaju informacije obavijesti događaja, broj podređenih za izgled nevažećeg događaja, svojstva za stanje stavke, povuci-i-ispusti, te ispuštanje efekta cilja ako je definiran

Možeš dodijeliti i gestu za pregled događaja na popisu (NVDA izbornik/Postavke/Geste unosa, kategorija „Praćenje događaja”). Popis sprema do 100 najnovijih obrađenih događaja.

If you find this add-on useful, please [review it][1] in the NVDA Add-on Store.

[1]: https://github.com/nvaccess/addon-datastore/discussions/2717
