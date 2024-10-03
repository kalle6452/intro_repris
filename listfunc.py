import random

def random_values(amount, start, stop):
    lista = []
    # We execute the for loop 'amount' of times and the values in the list will be between
    # start and stop(inclusive).
    for i in range(amount):
        roll = random.randint(start,stop)
        lista.append(roll)
    return lista

def filter_even(numbers):
    even = []
    # We determine if a number is even by taking the modulus.
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
    return even

def sum_of_list(numbers):
    sum = 0
    # We add all elements in list even in a variable sum.
    for i in numbers:
        sum += i
    return sum


def capitalize_names(names):
    lista = []
    # We use .title() to capitalize first letter of every word in list.
    for i in names:
        names = i.title()
        lista.append(names)
    return lista

def is_strictly_increasing(original):
    j = 0
    # If the current value in list 'i' is greater than the previous value 'j' we set j=i
    # If this pattern repeats for the entire for loop j will be greater than zero and we return True
    # if at any point the previous value is greater or equal to the current value we set j=0 and 
    # terminate the for loop which means that the function will return False.
    for i in original:
        if i > j:
            j = i
        else:
            j = 0
            break
    if j == 0:
        return False
    elif j > 0: 
        return True    

def get_unique_elements_numbers(original):
    comparison = []
    # If i is not in comparison we append i to comparison, otherwise we won't.abs
    # This will yield a list with only unique values.
    for i in original:
        if i not in comparison:
            comparison.append(i)
    return comparison

# Only for testing if Jupyter doesn't work

original = random_values(10,1,10)
even = filter_even(original)
sum = sum_of_list(even)
names = ['luke', 'leia', 'han', 'chewbacca']
Names = capitalize_names(names)
increase_list = [1,3,4,7,8]
increasing = is_strictly_increasing(original)
unique = get_unique_elements_numbers(original)
print(f'Original list of numbers: {original}')
print(f'Filtered even numbers: {even}')
print(f'Sum of even numbers: {sum}')
print(f'Original list of names: {names}')
print(f'Capitalized names: {Names}')
print(f'Original list is strictly increasing?: {increasing}')
print(f'Increasing list is... increasing?: {is_strictly_increasing(increase_list)}')
print(f'Unique numbers in original list: {unique}')