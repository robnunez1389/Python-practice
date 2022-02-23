sentence = input("Sentence: ")
word = input("Word to look for in sentence: ")
sentence = str.lower(sentence)
v = sentence.count(word)


print_statement = "There are {} occurrences of '{}' in the sentence."

print(print_statement.format(v, word))