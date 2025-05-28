#Program to count number of unique words in a given sentence using sets. 
def count_unique_words(sentence):  
     
    words = sentence.lower().split()  
    unique_words = set(words)  
    return len(unique_words), unique_words  

sentence = input("Enter a sentence: ")  
unique_count, unique_words = count_unique_words(sentence)  

print(f"Number of unique words: {unique_count}")  
print("Unique words:", unique_words)