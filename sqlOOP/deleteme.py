# find the largest product of two numbers in this list

numbers = [2,7,3,67,9,6,4,3,6]

def largest_product(numbers: list):
    sorted_list = sorted(numbers)
    largest_fraction = sorted_list[-1]/sorted_list[0]
    print(largest_fraction)


largest_product(numbers)

