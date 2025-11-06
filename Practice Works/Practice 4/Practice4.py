def PositNumbersProverka(Choto):
    PositiveCount = 0
    for n in Choto:
        if n > 0:
            PositiveCount += 1
    return PositiveCount

print("Задание 1: Поиск массива с наименьшим числом положительных элементов")
RazmerMass = 5
A =[]
B =[]

print(f"\nВведите {RazmerMass} чисел для массива A:")
for i in range(RazmerMass):
    a = input(f"Введите {i+1}-е число: ")
    A.append(int(a))

print(f"\nВведите {RazmerMass} чисел для массива B:")
for i in range(RazmerMass):
    b = input(f"Введите {i+1}-е число: ")
    B.append(int(b))

PosInA = PositNumbersProverka(A)
PosInB = PositNumbersProverka(B)

print("\nРезультаты подсчета:")
if PosInA < PosInB:
    print(f"Массив A(в нём меньше + чисел): {A}")
    print(f"Массив B: {B}")
elif PosInB < PosInA:
    print(f"Массив B(в нём меньше + чисел): {B}")
    print(f"Массив A: {A}")
else:
    print("В обоих массивах одинаковое количество положительных элементов.")
