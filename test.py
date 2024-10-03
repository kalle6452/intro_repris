# Listan ska skrivas kontinuerligt
# Ändra så att 0 funkar, samt att negativa tal funkar vid första inputen.
# Skriv kommentarer för alla uppgifter
print('Enter positive integers. End by giving a negative integer.')
lista = []
integer = 1
i = 0
blank = ''
while integer >= 0:
    integer = int(input(f'Integer {i+1}: {blank}'))
    if integer > 0:
        lista.append(integer)
        i += 1
    elif integer == 0:
        #integer = int(input(f'zero is neither positive nor negative, please try again: {blank}'))
        print('zero is neither positive nor negative, please try again')
    elif not lista and not i > 0:
        print('you have to start with a positive number!')
        integer = 0
print(f'Number of positive integers: {i}') 
print('Positive numbers:', end=' '),   
for j in lista[:-1]:
    print(str(j), end=', ')
print(lista[i-1])
