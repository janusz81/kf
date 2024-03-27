# kf
Drobna pomoc w przygotowaniu do egzaminu kf.

# literowanie.py
Program pomaga w nauce literowania.
Przykład uruchomienia:
  "python literowanie.py data/literowanie.dat 5"
Zostanie zadanych 5 losowych zadań z literowania. Zamieniamy wg polecania:
  -znak - zamiana na znak (litera lub cyfra)
  -ang - zamiana na literowanie wg schematu angielskiego (Alfa, Beta, Charlie, itd...)
  -pol - zamiana na literowanie wg schematu polskiego (Adam, Barbara, Cezary, itd...)
Sprawdzając poprawność program ignoruje wielkość liter, spacje i to czy cyfry zapisane są znakiem czy wyrazem (wszystko jedno czy wpiszemy "Jeden" czy "1", "Seven" czy "7").
Jeśli szkoda nam czasu na literowanie cyfr można je wykluczyć wpisując znak "#" na początku odpowiednich linii w pliku data/literowanie.dat

# pytania.py
Program odpytuje z kilku tematów.
Przykłady uruchomienia:
  "python pytania.py data/okregi.dat 5" - 5 pytań dotyczących numeracji poszczególnych województw, odpowiedzią jest cyfra 1-9,
  "python pytania.py data/kodyq.dat 5" - 5 pytań o kod Q dla podanego wyrażenia plik "kodyq.dat" to mniejszy zbiór kodów, "kodyq2.dat" to zbiór kodów bardziej rozbudowany
  "python pytania.py data/bandplan.dat 5" - 5 pytań dotyczących zakresów częstotliwości dozwolonych w kf amatorskim, niestety odpowiedź musi być w określonym formacie tzn długość fali w metrach z dopiskiem "m" np "40m" a zakres częstotliwości to dwie liczby oddzielone "-" i na końcu jednostka (kHz lub MHz - kHz dla zakresów<30MHz, MHz dla zakresów>30MHz np "7000-7200kHz".
  
