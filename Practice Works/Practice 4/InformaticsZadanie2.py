def NahodimPeresechenie(S1,S2):
    Intersection = []
    for c1 in S1:
        for c2 in S2:
            if c1==c2:
                if c1 not in Intersection:
                    Intersection.append(c1)

    Znachenie = 0.0
    if len(Intersection) > 0:
        TotalSum =0
        for a in Intersection:
            TotalSum += a
        Znachenie = TotalSum/len(Intersection)

    return Intersection, Znachenie

S1 = []
S2 = []

while True:
    try:
        Size1 = int(input("\nСколько чисел будет в множестве A: "))
        break
    except ValueError:
            print("Ощибка, введите ЦЕЛОЕ ЧИСЛО!!")
print(f"Введите {Size1} чисел для множества A:")
for i in range(Size1):
    while True:
        try:
            N = int(input())
            S1.append(N)
            break
        except ValueError:
            print("Ощибка, введите целые ЧИСЛА!!")

while True:
    try:
        Size2 = int(input("\nСколько чисел будет в множестве B: "))
        break
    except ValueError:
        print("Ощибка, введите ЦЕЛОЕ ЧИСЛО!!")
        
print(f"Введите {Size2} чисел для множества B:")
for i in range(Size2):
    while True:
        try:
            N = int(input())
            S2.append(N)
            break
        except ValueError:
            print("Ощибка, введите целые ЧИСЛА!!")

ObshieChisla, SredneeZnachenie = NahodimPeresechenie(S1, S2)

print("\n РЕЗУЛЬТАТ")
if ObshieChisla == 0:
    print("Пересечение множеств пустое хд")
else:
    print(f"Пересечение множеств: {ObshieChisla}")
    print(f"Среднее значение этих элементов: {SredneeZnachenie}")
