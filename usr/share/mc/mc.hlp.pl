[Contents]
  OPISDESCRIPTION
  OPCJEOPTIONS
  OpisOverview
  Obsługa myszyMouse Support

  KlawiszeKeys
    Klawisze różneMiscellaneous Keys
    Panel KatalogówDirectory Panels
    Linia PowłokiShell Command Line
    Podstawowe klawisze ruchuGeneral Movement Keys
    Linia wejściowa klawiszyInput Line Keys

  Linia menuMenu Bar
    Lewe i prawe menuLeft and Right Menus
      Tryby wyświetlania (Listing modes)Listing Mode...
      Porządek sortowania (Sort order...)Sort Order...
      Filtry (Filter...)Filter...
      Odśwież (Reread)Reread
    Menu plików (File menu)File Menu
      Szybka zmiana katalogów (Quick cd) M-cQuick cd
    Menu komend (Command Menu)Command Menu
      Drzewo katalogów (Directory Tree)Directory Tree
      Znajdź plik (Find File)Find File
      Panel zewnętrznyExternal panelize
      HotlistHotlist
      Edycja rozszerzeń pliów (Extension File Edit)Extension File Edit
      Prace w tle (Background jobs)Background Jobs
      Edycja menu użytkownika (Menu File Edit)Menu File Edit
    Menu opcji (Options Menu)Options Menu
      KonfiguracjaConfiguration
      Wygląd (Layout)Layout
      Potwierdzanie (Confirmation)Confirmation
      Wyświetlanie znaków (Display bits)Display bits
      Nauka klawiszy (Learn keys)Learn keys
      Wirtualny system plików (Virtual FS)Virtual FS
      Zapisz ustawienia (Save Setup)Save Setup

  Wykonywanie poleceń systemu operacyjnego (Executing operating system commands)Executing operating system commands
    Wbudowana komenda cd (The cd internal command)The cd internal command
    Obsługa makr (Macro Substitution)Macro Substitution
    Obsługa podpowłoki (The subshell support)The subshell support
  ChmodChmod
  ChownChown
  Zaawansowane chown (Advanced Chown)Advanced Chown
  Operacje na plikach (File Operations)File Operations
  Maski kopiowania/przenoszenia (Mask Copy/Rename)Mask Copy/Rename
  Wbudowany podgląd plikówInternal File Viewer
  Wbudowany edytor plikówInternal File Editor
  DokańczanieCompletion
  Wirtualny system plików (Virtual File System)Virtual File System
    System plików FTP (FTP File System)FTP File System
    System plików tar (Tar File System)Tar File System
    Transfer plików pomiędzy systemami plików (FIle transfer over SHell filesystem)FIle transfer over SHell filesystem
    Sieciowe systemy plikówNetwork File System
    Odzyskiwanie plikówUndelete File System
  Polskie znakiPolskie znaki
  KoloryColors
  Specjalne ustawieniaSpecial Settings
  Baza danych terminali (Terminal databases)Terminal databases

  PLIKIFILES
  DOSTĘPNOŚĆAVAILABILITY
  ZOBACZ TAKŻESEE ALSO
  AUTORZYAUTHORS
  BŁĘDYBUGS
  TŁUMACZENIETŁUMACZENIE
  LicencjaLicense
  Nieoficjalne tłumaczenie licencjiLicense-pl
  Okna zapytaniaQueryBox
  Jak korzystać z pomocyHow to use help
[DESCRIPTION]
OPIS

Midnight Commander jest przeszukiwarką
katalogów/menedżerem plików dla systemów Unixopodobnych[OPTIONS]
OPCJE


-a      Wyłącza używanie symboli graficznych przy
        rysowaniu ramek.

-b      Wymusza wyświetlanie czarno-białe.

-c      Wymusza wyświetlanie w kolorze, zobacz sekcję
        Kolory żeby zasięgnąć szerszej informacji.

-C arg  Używane do wybierania innego koloru, który ma być
        obecny w linii poleceń. Format argumentu arg jest
        opisany w sekcji Kolory.

-d      Wyłącza używanie myszy.

-f      Wyświetla wkompilowane ścieżki, w których
        Mindnight Commander szuka swoich plików.

-k      Resetuje "miękkie" klawisze do ich standardowych
        funkcji z termcap/terminfo. Użyteczne tylko przy
        terminalach HP, kiedy klawisze funkcyjne nie
        działają.

-l plik Zachowuje logi z serwerów ftp do pliku plik.

-P      Przy zakończeniu programu, Midnight Commander
        wydrukuje na ekranie katalog, w którym
        pracowaliśmy na końcu; to w połaczeniu z funkcją
        napisaną poniżej pozwoli ci na przeglądanie
        swoich katalogów i automatyczne przejście do
        tego, w którym byłeś ostatnio (dziękuję Torbenowi
        Fjerdingstadowi i Sergeyowi za wkład w tę funkcję
        oraz za kod źródłowy, który wprowadzili w życie).
użytkownicy basha i zsh:

mc ()
{
        MC=$HOME/tmp/mc$$-"$RANDOM"
        /usr/bin/mc -P "$@" > "$MC"
        cd "`cat $MC`"
        rm "$MC"
        unset MC;
}

użytkownicy tcsh:
alias mc 'setenv MC `/usr/bin/mc -P !*`; cd $MC; unsetenv MC'
        Wiem, że ta funkcja mogłaby być krótsza dla basha
        i zsh, ale małe cudzysłowy nie zaakceptowały by
        zawieszenia programu kombinacją C-z.

-s      Włącza tryb powolnego terminala, w którym program
        nie będzie rysował zbyt obciążających znaków
        graficznych oraz wyłączy opcję weryfikacji.

-t      Używane tylko jeśli kod był skompilowany przy
        użyciu Slanga i terminfo: powoduje, że Midnight
        Commander będzie używać zmiennej środowiskowej
        TERMCAP do pokazywania informacji terminala,
        zamiast informacji w systemowej bazie typów
        terminali.

-u      Wyłącza używanie równoległej powłoki (ma sens
        tylko jeśli Midnight Commander był kompilowany z
        obsługą równoległych powłok).

-U      Włącza użycie jednoczesnego inerpretatora poleceń
        (ma sens tylko jeśli Midnight Commander był
        zbudowany z ustawieniem powłoki w tle jako opcji
        dodatkowej).

-v plik Włącza wbudowany podgląd w celu obejrzenia
        wybranego pliku plik.

-V      Wyświetla wersję programu.

-x      Wymusza włączenie trybu xterm. Używane kiedy
        działa się na terminalach wyposażonych w opcje
        xterm (dwa tryby ekranu i możliwość wysyłania
        myszą sygnałów wyjścia).

Jeśli wybrano, pierwszy katalog używany jest do
wyświetlenia w pierwszym panelu. Drugi wyświetlany jest w
drugim panelu.[Overview]
Opis

Ekran Midnight Commandera podzielony jest na cztery
części. Prawie cały obszar ekranu zajmują dwa panele.
Standardowo przedostatnia od dołu linijka ekranu,
przeznaczona jest do wpisywania poleceń, a ostatnia
pokazuje klawisze funkcyjne. Najwyższy wiersz jest
wierszem menu. Może on być niewidoczny, ale pojawia się
zawsze po kliknięciu w najwyższą linię ekranu, albo po
wciśnięciu klawisza F9.

Midnight Commander pozwala na oglądanie dwóch paneli w tym
samym czasie. Jeden z nich jest panelem aktywnym
(podświetlona linia wyboru znajduje się właśnie w nim).
Niemal wszystkie operacje wykonuje się na panelu aktywnym.
Niektóre operacje, jak np. kopiowanie, zmiana nazwy
używają jako domyślnego miejsca docelowego katalogu
otwartego w panelu nieaktywnym (nie martw się, zawsze
zostaniesz poproszony o potwierdzenie takiej operacji). W
celu zasięgnięcia szerszych informacji zajrzyj do działów
Panele katalogów, Lewe i prawe menu oraz Menu plików.

Możesz wywoływać dowolne komendy systemowe po prostu
wpisując je. Wszystko co piszesz pojawia się w linii
poleceń i po naciśnięciu klawisza Enter zostanie wykonane
przez Midnight Commandera. Przeczytaj sekcję Linia powłoki
i Linia wejściowa klawiszy, żeby nauczyć się więcej na ten
temat.

[Mouse Support]
Obsługa myszy

Midnight Commander obsługuje mysz. Moduł ten jest
uruchamiany wtedy kiedy korzystasz z terminala xterm(1)
(działa nawet wtedy, kiedy łączysz się przez telnet albo
rlogin z innym komputerem z terminala xterm) lub jeśli
korzystasz z linuksa na konsoli z zainstalowanym serwerem
gpm(1).

Kiedy klikniesz lewym przyciskiem na panel z katalogami,
plik zostanie wybrany jako aktywny; jeśli klikniesz prawym
przyciskiem zostanie on zaznaczony [lub odznaczony - w
zależności od jego aktualnego stanu - działanie podobne do
klawisza Insert - przyp. tłumacza].

Podwójne kliknięcie w plik spowoduje wykonanie pliku,
jeśli jest on wykonywalny, a jeśli rozszerzenie pliku jest
rozpoznawane przez Midnight Commander'a i dostępny jest
odpowiedni program, jest on uruchamiany.

Możliwe jest również wykonywanie komend przypisanych
klawiszom funkcyjnym przez kliknięcie w nie.

Jeśli kliknięcie odbędzie się w rejonie górnej lini panelu
z katalogami, zostanie on przewinięty jedną stronę wstecz.
Podobnie kliknięcie na dolną ramkę przewija tekst jedną
stronę do przodu. Ta opcja klikania w ramki działa również
przy przeglądaniu pomocy i przy drzewie katalogów.

Standardowo czas autopowtórzenia przy klikaniu myszą
wynosi 400 milisekund. Tę wartość można zmienić edytując
plik ~/.mc/ini i zmieniając parametr mouse_repeat_rate.

Jeśli używasz Midnight Commandera z obsługą myszy, możesz
"przeszczepiać" kawałki tekstów i używać standardowych
zastosowań myszki (kopiowanie i wklejanie) za pomocą
klawisza Shift.

[Keys]
Klawisze

Niektóre komendy Midnight Commandera wywołuje się
kombinacją klawiszy Control (czasem opisywanego jako CTRL
lub CTL) lub Meta (opisywanego ALT lub nawet Compose). W
tym manualu (pliku pomocy) będziemy używać następujących
kombinacji: C-<klawisz> - znaczy: trzymając klawisz
Control naciśnij <klawisz>. Więc C-f będzie oznaczać:
trzymając Control, naciśnij f.

M-<klawisz> - znaczy, że trzymając klawisz Meta lub alt
naciskamy <klawisz>. Jeśli na twojej klawiaturze nie ma
ani klawisza Alt ani Meta, naciśnij ESC, puść go i wtedy
naciśnij <klawisz> [skutek ten sam, acz jednak użycie
trochę mniej przyjemne i bardziej skomlikowane - przyp.
tłumacza].

Wszystkie linie wprowadzające Midnight Commandera używają
w przybliżeniu tych samych przypisań klawiszy co wersja
GNU edytora Emacs.

Jest wiele sekcji mówiących o klawiszach. Ta następująca
jest najważniejsza.

Sekcja Menu plikówFile Menu opisuje skróty klawiszowe do komend
pojawiających się w menu plików. Ta sekcja zawiera funkcję
klawiszy. Większość z tych komend wywołuje jakąś akcję
przede wszystkim na jednym lub kilku wybranych plikach.

Sekcja Panele katalogoweDirectory Panels opisuje klawisze, które
zaznaczają plik lub pliki jako docelowe do dalszych
działań (akcją jest najczęściej jedna z tych
przedstawionych w menu plików).

Sekcja Komendy linii poleceń wypisuje listę klawiszy,
które są używane do wprowadzania lub edytowania tekstów w
wierszu poleceń. Większość z nich kopiuje nazwy, i inne
tego typu, z panelu katalogów do linii poleceń (żeby
uniknąć ich przepisywania), lub pozwala zwiedzić historię
komend linii poleceń.

Klawisze linii wejściowych są używane do edytowania linii
na wejściu (przy wpisywaniu). Oznacza, to że stosuje się
je zarówno do linii poleceń jak do okien dialogowych.

[Miscellaneous Keys]
Klawisze różne

Jest tu kilka klawiszy, które nie kwalifikują się do
żadnej z wymienionych powyżej grup:

Enter. Jeśli jest wpisany jakiś tekst w linii poleceń (na
samym dole, pod panelami), to wpisana komenda jest
wykonywana. Jeśli nic nie jest wpisane, i linia wyboru
jest na jakimś katalogu, Midnight Commander wykonuje
komendę chdir(2) (zmiana katalogu) do wybranego katalogu i
odświeża zawartość panelu; jeśli linia wyboru jest na
pliku wykonywalnym jest on wykonywany. I wreszcie jeśli
rozszerzenie pliku zgadza się z obługiwanym przez programy
zewnętrzne, które są obsługiwane prze Midnight Commandera,
są one wywoływane z owym programem.

C-l. Od nowa rysuje wszystkie informacje okna Midnight
Commandera.

C-x c. Uruchamia komendę Chmod dla aktualnego pliku lub
zaznaczonych plików.

C-x o. Uruchamia komendę Chown dla aktualnego pliku lub
zaznaczonych plików.

C-x l. Uruchamia komendę dowiązywania.

C-x s. Uruchamia komendę miękkiego dowiązywania.

C-x i. Zmienia aktywny panel.

C-x q. Przełacza nieaktywny panel w tryb "quick view".

C-x !. Wykonuje komendę z zewnętrznego panelu.

C-x h. Uruchamia komendę dodawania katalogów do hotlisty.

M-!. Uruchamia komendę filtrowanego podglądu, opisanego w
sekcji Podgląd.

M-?. Uruchamia komendę szukania pliku.

M-c. Włącza okno dialogowe quick cd (szybkiej zmiany
katalogów)

C-o. Jeśli program jest uruchamiany na konsoli typu Linux
lub FreeBSD lub też na konsoli xterm, pokaże wyjście
ostatnio wykonywanego programu. Jeśli uruchomiono Midnight
Commandera na konsoli type Linux, MC używa zewnętrznego
programu (cons.saver) w celu zachowywyania i odzyskiwania
informacji na ekranie komputera.

Jeśli użycie trybu powłoki w tle jest wkompilowane, możesz
nacisnąć C-o w dowolnej chwili i zostataniesz przeniesiony
z powrotem bezpośrednio do głównego okna Midnight
Commandera, żeby powrócić do wykonywania aplikacji po
prostu naciśnij znów C-o. Jeśli masz zawieszoną aplikację
właśnie przez użycie tego triku, nie będziesz mógł
"odpalać" innych programów spod Midnight Commandera dopóki
nie zamkniesz zawieszonego programu.

Aby dowiedzieć się czegoś na temat polskiech liter w
Midnight Commanderze przeczytaj sekcję Polskie litery.

[Directory Panels]
Panel Katalogów

Sekcja opisuje klawisze, które operują na panelu
katalogów. Jeśli chcesz wiedzieć jak zmienić panele zobacz
sekcję Lewe i prawe menu.

Tab, C-i. Zmienia aktywny panel. Stary panel staje się w
tym momencie aktywnym panelem, a aktywny staje się starym.
Linia wyboru zmienia swoje położenia do aktywnego panelu.

Insert, C-t. Do zaznaczania plików możesz używać klawisza
Insert lub C-t. Żeby odznaczyć plik po prostu zaznacz
jakiś już zaznaczony.

M-g, M-r, M-j. Używane do wybierania najwyższego,
środkowego i najniższego pliku w panelu.

C-s, M-s. Uruchamia szukanie pliku w katalogu na podstawie
jego nazwy. Kiedy szukanie jest aktywne, każde naciśnięcie
klawisza doda jeden znak do poszukiwania zamiast wypisania
go linii poleceń. Jeśli opcja "Show mini-status" jest
włączona, szukany ciąg znaków pojawia się w linii
mini-statusu. Kiedy wpisujemy znak, linia wyboru
przemieszcza się do następnego pliku zaczynającego się od
podanych liter. Klawisze backspace lub del mogą być
używane do poprawiania błędów. Jeśli C-s zostanie
naciśnięte ponownie, Midnight Commander rozpoczyna
szukanie następnego pliku zaczynającego się od podanych
znaków.

M-t. Przełącza tryb wyświetlania do następnego możliwego.
Używając tej opcji łatwo jest przejść szybko z długiego do
krótkiego trybu wyświetlania jak również do tego
zdefiniowanego przez użytkownika.

C-\ (control-backslash). Pokazuje hotlistę katalogów i
zmienia katalog do wybranego przez użytkownika.

+ (plus). Używane do zaznaczania grupy plików. Midnight
Commander zapyta o wyrażenie opisującą grupę. Jeśli opcja
Shell Patterns jest włączona, typ wyrażeń jest bardzo
podobny do tego w powłoce (* dla zera i więcej znaków i ?
dla jednego znaku). Jeśli zaś opcja Shell Patterns jest
wyłączona, sposób zaznaczania plików jest zgodny z
ustawieniami (zobacz ed(1)).

Jeśli wyrażenie zaczyna się od ukośnika (/), wtedy
zaznaczone zostaną katalogi zamiast plików.

\ (backslash). Używaj znaków "\" do odznaczania grupy
plików. Jest to przeciwieństwo klawisza plus.

strzałka do góry, C-p. Przenosi linię wyboru do
poprzedniej pozycji w panelu.

strzałka do dołu, C-n. Przenosi linię wyboru do następnej
pozycji w panelu.

home, a1, M-<. Przenosi linię wyboru do pierwszej pozycji
w panelu.

end, c1, M->. Przenosi linię wyboru do ostatniej pozycji w
panelu.

PageDown, C-v. Przenosi linię wyboru jedną stronę do dołu.

PageUp, M-v. Przenosi linię wyboru jedną stronę do góry.

M-o. Jeśli drugi panel jest zwykłym panelem wyświetlającym
i w aktywnym panelu stoisz na katalogu, drugi panel będzie
pokazywać zawartość akutalnego katalogu (tak jak w Emacsie
kombinacja C-o). Jeśli nie stoisz na katalogu zawartością
drugiego katalogu stanie się katalog o jedno piętro wyższy
od aktualnego.

C-PageUp, C-PageDown. Działa tylko na konsoli typu Linux:
wykonuje przejście do katalogu ".." lub do aktualnie
wybranego, w zależności od kombinacji.

M-y. Przenosi do poprzedniego katalogu w historii, podobne
do kliknięcia myszką. '<'.

M-u. Przechodzi do następnego katalogu w historii, podobne
do kliknięcie myszką w '>'.

M-S-h, M-H. Wyświetla historię katalogów, podobne
działanie do kliknięcia myszką 'v'.

[Shell Command Line]
Linia Powłoki

Ta sekcja opisuje klawisze, które są użyteczne do
efektywniejszego wpisywania podczas podawania komend
powłoki.

M-Enter. Kopiuje nazwę aktualniego wybranego pliku do
linii poleceń.

C-Enter. To samo co M-Enter, działa tylko na konsoli typu
Linux.

M-Tab. Wykonuje dokończenie nazw plików, komend,
zmiennych, użytkowników, nazw hostów za Ciebie.

C-x t, C-x C-t. Kopiuje nazwy zaznaczonych plików (lub
jeśli nie ma zaznaczonych - aktywnego) w aktywnym (C-x t)
lub nieaktywnym panelu (C-x C-t) do linii poleceń.

C-x p, C-x C-p. Pierwsza kombinacja kopiuje pełną ścieżkę
z aktywnego, a druga z nieaktywnego panelu.

C-q. Komenda 'quote' (cytuj) może być używana do
wpisywania do wiersza poleceń znaków, które normalnie
przechwytywane są przez Commandera (tak jak znak '+').

M-p, M-n. Używaj tych klawiszy, żeby przeglądać historię
komend. M-p wyświetla poprzednią, a M-n następną komendę.

M-h. Wyświetla historię aktualnej linii poleceń.

[General Movement Keys]
Podstawowe klawisze ruchu

Przeglądarka pomocy, podgląd plików i drzewo katalogów
używają podobnych klawiszy do przemieszczania. Przez to
akceptują dokładnie te same klawisze. Każde z nich z
resztą traktują je jako swoje własne.

Niektóre partie Midnight Commandera również używają tych
klawiszy, więc niniejsza sekcja może być użyteczna również
dla tych partii.

strzałka w górę, C-p. Przechodzi jedną linię wstecz.

strzałka w dół, C-n. Przechodzi jedną linię naprzód.

Page Up, M-v. Przechodzi jedną stronę wstecz.

Next Page, Page Down, C-v. Przechodzi jedną stronę
naprzód.

