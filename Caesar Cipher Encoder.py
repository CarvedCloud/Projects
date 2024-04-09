'''
shifting of letters

Example:-

shift of 3

original: the quick brown

code: wkh txlfn eurzq
'''
message = "the quick brown fox jumps over the lazy dog"
shift_number = 5

coded_message = ""
for letter in message:
    if letter == " ":
        coded_message += " "
    elif (ord(letter) + shift_number) > 122:
        coded_message += chr((ord(letter) + shift_number - 122) + 96)
    else:
        coded_message += (chr(ord(letter) + shift_number))

print(coded_message)


'''
for letter in message:
    if (ord(letter) + shift_number) > 122:
        coded_message += chr((ord(letter) + shift_number - 122) + 96)
'''    



#If the assigned number of the character added to the shift_number is greater
#than 122, subtract 122 from the larger number (assigned number + shift_number)
#and add obtained number to 97. take the character of the sum obtained.  

#above paragraph is the logic behind line 19 and line 20

# the above code only works for shift numbers less than 26
