word = input("String to convert:")
n = int(input("How many last letters should be converted? "))
first_part = word[:len(word) - n]
last_part =  word[len(word) - n:]
print(first_part + str.upper(last_part))