Home, A1. Przechodzi do początku.

End, C1. Przechodzi na koniec.

Przeglądarka pomocy i podgląd plików akceptują następujące
klawisze (poza tymi opisanymi powyżej).

b, C-b, C-h, Backspace, Delete. Przechodzi jedną stronę
wstecz.

klawisz spacji. Przechodzi jedną stronę naprzód.

u, d. Przechodzi pół strony naprzód lub wstecz.

g, G. Przechodzi do początku lub do końca.

[Input Line Keys]
Linia wejściowa klawiszy

Linie wejściowe (te używane w linii komend i w oknach
dialogowych), akceptują następujące klawisze:

C-a. umieszcza kursor na początku linii.

C-e. umieszcza kursor na końcu linii.

C-b, move-left. przenosi kursor o jedną pozycję w lewo.

C-f, move-right. przenosi kursor o jedną pozycję w prawo.

M-f. przesuwa kursor o jedno słowo naprzód.

M-b. przesuwa kursor o jedno słowo wstecz.

C-h, backspace. kasuje poprzedni znak.

C-d, Delete. kasuje znak w miejscu kursora (nad nim).

C-@. wstawia zaznaczenie do kasowanie (patrz następne
pozycje).

C-w. kopiuje tekst spomiędzy kursora i zaznaczenia do
bufora i usuwa go z linii poleceń.

M-w. to samo co C-w tylko, że nie usuwa tekstu z linii.

C-y. wstawia spowrotem zawartość wyciętego bufora.

C-k. wycina tekst od kursora do końca linii.

M-p, M-n. Używaj tych klawiszy, żeby przeglądać historię
komend. M-p wyświetla poprzednią, a M-n następną.

M-C-h, M-Backspace. kasuje jedno słowo wstecz
(poprzednie).

M-Tab. Wykonuje dokończenie nazw plików, komend,
zmiennych, użytkowników, nazw hostów za Ciebie.



[Menu Bar]
Linia menu

Linia menu uaktywnia się kiedy wciskasz klawisz F9 lub
kiedy klikasz myszką na najwyższy wiersz ekranu. Linia
menu ma pięć podmenu: "left", "file", command", "options"
i "right" (po polsku to jest "lewe", "plik", "komendy",
"opcje", "prawe").

Lewe i prawe menu pozwalają ci na modyfikacje wyglądu
lewego i prawego panelu katalogowego.

Menu plik pozwala na wykonanie akcji na aktualnym lub
zaznaczonych plikach.

Menu komend mieści w sobie możliwe do wykonania akcje,
które są dużo bardziej globalne i nie mają związku z
aktualnym i zaznaczonymi plikami.

[Left and Right Menus]
Lewe i prawe menu

Wygląd panelu katalogowego może zostać zmieniony poprzez
menu left i right.

[Listing Mode...]
Tryby wyświetlania (Listing modes)

Tryby wyświetlania są używane do zmienia ustawień przy
wyświetlaniu. Dostępne są cztery różne tryby: Full, Brief,
Long i User. Tryb "Full" pokazuje nazwę, rozmiar i czas
modyfikacji pliku.

Tryb "Brief" pokazuje tylko nazwę pliku i ma dwie kolumny
(dzięki temu może pokazywać nawet dwa razy więcej niż inne
tryby). Tryb "Long" jest podobny do wyniku polecenia ls
-l. Zabiera on szerokość całego ekranu.

Jeśli wybierzesz tryb "user" (użytkownika), będziesz mógł
wybrać własny sposób wyświetlania.

Tryb użytkownika musi zaczynać się od określenia wielkości
panelu. Może to być "half" (pół) lub "full" (cały) i
określa, czy ma być widoczny jeden duży panel na cały
ekran czy dwa mniejsze.

Po rozmiarze panelu możesz włączyć tryb dwóch kolumn
panelu. Robi się to dodając liczbę "2" do tekstu formatu.

Po tym wpisujesz już nazwy pól z podaniem opcjonalnej
wielkości. Wszystkie możliwe pola jakich możesz użyć to:

name    wyświetla nazwę pliku.

size    wyświetla wielkość pliku.

bsize   jest alternatywą dla format size. Wyświetla
        rozmiar plików, a dla katalogów po prostu
        wyświetla tekst "SUB-DIR" lub "UP--DIR".

type    wyświetla jednoznakowy opis typu pliku. Ten znak
        jest taki sam co ten wyświetlany prze komendę ls
        z flagą -F. Wyświetlana jest gwiazdka dla plików
        wykonywalnych, ukośnik dla katalogów, małpa (@)
        dla dowiązań, znak równości dla gniazd, minus dla
        urządzeń niestniejących, znak plus dla urządzeń
        istniejących, pionową kreskę (|) dla kolejek
        FIFO, tyldę dla dowiązań symbolicznych, i
        wykrzyknik dla dowiązań wskazujących na
        nieistniejący plik.

mark    Gwiazdka jeśli plik jest zaznaczony, spacja jeśli
        nie jest.

mtime   czas ostatniej modyfikacji pliku.

atime   czas ostatniego dostępu do pliku.

ctime   czas utworzenia pliku.

perm    tekst reprezentujący aktualne uprawnienia do
        pliku.

mode    wartość (cyfrowa) przedstawiająca prawa do pliku.

nlink   liczba dowiązań do pliku. ngid GID (numeryczny).

nuid    UID (numeryczny).

owner   właściciel pliku.

group   grupa pliku.

inode   numer i-węzła pliku.

Możesz również używać następujących znaków dla zmiany
wyświetlania:

space   spacja w formacie wyświetlania.

|       Ten znak jest używany w celu dodania pionowej
        linii od formatu wyświetlania.

Żeby wymusić szerokość pola, po prostu dodaj ':' a potem
ilość znaków jakie chcesz żeby miało pole. Jeśli numer
zaczyna się od '+', to szerokość nie może być mniejsza od
podanej, jeśli program zobaczy, że jest jeszcze trochę
miejsca na ekranie, rozszerzy to pole.

Na przykład tryb Full wyświetla w formacie:

half type name | size | mtime

A format Long wyświetla w formacie:

full perm space nlink space owner space group space size
space mtime space name

A to jest całkiem ładny tryb użytkownika:

half name | size:7 | type mode:3

Panele mogą być również przestawione do następujących
trybów:

Info    Tryb info wyświetla informację o aktualnie
        zaznaczonym pliku i (jeśli to możliwe) o systemie
        plików.

Tree (drzewo)
        Widok drzewa jest całkiem podobny do widoku
        Drzewa katalogówDirectory Tree. Zobacz tę sekcję jeśli chcesz
        się dowiedzieć czegoś na ten temat.

Quick View
        W tym trybie, panele zostaną przełączone w tryb
        zredukowanego podglądu wyświetlającego zawartość
        aktualnego pliku. Jeśli zaznaczysz panel
        (klawiszem tab lub myszką), będziesz miał dostęp
        do większości komend podglądu.[Sort Order...]
Porządek sortowania (Sort order...)

Istnieje osiem porządków sortowania. Przez: nazwę,
rozszerzenie, datę modyfikacje, datę odczytu, datę zmiany,
rozmiar, numeru i-węzła i niesortowane. Porządek
sortowanie możesz wybrać w oknie dialogowym porządku
sortowania. Możliwe jest również wybranie porządku
wstecznego (od tyłu).

Standardowo, katalogi są sortowane przed plikami, ale może
to być zmienione przez opcję Mix all files (mieszaj
wszystkie pliki).

[Filter...]
Filtry (Filter...)

Komenda filtra pozwala ci na podanie rozszerzenia, które
musi być spełnione, żeby pliki były widoczne (na przykład
*.tar.gz). Niezależnie od filtru katalalogi i dowiązania
do katalogów są zawsze pokazywane.

[Reread]
Odśwież (Reread)

Komenda odśwież odświeża widok wszystkich plików w
katalogów. Jest to użyteczne jeśli inny proces stworzył
lub usunął jakiś pliki. Jeśli użyłeś panelu zewnętrznego,
wszystkie informacje zostaną przywrócone do prawdziwego
stanu.[File Menu]
Menu plików (File menu)


Midnight Commander używa klawiszy F1 - F10 jako skrótów
klawiszowych do komend występujących w menu plików. Na
terminalach bez funkcji klawiszowych (F1 - F10) można
używać kombinacji klawisza Escape i numeru ( odpowiednio 1
dla F1, 2 dla F2 itd. )

Menu plików ma następujące komendy (skróty klawiszowe
umieszczone są na dole ekranu):

Pomoc (F1)

Wywołuje wbudowaną przeglądarkę plików pomocy. Wewnątrz
niej można używać klawisza Tab żeby przejść do następnego
dowiązania, Enter żeby przejść do wybranego dowiązania.
Klawisze Spacji i Backspace są używane do poruszania się
naprzód i wstecz na stronach pomocy. Naciśnij klawisz F1
żeby uzyskać pełną listę dostępnych klawiszy w pomocy.

Menu (F2)

Wywołuje menu użytkownika. Menu użytkownika jest łatwym w
użyciu narzędziem służącym do obsługi zewnętrznych
programów i dodatkowych opcji Midnight Commandera.

Podgląd (F3, Shift-F3)

Włącza podgląd aktualnie wybranego pliku. Standardowowo
wywoływany jest wbudowany podgląd plików, ale jeśli opcja
"Use internal view" jest wyłączona, wywoływany jest
zewnętrzny program do poglądu, wskazywany przez zmienną
PAGER. Jeśli jednak zmienna PAGER nie została jeszcze
zdefiniowana, wywoływana jest komenda "view". Jeśli
użyjesz kombinacji klawiszy Shift-F3, pogląd zostanie
wywołany bez jakiegokolwiek formatownia pliku.

Filtrowany podgląd (M-!)

Ta kombinacja klawiszy oczekuje na komendę i jej argument
(argumentem standardowo jest wybrany aktualnie plik), całe
wyjście programu przekierowywane jest do pliku, który
zostaje automatycznie wyświetlony na ekranie w trybie
podglądu.

Edycja (F4)

Aktualnie ta komenda wywołuje edytor vi(1) lub edytor
wybrany w zmiennej środowiskowej, lub wbudowany wewnętrzny
edytor plików jeśli opcja use_internal_edit jest włączona.

Kopiuj (F5)

Włącza okno dialogowe, w którym standardowo znajduje się
ścieżka do katalogu w nieaktywnym panelu, po czym kopiuje
aktualny plik (lub wybrane jeśli wybrano jakiekolwiek) do
katalogu, który wybraliśmy w oknie dialogowym. Podczas
procesu kopiowania możesz go w każdej chwili przerwać
wciskając C-c lub Esc. Żeby dowiedzieć się czegoś więcej
na temat jokerów w ścieżce źródłowej (którymi najczęściej
będą * lub ^\(.*\)$) i innych możliwych określeń w
katalogu docelowym zobacz kategorię "Maski
kopiowania/przenoszenia"

Na niektórych systemach możliwe jest kopiowanie w tle,
robi się to klikając na przycisk backgorund (lub
naciskając kombinację M-b w oknie dialogowym). Background
Jobs jest używane do kontrolowania prac w tle.

Link (C-x l)

Tworzy sztywne dowiązanie do aktualnego pliku.

SymLink (C-x s)

Tworzy symboliczne dowiązanie do aktualnego pliku. Dla
tych, którzy nie wiedzą co to jest dowiązanie: tworzenie
dowiązania do pliku jest tak jak kopiowanie pliku, z tym
tylko, że zarówno plik źródłowy i docelowy reprezentują
ten sam plik. Na przykład, jeśli edytujesz jeden z tych
plików, zmiany, które czynisz pojawiają się w obu plikach.
Niektórzy mówią na dowiązania aliasy lub skróty.

Twarde dowiązanie wydaje się być prawdziwym plikiem. Po
stworzeniu go nie ma możliwości rozróżnienia, który z
plików jest oryginalny, a który jest dowiązaniem. Jest
bardzo ciężko zauważyć, że wskazują one na ten sam plik.
Używaj dowiązań twardych wtedy kiedy nie chcesz tego
wiedzieć.

Dowiązanie symboliczne jest tylko odwołaniem do
oryginalnego pliku. Jeśli ten plik zostanie wyrzucony,
dowiązanie stanie się bezużyteczne. Jest całkiem łatwo
zauważyć, że pliki odnoszą się w gruncie rzeczy do tego
samego. Midnight Commander pokazuje znak "@" przed nazwą
pliku jeśli jest dowiązaniem symbolicznym do innych (poza
katalogami, przed którymi pokazuje tyldę (~)). Oryginalny
plik wskazywany przez dowiązanie jest pokazywany w linii
mini-statusu, jeśli opcja "Show mini-status" jest
włączona. Używaj dowiązań symbolicznych, jeśli chcesz
unikąć problemów z rozpoznawaniem twardych dowiązań.

Zmiana nazwy/przeniesienie (F6)

Włącza okno dialogowe, gdzie standardowo wpisana jest
nazwa katalogu w nieaktywnym panelu, i przenosi aktualnie
wybrany plik (lub zaznaczone jeśli choć jeden jest
zaznaczony) do katalogu wpisanego w oknie dialogowym.
Podczas procesu przenoszenia możesz użyć kombinacji
klawiszy C-c lub ESC, żeby przerwać operację. Po więcej
szczegółów zobacz operację Kopiuj opisaną powyżej.
Większość rzeczy jest całkiem podobna.

Na niektórych systemach możliwe jest przenoszenie w tle,
robi się to klikając na przycisk background (lub
naciskając kombinację M-b w oknie dialogowym). Background
Jobs jest używane do kontrolowania prac w tle.

"Utwórz katalog (F7)"

Włącza menu dialogowe i zakłada katalog o podanej nazwie

Kasuj (F8)

Kasuje aktualnie wybrany lub zaznaczone pliki w aktywnym
panelu. Podczas procesu możesz nacisnąć C-C lub Esc żeby
przerwać operację. [skasowane pliki nie będą jednak
odzyskane - przyp. tłumacza].

Zaznacz grupę (+)

Używane do zaznaczania grupy plików. Midnight Commander
będzie żądał tekstu opisującego grupę plików. Jeśli opcja
Shell Patterns jest włączona, tekst będzie traktowany jako
globalny dla interpretatora (* oznacza zero lub więcej
znaków a ? oznacza jeden znak). Jeśli opcja Shell Patterns
jest wyłączona, wtedy zaznaczanie plików jest robione z
zastosowaniem norm zewnętrznych (zobacz ed (1)).

Żeby zaznaczyć katalogi zamiast plików, tekst musi
zaczynać sie od znaku '/'.

Odznacz grupę (\)

Używane do odznaczania grupy plików. Jest przeciwieństwem
komendy Zaznacz pliki.

Wyjdź (F10, Shift-F10)

Zamyka Midnight Commandera. Shift-F10 jest używany jeśli
używasz "wrappera" powłoki. Shift-F10 nie przeniesie cię
do katalogu, w którym byłeś ostatnio w Midnight
Commanderze, zamiast tego przejdzie do katalogu, z którego
uruchomiłeś program.

[Quick cd]
Szybka zmiana katalogów (Quick cd) M-c

Ta komenda jest bardzo użyteczna, jeśli masz już pełną
linię poleceń, a chcesz przejść do innego katalogu.
Uruchamia ona małe okno dialogowe, w którym podajesz to co
po normalnej komendzie cd po czym naciskasz Enter.
Wszystkie opcje są dokładnie takie same jak we wbudowanej
komendzie cd.

[Command Menu]
Menu komend (Command Menu)

Komenda drzewo katalogów (Directory tree) pokazuje drzewo
katalogów.

Komenda "Find file" szuka pliku spełniającego podane
warunki, natomiast komenda "Swap panels" zamienia
zawartości obu paneli.

Komenda "Panels on/off" pokazuje wyjście ostatniej komendy
interpetatora poleceń. Działa ona tylko na terminalach
typu Linux lub FreeBSD.

Komenda porównywania katalogów (Compare directories) (C-x
d) porównuje zawartości panelu katalogowego z drugim.
Możesz potem użyc Kopiuj (F5) żeby stworzyć dwa dokładnie
identyczne panele. Metoda "quick" porównuje tylko i
wyłącznie rozmiary plików i ich daty. Metoda "thorough"
porównuje pliki bajt po bajcie. Ta metoda działa tylko
wtedy kiedy komputer obsługuje wywołanie mmap(2). Metoda
"size-only" zwraca uwagę tylko na rozmiar plików. Nie ma
dla niej żadnego znaczenia czy plik ma inną datę lub
zawartość, liczy się tylko rozmiar.

Komenda historii komend (Command history) pokazuje listę
wpisanych komend. Ta, którą wybierzesz, jest kopiowana do
linii poleceń. Do historii komend można mieć dostęp
również przy użyciu kombinacji M-p lub M-n.

Komenda hotlisty katalogów (Directory hotlist) (C-\)
pozwala na zmienianie katalogów do tych najczęściej
używanych dużo szybciej.

Komenda panelu zewnętrznego (External panelize) pozwala na
wykonywania programów zewnętrznych i ustawienia zawartości
paneli na to co zwróciła wywołana komenda.

Komenda edycji rozszerzeń plików (Extension file edit)
pozwala na własny wybór programów, które mają być używane
do wykonywania plików z podanymi rozszerzeniami. Komenda
edycji pliku menu (Menu file edit) może być używana do
edytowania menu użytkownika (tego, które pojawia się po
naciśnięciu kombinacji F2).

[Directory Tree]
Drzewo katalogów (Directory Tree)

Możesz wybierać katalogi z drzewa katalogów i Midnight
Commander przejdzie do wybranego przez Ciebie katalogu.

Są dwa sposoby wywoływania drzewa. Prawdziwa komenda
drzewa katalogów jest dostępna z menu komend. Inną metodą
jest wybranie drzewa z menu "lewego" bądź "prawego".

Żeby nie mieć zbyt dużych opóźnień Midnight Commander
skanuje tylko małą ilość katalogów (tę potrzebną w danej
chwili). Jeśli jakiegoś katalogu nie widać przejdź do jego
katalogu nadrzędnego i naciśnij C-r (lub F2).

Możesz używać następujących klawiszy:

Generalne klawisze ruchu są akceptowane.

Enter. W drzewie katalogów, wychodzi z trybu drzewa i
przechodzi znów do trybu zwykłego panelu. W podglądzie
drzewa zmienia katalog w drugim panelu i zostaje w trybie
podglądu drzewa w panelu aktywnym.

C-r, F2 (Rescan). Odświeża aktualny katalog. Używane jeśli
drzewo nie jest już aktualne. Nie pokazuje katalogów,
które już istnieją lub pokazuje te, których już nie ma.

F3 (Forget). Usuwa aktualny katalog z drzewa katalogów.
Używaj tego jeśli chcesz usunąć "śmiecące" i niepotrzebne
katalogi z wyświetlania. Żeby były one znów widoczne
wystarczy nacisnąć F2.

F4 (Static/Dynamic). Przełącza pomiędzy dynamicznym
(standardowo) i statycznym trybem nawigacji.

W trybie statycznym możesz używać strzałek do dołu i do
góry do wybierania katalogu. Wszystkie zwiedzone katalogi
są widoczne.

W trybie dynamicznym możesz używać strzałek w celu
wybrania równorzędnego katalogu, strzałki w lewo żeby
dostać się do katalogu domowego, strzałki w prawo w celu
dostania się do katalogu podrzędnego. Widoczne jest tylko
najbardziej aktualne drzewo katalogów. Drzewo zmienia się
więc dynamicznie podczas twojego przemieszczania.

F5 (Copy). Kopiuje katalog.

F6 (RenMov). Przenosi katalog.

F7 (Mkdir). Tworzy nowy katalog poniżej aktualnego.

F8 (Delete). Kasuje katalog z systemu plików.

C-s, M-s. Szuka natępnego katalogu spełniającego podane
warunki szukania. Jeśli taki nie istnieje te klawisze
spowodują przemieszczenie się o jedną linię w dół.

C-h, Backspace. Kasuje ostatni znak w ciągu znaków do
poszukiwania.

Jakikolwiek inny klawisz. Dodaje klawisz do ciągu znaków
do szukania i przenosi do najbliższego katalogu, którego
nazwa zaczyna się od tych znaków. W podglądzie drzewa
musisz najpierw uaktywnić szukanie naciskając C-s. Ciąg
szukający jest pokazywany w linii mini-statusu.

Następujące klawisze są dostępne tylko w drzewie
katalogów. Nie działają one w poglądzie katalogów.

F1 (Help). Wywołuje podgląd pomocy i pokazuje tę sekcję.

Esc, F10. Wychodzi z drzewa. Nie zmienia katalogów.

Mysz jest obsługiwana. Podwójne kliknięcie ma znaczenie
identyczne do klawisza Enter. Zobacz również sekcję
Obsługa myszy.

