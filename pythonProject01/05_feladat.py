#Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó
#által megadott, szintén ebbe a
#tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!

"""2. Feladat
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás),
majd adjon tájékoztatást, hogy eltalálta-e!"""
import random

random_szam = random.randint(1, 3)
szam= int(input("Mondj egy számot 1-3 között! "))
if random_szam == szam:
    print("Én is erre gondoltam")
elif random_szam < szam:
    print("A tiéd nagyobb;)")
elif random_szam > szam:
    print("Az enyém nagyobb haha")