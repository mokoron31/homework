def calculate_structure_sum(data_structure, sum_=0):
    if isinstance(data_structure, int):
        sum_ += data_structure
    if isinstance(data_structure, str):
        sum_ += len(data_structure)
    if isinstance(data_structure, (list,set,tuple)):
        for elem in data_structure:
            sum_ += calculate_structure_sum(elem)
    if isinstance(data_structure,dict):
        for k,v in data_structure.items():
            sum_ += calculate_structure_sum(k,v)
    return sum_






data_structure = [

  [1, 2, 3],

  {'a': 4, 'b': 5},

  (6, {'cube': 7, 'drum': 8}),

  "Hello",

  ((), [{(2, 'Urban', ('Urban2', 35))}])

]

result = calculate_structure_sum(data_structure)
print(result)