[Find File]
Znajdź plik (Find File)

Komenda znajdź plik najpierw pyta się o startowy katalog
do przeszukiwania i o nazwę pliku, który ma być
znaleziony. Wciskając przycisk "Tree" (drzewo) możesz
wybrać katalog startowy z drzewa katalogów.

Pole trzecie akceptuje wszystkie wyrażenia podobne do tych
w egrep(1). Oznacza to, że musisz rozpoczynać znaki o
specjalnym znaczeniu kombinacją "\" np. szukając "strcmp
(" będziesz musiał wpisać "strcmp \(" (bez cudzysłowów
oczywiście).

Możesz zacząć przeszukiwanie naciskając przycisk Ok.
Podczas szukania możesz zatrzymać proces przy użyciu
przycisku Stop i kontynuować po naciśnięciu Startu.

Możesz przeglądać liste znalezionych plików za pomocą
strzałek do dołu i do góry. Komenda Chdir przejdzie do
katalogu aktualnie wybranego. Przycisk Again zapyta się o
nowe parametry do szukania (rozpocznie proces od nowa).
Przycisk Quit kończy przeszukiwanie. Przycisk Panelize
umieści znalezione pliki w aktywnym panelu katalogowym
tak, że będziesz mógł wykonywać na nich standardowe
czynności (podgląd, kopiowanie, przenoszenie, kasowanie
itp.). Po spanelizowaniu wystarczy naciśnąć C-r żeby
powrócić do normalnego trybu.

Możliwe jest posiadanie listy katalogów, których szukanie
plików nie powinno uwzględniać (na przykład możesz chcieć
ominąć przeszukiwanie CDROMu i innych podmontowanych
systemów plików).

Katalogi do omijania powinny być umieszczone w zmiennej
find_ignore_dirs w sekcji Misc twojego pliku ~/.mc/ini.

Składowe katalogów powinny być oddzielone od siebie przez
średniki, to jest przykład:

[Misc]
find_ignore_dirs=/cdrom:/nfs/wuarchive:/afs

Możesz woleć używać panelu zewnętrznego do wykonywania
niektórych operacji. Szukanie pliku jest dobre tylko dla
prostych zapytań. Używając panelu zewnętrznego możesz
dokonywać tak skomplikowanych wyszukiwań jak tylko
pragniesz.

[External panelize]
Panel zewnętrzny

Panel zewnętrzny pozwala ci na wykonywanie zewnętrznych
programów i oglądanie ich wyjścia jako zawartości
aktywnego panelu.

Na przykład, jeśli chcesz aby w aktywnym panelu
wyświetlone zostały wszystkie dowiązania w aktywnym
katalogu, możesz użyć panelu zewnętrznego i następującej
komendy:

find . -type l -print
Zanim komenda zakończy działanie, zawartość katalogów nie
będzie już dłużej zawartością aktualnego katalogu, ale
wszystkie pliki będą symbolicznymi dowiązaniami.

Jeśli chcesz wyświetlić wszystkie pliki, które ściągnąłeś
ze swoich serwerów ftp, możesz użyć tej komendy awk żeby
wypisać nazwę pliku z logów transferu:

awk '$9 ~! /incoming/ { print $9 }' < /usr/adm/xferlog

Możesz zapisać sobie często używane komendy pod jakąś
nazwą, po to żeby móc ich potem używać dużo łatwiej.
Robisz to po prostu wpisując komendę w linii wejściowej, a
potem naciskająć przycisk Add. Potem wpisujesz nazwę, pod
jaką ta komenda ma być widoczna. Następnym razem po prostu
wybierasz tę komendę z listy i nie musisz już wpisywać jej
ponownie.

[Hotlist]
Hotlist

Hotlista katalogów pokazuje nazwy katalogów wprowadzonych
do hotlisty. Midnight Commander zmieni miejsce do tego,
które wskazuje nazwa katalogu. Z hotlisty możesz wyrzucać
już dodane pozycje par nazw/wskazań i dodawać nowe. Dla
dodawania możesz wykorzystać kombinację (C-x h), która
dodaje ścieżkę aktualnego katalogu do hotlisty. Użytkownik
musi tylko podać pod jaką nazwą ma być ten katalog
widoczny.

Powoduje to przechodzenie do częściej przeglądanych
katalogów znacznie szybciej. Możesz używać ciągle wartości
CDPATH opisanej w sekcji Wewnętrzne przemieszczanie.

[Extension File Edit]
Edycja rozszerzeń pliów (Extension File Edit)

Ta komenda wywoła twój edytor na plik ~/.mc/bindings.
Format tego pliku jest następujący (zmienił się on
począwszy od wersji 3.0):

Wszystkie linie zaczynające się od #, lub puste, nie są
brane pod uwagę.

Linie zaczynające się od pierwszej kolumny powinny mieć
następujący format:

słowo kluczowe/wzorzec, tj. wszystko po słowie kluczowym/
dopóki nową linią nie jest wzorzec

słowami kluczowymi mogą być:

shell

        (wzorzec jest wtedy wyrażeniem (bez jokerów), tj.
        pasują wszystkie pliki *wzorzec. Np.: .tar znaczy
        *.tar)

regex

        (wzorzec jest normalnym wyrażeniem)

type

        (plik spełnia wymagania jeśli `file %f` zgadza
        się z wyrażeniem wzorca (nazwa: część z `file %f`
        jest usuwana))

default

        (wszystkie pliki spełniają, nie ważne jaki jest
        wzorzec)

Inne linie powinny zaczynać się od spacji lub tabulacji i
powinny mieć one następujący format:

słowo kluczowe=komenda (bez spacji przy znaku =), gdzie
słowem kluczowym powinno być:

Open (Otwórz) (jeśli użytkownik naciśnie Enter lub kliknie
dwukrotnie), View (Podgląd) (F3), Edit (Edytuj) (F4).

command jest jakąkolwiek jedną linią powłoki, z
zastosowaniem prostego makra.

Cele są przeliczane od góry do dołu (porządek jest tu
istotny). Jeśli jakiejś akcji brakuje, poszukiwanie
kontynuuje się tak jakby wcześniej nie nastąpiła żadna
zgodność (tj. jeśli zgadza się z wzorcem pierwszym i
trzecim i brakuje w pierwszym akcji View, to naciskając F3
użyta będzie akcja z trzeciego wzorca). Opcja default
powinna wychwycić wszystkie możliwe akcje.

[Background Jobs]
Prace w tle (Background jobs)

Pozwalają ci one kontrolować status jakichkolwiek procesów
wykonywanych w tle przez Midnight Commandera (tylko
operacje kopiowania i przenoszenia, mogą być wykonywane w
tle). Z tego menu możesz zastopować, zresetować i "zabić"
proces w tle.

[Menu File Edit]
Edycja menu użytkownika (Menu File Edit)

Menu użytkownika jest bardzo użytecznym menu, które może
być tworzone w sposób dowolny, przez użytkownika. Kiedy
tylko próbujesz coś zrobić przy użyciu tego menu, ładowany
jest plik .mc.menu z aktualnego katalogu, ale tylko wtedy
kiedy jest on w posiadaniu użytkownika lub roota i mamy do
niego prawa zapisu. Jeśli takiego nie ma próbuje się z
plikiem ~/.mc/menu z tymi samymi założeniami, jeśli jego
też nie ma - używa się standardowego pliku systemowego,
który znajduje się w /usr/share/mc/mc.menu.

Format pliku z menu użytkownika jest bardzo prosty. Linie
zaczynające się od czegokolwiek innego niż spacja lub
tabulacja, są traktowane jako wtyczki do menu (aby móc
używać ich potem jako gorących klawiszy, dobrze jest aby
pierwszy znak był literą). Wszystkie linie zaczynające od
spacji lub tabulacji, są komendami, które mają być
wykonane jeśli wtyczka zostanie wybrana.

Kiedy opcja zostaje wybrana, wszystkie komendy należące do
tej opcji kopiowane są do pliku w katalogu tymczasowym
(najczęściej do /usr/tmp), a potem plik jest wykonywany.
Pozwala to użytkownikowi wkładać normalne konstrukcje
powłoki do konstrukcji kodu wykonywanego. Po więcej
informacji zobacz, używania makr.

To jest przykładowy plik mc.menu:

A	Wyrzuć aktualny plik.
	od -c %f

B	Stwórz raport o błędzie i wyślij do roota.
	I=`mktemp ${MC_TMPDIR:-/tmp}/mail.XXXXXX` || exit 1
	vi $I
	mail -s "Błąd Midnight Commandera" root < $I
	rm -f $I

M	Przeczytaj pocztę.
	emacs -f rmail

N	Przeczytaj grupę dyskucyjną.
	emacs -f gnus

J	Skopiuj rekursywnie cały aktualny katalog.
	tar cf - . | (cd %D && tar xvpf -)

= f *.tar.gz | f *.tgz & t n
X       Zdekompresuj skompresowany plik tar.
	tar xzvf %f

Standardowe warunki

Każda opcja może być opatrzona w warunki. Warunek musi
zaczynać się od pierwszej kolumny i od znaku '='. Jeśli
warunek jest prawdziwy, opcja stanie się opcją domyślną.

Składnia warunku: 	= <warunek>
	    lub:	= <warunek> | <warunek> ...
	    lub:	= <warunek> & <warunek> ...

Warunek jest jednym z następujących:

  f <wzorzec>           aktualny plik zgodny z wzorcem?
  F <wzorzec>           plik w drugim panelu zgodny z wzorcem?
  d <wzorzec>           aktualny katalog spełniający wzorzec?
  D <wzorzec>           katalog w drugim panelu spełniający wzorzec?
  t <typ>               aktualny pliku typu typ?
  T <typ>               plik w drugim panelu typu typ?
  ! <warunek>           zaprzeczenie warunku

Wzorzec jest normalnym wzorcem powłoki lub wyrażeniem,
podobnym do wzorca powłoki. Możesz zmienić globalne
ustawienia wzorców powłoki pisząc "shell_patterns=x" w
pierwszej linii menu użytkownika (x jest równe 0 lub 1).

Typ jest jednym lub więcej z podanych znaków:

  n	nie katalog
  r	zwykły plik
  d	katalog
  l	dowiązanie
  c	specjalny znak
  b	specjalny blok
  f	fifo
  s	gniazdo
  x	wykonywalny
  t	zaznaczony

Na przykład 'rlf' oznacza zwykły plik, dowiązanie lub
fifo. Typ 't' jest trochę odmienny ponieważ dotyczy panelu
a nie pliku. Warunek '=t t' jest prawdziwy jeśli są jakieś
zaznaczone pliki w aktywnym panelu, a fałszywy jeśli nie
ma.

Jeśli warunek rozpoczyna się od '=?' zamiast '=' droga
przechodzenia przez warunki będzie pokazywana za każdym
razem kiedy warunek będzie obliczany [przydatne do
wyszukiwania błędów - przyp. tłumacza].

Warunki są obliczane od lewej do prawej. Oznacza to, że
	= f *.tar.gz | f *.tgz & t n
jest liczone tak samo jak
	( (f *.tar.gz) | (f *.tgz) ) & (t n)

To jest prosty przykład zastosowania tych warunków:

= f *.tar.gz | f *.tgz & t n
L	Listuje zawartość skompresowanego archiwum tar
	gzip -cd %f | tar xvf -

Warunki dodania

Jeśli warunek rozpoczyna się od znaku '+' (lub '+?')
zamiast od '=' (lub '=?') jest to warunek dodania. Jeśli
warunek jest prawdziwy, opcja menu będzie dołączona do
menu. Jeśli nie jest prawdziwy, nie będzie ona w nim
zawarty.

Możesz łączyć ze sobą standardowe i dodane warunki
zaczynając warunek od kombinacji '+=' lub '=+' (lub '+=?'
lub '=+?' jeśli chcesz zobaczyć trasę błędów). Jeśli
chcesz użyć różnych warunków, dodanego i standardowego,
możesz poprzedzić wpis menu dwoma wierszami warunkowymi.
Jednym zaczynającym się od znaku '+', a drugim od '='.

Wszelkie komentarze rozpoczynają się od znaku '#'.

[Options Menu]
Menu opcji (Options Menu)

Midnight Commander ma niektóre opcje, które mogą być
włączane lyb wyłączane w różnych oknach dialogowych z tego
menu. Opcja jest włączona jeśli widnieje przed nią
gwiazdka lyb "x".

Komenda Configuration włącza okno dialogowe, z którego
możesz zmienić większość ustawień Midnight Commandera.

Menu Layout pozwala na zmianę wielu ustawień, które mają
znaczący wpływ na to jak MC będzie wyglądał na ekranie.

Menu Confirmation włącza okno dialogowe, w którym możesz
ustawić przy wykonaniu których operacji chcesz być pytany
o potwierdzenie.

Menu Display bits pozwala określić jakiego typu znaki twój
terminal jest w stanie wyświetlić.

Menu Learn Keys pokazuje okno dialogowe, w którym możesz
poznać które klawisze nie działają i w razie problemów
naprawić to.

Menu Virtual FS pokazuje okno, w którym możesz zmienić
niektóre ustawienia dotyczące systemów VFS.

Komenda Save Setup zachowuje wszystkie ustawienia z menu
Lewego, Prawego i Opcji.

[Configuration]
Konfiguracja

Opcje w tym oknie są podzielone na trzy grupy: opcje
panelu (Panel Options), zatrzymaj po uruchomieniu (Pause
after run) i inne opcje (Other Options).

Opcje panelu

Show Backup Files. Standardowo Midnight Commander nie
wyświetla plików kończących się znakiem '~' (tak jak
komenda ls -B w wersji GNU).

Show Hidden Files. Standardowo Midnight Commander
wyświetla wszystkie pliki zaczynające się od kropki (tak
jak ls -a).

Mark moves down. Standardowo kiedy zaznaczasz plik
(zarówno przy użyciu C-t lub klawisza Insert) linia wyboru
przenosi się o jedno w dół.

Drop down menus. Kiedy ta opcja jest włączona, kiedy
naciskasz klawisz F9 menu będzie aktywowane, w przeciwnym
wypadku zostaniesz tylko przeniosiony do tytułów w tym
menu i będziesz musiał wybrać opcję ręcznie przy użyciu
strzałek bądź też przy użyciu pierwszej litery z nazwy
konkretnego menu.

Mix all files. Jeśli ta opcja jest włączona, wszystkie
pliki i katalogi są pomieszane razem. Jeśli zaś jest
wyłączona, katalogi (i dowiązania do nich), są listowane
na początku a pozostałe pliki dopiero za nimi.

Fast directory reload. Standardowo ta opcja jest
wyłączona. Jeśli ją włączysz Midnight Commander będzie
używał triku do sprawdzenia czy zawartość katalogu się
zmieniła. Trik polega na tym, że sprawdza się i-węzeł
katalogu i jeśli się on zmienił to katalog jest ładowany
na nowo. Oznacza to przeładowywanie zawartości panelu
tylko wtedy, kiedy tworzysz lub kasujesz pliki. Jeśli
robisz inne zmiany (rozmiaru, właściciela, uprawnień,
grupy itp.) będziesz musiał ręcznie przeładować widok (np.
używając kombinacji klawiszy C-r).

Zatrzymaj po uruchomieniu

Po wykonaniu komendy, Midnight Commander może zrobić
pauzę, po to abyś mógł spokojnie przejrzeć wyjście
ostatniej komendy. Są trzy możliwe wartości dla tej
zmiennej:

        Nigdy (Never) Oznacza, że nie chcesz widzieć
        wyjścia twojej komendy. Jeśli używasz termianala
        typu Linux lub FreeBSD czy też xterm, będziesz
        mógł jednak zobaczyć jej wyjście naciskając C-o.

        "On dumb terminals" Będziesz miał pauzę po
        uruchomieniu na terminalach, które nie są w
        stanie pokazywać widoku ostatniej komendy (na
        wszystkich terminalach, które nie są xtermami lub
        Linux).

        Zawsze (Always) Program zatrzyma się po wykonaniu
        każdej z twoich komend.

Inne opcje

Operacje weryfikacji (Verbose operation). Przełącza czy
podczas kopiowania, kasowania, przenoszenia plików ma być
pokazywane okno dialogowe pokazujące stopień
zaawansowania. Jeśli masz powolny terminal, możesz chcieć
wyłączyć weryfikację. Jest to wykonywane automatycznie za
ciebie jeśli twój terminal jest wolniejszy niż 9600 bps.

Zliczaj wszystko (Compute totals). Jeśli ta opcja jest
włączona, Midnight Commander zlicza wszytkie bajty plików,
które są przeznaczone do kopiowania, przenoszenia,
kasowania. Spowoduje to wyświetlanie dużo bardziej
zaawansowanego wskaźnika postępu w zamian zmiejszając
trochę prędkość. Ta opcja nie ma żadnego znaczenia jeśli
opcja Verbose operation jest wyłączona.

Wzorce powłoki (Shell patterns). Standardowo komendy
zaznacz (Select), odznacz (Unselect), i filtruj (Filter)
będą używać wyrażeń takich samych jak powłoka. Oznacza to,
że gwiazdka oznacza zero lub więcej znaków, znak zapytania
dokładnie jeden znak, a każdy inny znak sam siebie. Jeśli
ta opcja jest wyłączona, stosowane są te, których używa w
komenda ed(1).

Auto Save Setup. Jeśli ta opcja jest włączona, kiedy
wychodzisz z Midnight Commandera konfiguracja MC zostanie
zachowana automatycznie (bez pytania) do pliku ~/.mc/ini.

Auto menus. Jeśli ta opcja jest włączona, menu użytkownika
będzie włączone na starcie. Użyteczne do budowania menu
dla nie unixowców.

Używaj wewnętrznego edytora (Use internal editor). Jeśli
ta opcja jest włączona, do edycji plików używany jest
wbudowany edytor plików. Jeśli ta opcja jest wyłączona,
używany będzie edytor wybrany w zmiennej EDITOR. Jeśli
żaden edytor nie został wybrany, używany będzie vi(1).
Zobacz sekcję Wewnętrzny edytor plików.

Używaj wewnętrznego podglądu (Use internal viewer). Jeśli
ta opcja jest włączona, wbudowany podgląd pliku jest
używany do oglądania pliku. Jeśli ta opcja jest wyłączona,
używany jest podgląd wybrany w zmiennej PAGER. Jeśli żaden
podgląd nie został wybrany, wywoływana jest komenda view.
Zobacz sekcję Wbudowany podgląd plików.

Dokańczanie: pokaż wszystkie (Complete: show all).
Standardowo Midnight Commander pokazuje wszystkie możliwe
dokończenia jeśli jest ich więcej, kiedy naciśniesz drugi
raz klawisz M-Tab, za pierwszym razem, po prostu dokańcza
to na ile można i wydaje krótki dźwięk. Jeśli chcesz
widzieć wszystkie możliwości po pierwszym naciśnięciu
M-Tab włącz tę opcję.

Obrotowy myślnik (Rotating dash). Jeśli ta opcja jest
włączona, Midnight Commander będzie pokazywał obracający
się myślnik w lewym górnym rogu, jeśli będzie akurat w
trakcie wykonywania jakiegoś procesu.

Lynx-like motion. Jeśli ta opcja jest włączona, możesz
używać strzałek przemieszczenia żeby automatycznie
zmieniać katalog jeśli aktualnie wybrany katalog jest
podkatalogiem, a linia poleceń jest pusta. Standardowo ta
opcja jest wyłączona.

Dowiązania podążające cd (Cd follows links). Ta opcja,
jeśli jest włączona, zmusza Midnight Commandera żeby
podążał za łańcuchem katalogów przy zmienianiu go w panelu
czy za pomocą komendy cd. To jest standardowe zachowanie
basha. Jeśli jest wyłączona, Midnight Commander podąża za
prawdziwą strukturą katalogów, więc cd .. jeśli wszedłeś
do katalogu poprzez dowiązanie, przeniesie cię do
prawdziwego katalogu na dysku, a nie tam gdzie wskazywało
dowiązanie.

Bezpieczne kasowanie (Safe delete). Jeśli ta opcja jest
włączona, nieumyślne kasowanie plików stanie się dużo
trudniejsze. Standardowy wybór w linii potwierdzenia
zmienia się z "Yes" na "No". Standardowo ta opcja jest
wyłączona.

[Layout]
Wygląd (Layout)

Meny wygląd pozwala ci na różne warianty zmieniania
ogólnego wyglądu zewnętrznego ekranu. Możesz wybrać, czy
linia menu, linia poleceń, linia hintów (pomocy) i linia
klawiszy funkcyjnych mają być widoczne. Na konsolach typu
Linux lub FreeBSD możesz wybrać ile linii ma być
pokazywanych na wyjściu okna.

Reszta powierzchni ekranu jest używana przez dwa panele
katalogowe. Możesz wybrać nawet czy panele mają być
ułożone poziomo czy pionowo. Kolejną możliwością jest
zmiana ich standardowej szerokości (bądź wysokości). Jest
ona standardowo równa, ale można to zmienić.

Standardowo cała zawartość panelu katalogowego jest
wyświetlana tą samą barwą, ale możesz zmienić to tak aby
uprawnienia i typy plików były wyświetlane specjalnym
podświetlonym kolorem. Jeśli podświetlanie uprawnień jest
włączone, część pól (ta z uprawnieniami i typami plików)
będzie podświetlona przy użyciu koloru wybranego jako
selected. Jeśli podświetlanie jest włączone, pliki są
kolorowane w zależnośći od swojego typu (np. katalogi,
pliki typu core, wykonywalne, ...).

Jeśli opcja Show Mini-Status jest włączona, jeden wiersz
informacji statusowych na temat aktualnie wybranej rzeczy
w panelu, będzie pokazany na dole panelu.

[Confirmation]
Potwierdzanie (Confirmation)

W tym menu możesz skonfigurować opcje potwierdzania dla
kasowania, zastępowania, wykonywania przez naciśnięcie
klawisza Enter, jak również wychodzenia z programu.

[Display bits]
Wyświetlanie znaków (Display bits)

Używane do konfigurowania zakresu znaków widocznych potem
na ekranie. To ustawienie może być 7-bitowe jeśli twój
terminal obsługuje tylko siedmiobitowe wyjście, ISO-8859-1
wyświetla wszystkie znaki z mapy ISO-8859-1 a pełny 8
bitowy przeznaczony jest dla tych terminali, które radzą
sobie z wyświetlaniem znaków ośmiobitowych.

Zobacz sekcję Polskie znaki, po więcej szczegółów na temat
ich używania w Midnight Commanderze.

[Learn keys]
Nauka klawiszy (Learn keys)

W tym oknie możesz przetestować czy twoje klawisz F1-F20,
Home, End itp. pracują poprawnie na twoim terminalu.
Często nie działają tak, ponieważ bazy danych terminali są
poniszczone.

Przemieszczać się możesz za pomocą klawisza Tab, za pomocą
klawiszy ruchu edytora vi ('h' lewo, 'j' dół, 'k' góra i
'l' prawo) i po tym jak już raz naciśniesz daną strzałkę
(zaznaczy się ona na OK), za ich pomocą również.

Klawisze testujesz po prostu naciskając każdy z nich. Jak
tylko naciśniesz klawisz i pracuje on zupełnie poprawnie,
obok nazwy klawisza powinno pojawić się OK. Kiedy klawisz
jest już sprawdzony, zaczyna pracować normalnie (np. F1
wciśnięty po raz pierwszy po prostu pokaże, że ten klawisz
działa, ale naciśnięty po raz drugi pokaże pomoc). Taka
sama sytuacja powtarza się przy strzałkach. Klawisz Tab
powinien pracować zawsze.

Jeśli niektóre klawisze nie pracują poprawnie, nie
zobaczysz OK obok ich nazwy po naciśnięciu ich. Możesz
chcieć je naprawić. Robisz to najeżdżając na odpowiedni
przycisk dla tego klawisza i naciskając Enter. Pokaże się
wtedy czerwona wiadomość i zostaniesz poproszony o podanie
odpowiedniego klawisza. Jeśli chcesz zrezygnować, po
prostu naciśnij Esc i poczekaj do czasu kiedy wiadomość
zniknie. W przeciwnym wypadku wciśnij klawisz, który sobie
życzysz i również poczekaj na zniknięcie okna.

Kiedy skończysz już ze wszystkimi klawiszami, możesz
nacisnąć Save żeby zachować zmiany do pliku ~/.mc/ini do
sekcji [terminal:TERM] (gdzie TERM jest nazwą twojego
aktualnego terminala) lub po prostu odrzucić je.

[Virtual FS]
Wirtualny system plików (Virtual FS)

Ta opcja daje ci kontrolę nad ustawieniami informacji
wirtualnego systemu plików. Midnight Commander zachowuje w
pamięci informacje związane z niektórymi wirtualnymi
systemami plików, po to żeby kolejne połączenia
przebiegały dużo szybciej (np. ściągane listy katalogów z
serwerów ftp).

Niemniej jednak, żeby mieć dostęp do zawartości
skompresowanego pliku (np. skompresowanego pliku tar)
Midnight Commander musi stworzyć tymczasowy
nieskompresowany plik na twoim dysku.

Dopiero kiedy informacje w pamięci i tymczasowe pliki na
dysku są zgodne z zasobami, możesz chcieć zmienić
parametry informacji znajdujących się w buforze podręcznym
po to, żeby zmniejszyć obciążenie dysku do mninimum albo
do zmaksymalizowania prędkości dostępu do najczęściej
używanych systemów plików.

System plików tar jest całkiem inteligentny jeśli chodzi o
przechowywanie plików: po prostu ściąga wejścia do
katalogów i kiedy chcemy więcej szczegółów o nim to system
je dla nas ściąga.

W rzeczywistości jednak, pliki tar najczęściej trzymane są
jako skompresowane i jako iż natura tych plików nie
pozwala na oglądanie ich bez dekompresji (nie ma tam
widocznych od razu wejść do katalogów), system plików musi
być najpierw zdekompresowany na dysk do pliku tymczasowego
i dopiero potem MC ma do niego dostęp taki jak do
normalnego pliku typu tar.

Teraz, kiedy tak kochamy odwiedzać różne pliki i zwiedzać
systemy plików typu tar na całym dysku, jest całkiem
prawdopodobne, że wyjdziesz z takiego pliku, a po krótkim
czasie będziesz chciał wejdść do niego spowrotem. Ponieważ
dekompresja jest powolna, Midnight Commander będzie robił
kopie plików w pamięci na określony czas, po upływie
którego pliki zostaną skasowane a miejsce zajmowane przez
nie zwolnione. Standardowo ten czas ustawiony jest na
jedną minutę.

System plików FTP trzyma listę katalogów z odwiedzanego
przez nas serwera w buforze podręcznym. Jego ważność
konfigurowana jest za pomocą opcji
ftpfsdirectorycachetimeout. Mała wartość dla tej opcji
może spowolnić wszystkie operacje na systemach ftp
ponieważ każda operacja będzie wymagać kolejnych zapytań
do serwera.

Ponadto możesz zdefiniować serwer proxy dla transferów ftp
i skonfigurować Midnight Commandera tak, aby zawsze go
używał. Zobacz sekcję System plików FTP (FTP File System)
po więcej szczegółów.[Save Setup]
Zapisz ustawienia (Save Setup)

Na starcie Midnight Commander będzie próbował odczytać
opcje startowe z pliku ~/.mc/ini. Jeśli on nie istnieje,
odczyta on konfiguracje z ogólnodostępnego pliku
/usr/share/mc/mc.ini. Jeśli on też nie istnieje MC użyje
swoich domyślnych ustawień.

Komenda Save Setup tworzy plik ~/.mc/ini zachowując
aktualne ustawienia lewego, prawego menu, jak również menu
opcji.

Jeśli właczysz opcję auto save setup, MC zawsze będzie
zachowywał standardowe ustawienie podczas wychodzenia.

Istnieją również ustawienia, które nie mogą być zmienione
z poziomu menu. Dla tych ustawień musisz wyedytować swój
plik konfiguracyjny za pomocą twojego ulubionego edytora.
Zobacz sekcję Specjalne ustawienia po więcej informacji.



[Executing operating system commands]
Wykonywanie poleceń systemu operacyjnego (Executing
operating system commands)

Możesz wykonywać komendy wpisując je bezpośrednio do linii
poleceń Midnight Commandera, lub wybierając program, który
chcesz wykonać za pomocą klawiszy przemieszczenia i
nacisnąć Enter.

Jeśli naciśniesz Enter na pliku, który nie jest
wykonywalny, Midnight Commander sprawdzi rozszerzenie
pliku i porówna je z rozszerzeniami wybranymi w pliku
rozszerzeń (Extensions File). Jeśli jakaś pozycja się
zgadza, wykonywana jest komenda (raczej bardziej
rozszerzone makro) powiązana z tym rozszerzeniem.

[The cd internal command]
Wbudowana komenda cd (The cd internal command)

Komenda cd jest interpretowana przez Midnight Commandera,
nie dokładnie tak samo jak wykonuje to powłoka. Przez to
rozkaz cd nie może zawierać wielu składników makr, które
są standardowo dostępne, jednak niektórych potrafi używać:

Tylda Znak tyldy (~) jest zawsze równoznaczny z wpisaniem
nazwy katalogu domowego. Jeśli po znaku tyldy dodasz jakiś
login użytkownika, zostanie on zastąpiony przez katalog
domowy wybranego użytkownika.

Na przykład, ~guest jest katalogiem domowym użytkownika
guest, podczas kiedy ~/guest jest katalogiem guest w twoim
katalogu domowym.

Poprzedni katalog (Previous directory) Możesz przeskakiwać
do katalogu, w którym byłeś poprzednio, używając
specjalnej nazwy katalogu '-' tak jak: cd -

katalogi CDPATH Jeśli katalog wybrany do przejścia nie
jest w naszym aktualnym katalogu, to Midnight Commander
używa ścieżki w zmiennej CDPATH do szukania w jakimkolwiek
z wymienionych tam katalogów.

Na przykład, możesz ustawić swoją zmienną CDPATH na
katalogi ~/src:/usr/src, pozwalając na zmianę katalogów na
jakikolwiek inny wewnątrz ~/src i /usr/src, z miejsca w
którym jesteś (np. cd linux przeniesie cię do katalogu
/usr/src/linux).

[Macro Substitution]
Obsługa makr (Macro Substitution)


Kiedy używamy menu użytkownika, wykonujemy plik o znajomym
rozszerzeniu, lub wykonujemy komendę z linii poleceń,
możemy użyć kilku bardzo prostych makr.

Są to:

"%f"

        Nazwa aktualnego pliku.

"%d"

        Nazwa aktulnego katalogu.

"%F"

        Nazwa pliku w niewybranym panelu.

"%D"

        Nazwa katalogu w niewybranym panelu.

"%t"

        Aktualnie zaznaczone pliki.

"%T"

        Pliki zaznaczone w nieaktywnym panelu.

"%u" i "%U"

        Podobne w działaniu do %t i do %T jednak z tą
        różnicą, że pliki po ich użyciu zostaną
        odznaczone. Oznacza to, że można ich użyć tylko
        raz w jednym menu, ponieważ potem nie będzie już
        żadnych plików zaznaczonych.

"%s" i "%S"

        Wybiera: zaznaczone pliki jeśli są jakieś, w
        przeciwnym razie aktualny plik.

"%cd"

        To jest specjalne makro, które jest używane do
        zmieniania aktualnego katalogu na wybrany
        katalog, na którego froncie jesteśmy. Jest to
        używane przede wszystkim jako interfejs do
        wirtualnych systemów plików.

"%view"

        To makro jest używane żeby włączać wbudowany
        podgląd plików. Może być ono pojedynczo lub z
        grupą argumentów. Jeśli postanawiasz używać
        któregokolwiek z tych argumentów musisz je
        koniecznie wziąć w nawiasy.

        Argumentami są: ascii aby wymusić podgląd w
        trybie ascii; hex aby wymusić podgląd w trybie
        szesnastkowym; nroff przekazuje podglądowi, że
        powinien interpretować pogrubione i podkreślone
        sekwencje programu nroff; unformated aby
        przekazać podglądowi, żeby nie interpretował
        komend nroff aby zrobić tekst pogrubiony lub
        podkreślony.

"%%"

        Znak %

"%{jakiś tekst}"

        Pyta się o zmienną. Pokazuje się okienko
        wejściowe i tekst wewnątrz klamerek używany jest
        jako zachęta (prompt). Makro jest zastępowane
        tekstem wpisanym przez użytkownika. Użytkownik
        może nacisnąć ESC lub F10 aby anulować. To makro
        nie działa jeszcze w linii poleceń.

[The subshell support]
Obsługa podpowłoki (The subshell support)

Podpowłoka (powłoka w tle) jest opcją, która musi być
wybrana przy kompilacji, działa ona z powłokami: bash,
tcsh i zsh.

Jeśli powłoka w tle jest włączona do komplilacji, Midnight
Commander będzie sobie tworzył kopie twojej powłoki (tej
zdefiniowanej w zmiennej SHELL, a jeśli nie ma, to będzie
czerpał bezpośrednio z pliku /etc/passwd) i odpalał pseudo
terminal, zamiast wywoływać nową powłokę za każdym razem
kiedy wywołujesz komendę, komenda będzie przekazana
powłoce w tle, jak tylko ją napiszesz. To pozwala ci na
zmianę wielu zmiennych, używanie funkcji powłoki i
zdefiniowanych aliasów, które są ważne dopóki nie
wyjdziesz z Midnight Commandera.

Jeśli używasz basha możesz wybrać startowe komendy twojej
powłoki w tle w pliku ~/.mc/bashrc, a ustawienia
klawiatury w ~/.mc/inputrc. Użytkownicy tcsh mogą wstawiać
komendy startowe do pliku ~/.mc/tcshrc.

Jeśli kod powłoki w tle jest użyty, możesz zawiesić
aplikację w dowolnej chwili po prostu naciskając
kombinację C-o i przeskakując spowrotem do Midnight
Commandera, jeśli zawiesisz jakąś aplikację nie będziesz
mógł używać innych zewnętrznych komend zanim nie wyjdziesz
z aplikacji, którą przerwałeś.

Extra dodatkiem do używania powłoki w tle jest to, że
zachęta widoczna w Midnight Commanderze jest tą samą,
którą aktualnie używasz w powłoce.

Zobacz sekcję Opcje po więcej informacji na temat tego,
jak możesz kontrolować powłokę w tle.

[Chmod]
Chmod

Okno Chmod jest używane do zmieniania atrybutów grupy
plików lub katalogów. Może być ono wywołane kombinacją C-x
c.

Okno Chmod ma dwie części - Uprawnienia (Permissions) i
Plik (File)

W sekcji Plik wyświetlana jest nazwa pliku lub katalogu i
jego uprawnienia w formie liczbowej jak również właściciel
i grupa.

W sekcji Uprawnienia jest kilka przycisków, z których
każdy odpowiada za odpowiednie uprawnienie do pliku.
Podczas zmieniania atrybutów, widzisz jak zmienia się
wartość liczbowa w oknie Plik.

Do poruszania pomiędzy okienkami (przyciskami i polami do
zaznaczania) używaj strzałek lub klawisza tab. Aby zmienić
pola lub wcisnąć przycisk używaj klawisza spacji. Możesz
również używać "gorących liter" aby go wybrać (są one
podświetlonymi literami na przyciskach).

Aby uaktywnić wprowadzone zmiany wciśnij Enter.

Kiedy pracujesz z grupą plików, lub katalogów, możesz
kliknąć na bit, który chcesz wybrać lub wyczyścić. Kiedy
już wybrałeś bity, które chcesz zmienić, możesz wcisnąć
jeden z przycisków aktywujących (Set marked lub Clear
marked).

I w końcu, aby wprowadzić dokładnie takie zmiany jak
wybrałeś, użyj przycisku [Set all], który zadziała na
wszystkich wybranych plikach.

[Marked all] włącza tylko zaznaczone atrybuty do wybranych
plików.

[Set marked] włącza zaznaczone bity w atrybutach
wszystkich wybranych plików.

[Clean marked] czyści zaznaczone bity z atrybutów
zaznaczonych plików.

[Set] ustawia atrybuty jednego pliku.

[Cancel] unieważnia komendę chmod.

[Chown]
Chown

Komenda chown jest używana do zmiany właściela/grupy
pliku. Skrótem klawiszowym jest kombinacja C-x o.

[Advanced Chown]
Zaawansowane chown (Advanced Chown)

Zaawansowane chown jest komendą łączącą w sobie komendy
chmod i chown. Możesz za jednym zamachem zmienić atrybuty
i właściela/grupę pliku.

[File Operations]
Operacje na plikach (File Operations)

Kiedy kopiujesz, przenosisz lub kasujesz pliki, Midnight
Commander pokazuje okno opisowe operacji na pliku.
Pokazuje nazwę pliku, na którym aktualnie dokonuje się
operacja. Widoczne są co najwyżej trzy linie postępu.
Pierwsza (file) mówi nam jak duża część pliku została już
przekopiowana. Druga (bytes) mówi jak duża część
wszystkich zaznaczonych plików została przekopiowana jak
do tej pory. Trzecia (count) mówi jaka ilość plików
została już przekopiowana. Jeśli opcja verbose jest
wyłączona, linia file i bytes nie jest pokazywana.

Są dwa przyciski na dole okna dialogowego. Naciskając
przycisk Skip ominiemy resztę aktualnie "ruszanego" pliku.
Naciskając przycisk Abort zatrzymamy całą operację,
pominiemy resztę plików.

Są trzy inne okna dialogowe, które mogą się włączyć
podczas operacji na plikach.

Okno błędów informuje nas o błędach zaistniałych podczas
operacji na pliku. Są w nim trzy możliwości wyboru.
Przycisk Skip mówi żeby pominąć wybrany plik, przycisk
Abort żeby przerwać całą operacją, a Retry aby ponowić
próbę (np. kiedy usunąłeś problem korzystając z innego
terminala).

Okno zastępowania jest pokazywane kiedy próbujesz
przenieść lub przekopiować plik, a taki już w miejscu
docelowym istnieje. Okno pokazuje daty i wielkości obu
plików. Naciśnij przycisk Yes aby nadpisać (zastąpić)
stary plik nowym, No aby pominąć ten plik, alL aby
zastąpić wszystkie pliki, nonE aby nigdy nie zastępować i
Update aby zastąpić ale tylko wtedy kiedy plik źródłowy
jest nowszy niż docelowy. Całą operację możesz przerwać
naciskając przycisk Abort.

Okno rekursywnego kasowania jest pokazywane kiedy
próbujesz skasować katalog, który nie jest pusty. Naciśnij
przycisk Yes aby skasować katalog rekursywnie, No aby
pominąć katalog, alL aby skasować wszystkie katalogi
rekursywnie i nonE aby pominąć wszystkie katalogi, które
nie są puste. Możesz przerwać całą opecją naciskając
przycisk Abort. Jeśli wybrałeś przycisk Yes lub alL
będziesz zapytany o potwierdzenie. Wybierz "yes" tylko
jeśli jesteś pewien, że chcesz skasować wszystko
rekursywnie.

Jeśli zaznaczyłeś pliki, i wykonujesz operacje tylko na
nich, to jeśli operacja się udała zostaną one odznaczone,
te, na których operacja nie przebiegła całkowicie
pomyślnie, pozostaną zaznaczone.

[Mask Copy/Rename]
Maski kopiowania/przenoszenia (Mask Copy/Rename)

Operacje przenoszenia i kopiowania pozwalają ci na
tłumaczenie nazw plików w łatwy sposób. Aby to zrobić,
musisz wybrać odpowiednią maskę źródłową i najczęściej w
nazwie docelowej użyć gwiazdek. Wszystkie pliki pasujące
do maski źródłowej są kopiowane/przenoszone w zgodzie z
maską docelową. Jeśli są jakieś pliki zaznaczone, tylko
one są brane pod uwagę przy wybieraniu plików.

Są jeszcze inne opcje, które możesz ustawić:

Opcja Follow links mówi czy dowiązania i dowiązania twarde
w katalogu źródłowym powinny być przenoszone jako
dowiązania czy też powinna być przegrywana ich zawartość
(plik, na który wskazują).

Opcja Dive into subdirs ... mówi co program ma robić,
kiedy kopiuje się katalog, a taki już istnieje.
Standardowo kopiuje się pliki do wewnątrz już istniejącego
katalogu (dodaje), po włączeniu tej opcji kopiuje się
katalog źródłowy do wnętrza tego katalogu. Może przykład
pomoże:

Chcesz przekopiować zawartość katalogu foo do /bla/foo,
które już istnieje. Normalnie (Dive nie jest włączone), mc
skopiuje to dokładnie do /bla/foo. Po włączeniu tej opcji
zawartość zostanie skopiowana do /bla/foo/foo ponieważ ten
katalog już istnieje.

Opcja Preserve attributes mówi czy zachowywać oryginalne
atrybuty pliku, czasy i jeśli jesteś rootem to nawet
numery UID i GID. Jeśli ta opcja jest wyłączona używana
jest aktualna wartość zmiennej umask.

"Use shell patterns on"

Jeśli opcja obsługi wzorców powłoki jest włączona, możesz
używać znaków '*' i '?' w maskach źródłowych. Działają one
tak jak w powłoce. W masce docelowej możesz używać tylko
'*' i '\<cyfra>'. Pierwsza maska '*' w nazwie docelowej
odnosi sie do pierwszej gwiazdki w masce źródłowej, druga
do drugiej itd. Joker '\1' odnosi się do pierwszego jokera
w masce źródłowej, '\2' odnosi się do drugiego i tak dalej
aż do '\9'. Joker '\0' oznacza pełną nazwę pliku
źródłowego.

Dwa przykłady:

Jeśli maska źródłowa jest "*.tar.gz", a miejscem docelowym
jest "/bla/*.tgz" i plikiem, który ma zostać przekopiowany
jest "foo.tar.gz", to kopią będzie "foo.tgz" w katalogu
"/bla".

Załóżmy, że chcesz zaminieć miejscami nazwę i rozszerzenie
pliku, tak, że plik "plik.c" ma być zmieniony na "c.plik"
itp. Maska źródłowa powinna być następująca: "*.*",
natomiast docelowa: "\2.\1".

"Use shell patterns off"

Kiedy wzorce powłoki są wyłączone, MC nie dokonuje
automatycznego grupowania plików. Musisz użyć
wyrażenia'\(...\)' w masce źródłowej aby zasygnalizować
istnienie jokerów w masce docelowej. Jest to trochę
łatwiejsze, ale też wymaga aby trochę się napisać. Z
drugiej jednak strony, makra są bardzo podobne tych
używanych kiedy wzorce powłoki są włączone.

Dwa przykłady:

Jeśli maską źródłową jest "^\(.*\)\.tar\.gz$", docelową
jest "/bla/*.tgz" i plikiem do przekopiowania jest
"foo.tar.gz", kopią będzie "/bla/foo.tgz".

Załóżmy, że chemy zamienić miejscami nazwę i rozszerzenia,
tak, że plik "plik.c" będzie się nazywał "c.plik" itp.
Maską źródłową powinno być "^\(.*\)\.\(.*\)$", a docelową
"\2.\1".

"Konwersje nazwy (Case Conversions)"

Możesz również zmieniać nazwy plików. Jeśli użyjesz '\u'
lub '\l' w masce docelowej, następny znak będzie
przekonwertowany na duży lub mały, zależnie od podanej
opcji.

Jeśli użyjesz '\U' lub '\L' w masce docelowej, następne
znaki będą zmieniane na małe lub duże (zależnie od opcji),
aż do napotkania znaku '\E' lub następnych '\U', '\L' bądź
też końca linii.

Konwersje '\u' i '\l' mają wyższy priorytet niż '\U' i
'\L'.

Na przykład, jeśli maską źródłową jest '*' (shell patterns
on) lub '^\(.*\)$' (shell patterns off) i maską docelową
jest '\L\u*', nazwa pliku będzie miała pierwszą literę
dużą, ale pozostałe już małe, niezależnie od obecnej
nazwy.

Możesz również używać '\' aby "podkreślić" znak. Na
przykład, '\\' jest backsleshem, a '\*' jest gwiazdką.

[Internal File Viewer]
Wbudowany podgląd plików

Wbudowany podgląd plików pozwala na dwa tryby
wyśmietlania: ASCII i hex. Aby przełączać się pomiędzy
tymi trybami używaj klawisza F4. Jeśli masz zainstalowany
program GNU gzip, będzie on automatycznie używany do
dekompresji plików w przypadku wystąpienia takiej
potrzeby.

Podgląd plików będzie próbował użyć najlepszej metody
zalecanej przez system lub rozszerzenie pliku. Wbudowany
podgląd plików będzie interpretował wiele ciągów znaków, i
włączał podkreślenie lub pogrubienie, powodując tym samym
dużo przyjemniejszy wygląd plików.

Kiedy jesteś w trybie hex, funkcja szukania akceptuje
tekst w cudzysłowach równie dobrze jak wartości
szesnastkowe.

Możesz mieszać ciągi znaków ze stałymi tak jak: "Ciąg"
0xFE 0xBB "więcej tekstu". Ciąg pomiędzy stałymi i
cudzysłowami jest po prostu ignorowany.

Kilka wewnętrznych szczegółów na temat podglądu: Na
systemach, które używają wywołania systemowego mmap(2),
program mapuje pliki zamiast je ładować; jeśli system nie
obsługuje mmap(2) lub plik pasuje do któregoś z wybranych
filtrów, podgląd użyje jego rozszerzalnych buforów, dzięki
temu ładując tylko te części, do których musisz mieć
aktualnie dostęp (dotyczy również plików skompresowanych).

Tu jest lista akcji powiązanych z każdym klawiszem, który
Midnight Commander obsługuje w wewnętrznym poglądzie.

F1 Wywołuje wbudowaną przeglądarkę pomocy.

F2 Przełącza tryb zawijania.

F4 Przełącza tryb wyświetlania.

F5 Idź do linii. Zostaniesz zapytany o numer linii i
zostanie ona wyświetlona na ekranie twojego monitora.

F6, /. Szukaj wyrażeń w dalszej części.

?, Wsteczne wyszukiwanie wyrażenia.

F7 Normalne wyszukiwaniewyszukiwanie w trybie hex.

C-s. Zaczyna normalne szukanie jeśli nie było żadnego
wcześniej, w przeciwnym razie szuka następnego
wystąpienia.

C-r. Zaczyna szukanie wsteczne jeśli jeszcze żadnego nie
było, w przeciwnym razie szuka następnego wystąpienia.

n. Szuka następnego wystąpienia.

F8 Przełącza tryby Raw i Parsed. Pokaże to plik w postaci
takiej w jakiej został znaleziony na dysku, lub jeśli
został wybrany jakiś filtr, bądź też plik spełnia
wymagania w pliku mc.ext, wyświetlane jest to co
przekazuje filtr. Aktualne ustawienie jest zawsze
przeciwne niż to napisane na przycisku, przycisk wskazuje
zawsze to co się stanie po jego naciśnięciu.

F9 Przełącza pomiędzy trybami format i unformat. Kiedy
tryb formatu jest włączony podgląd będzie interpretował
niektóre sentencje i pokazywał tekst pogrubiony i
podkreślony innymi kolorami. Wynika z tego, że przycisk
wskazuje co innego niż jest aktualnie (patrz wyżej).

F10, Esc. Wychodzi z wbudowanego podglądu.

Page Down, space, C-v. Przewija jedną stronę naprzód.

Page Up, M-v, C-b, backspace. Przewija jedną stronę
wstecz.

strzałka w dół. Przewija jedną linię naprzód.

strzałka w górę. Przewija jedną linię wstecz.

C-l. Odświeża ekran.

!. Włącza powłokę w aktualnym katalogu roboczym.

C-f. Przeskakuje do następnego pliku.

C-b. Przeskakuje do poprzedniego pliku.

M-r. Przełącza linijkę.

Możliwe jest poinstruowanie podglądu pliku jak ma
wyświetlać plik, zobacz sekcję Edycja pliku rozszerzeń.[Internal File Editor]
Wbudowany edytor plików

Wbudowany edytor plików ma większość funkcji posiadanych
przez inne edytory pełno-ekranowe. Jest wywoływany po
naciśnięciu klawisza F4 o ile opcja use_internal_edit jest
ustawiona w pliku startowyn. Ma maksymalny rozmiar pliku
wynoszący szesnaście megabajtów i potrafi bez skazy
edytować pliki binarne.

Opcje, które aktualnie posiada to: kopiowanie,
przenoszenie, kasowanie, wycinanie i wklejanie bloków;
klawisz dla klawisza undo; rozciągane menu; wklejanie
plików; definiowanie makr; szukanie i zastępowanie wyrażeń
regularnych (i nasze własne funkcje scanf-printf szukające
i zamieniające); strzałki z Shiftem zaznaczające teksty w
stylu MSW-MAC (tylko dla konsoli typu Linux); przełączanie
trybu wstawiania-zastępowania; opcja pozwalająca na
"przerzucenie" bloku tekstu przez komendę powłoki jak na
przykład indent.

Edytor jest bardzo prosty w użyciu i nie wymaga żadnego
przygotowania. Aby zobaczyć jakie są klawisze po prostu
obejrzyj odpowiednie menu rozwijalne. Inne klawisze to:
przemieszczanie z Shiftem zaznaczające tekst. Ctrl-Ins
kopiuje do pliku cooledit.clip a Shift-Ins wkleja z pliku
cooledit.clip. Shift-Del Wycina do cooledit.clip, a
Ctrl-Del kasuje zaznaczony tekst. Klawisze dokończenia
również dają Enter z automatycznym wcięciem. Podświetlanie
myszą również działa, i możesz je przesłonić i spowodować
normalne zaznaczanie tekstu (takie jak obsługuje terminal)
po prostu trzymając klawisz Shift.

Aby zdefiniować makro, naciśnij Ctrl-R i potem naciśnij
klawisze, które chcesz aby były wykonywane. Naciśnij
ponownie Ctrl-R kiedy skończysz. Możesz również
przyporządkować makro do dowolnego klawisza jaki chcesz
naciskając ten klawisz. Makro jest wykonywane kiedy
naciśniesz Ctrl-A i przyporządkowany klawisz. Makro jest
wykonywane również jeśli naciśniesz klawisz Meta, Ctrl,
lub Esc i wybrany klawisz, jednak tylko jeśli ten klawisz
nie jest używane przez inne funkcje. Raz zdefiniowane,
makro wędruje sobie do pliku .mc/cedit/cooledit.macros w
twoim katalogu domowym. Możesz skasować makro kasując
odpowiednią linię z tego pliku.

F19 sformatuje format C jeśli jest podświetlony. Żeby to
działało, stwórz wykonywalny plik .mc/cedit/edit.indent.rc
w twoim katalogu domowym zawierający poniższe:

#!/bin/sh
/usr/bin/indent -kr -pcs $HOME/.mc/cedit/cooledit.block >& /dev/null
cat /dev/null > $HOME/.mc/cedit/cooledit.error

Możesz używać funkcji scanf do przeszukiwania i
zastępowania formatów znaków w C. Najpierw jest rzuć okiem
na stronę manuala funkcji sscanf i sprintf aby zobaczyć
jaki jest format ciągów i jak on działa. Załóżmy, że
chcesz wszystkie wystąpienia ciągu złożonego z, powiedzmy,
otwartego nawiasu, trzech oddzielonych przecinkami liczb i
nawiasu zamykającego, zastąpić ciągiem złożonym ze słowa
jabłka, trzeciej liczby, słowa pomarańcze i drugiej
liczby. Należy wówczas tak wypełnić okno dialogowe
zastępowania:

 Enter search string
(%d,%d,%d)
 Enter replace string
jabłka %d pomarańcze %d
 Enter replacement argument order
3,2

Ostatnia linia mówi, że w miejscu pierwszego i drugiego
argumentu wyniku mają być użyte trzeci i drugi wejściowy.

Jest również dobrym polecenia włączenie opcji pytania się
przed zamianą, ponieważ zgodność jest znajdowana
kiedykolwiek tylko liczba argumentów znalezionych zgadza
sie z liczbą podanych, co nie zawsze jest prawdziwą
zgodnością. Scanf traktuje również białe znaki jako
elastyczne. Zauważ, że format scanfa % jest również bardzo
użyteczny dla skanowania znaków i białych spacji.

Edytor wyświetla również znaki nieamerykańskie (160+).
Kiedy edytujesz plik binarny, powinieneś ustawić opcję
display bits do 7 bitów w menu opcji, aby utrzymać
przejrzystość odstępów między znakami.

Zobacz sekcję Polskie znaki, aby poznać szczegóły na temat
używania polskich znaków w Midnight Commanderze.

[Completion]
Dokańczanie


Pozwól Midnight Commanderowi pisać za ciebie.

Spróbuj użyć dokończenia na tekście przed aktualną
pozycją. MC próbuje dokończyć tekst jako zmienną (jeśli
tekst zaczyna się od znaku $), nazwę użytkownika (jeśli
tekst zaczyna się od znaku ~), nazwę hosta (jeśli tekst
zaczyna się od znaku @) lub komendę (jeśli jesteś w linii
komend w pozycji gdzie możesz wpisać jakąś komendę,
możliwe dokończenia będą zawierać również zarezerwowane
słowa i wbudowane komendy powłoki). Jeśli żaden z
powyższych warunków nie jest spełniony, próbuje się
dokańczać nazwę pliku.

Nazwa pliku, nazwa użytkownika i hosta, pracuje we
wszystkich liniach wejścia, dokańczanie komend pracuje
tylko w wybranych. Jeśli dokańczanie jest rozbudowane
(jest więcej różnych możliwości), MC wyda krótki dźwięk, a
następna akcja będzie zależeć od wartości zmiennej
Complete: show all w menu konfiguracja. Jeśli jest ona
włączona, zostanie wyświetlona lista wszystkich możliwych
nazw. Właściwą nazwę możesz wybrać za pomocą strzałek a
potem naciskając klawisz Enter na właściwej pozycji.
Możesz także nacisnąć pierwsze litery, którymi różnią się
możliwości aby odrzucić tak dużą część dokończeń jak to
tylko możliwe. Jeśli naciśniesz znowu M-Tab, pokazane
zostaną tylko te pozycje, które zaczynają się od kolejnych
podanych liter. Kiedy nie maja już więcej możliwości, okno
znika, ale możesz je wcześniej schować używając klawiszy
anulujących: Esc, F10 oraz strzałek w lewo i prawo. Jeśli
Complete: show all jest wyłączone, okno z listą włącza się
dopiero wtedy, kiedy naciskasz M-Tab po raz drugi. Za
pierwszym razem MC wydaje tylko krótki dźwięk.

[Virtual File System]
Wirtualny system plików (Virtual File System)

Midnight Commander jest dostarczany z kodem pozwalający na
dostęp do systemów plików. Ten kod nazywany jest
wirtualnym systemem plików. Pozwala on Midnight
Commanderowi manipulować plikami trzymanymi na systemach
nie Unixowych.

Aktualnie Midnight Commander jest wyposażony w niektóre
wirtualne systemy plików (VFS): lokalny system plików,
używany do dostępu do typowych systemów plików Unixowych;
ftpfs używanego do manipulowania plikami na zdalnych
systemach na poprzez protokół FTP; tarfs używany do
manipulania plikami w systemach tar i w skompresowanych
systemach tar; undelfs, używany do odzyskiwania
skasowanych plików na systemach typu ext2 (standardowy
system pracy systemu Linux), fish (do manipulowania
plikami poprzez połączenia powłok takich jak rsh czy ssh)
i w końcu system mcfs (system plików Midnight Commandera),
oparty o sieć.

Kod VFS potrafi interpretować poprawnie wszystkie nazwy
ścieżek i przekazuje je do właściwego systemu plików.
Format używany dla każdego z systemów plików jest opisany
w swojej oddzielnej sekcji.

[FTP File System]
System plików FTP (FTP File System)

Ftpfs pozwala na manipulowanie plikami na zdalnych
komputerach, do normalnego użytku, możesz próbować używać
panelowych komend FTP i dowiązań (dostępnych z linii menu)
lub zmienić ścieżkę bezpośrednio za pomocą zwykłej komendy
cd wyglądającej tak jak poniżej:

/#ftp:[!][użytkownik[:hasło]@]komputer[:port][zdalny
katalog]

