# sor = 1
# while sor <= 3:
#     oszlop = 1
#     while oszlop <= 5:
#         print('O ', end='')
#         oszlop = oszlop + 1
#     print('')
#     sor = sor + 1


user_input = int(input('Adj meg egy páros számot: '))
darab = 1
sor = 1
oszlop = 1
if user_input %2 == 0:
    while sor <=4:
        oszlop = 1
        while oszlop <= darab:
            print('0 ', end ='')
            oszlop = oszlop + 1
        print('')
        darab = darab + 1
        sor = sor + 1
if  user_input %2 != 0:
    print()