word = input("enter the word-> ")
if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u' or word[0] == 'A' or word[0] == 'E' or word[0] == 'I' or word[0] == 'O' or word[0] == 'U':
    newWord = word + "way"
    print(newWord)
else:
    lastchar = word[0]
    newWord = (word[1:len(word)] + lastchar + "ay")
    # newWord = (word[1:] + lastchar + "ay") //same ans will come
    print(newWord)

# 2ND method
# word = input("Enter the word-> ")
# if word[0].lower() in 'aeiou':
#     new_word = word + "way"
# else:
#     new_word = word[1:] + word[0] + "ay"
# print(new_word)