Parametry użytkownik, port i zdalny katalog są opcjonalne.
Jeśli wybierzesz element użytkownik Midnight Commander
spróbuje zalogować się na zdalnym komputerze jako zadany
użytkownik, w przeciwnym razie użyje twojego loginu.
Opcjonalne jest również hasło, jeśli jest obecne zostanie
użyte do nawiązania połączenia. To użycie nie jest
zalecane (tak samo jak trzymanie tego w twojej hotliście,
dopóki nie ustawisz odpowiednich uprawnień, aby nikt
niepowołany nie miał do tego dostępu).

Przykłady:

    /#ftp:ftp.nuclecu.unam.mx/linux/local
    /#ftp:tsx-11.mit.edu/pub/linux/packages
    /#ftp:!behind.firewall.edu/pub
    /#ftp:guest@remote-host.com:40/pub
    /#ftp:miguel:xxx@server/pub

Aby połączyć się z serwerem znajdującym się za firewallem,
będziesz musiał użyc przedrostka ftp://! aby wymusić na
Midnight Commanderze używanie serwera proxy do transferu
danch. Serwer proxy definiuje się w oknie dialogowym
wirtualnego systemu plików.

Inną możliwością jest ustawienie opcji Always use ftp
proxy w oknie konfiguracyjnym wirtualnego systemu plików.
Skonfiguruje to program tak, aby zawsze używał serwera
proxy. Jeśli ta zmienna jest ustawiona, program będzie
robił dwie rzeczy: konsultował plik /usr/share/mc.no_proxy
w celu znalezienia linii zawierających nazwy serwerów,
które są lokalne (jeśli nazwa hosta zaczyna się od kropki,
uznaje się, że jest to domena) i sprawdza czy jakieś hosty
bez kropek w nazwie są widoczne bezpośrednio.

