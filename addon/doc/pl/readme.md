# Event Tracker

* Author: Joseph Lee, Thiago Seus

Ten dodatek wyświetla informacje o obiektach, dla których zdarzenia zostały uruchomione. Właściwości zarejestrowane w trybie dziennika debugowania obejmują typ obiektu, nazwę, rolę, zdarzenie, moduł aplikacji i informacje specyficzne dla interfejsu API ułatwień dostępu, takie jak accName dla obiektu IAccessible i identyfikator automatyzacji dla obiektów UIA.

Uwagi:

* Ten dodatek jest przeznaczony dla deweloperów i zaawansowanych użytkowników, którzy muszą śledzić zdarzenia pochodzące z aplikacji i różnych kontrolek.
* Aby korzystać z dodatku, NVDA musi logować się w trybie debugowania (skonfigurowanym z poziomu ustawień ogólnych/rejestrowania lub ponownie uruchomić z włączonym rejestrowaniem debugowania).
* Możliwe, że dodatki załadowane wcześniej niż Event Tracker mogą nie przekazać zdarzenia innym dodatkom, w tym Event Tracker. Jeśli tak się stanie, Moduł śledzenia zdarzeń nie będzie mógł rejestrować zdarzeń.
* Zdarzenia są obsługiwane z globalnych wtyczek, modułów aplikacji, przechwytywaczy drzew i obiektów NVDA w tej kolejności.

## Wydarzenia i informacje o nich

Śledzone i rejestrowane są następujące zdarzenia:

* Manipulacja ostrością: wzmocnienie ostrości, utrata ostrości, wprowadzenie ostrości, pierwszy plan
* Zmiany: nazwa, wartość, stan, opis, aktywny region
* Inne zdarzenia: alert
* Zdarzenia UIA: kontroler, efekty upuszczania i upuszczania elementów przeciągniętych, wybrany element, stan elementu, układ unieważniony, powiadomienie, alert systemowy, zmiana tekstu, otwarta podpowiedź, otwarte okno

Dla każdego zdarzenia rejestrowane będą następujące informacje:

* Nazwa wydarzenia
* Obiekt
* Nazwa obiektu
* Rola obiektu
* Wartość lub stan obiektu w zależności od zdarzeń
* Moduł aplikacji
* W przypadku obiektów IAccessible: nazwa acc, identyfikator podrzędny
* W przypadku obiektów UIA: identyfikator automatyzacji, nazwa klasy, właściwości powiadomienia w przypadku rejestrowania informacji o zdarzeniu powiadomienia, liczba elementów podrzędnych dla zdarzenia unieważnionego układu, właściwości stanu elementu, upuszczanie przeciągania i efekt docelowy upuszczania, jeśli został zdefiniowany

Możesz także przypisać gest do wyświetlania zdarzeń na liście (menu NVDA / preferencje / gesty wprowadzania, kategoria Śledzenie zdarzeń). Lista zapisuje do 100 ostatnio przetworzonych zdarzeń.

If you find this add-on useful, please [review it][1] in the NVDA Add-on Store.

[1]: https://github.com/nvaccess/addon-datastore/discussions/2717
