words = open("test.txt", "r")
wordreader = words.read()
counter_char = 0
counter_word = 1
counter_sentence = 0
for char in wordreader:
    if char == " ":
        counter_word += 1
    elif char == ".":
        counter_sentence += 1
    elif (char != " ") and (char != "."):
        counter_char += 1

print(counter_char)
print(counter_sentence)
print(counter_word)