Jeśli używasz systemu ftpfs będąc za routerem filtrującym,
który nie pozwala ci na używanie standardowej metody
otwierania plików, możesz chcieć wymusić na programie
używanie trybu passive-open. Aby tego używać ustaw opcję
ftpfs_use_passive_connections w pliku inicjującym.

Midnight Commander przechowuje listę katalogów w buforze
podręcznym. Czas wyrzucania bufora jest ustawiany w oknie
dialogowym Wirtualnego Systemu Plików. To ma śmieszną
właściwość taką, że nawet kiedy wystąpią jakieś zmiany w
katalogu, nie będą one pokazane w strukturze katalogów,
dopóki nie wymusisz tego przy użyciu kombinacji C-r. To
jest dobre rozwiązanie (jeśli myślisz, że to jest bug, to
pomyśl o pracy na zdalnych systemach położonych po drugiej
stronie Atlantyku przy użyciu ftpfs :) ).

[Tar File System]
System plików tar (Tar File System)

System plików tar pozwala na dostęp w trybie
tylko-do-odczytu do plików typu tar i do skompresowanych
plików typu tar, za pomocą komendy chdir. Aby zmienić
katalog na plik tar, możesz zmienić aktualny katalog
używając następującej konstrukcji:

/nazwa_pliku.tar:utar/[katalogu-wewnątrza-archiwum]

Plik mc.ext pozwala już na tworzenie skrótów do plików
tar, oznacza to, że możesz wybrać jakiś plik tar i
nacisnąć enter aby do niego wejść, zobacz sekcję Edycja
pliku rozszerzeń po więcej szczegółów na temat tego jak
zostało to pomyślane.

Przykłady

    mc-3.0.tar.gz#utar/mc-3.0/vfs
    /ftp/GCC/gcc-2.7.0.tar#utar

Późniejszy podaje pełną ścieżkę archiwum tar.[FIle transfer over SHell filesystem]
Transfer plików pomiędzy systemami plików (FIle transfer
over SHell filesystem)


System plików fish jest systemem opartym na sieci, który
pozwala na manipulowanie plikami na obcej maszynie tak
jakby były one lokalne. Aby tego używać, druga strona musi
również mieć ustawiony serwer fish, lub musi mieć powłokę
kompatybilną z bashem.

Aby połączyć się z obcą maszyną, musisz tylko zmienić
katalog do specjalnego katalogu, którego nazwa jest w
następującym formacie:

/#sh:[użytkownik@]komputer[:opcje];/[zdalny-katalog];</em>
Elementy użytkownik, opcje i zdalny katalog są opcjonalne.
Jeśli podasz użytkownika Midnight Commander spróuje
zalogować się na obcy komputer jako zadany użytkownik w
przeciwnym razie użyty zostanie twój login.

Jako opcja może wystąpić 'C' - włącza kompresje i 'rsh' -
włącza rsh zamist ssh. Jeśli zdalny-katalog istnieje, twój
aktualny katalog na zdalnym komputerze będzie ustawiony na
niego.

Przykłady:

    /#sh:onlyrsh.mx:r/linux/local
    /#sh:joe@want.compression.edu:C/private
    /#sh:joe@noncompressed.ssh.edu/private
[Network File System]
Sieciowe systemy plików

Midnight Commander pozwala na obsługę zdalnych systemów i
manipulowanie na ich dyskach, tak jakby były one lokalne.
Żeby to było możliwe druga maszyna musi być uruchomiona
razem z programem mcserv(8).

Żeby podłączyć się do obcego komputera musisz przejść do
katalogu w specjalny sposób opisany poniżej:

mc:[użytkownik@]komputer[:port][katalog]

Użytkownik, port i katalog są opcjami nieobowiązkowymi.
Jeśli podasz użytkownika Midnight Commander spróbuje
zalogować się do systemu zdalnego jako zadany użytkownik,
w przeciwnym wypadku spróbuje użyć twojej aktualnej nazwy
zgłoszeniowej.

