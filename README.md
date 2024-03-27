# kf
Drobna pomoc w przygotowaniu do egzaminu kf.

# literowanie.py
Program pomaga w nauce literowania.<br/>
Przykład uruchomienia:<br/>
  "<b>python literowanie.py data/literowanie.dat 5</b>"<br/>
Zostanie zadanych 5 losowych zadań z literowania. Zamieniamy wg polecania:<br/>
  <ul>
    <li>znak - zamiana na znak (litera lub cyfra)</li>
    <li>ang - zamiana na literowanie wg schematu angielskiego (Alfa, Beta, Charlie, itd...)</li>
    <li>pol - zamiana na literowanie wg schematu polskiego (Adam, Barbara, Cezary, itd...)</li>
  </ul>
Sprawdzając poprawność program ignoruje wielkość liter, spacje i to czy cyfry zapisane są znakiem czy wyrazem (wszystko jedno czy wpiszemy "Jeden" czy "1", "Seven" czy "7").<br/>
Jeśli szkoda nam czasu na literowanie cyfr można je wykluczyć wpisując znak "#" na początku odpowiednich linii w pliku data/literowanie.dat<br/>

# pytania.py
Program odpytuje z kilku tematów.<br/>
Przykłady uruchomienia:<br/>
<ul>
  <li><b>"python pytania.py data/okregi.dat 5</b>" - 5 pytań dotyczących numeracji poszczególnych województw, odpowiedzią jest cyfra 1-9,</li>
  <li><b>"python pytania.py data/kodyq.dat 5</b>" - 5 pytań o kod Q dla podanego wyrażenia plik "kodyq.dat" to mniejszy zbiór kodów, "kodyq2.dat" to zbiór kodów bardziej rozbudowany</li>
  <li><b>"python pytania.py data/bandplan.dat 5</b>" - 5 pytań dotyczących zakresów częstotliwości dozwolonych w kf amatorskim, niestety odpowiedź musi być w określonym formacie tzn długość fali w metrach z dopiskiem "m" np "40m" a zakres częstotliwości to dwie liczby oddzielone "-" i na końcu jednostka (kHz lub MHz - kHz dla zakresów<30MHz, MHz dla zakresów>30MHz np "7000-7200kHz".</li>
</ul>
