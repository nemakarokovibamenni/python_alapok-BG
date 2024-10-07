"""Thonny fejlesztői környezetben készíts egy rövid programot, amely
kommentként tartalmazza a program funkciójának leírását,
konstansként tárolja PI értékét,
egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
kiszámolja és a képernyőre kiírja a kör kerületét és területét!"""

#PI értéke
PI=3.14

#kör sugara
R=5

#kör kerülete
print("Kerület")
print(2*R*PI)

#kör területe
print("Terület")
print(R*R*PI)



"""Készíts egy rövid programot, amely egy változóban eltárol egy szót. 
Próbáld meg ennek a változónak a tartalmát int értékké átalakítani. 
Mit tapasztalsz? Milyen üzenet jelenik meg a képernyőn?"""

#szo = 'alma'
#szo = int(szo)
#print(szo)
#ValueError: invalid literal for int() with base 10: 'alma'


"""Készíts egy rövid programot, amelyben egy olyan változó értékét szeretnéd kiíratni, ami előzőleg nem is szerepel a kódodban. 
Hogyan jelöli a fejlesztői környezet a hibát? Futtasd! Milyen hibaüzenetet kapsz?"""

print(makk)
#NameError: name 'makk' is not defined