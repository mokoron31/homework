values_list_2 = [1,"try"]
values_list = [1,'str',2.3]
values_dict = {'a':True, 'b':2.9, 'c':12}
def print_params(a=1, b='строка', c=True):
    values_list





    print(a, b, c)


print_params(2, 'столбец', False)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
