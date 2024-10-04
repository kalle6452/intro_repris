# Rätt!!!!
# Jupyter är mer konsekvent?
# Listan ska skrivas kontinuerligt?
# Skriv kommentarer för alla uppgifter
print('Enter positive integers. End by giving a negative integer.')
lista = []
# So that our while loops starts
integer = 1
i = 0
# So that there will be a blankspace before user input.
blank = ''
while integer >= 0:
    integer = int(input(f'Integer {i+1}: {blank}'))
    # If the integer is positive we append it to lista and add += i so that the user knows how many
    # integers they've written.
    if integer > 0:
        lista.append(integer)
        i += 1
    # If a user inputs zero the user will have to try again for the current index in list.
    elif integer == 0:
        print('zero is neither positive nor negative, please try again')
    # If the user inputs a negative value but they have not already put in a positive integer.
    elif not lista and not i > 0:
        print('you have to start with a positive number!')
        integer = 0
print(f'Number of positive integers: {i}') 
print('Positive numbers:', end=' '),   
# To make the output conform with requirements by removing [] and putting , after all numbers except the last one.
for j in lista[:-1]:
    print(str(j), end=', ')
print(lista[i-1])