Port jest używany jeśli zdalny komputer jest odpalony na
niestandardowych portach (zobacz stronę manuala mcserv(8)
po więcej informacji o portach); i wreszcie jeśli katalog
jest podany, twoim katalogiem domowym na zdalnym
komputerze będzie ten podany.

Przykłady:

    mc:ftp.nuclecu.unam.mx/linux/local
    mc:joe@foo.edu:11321/private

[Undelete File System]
Odzyskiwanie plików

Na systemach Linuksowych, jeśli dodałeś w konfiguracji
opcję przywracania skasowanych plików z systemów ext2,
będziesz w stanie to robić. Odzyskiwanie plików jest
możliwe tylko i wyłącznie na systemach typu ext2.
Przywracany system plików jest tylko nakładką na
bibliotekę ext2fs: odzyskiwanie nazw wszystkich
skasowanych plików i próba uczynienia z nich normalnej
partycji.

Żeby używać tych systemów plików, będziesz musiał przejść
od specjalnego pliku, którego nazwa składa się z
przedrostka "undel:" i nazwy pliku, w której ów plik
rezyduje.

Na przykład, aby odzyskać skasowane pliki z drugiej
partycji pierwszego dysku scsi Linux, będziesz musiał użyć
następującej ścieżki:

    undel:/dev/sda2

Może to chwilkę potrwać zanim pliki zostaną pokazane i
będziesz mógł je normalnie oglądać.

[Polskie znaki]
Polskie znaki

Midnight Commander bardzo dobrze radzi sobie z obsługą
znaków nieamerykańskich (160+) w tym polskich. Ważne jest
aby mieć ustawione polskie znaki na konsoli (tzn. aby
powłoka je obsługiwała). Jeśli używasz basha musisz tylko
ustawić w pliku inputrc ( /etc/inputrc lub ~/.inputrc)
następujące wartości:

set meta-flag on
set convert-meta off
set output-meta on

w pliku /etc/sysconfig/i18n:

SYSFONT=lat2u-16
SYSFONTACM=iso02

natomiast w pliku /etc/sysconfig keyboard:

KEYTABLE=pl

Potem użyj poleceń /sbin/setsysfont i loadkeys pl. [Zwróć
uwagę na to, że te pliki są charakterystyczne dla
dystrybucji RedHat, jeśli masz inną i wiesz jak to
ustawić, to napisz do mnie, a ja to tu dopiszę [ patrz
tłumacz na dole ;)) ]].

Teraz wystarczy już tylko włączyć odpowiednie opcje w menu
opcji (klawisz F9). W menu opcji wybieramy Display bits i
włączamy opcje ISO 8859-1 oraz Full 8 bits input. Potem
zapisujemy konfigurację w opcje | Save setup.

I gotowe - polskie literki działają również w podglądzie i
wbudowanym edytorze plików.

[Colors]
Kolory

Midnight Commander próbuje sprawdzić czy twój terminal
obsługuje kolory używając bazy danych terminali. Czasami
jest to zmieniane przez różne flagi startowe, np. możesz
wymusić wyświetlanie czarno-białe lub kolorowe startując z
opcją odpowiednio -b i -c.

Jeśli program jest skompilowany z menedżerem ekranu Slang
zamiast ncurses, sprawdzi on również wartość zmiennej
COLORTERM. Jeśli jest ustawiona, ma takie samo znaczenie
jak opcja -c.

Możesz wybrać terminale, które zawsze żądają wyświetlania
w kolorze, poprzez dodanie ich do pozycji color_terminals
w sekcji pliku startującego. Uchroni to Midnight
Commandera przed próbami odkrycia typu twojego terminala.
Na przykład
[Colors]
color_terminals=linux,xterm
color_terminals=terminal-name1,terminal-name2...

Program może być skompilowany zarówno z bibliotekami slang
jak i ncurses. Ncurses nie obsługuje metody wymuszania
wyświetlania, zawsze sprawdza w bazie danych terminali.

Midnight Commander umożliwia również zmianę standardowych
barw ekranu. Aktualnie kolory są skonfigurowane przy
użyciu zmiennej MC_COLOR_TABLE w sekcji Colors pliku
startowego.

W sekcji kolorów, standardowa mapa kolorów jest ładowana
ze zmiennej base_color. Możesz wybrać swoją własną mapę
dla terminala poprzez użycie nazwy terminala jako klucza w
tej sekcji. Na przykład:

[Colors]
base_color=
xterm=menu=magenta:marked=,magenta:markselect=,red

Format definicji kolorów jest następujący:

  <słowo kluczowe>=<kolor powierzchni">,<kolor tła>:<słowo kluczowe>= ...

Kolory są opcjonalne, a słowa kluczowe są następujące:
normal, selected, marked, markselect, errors, input,
reverse menu, menusel, menuhot, menuhotsel, gauge; kolory
okien dialogowych: dnormal, dfocus, dhotnormal, dhotfocus;
Kolory pomocy: helpnormal, helpitalic, helpbold, helplink,
helpslink; Kolory podglądu: viewunderline; Specjalne tryby
podświetlenia: executable, directory, link, device,
special. [nie tłumaczyłem nazw z racji tego, że trzeba je
stosować w ich angielskim brzmieniu - jeśli jesteś aż tak
zaawansowany, użyj słownika].

Okna dialogowe mogą mieć następujące kolory: dnormal
używany do normalnego tekstu, dfocus jest kolorem używanym
do wyświetlania aktualnego komponentu, dhotnormal jest
kolorem używanym do odróżnienia klawiszy w normalnych
komponentach, a dhotfocus jest używany do wyświetlania
owych w aktualnie wybranym.

Menu używa tego samego schematu, ale jako nazw kolorów
używa menu, menusel, menuhot i menuhotsel.

Pomoc używa następujących kolorów: helpnormal używany do
normalnego tekstu, helpitalic używa tej samej czcionki,
którą wykorzystuje manual do wyświetlania czcionki typu
italic, helpbold tak samo jak wyżej tylko czcionki są typu
bold, helplink używane dla niewybranych jeszcze dowiązań i
helpslink używane dla już wybranych.

gauge pokazuje kolor wypełnienia pokazywany przy wskaźniku
postępu [ang. gauge], ukazującym ile procent pliku zostało
przekopiowane itp. w graficzny sposób.

Dla trybu wysokiego podświetlania directory jest używane
jako kolor do wyświetlania katalogów; executable dla
plików wykonywalnych; link do wyświetlania dowiązań;
device do wyświetlania plików urządzeń (devices); special
dla plików specjalnych, takich jak gniazda FIFO i IPC;
core dla wyświetlania plików typu core (zobacz również tę
opcję w sekcji Specjalne ustawienia).

Możliwe kolory to: black, gray, red, brightred, green,
brightgreen, brown, yellow, blue, brightblue, magenta,
brightmagenta, cyan, brightcyan, lightgray and white.
[sorry, że ich nazw nie tłumaczyłem, ale używać ich trzeba
w oryginalnym brzmieniu :))].

[Special Settings]
Specjalne ustawienia

Większość ustawień Midnight Commandera może być zmieniana
z poziomu menu. Pomimo tego jest pewna ilość ustawień,
których zmiana możliwa jest jedynie poprzez zmianę w
plikach konfiguracyjnych.

Opcje mogą być ustawione w twoim pliku ~/.mc/ini :

clear_before_exec.

        Standardowo Midnight Commander czyści ekran przed
        wykonaniem komendy. Jeśli chciałbyś widzieć
        wyjście komendy na dole ekranu, wyedytuj twój
        plik ~/mc/ini i zmień pole clear_before_exec na
        0.

confirm_view_dir.

        Jeśli naciskasz F3 na katalogu, normalnie MC
        wchodzi do niego. Jeśli ta opcja ma wartość 1, MC
        zapyta się o potwierdzenie przed wejściem do tego
        katalogu, jeśli masz zaznaczone jakieś pliki.

drop_menus.

        Jeśli ta opcja jest ustawiona, kiedy naciskasz
        klawisz F9, rozciągane menu będzie od razu
        rozłożone, w przeciwnym wypadku znajdziesz się po
        prostu w najwyższym wierszu ekranu traktowanym
        jako menu. Będziesz musiał użyć strzałek lub
        pierwszych literek, aby wybrać konkretne menu.

ftpfs_retry_seconds.

        Wartość jest ilością sekund, przez które Midnight
        Commander będzie czekał cierpliwie zanim
        rozpocznie łączenie się z serwerem ftp od nowa.
        Dzieje się to wtedy kiedy serwer odmówił
        połączenia lub hasło jest nieprawidłowe. Jeśli
        wartość wynosi zero, nie nastąpi próba ponownego
        połączenia z serwerem.

ftpfs_use_passive_connections.

        Standardowo ta opcja jest wyłączona. Powoduje
        ona, że ftpfs otwiera połączenia pasywne dla
        transmisji danych. Jest to używane przez ludzi,
        którzy siedzą za ruterami filtrującymi. Działa to
        tylko wtedy, kiedy nie używasz serwera ftp proxy.

max_dirt_limit.

        Opisuje jak wiele odświeżeń ekranu może być
        maksymalnie ominięte we wbudowanym podglądzie
        plików. Normalnie ta wartość jest ważna, gdyż MC
        automatycznie dostosowuje liczbę odświeżeń do
        liczby naciśniętych klawiszy. Chociaż na bardzo
        wolnych komputerach lub na klawiaturach z szybkim
        powtarzaniem klawiszy, duża wartość mogłaby
        spowodować skoki ekranu i utratę płynności.

        Wydaje się, że wartość 10 dla max_dirt_limit jest
        najlepszym ustawieniem i to jest wartość
        standardowa tej funkcji.

mouse_move_pages.

        Kontroluje czy przewijanie w panelu za pomocą
        myszki odbywa się strona po stronie czy linijka
        po linjce.

mouse_move_pages_viewer.

        Tak samo jak wyżej tylko, że we wbudowanym
        wewnętrznym podglądzie plików.

navigate_with_arrows.

        Jeśli ta opcja jest włączona, możesz używać
        strzałek do automatycznego przemieszczanie się
        pomiędzy katalogami, jeśli linia poleceń jest
        pusta. (dotyczy to strzełek w bok).

nice_rotating_dash

        Jeśli jest włączony, Midnight Commander będzie
        pokazywał w lewym górnym rogu obracający się
        myślnik kiedy będzie wykonywał jakiś proces.

old_esc_mode

        Standardowo Midnight Commander traktuje klawisz
        ESC jako przedrostek (old_esc_mode=0). Jeśli
        włączysz tę opcję (old_esc_mode=1), to klawisz
        ESC będzie przedrostkiem dla innego klawisza, ale
        jeśli ten nie nastąpi, będzie on zinterpretowany
        jako klawisz anulowania (tak jak ESC ESC).


only_leading_plus_minus

        zmienia znaczenia znaków '+', '-', '*' w linii
        komend (wybór, odznaczenie, odwrócenie
        zaznaczenia). Standardowo działają one tylko
        wtedy kiedy linia poleceń jest pusta. Jeśli coś
        jest w niej już napisane, znaki te są traktowane
        jako normalne. Jest to przydatne gdyż najczęściej
        w trakcie pisania nie chcemy zmieniać
        zaznaczenia. Jednak czasami ... - wystarczy
        przestawić tę opcję i klawisze te będą zawsze
        działać. panel_scroll_pages

        Jeśli ustawione (standardowo), panel będzie
        przewijany o połowę za każdym razem kiedy kursor
        dochodzi do dolnej lub górnej linii, w przeciwnym
        wypadku przewijanie będzie się odbywać linia po
        linii.

show_output_starts_shell

        Ta opcja pracuje jeśli nie używasz obsługi
        powłoki w tle. Kiedy użyjesz kombinacji klawiszy
        C-o i ta opcja jest włączona, będziesz miał nową
        powłokę. Jeśli nie, dowolny klawisz przywróci
        znów Midnight Commandera (C-o działa jak
        podgląd).

show_all_if_ambiguous.

        Standardowo Midnight Commander pokazuje wszystkie
        możliwe dokończenia jeśli jest ich więcej i
        naciśnięto kombinację M-Tab po raz drugi, za
        pierwszym razem dokończone zostanie tylko tyle
        ile jest to możliwe i jeśli będzie więcej
        możliwości słychać będzie krótkie bipnięcie.
        Jeśli chcesz widzieć wszystkie możliwe
        dokończenia już po pierwszym naciśnięciu M-Tab,
        zmień tę opcję na 1.

torben_fj_mode

        Jeśli ta opcja jest włączona, klawisze home i end
        będą działały troszkę inaczej w panelach, zamiast
        przemieszczać linię wyboru do pierwszej lub
        ostatniej linii w panelu, będą działały tak jak
        jest to opisane poniżej:

        Klawisz home będzie: przechodził do środkowej
        linii, jeśli jest pod nią; w przeciwnym wypadku
        będzie przechodził do najwyższej linii w panelu,
        jeśli już w niej jest, będzie przechodził do
        pierwszego pliku w panelu.

        Klawisz end ma podobne zastosowanie: przechodzi
        do środkowej linii, jeśli jest nad nią; w
        przeciwnym wypadku przechodzi do najniższej linii
        w panelu, chyba że już się w niej znajduje, wtedy
        przechodzi do ostatniego pliku w panelu.

highlight_mode Standardowo wszystkie informacje w panelach
są wyświetlane tym samym kolorem. Jeśli ta warość jest
ustawiona na 1, to uprawnienia lub tryb będą wyświetlane
przy użyciu podświetlonej barwy, tak aby pokazać
ustawienia dla użytkownika. Tak więc prawa do odczytu,
zapisu i wykonywania będą wyświetlane na żółto (tzn.
kolorem selected). W dodatku jeśli ta zmienna jest
ustawiona na 2, to całe linie są wyświetlane w kolorze
odpowiadającym ich typowi (zobacz sekcję Kolory).
Podświetlenie uprawnień również pracuje w tym trybie.

use_file_to_guess_type

        Jeśli ta zmienna jest ustawiona (standardowo)
        próbuje się dostosować rozszerzenie pliku do tego
        wybranego w pliku mc.ext.

xterm_mode

        Jeśli ta opcja jest włączona (standardowo tak nie
        jest) kiedy przeglądasz plik w panelu drzewa,
        będzie on automatycznie przeładowywał drugi panel
        na zawartość wybranego katalogu.

[Terminal databases]
Baza danych terminali (Terminal databases)

Midnight Commander pozwala ci na naprawienie bazy danych
terminali bez posiadania uprawnień roota. Midnight
Commander szuka w pliku startowym (mc.lib położonego w
katalogach z bibliotekami Midnight Commandera) lub w pliku
~/.mc/ini sekcji "terminal:nazwa-twojego-terminala" i
potem sekcji "terminal:general", każda linia sekcji
zawiera symbol klawisza, który chcesz zdefiniować,
zaczynające się do znaku równości i definicji klawisza.
Możesz użyć kombinacji \E aby reprezentować znak escape i
^x aby reprezentować znak Control-x.

Możliwymi klawiszami symboli są:

f0 do f20     Klawisze funkcyjne f0-f20
bs            backspace
home          klawisz home
end           klawisz end
up            strzałka w górę
down          strzałka w dół
left          strzałka w lewo
right         strzałka w prawo
pgdn          klawisz page down
pgup          klawisz page up
insert        znak insert
delete        znak delete
complete      do dokańczania

