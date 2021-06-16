list1 = [0,1,2,3,4,5,6,7]

def odd_or_even(list = [], element_from_list = 0):
    if list.index(element_from_list) % 2 == 0:
        return True
    else:
        return False

print(odd_or_even(list1, 3))

number2 = 2
number1 = 1

list2 = [number1, number2]

print(list2)