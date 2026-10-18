# Triki Adventure — po polsku

[English](../README.md) · [Українська](README.uk.md) · **Polski** · [Русский](README.ru.md)

**Triki Adventure** to eksperymentalna gra na iPhone'a, w której fizyczna figurka Żabka Triki działa jako kontroler ruchowy Bluetooth. Projekt jest niezależny i nie jest oficjalnie powiązany z Żabką.

## Co już działa
- Połączenie z figurką przez BLE na Macu.
- Odczyt danych żyroskopu i akcelerometru.
- Kompilacja aplikacji SwiftUI i instalacja na iPhonie.
- Sterowanie grą przez BLE bezpośrednio na iPhonie wymaga jeszcze testów.

## Etapy
1. Dodać rzeczywiste pliki projektu Xcode do repozytorium.
2. Uruchomić stabilne BLE na iPhonie.
3. Dodać kalibrację ruchu i sterowanie dotykowe.
4. Stworzyć pierwszy grywalny poziom.
5. Rozbudować poziomy, przeciwników i system postępu.
6. Przetestować i przygotować wydanie.

## Twórz własne projekty z Triki
Wykorzystując [eksperymentalny przykład kodu](../examples/README.md) i [dokumentację protokołu BLE](BLE_PROTOCOL.md), możesz opracować własną grę, sterownik gestów, prototyp edukacyjny lub instalację interaktywną.

**Uwaga:** przykład nie został jeszcze osobno przetestowany, a kod jest dostępny na [licencji MIT](../LICENSE), która zezwala na wykorzystanie i modyfikacje pod warunkiem zachowania informacji o prawach autorskich.

[Architektura](ARCHITECTURE.md) · [Plan prac](ROADMAP.md) · [Rozwój](DEVELOPMENT.md)
