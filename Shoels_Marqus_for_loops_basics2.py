# 1 Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list

print(biggie_size([-1, 3, 5, -5]))

# 2 Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values.

def count_positives(list):
    count = 0
    for val in list:
        if val > 0:
            count += 1
    list[len(list) - 1] = count
    return list

print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -2, -7, -2]))

# 3 Sum Total - Create a function that takes a list and returns the sum of all the values in the array.

def sum_total(list):
    total = 0
    for val in list:
        total += val
    return total

print(sum_total([1, 2, 3, 4]))
print(sum_total([6, 3, -2]))

# 4 Average - Create a function that takes a list and returns the average of all the values.

def average(list):
    total = 0
    for val in list:
        total += val
    return total / len(list)

print(average([1, 2, 3, 4]))

# 5 Length - Create a function that takes a list and returns the length of the list.

def length(list):
    count = 0
    for val in list:
        count += 1
    return count

print(length([37, 2, 1, -9]))
print(length([]))

# 6 Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.

def minimum(list):
    if len(list) == 0:
        return False
    result = 0
    for val in (list):
        if val < result:
            result = val
        return result

print(minimum([37, 2, 1, -9]))
print(minimum([]))

# 7 Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.

def maximum(list):
    if len(list) == 0:
        return False
        result = 0
    for val in (list):
        if val > result:
            result = val
        return result

print(maximum([37, 2, 1, -9]))
print(maximum([]))

# 8 Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.

def ultimate_analysis(list):
    dict = {
        'sum_total': [],
        'maximum': [],
        'minimum': [],
        'average': [],
        'length': 0
    }
    if len(list) == 0:
        return dict
    else:
        dict['sum_total'] = 0
        dict['maximum'] = list[0]
        dict['minimum'] = list[0]

    for val in list:
        if val > dict['maximum']:
            dict['maximum'] = val
        elif val < dict['minimum']:
            dict['minimum'] = val
            dict['sum_total'] += val
            dict['length'] += 1
            dict['average'] = dict['sum_total'] / len(list)
    return dict

print(ultimate_analysis([37, 2, 1, -9]))
print(ultimate_analysis([]))

#9 Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. 

def reverse_list(list):
    half_len = int(len(list) / 2)
    for i in range(half_len):
        list[i] , list[len(list) - 1 - i] = list[len(list) - 1 - i], list[i]
    return list

print(reverse_list([37, 2, 1, -9]))