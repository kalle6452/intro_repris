def is_palindrome(string):
    #string = input(f'Enter a string: ')
    # Removing non all non-alphabetocal characters
    string = ''.join(filter(str.isalpha, string))
    # Removing all blankspaces so string is one word
    string = ''.join(string.split())
    # Making all letters in string lowercase
    string = string.lower()
    #print(string)
    forward = []
    invers = []
    # We go through the string forwards and than put it in the list forward
    # We do the same but instead go through the string backwards and than into backward list.abs
    # if the list is the same in both directions than it is palindrome.
    for i in string:
        forward.append(i)
    for i in reversed(string):
        invers.append(i)
    if string != 'stop':
        if forward == invers:
            print('palindrome')
            return True
        else:
            print('not palindrome')
            return False
    elif string == 'stop':
        print('Program will end now')

string = 'test'
while string != 'stop':
    string = input(f'Enter a string: ')
    is_palindrome(string)