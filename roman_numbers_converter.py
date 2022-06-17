#zamiana cyfr arabskich na rzymskie i na odwrót

liczby_dict = {"1":"I", "2":"II", "3":"III", "4":"IV", "5":"V", "6":"VI", "7":"VII", "8":"VIII", "9":"IX", "10":"X",
               "20":"XX", "30":"XXX", "40":"XL", "50":"L", "60":"LX", "70":"LXX", "80":"LXXX", "90":"XC", "100":"C",
               "200":"CC", "300":"CCC", "400":"CD", "500":"D", "600":"DC", "700":"DCC", "800":"DCCC", "900":"CM",
               "1000":"M", "1500":"MD", "2000":"MM", "3000":"MMM"}

rzymskie_dict = {"I":"1", "II":"2", "III":"3", "IV":"4", "V":"5", "VI":"6", "VII":"7", "VIII":"8", "IX":"9", "X":"10",
                 "XX":"20", "XXX":"30", "XL":"40", "L":"50", "LX":"60", "LXX":"70", "LXXX":"80", "XC":"90", "C":"100",
                 "CC":"200", "CCC":"300", "CD":"400", "D":"500", "DC":"600", "DCC":"700", "DCCC":"800", "CM":"900",
                 "M":"1000", "MD":"1500", "MM":"2000", "MMM":"3000"}

liczby_rzymskie = ["I", "X", "L", "C", "D", "M"]

def zamiana_arabskie_na_rzymskie(dlugosc_liczby):
    wynik = ""
    for poz in range(dlugosc_liczby):
        if int(liczba_do_zmiany[poz]) == 0:
            continue
        else:
            aaa = str(int(liczba_do_zmiany[poz]) * int("1" + "0" * (dlugosc_liczby - 1 - poz)))
            #print(liczby_dict[aaa])
            wynik = wynik + liczby_dict[aaa]
    return wynik

def zamiana_rzymskie_na_arabskie(dlugosc_liczby):
    wynik = 0
    skip = 0
    for poz in range(dlugosc_liczby):
        if poz < dlugosc_liczby-1: #sprawdzamy czy nie jesteśmy już na koncu liczby w pętli FOR, inaczej będzie out of index
            if skip == 0: #warunek sprawdza czy przeskoczyć jedną cyfre jeżeli pierwsza była mniejsza np. IX, CM, IV
                if int(rzymskie_dict[liczba_do_zmiany[poz]]) < int(rzymskie_dict[liczba_do_zmiany[poz+1]]):
                    #sprawdzamy czy jest para liter, czyli czy najpierw jest mniejsz a później większa np. IX, CM, IV
                    print(rzymskie_dict[liczba_do_zmiany[poz:poz+2]])
                    wynik = wynik + int(rzymskie_dict[liczba_do_zmiany[poz:poz+2]])
                    skip = 1
                else:
                    #print(rzymskie_dict[liczba_do_zmiany[poz]])
                    wynik = wynik + int(rzymskie_dict[liczba_do_zmiany[poz]])
            else:
                skip = 0
                continue
        else:
            #print(rzymskie_dict[liczba_do_zmiany[poz]])
            wynik = wynik + int(rzymskie_dict[liczba_do_zmiany[poz]])
    return str(wynik)

liczba_do_zmiany = input("Wprowadz liczbę: ")
liczba_do_zmiany = liczba_do_zmiany.upper()

if len(liczba_do_zmiany) > 0:
    if liczba_do_zmiany.isnumeric():
        if int(liczba_do_zmiany) < 4000:
            print("liczba rzymska: " + zamiana_arabskie_na_rzymskie(len(liczba_do_zmiany)))
        else:
            print("Standardowy zakres liczb rzymskich to 1-3999")
            exit()
    else:
        for a in liczba_do_zmiany:
            if a not in liczby_rzymskie:
                print("Nie ma takiej liczby rzymskiej lub nie jest to liczba: " + a)
                exit()
        print("liczba arabska: " + zamiana_rzymskie_na_arabskie(len(liczba_do_zmiany)))
else:
    print("Wprowadz jakąś liczbę!")