Na przykład, aby zdefiniować klawisz insert jako Escape +
[ + O + p, możesz ustawić to pliku ini:

insert=\E[Op

Symbol klawisza complete reprezentuje sekwencję wyjścia
używaną do wywoływania procesu dokańczania, jest to
wywoływane kombinacją M-tab, ale możesz zdefiniować inne
klawisze do wykonywania tych samych funkcji (na tych
klawiaturach z toną fajnych i zupełnie bezużytecznych
klawiszy).



[FILES]
PLIKI


Program będzie pobierał wszystkie swoje informacje ze
zmiennej MCHOME, jeśli jest ona nie ustawiona to znowu
przetwarzany jest katalog /usr.

/usr/share/mc.hlp

        Plik pomocy dla programu.

/usr/share/mc/mc.ext

        Standardowy plik rozszerzeń plików.

~/.mc/bindings

        Własny plik użytkownika, konfiguruje podgląd i
        edycje plików. Ma wyższy priorytet niż plik
        systemowy.

/usr/share/mc/mc.ini

        Standardowy plik setupu do Midnight Commandera,
        używany tylko wówczas, kiedy użytkownik nie ma
        swojego własnego pliku ~/.mc/ini.

/usr/share/mc/mc.lib

        Globalne ustawienia Midnight Commandera.
        Ustawienia w tym pliku są uwzględniane przez
        wszystkie sesje Midnight Commandera, użyteczne do
        definiowania ogólnosystemowych ustawień
        terminali.

~/.mc/ini

        Własny setup użytkownika. Jeśli ten plik jest
        dostępny, jest ładowany zamiast pliku globalnego.

/usr/share/mc/mc.hint

        Plik zawierający podpowiedzi (hints) wyświetlane
        przez program.

/usr/share/mc/mc.menu

        Ten plik zawiera informacje o ogólnosystemowych
        aplikacjach w menu.

~/.mc/menu

        Własny plik menu użytkownika. Jeśli ten plik jest
        obecny jest używany zamiast pliku globalnego.

~/.mc/tree

        Lista katalogów drzewa katalogów i podglądu
        drzewa. Jedna linia jest jednym wejściem. Linie
        zaczynające się od ukośnika są pełnymi nazwami
        katalogów. Linie zaczynające się od numeru mają
        tyle znaków ile poprzedni katalog. Jeśli chcesz
        możesz stworzyć plik używając komendy "find /
        -type d -print | sort > ~/.mc/tree". Normalnie
        nie ma sensu tego czynić, gdyż Midnight Commander
        robi to sam za ciebie.

./.mc.menu

        Lokalny plik zdefiniowany przez użytkownika.
        Jeśli ten plik jest dostępny, jest używany
        zamiast pliku w katalogu domowym i
        ogólnosystemowego.

[AVAILABILITY]
DOSTĘPNOŚĆ

Najnowsza wersja programu jest do zdobycia na serwerze
ftp.nuclecu.unam.mc w katalogu /linux/local i w Europie na
serwerze sunsite.mff.cuni.cz w katalogu /GNU/mc i na
serwerze ftp.teuto.de w katalogu /lmb/mc.[SEE ALSO]
ZOBACZ TAKŻE

ed(1), gpm(1), mcserv(8), terminfo(1), view(1), sh(1),
bash(1), tcsh(1), zsh(1).

Strona Midnight Commander w sieci World Wide Web:
	http://www.ibiblio.org/mc/

[AUTHORS]
AUTORZY

Miguel de Icaza (miguel@roxanne.nuclecu.unam.mx), Janne
Kukonlehto (jtklehto@paju.oulu.fi), Radek Doulik
(rodo@ucw.cz), Fred Leeflang (fredl@nebula.ow.org), Dugan
Porter (dugan@b011.eunet.es), Jakub Jelinek
(jj@sunsite.mff.cuni.cz), Ching Hui
(mr854307@cs.nthu.edu.tw), Andrej Borsenkow
(borsenkow.msk@sni.de), Norbert Warmuth
(nwarmuth@privat.circular.de), Mauricio Plaza
(mok@roxanne.nuclecu.unam.mx), Paul Sheer
(psheer@icon.co.za) and Pavel Machek (pavel@ucw.cz) are
the developers of this package; Alessandro Rubini
(rubini@ipvvis.unipv.it) has been especially helpful
debugging and enhancing the program's mouse support, John
Davis (davis@space.mit.edu) also made his S-Lang library
available to us under the GPL and answered my questions
about it, and the following people have contributed code
and many bug fixes (in alphabetical order):

Adam Tla/lka (atlka@sunrise.pg.gda.pl), alex@bcs.zp.ua
(Alex I. Tkachenko), Antonio Palama, DOS port
(palama@posso.dm.unipi.it), Erwin van Eijk
(wabbit@corner.iaf.nl), Gerd Knorr
(kraxel@cs.tu-berlin.de), Jean-Daniel Luiset
(luiset@cih.hcuge.ch), Jon Stevens
(root@dolphin.csudh.edu), Juan Francisco Grigera, Win32
port (j-grigera@usa.net), Juan Jose Ciarlante
(jjciarla@raiz.uncu.edu.ar), Ilya Rybkin
(rybkin@rouge.phys.lsu.edu), Marcelo Roccasalva
(mfroccas@raiz.uncu.edu.ar), Massimo Fontanelli
(MC8737@mclink.it), Pavel Roskin
(pavel_roskin@geocities.com), Sergey Ya. Korshunoff
(root@seyko.msk.su), Thomas Pundt
(pundtt@math.uni-muenster.de), Timur Bakeyev
(timur@goff.comtat.kazan.su), Tomasz Cholewo
(tjchol01@mecca.spd.louisville.edu), Torben Fjerdingstad
(torben.fjerdingstad@uni-c.dk), Vadim Sinolitis
(vvs@nsrd.npi.msu.su) and Wim Osterholt
(wim@djo.wtm.tudelft.nl).

[BUGS]
BŁĘDY

W pliku TODO dystrybucji znajdziesz informacje na temat
tego, co pozostało jeszcze do zrobienia.

Jeśli chcesz zgłosić kłopoty z programem [błędy w nim],
wyślij e-mail [po angielsku], na adres mc-devel@gnome.org.

Do zgłoszenia błędu dołącz opis problemu, versję programu,
którego używasz (wyświetla ją mc -V), system operacyjny,
na którym pracujesz i jeśli program się wykłada,
chcielibyśmy dostać ślad stosu.[TŁUMACZENIE]
TŁUMACZENIE

Maciej Wojciechowski wojciech@staszic.waw.pl

[main]
 lqwqk     k           k     
 x x x .   x     .     x     
 x x x k lqu wqk k lqw tqk n 
 x x x x x x x x x x x x x x 
 v   v v mqv v v v mqu v v mj
     qqqqqqCommanderqj 

To główny ekran pomocy Midnight Commandera.

Aby dowiedzieć się, jak korzystać z interaktywnej pomocy
naciśnij EnterHow to use help. Możesz też przejść bezpośrednio do spisu
treściContents pomocy.

GNU Midnight Commander został napisany przez autorówAUTHORS.

GNU Midnight Commander jest dostarczany ABSOLUTNIE BEZ
ŻADNEJ GWARANCJIWarranty. Jest on wolnym oprogramowaniem, 
więc dozwolona jest jego redystrybucja na zasadach 
GNU General Public LicenseLicense (jej nieoficjalne tłumaczenie
znajdziesz tutajLicense-pl).

[License]
Licencja

Nieoficjalne polskie tłumacznie znajdziesz tutajLicense-pl.


                GNU GENERAL PUBLIC LICENSE
                   Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.
 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

 Everyone is permitted to copy and distribute verbatim
copies of this license document, but changing it is not
allowed.

                         Preamble

  The licenses for most software are designed to take away
your freedom to share and change it.  By contrast, the GNU
General Public License is intended to guarantee your
freedom to share and change free software--to make sure
the software is free for all its users.  This General
Public License applies to most of the Free Software
Foundation's software and to any other program whose
authors commit to using it.  (Some other Free Software
Foundation software is covered by the GNU Library General
Public License instead.)  You can apply it to your
programs, too.

  When we speak of free software, we are referring to
freedom, not price.  Our General Public Licenses are
designed to make sure that you have the freedom to
distribute copies of free software (and charge for this
service if you wish), that you receive source code or can
get it if you want it, that you can change the software or
use pieces of it in new free programs; and that you know
you can do these things.

  To protect your rights, we need to make restrictions
that forbid anyone to deny you these rights or to ask you
to surrender the rights.  These restrictions translate to
certain responsibilities for you if you distribute copies
of the software, or if you modify it.

  For example, if you distribute copies of such a program,
whether gratis or for a fee, you must give the recipients
all the rights that you have.  You must make sure that
they, too, receive or can get the source code.  And you
must show them these terms so they know their rights.

  We protect your rights with two steps: (1) copyright the
software, and (2) offer you this license which gives you
legal permission to copy, distribute and/or modify the
software.

  Also, for each author's protection and ours, we want to
make certain that everyone understands that there is no
warranty for this free software.  If the software is
modified by someone else and passed on, we want its
recipients to know that what they have is not the
original, so that any problems introduced by others will
not reflect on the original authors' reputations.

  Finally, any free program is threatened constantly by
software patents.  We wish to avoid the danger that
redistributors of a free program will individually obtain
patent licenses, in effect making the program proprietary.
To prevent this, we have made it clear that any patent
must be licensed for everyone's free use or not licensed
at all.

  The precise terms and conditions for copying,
distribution and modification follow.

                GNU GENERAL PUBLIC LICENSE
            TERMS AND CONDITIONS FOR COPYING,
              DISTRIBUTION AND MODIFICATION

  0. This License applies to any program or other work
which contains a notice placed by the copyright holder
saying it may be distributed under the terms of this
General Public License.  The "Program", below, refers to
any such program or work, and a "work based on the
Program" means either the Program or any derivative work
under copyright law: that is to say, a work containing the
Program or a portion of it, either verbatim or with
modifications and/or translated into another language.
(Hereinafter, translation is included without limitation
in the term "modification".)  Each licensee is addressed
as "you".

Activities other than copying, distribution and
modification are not covered by this License; they are
outside its scope.  The act of running the Program is not
restricted, and the output from the Program is covered
only if its contents constitute a work based on the
Program (independent of having been made by running the
Program).  Whether that is true depends on what the
Program does.

  1. You may copy and distribute verbatim copies of the
Program's source code as you receive it, in any medium,
provided that you conspicuously and appropriately publish
on each copy an appropriate copyright notice and
disclaimer of warranty; keep intact all the notices that
refer to this License and to the absence of any warranty;
and give any other recipients of the Program a copy of
this License along with the Program.

You may charge a fee for the physical act of transferring
a copy, and you may at your option offer warranty
protection in exchange for a fee.

  2. You may modify your copy or copies of the Program or
any portion of it, thus forming a work based on the
Program, and copy and distribute such modifications or
work under the terms of Section 1 above, provided that you
also meet all of these conditions:

    a) You must cause the modified files to carry
prominent notices stating that you changed the files and
the date of any change.

    b) You must cause any work that you distribute or
publish, that in whole or in part contains or is derived
from the Program or any part thereof, to be licensed as a
whole at no charge to all third parties under the terms of
this License.

    c) If the modified program normally reads commands
interactively when run, you must cause it, when started
running for such interactive use in the most ordinary way,
to print or display an announcement including an
appropriate copyright notice and a notice that there is no
warranty (or else, saying that you provide a warranty) and
that users may redistribute the program under these
conditions, and telling the user how to view a copy of
this License.  (Exception: if the Program itself is
interactive but does not normally print such an
announcement, your work based on the Program is not
required to print an announcement.)

These requirements apply to the modified work as a whole.
If identifiable sections of that work are not derived from
the Program, and can be reasonably considered independent
and separate works in themselves, then this License, and
its terms, do not apply to those sections when you
distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a
work based on the Program, the distribution of the whole
must be on the terms of this License, whose permissions
for other licensees extend to the entire whole, and thus
to each and every part regardless of who wrote it.

Thus, it is not the intent of this section to claim rights
or contest your rights to work written entirely by you;
rather, the intent is to exercise the right to control the
distribution of derivative or collective works based on
the Program.

In addition, mere aggregation of another work not based on
the Program with the Program (or with a work based on the
Program) on a volume of a storage or distribution medium
does not bring the other work under the scope of this
License.

  3. You may copy and distribute the Program (or a work
based on it, under Section 2) in object code or executable
form under the terms of Sections 1 and 2 above provided
that you also do one of the following:

    a) Accompany it with the complete corresponding
machine-readable source code, which must be distributed
under the terms of Sections 1 and 2 above on a medium
customarily used for software interchange; or,

    b) Accompany it with a written offer, valid for at
least three years, to give any third party, for a charge
no more than your cost of physically performing source
distribution, a complete machine-readable copy of the
corresponding source code, to be distributed under the
terms of Sections 1 and 2 above on a medium customarily
used for software interchange; or,

    c) Accompany it with the information you received as
to the offer to distribute corresponding source code.
(This alternative is allowed only for noncommercial
distribution and only if you received the program in
object code or executable form with such an offer, in
accord with Subsection b above.)

The source code for a work means the preferred form of the
work for making modifications to it.  For an executable
work, complete source code means all the source code for
all modules it contains, plus any associated interface
definition files, plus the scripts used to control
compilation and installation of the executable.  However,
as a special exception, the source code distributed need
not include anything that is normally distributed (in
either source or binary form) with the major components
(compiler, kernel, and so on) of the operating system on
which the executable runs, unless that component itself
accompanies the executable.

If distribution of executable or object code is made by
offering access to copy from a designated place, then
offering equivalent access to copy the source code from
the same place counts as distribution of the source code,
even though third parties are not compelled to copy the
source along with the object code.

  4. You may not copy, modify, sublicense, or distribute
the Program except as expressly provided under this
License.  Any attempt otherwise to copy, modify,
sublicense or distribute the Program is void, and will
automatically terminate your rights under this License.
However, parties who have received copies, or rights, from
you under this License will not have their licenses
terminated so long as such parties remain in full
compliance.

  5. You are not required to accept this License, since
you have not signed it.  However, nothing else grants you
permission to modify or distribute the Program or its
derivative works.  These actions are prohibited by law if
you do not accept this License.  Therefore, by modifying
or distributing the Program (or any work based on the
Program), you indicate your acceptance of this License to
do so, and all its terms and conditions for copying,
distributing or modifying the Program or works based on
it.

  6. Each time you redistribute the Program (or any work
based on the Program), the recipient automatically
receives a license from the original licensor to copy,
distribute or modify the Program subject to these terms
and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights
granted herein.  You are not responsible for enforcing
compliance by third parties to this License.

  7. If, as a consequence of a court judgment or
allegation of patent infringement or for any other reason
(not limited to patent issues), conditions are imposed on
you (whether by court order, agreement or otherwise) that
contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you
cannot distribute so as to satisfy simultaneously your
obligations under this License and any other pertinent
obligations, then as a consequence you may not distribute
the Program at all.  For example, if a patent license
would not permit royalty-free redistribution of the
Program by all those who receive copies directly or
indirectly through you, then the only way you could
satisfy both it and this License would be to refrain
entirely from distribution of the Program.

If any portion of this section is held invalid or
unenforceable under any particular circumstance, the
balance of the section is intended to apply and the
section as a whole is intended to apply in other
circumstances.

It is not the purpose of this section to induce you to
infringe any patents or other property right claims or to
contest validity of any such claims; this section has the
sole purpose of protecting the integrity of the free
software distribution system, which is implemented by
public license practices.  Many people have made generous
contributions to the wide range of software distributed
through that system in reliance on consistent application
of that system; it is up to the author/donor to decide if
he or she is willing to distribute software through any
other system and a licensee cannot impose that choice.

This section is intended to make thoroughly clear what is
believed to be a consequence of the rest of this License.

  8. If the distribution and/or use of the Program is
restricted in certain countries either by patents or by
copyrighted interfaces, the original copyright holder who
places the Program under this License may add an explicit
geographical distribution limitation excluding those
countries, so that distribution is permitted only in or
among countries not thus excluded.  In such case, this
License incorporates the limitation as if written in the
body of this License.

  9. The Free Software Foundation may publish revised
and/or new versions of the General Public License from
time to time.  Such new versions will be similar in spirit
to the present version, but may differ in detail to
address new problems or concerns.

Each version is given a distinguishing version number.  If
the Program specifies a version number of this License
which applies to it and "any later version", you have the
option of following the terms and conditions either of
that version or of any later version published by the Free
Software Foundation.  If the Program does not specify a
version number of this License, you may choose any version
ever published by the Free Software Foundation.

  10. If you wish to incorporate parts of the Program into
other free programs whose distribution conditions are
different, write to the author to ask for permission.  For
software which is copyrighted by the Free Software
Foundation, write to the Free Software Foundation; we
sometimes make exceptions for this.  Our decision will be
guided by the two goals of preserving the free status of
all derivatives of our free software and of promoting the
sharing and reuse of software generally.

[Warranty]
                       NO WARRANTY

  11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE,
THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT
PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED
IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS TO THE
QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.
SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR
AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY
OTHER PARTY WHO MAY MODIFY AND/OR REDISTRIBUTE THE PROGRAM
AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR
CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY
TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED
BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO
OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR
OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
DAMAGES.

               END OF TERMS AND CONDITIONS

      How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of
the greatest possible use to the public, the best way to
achieve this is to make it free software which everyone
can redistribute and change under these terms.

  To do so, attach the following notices to the program.
It is safest to attach them to the start of each source
file to most effectively convey the exclusion of warranty;
and each file should have at least the "copyright" line
and a pointer to where the full notice is found.

<one line to give the program's name and a brief idea of
what it does.>
Copyright (C) <year>  <name of author>

    This program is free software; you can redistribute it
and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation;
either version 2 of the License, or (at your option) any
later version.

    This program is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY; without even the
implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License
for more details.

    You should have received a copy of the GNU General
Public License along with this program; if not, write to
the Free Software Foundation, Inc., 51 Franklin Street,
Fifth Floor, Boston, MA  02110-1301  USA

Also add information on how to contact you by electronic
and paper mail.

If the program is interactive, make it output a short
notice like this when it starts in an interactive mode:

Gnomovision version 69, Copyright (C) year name of author
Gnomovision comes with ABSOLUTELY NO WARRANTY; for details
type `show w'.  This is free software, and you are welcome
to redistribute it under certain conditions; type `show c'
for details.

The hypothetical commands `show w' and `show c' should
show the appropriate parts of the General Public License.
Of course, the commands you use may be called something
other than `show w' and `show c'; they could even be
mouse-clicks or menu items--whatever suits your program.

You should also get your employer (if you work as a
programmer) or your school, if any, to sign a "copyright
disclaimer" for the program, if necessary.  Here is a
sample; alter the names:

  Yoyodyne, Inc., hereby disclaims all copyright interest
