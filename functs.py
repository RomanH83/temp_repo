# Zrobić funkcję która dostaje listę w której może znajdować się nieokreślona liczba zagnieżdżonych list
# np. [1, [2, [3, 4]], 5, [6, 7], 8, [9, [10]]], funkcja ma zwracać listę wypłaszczoną, czyli
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def nested_lists_flattener_gen(nested_list):
    '''
    Takes a (deeply)nested list and returns a flattened one as a generator
    '''
    for lst in nested_list:
        if isinstance(lst, list):
            yield from nested_lists_flattener(lst)
        else:
            yield lst

def nested_lists_flattener(nested_list):
    return list(nested_lists_flattener_gen(nested_list))

if __name__ == '__main__':
    lst = [1, [2, [3, 4]], 5, [6, 7], 8, [9, [10]]]
    print(nested_lists_flattener(lst))