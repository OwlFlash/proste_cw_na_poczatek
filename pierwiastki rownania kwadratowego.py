print("Podaj 'a' różne od zera")
while True:

    a = float(input())
    if a == 0:
        print("Podane równanie nie będzie kwadratowe. Podaj 'a' różne od zera")
    else:
        break

print("Podaj 'b'")
b = float(input())
print("Podaj 'c'")
c = float(input())
delta = (b ** 2) - 4 *a *c


if delta > 0 :
    x1 = (-b + delta ** 0.5)/ (2 *a)
    x2 = (-b - delta ** 0.5)/ (2 *a)
    print("Podane równanie kwadratowe ma dwa rozwiązania. X1 : {}  i X2 : {}". format(x1,x2))
elif delta == 0:
    x0 = (-b)/2*a
    print("Podane równanie kwadraatowe ma jedno rozwiązanie X : {}".format(x0))
else:
    print("Podane równanie kwadratowe nie ma rozwiązań")
