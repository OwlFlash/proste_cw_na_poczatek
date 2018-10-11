print("Podaj liczbe całkowitą")

while True:
    try:
        x = int(input())
        if x % 2 == 0:
            print("Podana przez Ciebie liczba {} jest parzysta".format(x))
            break
        else:
            print("Podana przez Ciebie liczba {} jest nieparzysta".format(x))
            break
    except ValueError :
        print("Podana liczba  nie jest całkowita.Podaj liczbę całkowitą")
    except NameError :
        print("Podany znak nie jest liczbą.Podaj liczbę całkowitą")# to si enigdy chyba nie wyswietli?



"""hile True:
    print(i)
    i = i + 1
    if(i > 3):
        break"""




