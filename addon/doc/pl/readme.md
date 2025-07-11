# Event Tracker #

* Author: Joseph Lee, Thiago Seus

Ten dodatek wyświetla informacje o obiektach, dla których zdarzenia zostały
uruchomione. Właściwości zarejestrowane w trybie dziennika debugowania
obejmują typ obiektu, nazwę, rolę, zdarzenie, moduł aplikacji i informacje
specyficzne dla interfejsu API ułatwień dostępu, takie jak accName dla
obiektu IAccessible i identyfikator automatyzacji dla obiektów UIA.

Uwagi:

* Ten dodatek jest przeznaczony dla deweloperów i zaawansowanych
  użytkowników, którzy muszą śledzić zdarzenia pochodzące z aplikacji i
  różnych kontrolek.
* Aby korzystać z dodatku, NVDA musi logować się w trybie debugowania
  (skonfigurowanym z poziomu ustawień ogólnych/rejestrowania lub ponownie
  uruchomić z włączonym rejestrowaniem debugowania).
* Możliwe, że dodatki załadowane wcześniej niż Event Tracker mogą nie
  przekazać zdarzenia innym dodatkom, w tym Event Tracker. Jeśli tak się
  stanie, Moduł śledzenia zdarzeń nie będzie mógł rejestrować zdarzeń.
* Zdarzenia są obsługiwane z globalnych wtyczek, modułów aplikacji,
  przechwytywaczy drzew i obiektów NVDA w tej kolejności.

## Wydarzenia i informacje o nich

Śledzone i rejestrowane są następujące zdarzenia:

* Manipulacja ostrością: wzmocnienie ostrości, utrata ostrości, wprowadzenie
  ostrości, pierwszy plan
* Zmiany: nazwa, wartość, stan, opis, aktywny region
* Inne zdarzenia: alert
* Zdarzenia UIA: kontroler, efekty upuszczania i upuszczania elementów
  przeciągniętych, wybrany element, stan elementu, układ unieważniony,
  powiadomienie, alert systemowy, zmiana tekstu, otwarta podpowiedź, otwarte
  okno

Dla każdego zdarzenia rejestrowane będą następujące informacje:

* Nazwa wydarzenia
* Obiekt
* Nazwa obiektu
* Rola obiektu
* Wartość lub stan obiektu w zależności od zdarzeń
* Moduł aplikacji
* W przypadku obiektów IAccessible: nazwa acc, identyfikator podrzędny
* W przypadku obiektów UIA: identyfikator automatyzacji, nazwa klasy,
  właściwości powiadomienia w przypadku rejestrowania informacji o zdarzeniu
  powiadomienia, liczba elementów podrzędnych dla zdarzenia unieważnionego
  układu, właściwości stanu elementu, upuszczanie przeciągania i efekt
  docelowy upuszczania, jeśli został zdefiniowany

Możesz także przypisać gest do wyświetlania zdarzeń na liście (menu NVDA /
preferencje / gesty wprowadzania, kategoria Śledzenie zdarzeń). Lista
zapisuje do 100 ostatnio przetworzonych zdarzeń.

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

* NVDA 2024.1 compatibility.
* opensourcesys/evtTracker #4: the first event's description no longer
  missing when first opening the event viewer. Contributed by: WangFeng
  Huang (hwf1324)

## Wersja 23.02

* Wymagana jest NVDA 2022.4 lub nowsza.
* Wymagany jest system Windows 10 21H2 (aktualizacja z listopada 2021
  r./kompilacja 19044) lub nowszy.
* Zdarzenie alertu (głównie dla obiektów IAccessible) będzie śledzone.

## Wersja 23.01

* Wymagana jest NVDA 2022.3 lub nowsza.
* System Windows 10 lub nowszy jest wymagany, ponieważ systemy Windows 7, 8
  i 8.1 nie są już obsługiwane przez firmę Microsoft od stycznia 2023 r.

## Wersja 22.12

* Dodano okno dialogowe listy zdarzeń (polecenie unsigned) do listy do 100
  ostatnich wydarzeń zarejestrowanych przez dodatek (Thiago Seus).
* Dodatkowe informacje o zdarzeniach, takie jak właściwości powiadomień UIA,
  są rejestrowane w tym samym czasie co zdarzenia.

## Wersja 22.10

* Ze względów bezpieczeństwa wymagana jest wersja NVDA 2022.2 lub nowsza.
* Śledzone są następujące zmiany właściwości UIA: efekt upuszczenia, efekt
  upuszczenia.
* Tekst właściwości stanu elementu UIA jest rejestrowany.
* NVDA nie będzie już odtwarzać dźwięków błędów lub będzie się wydawało, że
  nic nie robi, jeśli obiekt nie definiuje nazwy klasy okna.

## Wersja 22.06

* NVDA 2021.3 lub nowsza jest wymagana ze względów bezpieczeństwa.

## Wersja 21.10

* NVDA 2021.2 lub nowsza jest wymagana ze względu na zmiany w NVDA, które
  mają wpływ na ten dodatek.
* Zdarzenie unieważnione w układzie UIA będzie śledzone.
* Informacje o roli obiektu i stanach będą przypominać informacje o
  deweloperach znalezione w nowszych wersjach NVDA.

## Wersja 21.07

* Pierwsze wydanie.

[1]: https://github.com/nvaccess/addon-datastore/discussions/2717
