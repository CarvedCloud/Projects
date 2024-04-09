coded_message = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
shift_number = 5

message = ""
for letter in coded_message:
    if letter == " ":
        message += " "
    elif (ord(letter) - shift_number < 97):
        message += chr((ord(letter) + (26 - shift_number)))
    else:
        message += (chr(ord(letter) - shift_number))

print(message)

