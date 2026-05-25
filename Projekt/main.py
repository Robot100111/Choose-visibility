
import random
wydarzenie = 0
while True:
    x = 0
    y = 0
    ruchy = 0
    print(r"""
             ____ ___    _    ____ _________ _______   ______ _____  _    
            |  _ \_ _|  / \  / ___|__  / ___|__  /\ \ / / ___|_   _|/ \   
            | |_) | |  / _ \ \___ \ / / |     / /  \ V /\___ \ | | / _ \  
            |  __/| | / ___ \ ___) / /| |___ / /_   | |  ___) || |/ ___ \
            |_|  |___/_/   \_\____/____\____/____|  |_| |____/ |_/_/   \_\


            J  A  Z  D  A     P  R  Z  E  Z     P  U  S  T  Y  N  I  Ę
    """)
    print("""Znajdujesz się na środku pustyni, a twoim celem jest dotarcie
    do oazy, bez stracenia cennego paliwa.""")
    print("Podaj swoją nazwę")
    auto = input()
    while True:
        print("""Jaki poziom trudności wybierasz?
        Łatwa, mapa od -5 do 5
        Średnia, mapa od - 10 do 10
        Trudna, mapa od -15 do 15""")
        poziom_trudności = input()
        if poziom_trudności == "Łatwa":
            mapa = 5
            paliwo = 15
            break
        elif poziom_trudności == "Średnia":
            mapa = 10
            paliwo = 25
            break
        elif poziom_trudności == "Trudna":
            mapa = 15
            paliwo = 35
            break
        else:
            print("Nie rozumiem tej komendy. Spróbuj ponownie.")
            continue
    while True:
        try:
            paliwo2 = int(input("Podaj ilość paliwa, którą chcesz mieć (od " + str(paliwo - 5) + " do " + str(paliwo + 5) + ")"))
        except ValueError:
            print("Nie rozumiem tej komendy. Spróbuj ponownie.")
            continue
        if paliwo2 < paliwo - 5 or paliwo2 > paliwo + 5:
            print("Nie rozumiem tej komendy. Spróbuj ponownie.")
            continue
        break
    while True:
        print("Wybierz, swoję auto: ")
        print("Terenówka - mniejsza szansa na wydarzenie")
        print("Sedan - większa szansa na wydarzenie")
        print("Sportowe - największa szansa na wydarzenie")
        auto = input()
        if auto == "Terenówka":
            auto = 16
            break
        elif auto == "Sedan":
            auto = 14
            break
        elif auto == "Sportowe":
            auto = 12
            break
        else:
            print("Nie rozumiem tej komendy. Spróbuj ponownie.")
            continue

    while True:
        try:
            x = int(input("Podaj kordynat x, na którym chcesz zacząć (od -3 do 3)"))
        except ValueError:
            print("Nie rozumiem tej komendy. Spróbuj ponownie.")
            continue
        if x > 3 or x < -3:
            print("Nie rozumiem tej komendy. Spróbuj ponownie.")
            continue
        try:
            y = int(input("Podaj kordynat y, na którym chcesz zacząć (od -3 do 3)"))
        except ValueError:
            print("Nie rozumiem tej komendy. Spróbuj ponownie.")
            continue
        if y > 3 or y < -3:
            print("Nie rozumiem tej komendy. Spróbuj ponownie.")
            continue
        else:
            break
    oaza_x = random.choice(list(range(-mapa, -mapa + 4)) + list(range(mapa - 3, mapa + 1)))
    oaza_y = random.choice(list(range(-mapa, -mapa + 4)) + list(range(mapa - 3, mapa + 1)))
    print(r"""Instrukcje:
    Użyj klawisza w, aby iść w górę
    Użyj klawisza s, aby iść w dół
    Użyj klawisza a, aby iść w lewo
    Użyj klawisza d, aby iść w prawo""")
    print("Oaza znajduję się na takich kordynatach: (" + str(oaza_x) + "," + str(oaza_y) + ")")
    print("-------------------------------------------------------------------------------")
    input("Naciśnij enter, aby rozpocząć grę")

    while True:
        while True: 
            print("-------------------------------------------------------------------------------")
            if wydarzenie == 1:
                print("Napotkałeś burzę piaskową! Tracisz paliwo!")
                paliwo2 = paliwo2 - 1
            if wydarzenie == 2:
                print("Napotkałeś zaspę! Tracisz paliwo!")
                paliwo2 = paliwo2 - 1
            if wydarzenie == 3:
                print("Napotkałeś wodę! Zyskujesz paliwo!")
                paliwo2 = paliwo2 + 1
            if wydarzenie == 4:
                print("Zapsypał cię piasek! Oaza zmienia położenie!")    
                oaza_x = random.choice(list(range(-mapa, -mapa + 4)) + list(range(mapa - 3, mapa + 1)))
                oaza_y = random.choice(list(range(-mapa, -mapa + 4)) + list(range(mapa - 3, mapa + 1)))
            if wydarzenie == 5:
                print("Napotkałeś wędrowcę! Zyskujesz paliwo!")
                paliwo2 = paliwo2 + 1
            print("pozycja (" + str(x) + "," + str(y) + ")")
            print("oaza (" + str(oaza_x) + "," + str(oaza_y) + ")")
            print("twoje paliwo (" + str(paliwo2) + ")")
            print("W jaką stronę chcesz iść? (wpisz: w, s, a lub d)")
            pozycja = input()
            if pozycja == "w":
                y = y + 1
                ruchy = ruchy + 1
                paliwo2 = paliwo2 - 1
                wydarzenie = random.randint(1, auto)
            elif pozycja == "s":
                y = y - 1
                ruchy = ruchy + 1
                paliwo2 = paliwo2 - 1
                wydarzenie = random.randint(1, auto)
            elif pozycja == "a":
                x = x - 1  
                ruchy = ruchy + 1
                paliwo2 = paliwo2 - 1
                wydarzenie = random.randint(1, auto)
            elif pozycja == "d":
                ruchy = ruchy + 1
                x = x + 1
                paliwo2 = paliwo2 - 1
                wydarzenie = random.randint(1, auto)
            else:   
                print("Nie rozumiem tej komendy")
                continue
            if x > mapa or y > mapa or x < -mapa or y < -mapa:
                print("Wypadłeś poza mapę!")
                paliwo2 = paliwo2 + 1
                if x > mapa:
                    x = mapa
                elif y > mapa:
                    y = mapa
                elif x < -mapa:
                    x = -mapa
                elif y < -mapa:
                    y = -mapa
                continue
            if x == oaza_x and y == oaza_y:
                break
            if paliwo2 <= 0:
                print(r"""
    ____  ____   __________ ____ ____      _    __    _____ _/_/  
    |  _ \|  _ \ |__  / ____/ ___|  _ \    / \  | //  | ____/ ___| 
    | |_) | |_) |  / /|  _|| |  _| |_) |  / _ \ |//|  |  _| \___ \ 
    |  __/|  _ <  / /_| |__| |_| |  _ <  / ___ \// |__| |___ ___) |
    |_|   |_| \_\/____|_____\____|_| \_\/_/   \_\_____|_____|____/ 
        STRACIŁEŚ CAŁE PALIWO! NIE UDAŁO CI SIĘ DOTRZEĆ DO OAZY!""")
                print("Auto:", auto)
                print("Końcowa pozycja:", x, y)
                break
        if paliwo2 <= 0:
            break
        print(r"""
    __        ____   ______ ____      _    __    _____ _/_/  
    | \      / /\ \ / / ___|  _ \    / \  | //  | ____/ ___| 
     \ \ /\ / /  \ V / |  _| |_) |  / _ \ |//|  |  _| \___ \ 
      \ V  V /    | || |_| |  _ <  / ___ \// |__| |___ ___) |
       \_/\_/     |_| \____|_| \_\/_/   \_\_____|_____|____/ 
            GRATULACJE! TWOJE AUTO DOJECHAŁO DO OAZY W """ + str(ruchy) + """ ruchach!""")
        print("Auto:", auto)
        print("Końcowa pozycja:", x, y)
        print("Pozostałe paliwo:", paliwo2)
                                                                       
        break
    while True:
        powtorka = input(" Chcesz zagrać ponownie? (t/n)")
        if powtorka == "t":
            break
        elif powtorka == "n":
            break
        else :
            print("Nie rozumiem tej komendy. Spróbuj ponownie.")
            continue
    if powtorka == "t":
        continue
    if powtorka == "n":
        break
            
