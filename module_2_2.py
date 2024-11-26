first = int(input('Ввeдите первое число '))
second = int(input('Ввeдите втрое число '))
third = int(input('Ввeдите третье число '))
if first==second and first==third and second==third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)

