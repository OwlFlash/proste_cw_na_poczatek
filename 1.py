#I.  Napisz program "powiel.py", który wczyta od użytkownika pewien napis, a następnie wyświetli 30 kopii tego napisu, każda w osobnej linii.

#II. Napisz program "pole_tr.py", który obliczy pole trójkąta, pod warunkiem że użytkownik poda wysokość i długość podstawy tego trójkąta. Uwzględnij, że wysokość i długość podstawy mogą być liczbami niecałkowitymi.

#III. Napisz program "odsetki.py", który obliczy stan konta za N lat, gdzie stan początkowy konta wynosi SPK, a stopa oprocentowania P % rocznie (obowiązuje miesięczna kapitalizacja odsetek). N, SPK i P podaje użytkownik programu.

#I
"""napis = input()
print("{} \n".format(napis) *30)
print(_________________________________)
#II
print("Podaj podstawę trójkąta")
podstawa =float(input())
print("Podaj wysokość trójkąta")
wysokosc = float(input())
Pole= (1/2) * podstawa *wysokosc"""
#III
print("Podaj Stan początkowy konta")
SPK = float(input())
print("Podaj roczną stopę oprocentowania")
P = float(input())
print("Podaj liczbę lat ")
N = float(input())
K = SPK*(1 + P/12)*12*N#COS TEN WZÓR PRZEKOMBINOWANY
print("Twoj kapitał( po {} lata przy oprocentowaniu {} % będzie wynosił {}". format(N,P,K))
ptint("aghhh")
# enfjowrgergwrgv
# rgergerg
# reg
# erg
# er
# ger
