from nltk.tokenize import TweetTokenizer
import string
import os

# assigning the functionality of the TweetTokenizer to a variable and establishing the search as case-insensitive 

tknzr = TweetTokenizer(preserve_case = False)

# while loop that runs true until user enters a valid file to search through 

while True:
    input_file_path = input("Enter the file to search: ")
    if not os.path.exists(input_file_path):
        print("Error: Invalid file. Please enter a valid file")
    else:
        break
        
         
    


# try-except block to read the file and determine if given file exists

try:
    with open(input_file_path, 'r') as file_connection:
        file_content = file_connection.read()
except FileNotFoundError:
    print(f"Error: File '{input_file_path}' not found. Please check your path and try again!")

# separates the file's connected strings/text from one another and makes "tokens" out of them to organize 

words = tknzr.tokenize(file_content)

# list populated by common words/tokens that ignore punctucation 

common_words = []
for word in words:
    if word not in string.punctuation:
        common_words.append(word)

# dictionary with keys populated by words themselves and values populated by the count/number of words found in the file (one search)

word_count = {}

for word in common_words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# function that returns second element of dictionary when called (count/value)

def get_count(counted_words):
    return counted_words[1]

# tuple created that sorts by keys (words/items) and values (counts) from the dictionary in descending order

words_sorted = sorted(word_count.items(), key = get_count, reverse = True)

# looping through word and count pairs of the newly sorted tuple and printing the top 10 results spaced by a tab (4 spaces) 

for word, count in words_sorted[:10]:
    print(f"{word}\t{count}")