in the program `Gnomovision' (which makes passes at
compilers) written by James Hacker.

  <signature of Ty Coon>, 1 April 1989
  Ty Coon, President of Vice

This General Public License does not permit incorporating
your program into proprietary programs.  If your program
is a subroutine library, you may consider it more useful
to permit linking proprietary applications with the
library.  If this is what you want to do, use the GNU
Library General Public License instead of this License.

[License-pl]
Nieoficjalne tłumaczenie licencji

Uwaga: To jest nieoficjalne tłumaczenie Powszechnej
Licencji Publicznej GNU na język polski. Nie zostało
opublikowane przez Free Software Foundation i pod względem
prawnym nie stanowi warunków rozpowszechniania
oprogramowania stosującego GNU GPL -- ustanawia je
wyłącznie oryginalny angielski tekst licencji GNU
GPLLicense. Tłumaczenie pochodzi ze strony
http://www.linux.org.pl/


           Powszechna Licencja Publiczna GNU
                Wersja 2, czerwiec 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.
 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

  Zezwala się na kopiowanie i rozpowszechnianie wiernych
kopii niniejszego dokumentu licencyjnego, jednak bez prawa
wprowadzania zmian. 

                     Preambuła

  Większość licencji na oprogramowanie pomyślana jest po
to, aby odebrać użytkownikowi możliwość swobodnego
udostępniania innym i zmieniania danego software'u.
Natomiast w wypadku Powszechnej Licencji Publicznej GNU
(GNU General Public License, GPL) celem jest
zagwarantowanie użytkownikowi swobody udostępniania i
zmieniania tego bezpłatnego oprogramowania, a więc danie
pewności, iż oprogramowanie jest wolno dostępne dla
wszystkich użytkowników. Niniejsza Powszechna Licencja
Publiczna dotyczy większości oprogramowania wydawanego
przez Fundację Wolnego Oprogramowania (Free Software
Foundation) oraz wszelkich innych programów, których
autorzy zobowiązują się do jej stosowania. (Niektóre
rodzaje oprogramowania wydawanego przez Fundację objęte są
Powszechną Licencją Publiczną GNU dla Bibliotek, GNU
Library General Public License). Użytkownik może stosować
ją również do swoich programów.

  Mówiąc o wolnym oprogramowaniu mamy na myśli swobodę, a
nie cenę. Nasze Powszechne Licencje Publiczne wprowadzono
po to, aby zapewnić Państwu swobodę rozpowszechniania
kopii tego oprogramowania (i - jeśli ktoś chce -
pobierania za tę usługę opłaty), jak również aby
udostępnić kod źródłowy oraz umożliwić dokonywanie zmian
tego oprogramowania lub wykorzystywania jego fragmentów w
nowych, wolnych programach. Nie bez znaczenia jest też
sama możliwość dotarcia do Państwa z informacją o
wszystkich tych udogodnieniach.

  W celu ochrony praw użytkownika jesteśmy zmuszeni
wprowadzać ograniczenia zabraniające komukolwiek
kwestionowanie jego praw albo sugerowanie rezygnacji z
tych praw. Ograniczenia te sprowadzają się do pewnych dla
Państwa obowiązków w przypadku rozpowszechniania przez Was
kopii naszego oprogramowania bądź dokonywania w nim zmian.

  Na przykład, jeśli rozprowadzacie Państwo kopie takiego
programu, niezależnie czy gratisowo, czy za opłatą,
musicie Państwo odbiorcy udzielić wszelkich tych praw,
jakie mieliście sami. Musicie zapewnić mu również
otrzymanie kodu źródłowego (lub możliwość otrzymania) oraz
przedstawić niniejsze Warunki, aby mógł on poznać swoje
prawa.

  Ochrona Państwa praw przebiega w dwóch etapach:

  1. zastrzegamy prawo własności autorskiej do
oprogramowania,
  
  2. oferujemy Państwu niniejszą licencję, która daje Wam
sankcjonowane prawem zezwolenie na kopiowanie,
rozpowszechnianie i/lub modyfikowanie tego oprogramowania.

  Ponadto dla ochrony tak autora, jak i naszej, pragniemy
mieć pewność, że każdy zrozumie, iż na niniejsze wolne
oprogramowanie nie udziela się gwarancji. W razie
dokonania w nim przez kogoś modyfikacji i puszczenia dalej
do obrotu, pragniemy, aby dalsi odbiorcy zdawali sobie
sprawę z tego, że problemy wprowadzone przez inne osoby
nie są wyrazem oryginalnych działań twórców.

  I rzecz ostatnia: każdemu wolnemu programowi stale
zagrażają patenty na oprogramowanie. Naszym pragnieniem
jest unikanie takiego niebezpieczeństwa, kiedy
redystrybutorzy wolnego programu indywidualnie uzyskują
prawa patentowe, nadając tym samym programowi charakter
prawnie zastrzeżony. W celu zapobieżenia takim zjawiskom
jednoznacznie wyjaśniliśmy, że każdy patent musi być
wydawany albo dla swobodnego użytku przez wszystkich, albo
nie wydawany wcale.

  Poniżej podajemy dokładne zasady i warunki kopiowania,
rozpowszechniania i modyfikowania.


            ZASADY I WARUNKI KOPIOWANIA,
          ROZPOWSZECHNIANIA I MODYFIKOWANIA

  0. Niniejsza Licencja dotyczy programów i innych prac,
na których umieszczona jest pochodząca od właściciela praw
autorskich informacja, że dany program lub praca może być
rozpowszechniana na warunkach niniejszej Powszechnej
Licencji Publicznej. Używane poniżej słowo "Program"
oznacza właśnie takie programy lub prace, zaś określenie
"praca oparta na Programie" dotyczy albo Programu, albo
pochodzącej od niego pracy w rozumieniu prawa autorskiego,
to jest pracy zawierającej Program lub jego część
dosłowną, bądź zmodyfikowaną i/lub przełożoną na inny
język. (W dalszym ciągu niniejszego, pojęcie przekładu
włącza się bez ograniczeń do terminu "modyfikacja"). Do
każdego licencjobiorcy będziemy zwracać się "per Ty".

  Niniejsza Licencja nie obejmuje działań innych niż
kopiowanie, rozprowadzanie i modyfikowanie - nie mieszczą
się one w jej zakresie. Czynność używania Programu nie
jest poddana ograniczeniom, a produkty uzyskane z Programu
objęte są Licencją tylko wtedy, gdy ich treść stanowi
pracę opartą na Programie (niezależnie od stworzenia jej
przy użyciu Programu). To, czy fakt taki jest prawdą,
zależy od tego, co dany Program wykonuje.

  1. Możesz kopiować i rozprowadzać w dowolnych mediach
wierne kopie kodu źródłowego Programu w otrzymanej formie
pod warunkiem, że w widoczny sposób i odpowiednio podasz
na każdej kopii właściwą informację o prawie autorskim i
zrzeczenie się uprawnień z tytułu gwarancji; wszelkie
napisy informacyjne na temat Licencji i faktu
nieudzielania gwarancji musisz chronić przed uszkodzeniem,
zaś wszystkim innym odbiorcom Programu musisz wraz z
Programem wręczać egzemplarz niniejszej Licencji. 

  Możesz pobierać opłatę za fizyczną czynność przekazania
kopii i według własnej decyzji możesz za opłatą proponować
ochronę gwarancyjną.

  2. Możesz modyfikować swoją kopię czy kopie Programu
oraz dowolne jego części, tworząc przez to pracę opartą na
Programie, jak również kopiować i rozprowadzać takie
modyfikacje i pracę na warunkach podanych w pkt.1 powyżej
- pod warunkiem przestrzegania całości poniższych wymogów:

    a) Musisz spowodować umieszczenie na zmodyfikowanych
plikach widocznej informacji o tym, że dane pliki zostały
przez ciebie zmienione, wraz z datą dokonania zmian.

    b) Musisz doprowadzić do tego, aby każda
rozpowszechniana lub publikowana przez ciebie praca, która
w całości lub części zawiera Program, albo pochodzi od
niego lub jego części, była w całości i bezpłatnie
licencjonowana dla wszelkich stron trzecich na warunkach
niniejszej Licencji.

    c) Jeżeli zmodyfikowany program podczas korzystania z
niego w normalnym trybie odczytuje polecenia
interaktywnie, musisz spowodować, aby po uruchomieniu
(użyty w interaktywny sposób w najzwyklejszym trybie),
wydrukowywał on lub wyświetlał powiadomienie o odnośnym
prawie autorskim i braku gwarancji (ewentualnie o
zapewnianiu gwarancji przez ciebie), oraz o tym, że
użytkownicy mogą redystrybuować ten program na niniejszych
warunkach wraz z informacją, jak użytkownik może zapoznać
się z treścią niniejszej Licencji. (Wyjątek: jeśli sam
Program jest interaktywny, ale normalnie nie drukuje
takiego powiadomienia, twoja praca oparta na nim też nie
musi wydrukowywać takiego powiadomienia).

  Niniejsze wymogi odnoszą się do zmodyfikowanej pracy
jako całości. Jeśli dające się ustalić sekcje danej pracy
nie pochodzą od Programu i mogą być racjonalnie uważane za
samodzielne i odrębne same w sobie, to niniejsza Licencja
i jej warunki nie mają zastosowania do takich sekcji przy
rozprowadzaniu ich przez ciebie jako odrębne prace. Jeśli
jednak rozprowadzasz je jako część całości, będącej pracą
opartą na Programie, rozpowszechnianie tej całości musi
być dokonywane na warunkach niniejszej Licencji, której
zezwolenia dla innych licencjobiorców rozciągają się w
całej szerokości na tę całość, a tym samym i na każdą
indywidualną jej część, niezależnie od jej autorstwa.

  Dlatego też intencją tego fragmentu nie jest roszczenie
sobie praw albo podważanie twych praw do pracy napisanej w
całości przez ciebie. Chodzi nam raczej o korzystanie z
prawa kontrolowania dystrybucji pochodnych i zbiorowych
prac opartych na Programie. 

  I jeszcze jedno: samo tylko połączenie z Programem (lub
z pracą opartą na Programie) innej pracy - nie opartej na
Programie, w ramach wolumenu nośnika przechowywania lub
dystrybucji, nie powoduje objęcia takiej pracy zakresem
niniejszej Licencji.

  3. Możesz kopiować i rozprowadzać Program (lub opartą na
nim pracę - zgodnie z pkt.2 w kodzie wynikowym lub w
formie wykonywalnej w myśl postanowień pkt.1 i 2 powyżej,
pod warunkiem zrealizowania również poniższych wymogów:

    a) Musisz dołączyć do niego odpowiadający mu,
kompletny i możliwy do odczytania przez urządzenia cyfrowe
kod źródłowy, który musi być rozpowszechniany na warunkach
pkt.1 i 2 powyżej i na nośniku zwyczajowo używanym dla
wzajemnej wymiany oprogramowania; lub

    b) dołączyć do niego pisemną ofertę, ważną co najmniej
3 lata, przyznającą każdej stronie trzeciej - za opłatą
nie przekraczającą twego kosztu fizycznego wykonywania
dystrybucji źródła - kompletną, odczytywalną przez
urządzenia cyfrowe kopię odpowiadającego mu kodu
źródłowego, rozprowadzaną na warunkach pkt.1 i 2 powyżej,
na nośniku zwyczajowo używanym do wzajemnej wymiany
oprogramowania; lub

     c) dołączyć do niego informację, jaką otrzymałeś na
temat oferty rozprowadzania odpowiedniego kodu źródłowego.
(Ta możliwość dozwolona jest tylko dla dystrybucji
niehandlowej i jedynie wtedy, gdy otrzymałeś dany program
w kodzie wynikowym lub formie wykonywalnej wraz z
wymienioną ofertą - zgodnie z podpunktem "b" powyżej).

  Określenie kod źródłowy dla pracy oznacza formę pracy
preferowaną dla wprowadzania do niej modyfikacji. Dla
wykonanej pracy, kompletny kod źródłowy oznacza cały kod
źródłowy wszystkich modułów, wszelkie sprzężone z nią
pośredniczące pliki opisujące oraz zbiory komend stosowane
do sterowania kompilacją i instalowaniem programów.
Niemniej jednak, jako wyjątek specjalny, dystrybuowany (w
formie źródłowej albo binarnej) kod źródłowy nie musi
obejmować niczego, co jest normalnie rozprowadzane przy
pomocy głównych komponentów (kompilator, jądro itd.)
systemu operacyjnego, na którym pracuje część wykonywalna,
o ile sam taki komponent towarzyszy tej części.

  Jeśli dystrybucja części wykonywalnej albo kodu
wynikowego realizowana jest poprzez oferowanie dostępu do
kopii z wyznaczonego miejsca, to oferowanie równoważnego
dostępu dla kopiowania kodu źródłowego z tego samego
miejsca liczy się jako rozpowszechnianie kodu źródłowego,
nawet gdy strony trzecie nie są zmuszone do kopiowania
źródła wraz z kodem wynikowym.

  4. Poza przypadkami jednoznacznie dozwolonymi w
niniejszej Licencji, nie możesz kopiować, modyfikować,
sublicencjonować ani rozpowszechniać Programu. We
wszystkich pozostałych wypadkach, każda próba skopiowania,
sublicencjonowania lub rozpowszechnienia Programu jest
nieważna i powoduje automatyczne wygaśnięcie twoich praw z
tytułu Licencji. Niemniej jednak, stronom, które już
otrzymały od ciebie kopie albo prawa w ramach niniejszej
Licencji, licencje nie wygasają tak długo, jak długo
strony te w pełni stosują się do nich.

  5. Nie musisz akceptować niniejszej Licencji, jeżeli jej
nie podpisałeś. Niemniej jednak, nic innego nie zapewni ci
zezwolenia na modyfikowanie lub rozprowadzanie Programu i
pochodzących od niego prac. Działania takie są prawnie
zabronione, jeżeli nie przyjmujesz niniejszej Licencji.
Dlatego też, poprzez modyfikowanie bądź rozpowszechnianie
Programu (lub pracy na nim opartej) dajesz wyraz swojej
akceptacji dla Licencji i wszelkich jej postanowień i
warunków dotyczących kopiowania, rozprowadzania i
modyfikowania Programu lub opartych na nim prac.

  6. W każdym przypadku redystrybucji przez ciebie
Programu (albo opartej na nim pracy), odbiorca
automatycznie otrzymuje od pierwotnego licencjodawcy
licencję na kopiowanie, rozpowszechnianie i modyfikowanie
Programu na niniejszych zasadach i warunkach. Na
korzystanie przez odbiorcę z udzielonych w niniejszej
Licencji praw nie możesz narzucać już dalszych ograniczeń.
Nie jesteś stroną odpowiedzialną za kontrolę
przestrzegania Licencji przez osoby trzecie.

  7. Jeśli na skutek wyroku sądowego lub zarzutu
naruszenia patentu, jak też z każdej innej przyczyny (nie
ograniczonej do kwestii patentowych) zostaną narzucone na
ciebie (niezależnie czy to mocą wyroku sądowego, umowy,
czy w inny sposób) warunki sprzeczne z warunkami
niniejszej Licencji, to nie zwalniają one ciebie z
warunków Licencji. Jeśli nie możesz prowadzić dystrybucji
tak, aby wypełniać jednocześnie swoje obowiązki z tytułu
niniejszej Licencji i inne odnośne obowiązki, to w
rezultacie nie możesz wcale rozprowadzać Programu. Na
przykład, gdyby licencja patentowa nie zezwalała na wolną
od opłat licencyjnych redystrybucję Programu przez
wszystkie osoby, które otrzymały kopie bezpośrednio lub
pośrednio od ciebie, to jedynym sposobem pozwalającym ci
na przestrzeganie i licencji patentowej, i Licencji
niniejszej, byłoby całkowite powstrzymanie się od
jakiejkolwiek dystrybucji Programu.

  Jeżeli w jakichś szczególnych okolicznościach któryś
fragment niniejszego punktu stałby się nieważny lub
niewykonywalny, to intencją jest, aby znajdowała
zastosowanie pozostała część punktu, a treść całego punktu
była stosowana w pozostałych okolicznościach. 

  Celem niniejszego punktu nie jest zachęcanie do
naruszania patentów czy innych praw własności, albo też do
podważania ich ważności; niniejszy punkt za swój jedyny
cel ma ochronę integralności systemu rozpowszechniania
wolnego oprogramowania, realizowanego za pomocą
publicznych licencji. Wielu ludzi bezinteresownie wniosło
swój wkład do stworzenia szerokiego zakresu oprogramowania
upowszechnianego w tym systemie, mając zaufanie do
konsekwentnego jego stosowania; wyłącznie do
autora/ofiarodawcy należy decyzja, czy życzy on sobie
rozprowadzania oprogramowania za pośrednictwem innego
systemu i licencjobiorca nie może tego prawa wyboru
ograniczać. 

  Intencją niniejszego punktu jest jasne i wyraźne
przedstawienie tego, co uważa się za skutki, jakie rodzi
pozostała część niniejszej Licencji.

  8. W przypadku, gdy dystrybucja i/lub używanie Programu
w niektórych krajach poddane jest ograniczeniom patentowym
lub zastrzeżeniom prawami autorskimi, początkowy posiadacz
praw autorskich, który poddaje Program pod oddziaływanie
niniejszej Licencji, może dodać wyraźnie zakreślone
geograficzne ograniczenie rozpowszechniania wyłączające te
kraje, dzięki czemu dystrybucja dozwolona będzie wyłącznie
w krajach czy wśród krajów nie objętych takim wyłączeniem.
W przypadku takim, niniejsza Licencja obejmuje dane
ograniczenie tak, jakby było ono wpisane w jej treść.

  9. W miarę potrzeby Fundacja Wolnego Oprogramowania może
publikować poprawione i/lub nowe wersje Powszechnej
Licencji Publicznej. Takie nowe wersje będą napisane w
duchu podobnym do obecnej wersji, ale mogą różnić się w
szczegółach poruszających nowe problemy czy zagadnienia.

  Każdej wersji nadaje się wyróżniający ją numer. Jeżeli
Program podaje numer wersji niniejszej Licencji, odnoszący
się do tej wersji i "wszelkich wersji następnych", masz do
wyboru albo stosować się do postanowień i warunków tej
wersji, albo którejkolwiek wersji późniejszej wydanej
przez Fundację Wolnego Oprogramowania. O ile Program nie
podaje numeru wersji niniejszej Licencji, możesz wybrać
dowolną wersję kiedykolwiek opublikowaną przez Fundację.

  10. Jeśli chcesz włączyć części Programu do innych
wolnych programów, których warunki rozpowszechniania są
inne, zwróć się pisemnie do autora z prośbą o pozwolenie.
W przypadku oprogramowania objętego przez Fundację prawem
autorskim, napisz do Fundacji; czasami czynimy od tego
odstępstwa. W naszej decyzji kierujemy się dwoma celami:
utrzymania wolnego statusu wszystkich pochodnych naszego
wolnego oprogramowania oraz - generalnie - promowania
współudziału i wielokrotnego stosowania oprogramowania.


                  WYRÓB BEZ GWARANCJI

  11. PONIEWAŻ PROGRAM JEST LICENCJONOWANY BEZPŁATNIE, NIE
JEST OBJĘTY GWARANCJĄ W ZAKRESIE DOZWOLONYM PRZEZ
OBOWIĄZUJĄCE PRZEPISY. O ILE NA PIŚMIE NIE STANOWI SIĘ
INACZEJ, POSIADACZE PRAW AUTORSKICH I/LUB INNE STRONY
ZAPEWNIAJĄ PROGRAM W STANIE, W JAKIM JEST ("JAK WIDAĆ")
BEZ JAKIEJKOLWIEK GWARANCJI, ANI WYRAŹNEJ, ANI DOMYŚLNEJ,
W TYM MIĘDZY INNYMI DOMYŚLNYCH GWARANCJI CO DO
PRZYDATNOŚCI HANDLOWEJ I PRZYDATNOŚCI DO OKREŚLONYCH
ZASTOSOWAŃ. CAŁOŚĆ RYZYKA W ZAKRESIE JAKOŚCI I
SKUTECZNOŚCI DZIAŁANIA PROGRAMU PONOSISZ SAM. W RAZIE
GDYBY PROGRAM OKAZAŁ SIĘ WADLIWY, PONOSISZ KOSZT CAŁEGO
NIEZBĘDNEGO SERWISU, NAPRAWY I KORYGOWANIA.

  12. O ILE OBOWIĄZUJĄCE PRAWO NIE STANOWI INACZEJ ALBO
CZEGOŚ INNEGO NIE UZGODNIONO W FORMIE PISEMNEJ, ŻADEN
POSIADACZ PRAW AUTORSKICH ANI INNA STRONA MODYFIKUJĄCA
I/LUB REDYSTRYBUJĄCA PROGRAM ZGODNIE Z POWYŻSZYMI
ZEZWOLENIAMI, W ŻADNYM WYPADKU NIE JEST ODPOWIEDZIALNA
WOBEC CIEBIE ZA SZKODY, W TYM SZKODY OGÓLNE, SPECJALNE,
UBOCZNE LUB SKUTKOWE, WYNIKŁE Z UŻYCIA BĄDŹ NIEMOŻLIWOŚCI
UŻYCIA PROGRAMU (W TYM, MIĘDZY INNYMI, ZA UTRATĘ DANYCH
LUB POWSTANIE DANYCH NIEDOKŁADNYCH, ALBO ZA STRATY
PONIESIONE PRZEZ CIEBIE LUB STRONY TRZECIE, JAK TEŻ
NIEDZIAŁANIE PROGRAMU Z INNYMI PROGRAMAMI), NAWET JEŚLI
DANY POSIADACZ BĄDŹ INNA STRONA ZOSTALI POWIADOMIENI O
MOŻLIWOŚCI POWSTANIA TAKICH SZKÓD.


              KONIEC ZASAD I WARUNKÓW

  Jak stosować niniejsze Warunki do Twoich nowych
programów

  Jeśli opracowujesz nowy program i chciałbyś, aby stał
się on przydatny dla szerokiego ogółu, najlepszą drogą do
osiągnięcia tego będzie nadanie twemu programowi
charakteru wolnego oprogramowania, które każdy może
redystrybuować i zmieniać na niniejszych warunkach.

  W tym celu do programu dołącz poniższe informacje.
Bezpieczniej jest dołączyć je na początku każdego pliku
źródłowego, dzięki czemu najskuteczniej można przekazać
fakt nieistnienia gwarancji; każdy plik powinien przy tym
nosić uwagę "copyright" i odnośnik, gdzie można znaleźć
pełną informację.

    nazwa programu i informacja, do czego on służy.
    Copyright (C) 19../20.. nazwisko autora

    Niniejszy program jest wolnym oprogramowaniem;
    możesz go rozprowadzać dalej i/lub modyfikować na
    warunkach Powszechnej Licencji Publicznej GNU,
    wydanej przez Fundację Wolnego Oprogramowania -
    według wersji 2-giej tej Licencji lub którejś z
    późniejszych wersji.

    Niniejszy program rozpowszechniany jest z nadzieją,
    iż będzie on użyteczny - jednak BEZ JAKIEJKOLWIEK
    GWARANCJI, nawet domyślnej gwarancji PRZYDATNOŚCI
    HANDLOWEJ albo PRZYDATNOŚCI DO OKREŚLONYCH
    ZASTOSOWAŃ. W celu uzyskania bliższych informacji -
    Powszechna Licencja Publiczna GNU.

    Z pewnością wraz z niniejszym programem otrzymałeś
    też egzemplarz Powszechnej Licencji Publicznej GNU
    (GNU General Public License); jeśli nie - napisz do
    Free Software Foundation, Inc., 51 Franklin Street,
    Fifth Floor, Boston, MA  02110-1301  USA

  Podaj też informacje o sposobie kontaktowania się z
tobą pocztą elektroniczną lub zwykłą.

  Jeśli dany program jest interaktywny, spraw, aby w
momencie wchodzenia w tryb interaktywny wyświetlał on
komunikat jak w poniższym przykładzie:

    Gnomovision wersja 69, Copyright C 19.. nazwisko

    Gnomovision wydawany jest ABSOLUTNIE BEZ ŻADNEJ
    GWARANCJI - w celu uzyskania dalszych szczegółów
    wpisz "show w". To jest wolne oprogramowanie i mile
    widziane jest dalsze rozpowszechnianie go przez
    ciebie na określonych warunkach - w celu uzyskania
    bliższych szczegółów wpisz "show c".

  Powyższe hipotetyczne polecenia "show w" i "show c"
winny powodować wyświetlenie odpowiednich części
Powszechnej Licencji Publicznej. Oczywiście możesz używać
innych poleceń niż "show w" i "show c"; mogą to być nawet
kliknięcia myszą lub pozycje menu - co tylko sobie uznasz
za stosowne.

  Powinieneś też poprosić swego pracodawcę (jeśli
pracujesz jako programista) czy też swoją szkołę (jeśli
jesteś uczniem), o podpisanie, w razie potrzeby,
"Rezygnacji z praw autorskich" do programu. Poniżej
podajemy przykład (zmień nazwy/nazwiska):

    My, firma Jojodyne Sp. z o.o. niniejszym zrzekamy
    się i rezygnujemy z wszelkich interesów prawnych w
    zakresie praw autorskich do programu "Gnomovision"
    (który realizuje następujące funkcje...), napisanego
    przez p.Jana Kowalskiego.

    Podpis: /-/ Gniewosław Wielkoważny

    Gniewosław Wielkoważny, Prezes...itp

  Powszechna Licencja Publiczna nie zezwala na włączanie
twego programu do programów prawnie zastrzeżonych. Jeśli
twój program jest biblioteką podprogramów, możesz
rozważyć, czy nie będzie korzystniej zezwolić na
powiązanie prawnie zastrzeżonych aplikacji z biblioteką.
Jeśli chciałbyś właśnie tego dokonać, zamiast niniejszej
Licencji zastosuj Powszechną Licencję Publiczną GNU dla
Bibliotek.

[QueryBox]
Okna zapytania

W oknach dialogowych użyj kursorów lub naciśnij
podświetloną literę aby wybrać opcję. Możesz też kliknąć
myszą na odpowiednim przycisku.

[How to use help]
Jak korzystać z pomocy

Do obsługi przeglądarki pomocy możesz użyć kursorów lub
myszy. Naciśnij strzałkę w dół aby przejść do
następnej pozycji lub przewinąć ekran w dół. Naciśnij
strzałkę w górę aby przejść do poprzedniej pozycji lub
przewinąć ekran w górę. Naciśnij strzałkę w prawo aby
podążyć za zaznaczonym odnośnikiem. Naciśnij strzałkę w
lewo aby powrócić do poprzedniego odwiedzonego węzła w
historii.

Jeśli twój terminal nie obsługuje klawiszy kursorów,
możesz użyć spacji aby przewinąć do przodu i klawisza
b aby przewinąć do tyłu. Użyj TAB aby przejść do
następnej pozycji i ENTER aby odwiedzić zaznaczony
odnośnik. Klawisz l wraca do poprzedniego odwiedzonego
węzła w historii. Naciśnij ESC aby wyjść z
przeglądarki pomocy.

Lewy przycisk myszy uaktywnia odnośnik lub przewija ekran.
Prawy wraca do poprzedniego węzła w historii.

Pełna lista klawiszy przeglądarki pomocy:

Podstawowe klawisze ruchuGeneral Movement Keys także
działają.

tab           Następna pozycja.
M-tab         Poprzednia pozycja.
dół           Następna pozycja lub przewiń ekran w dół.
góra          Poprzednia pozycja lub przewiń w górę.
prawo, enter  Uaktywnia odnośnik.
lewo, l       Poprzedni węzeł w historii.
F1            Pomoc dla przeglądarki pomocy.
n             Następny węzeł.
p             Poprzedni węzeł.
c             Przejście do Spisu treści.
F10, esc      Wyjście z przeglądarki pomocy.

Local variables:
fill-column: 58
end:
