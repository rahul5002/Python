#3.  Input a sentence and print words in separate lines. 
sentence = input("Enter a sentence: ")
print("Words in the sentence:")
for word in sentence.split():
    print(word)
