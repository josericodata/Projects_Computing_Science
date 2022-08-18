#CA 1
#Student Name: Jose Maria Rico Leal - 10539218
#Module Name: B8IT117 Object Oriented Programming
#Presentation Date: Tuesday 26th of October

#Importing pandas library to give a timestamp to new files
import pandas as pd 

today = pd.Timestamp('today')

def get_textname():
    # Ask the use the name of the text file to create an index for.
    name = input('For which file would you like me to create a word index? ')
    return name

def create_dictionary(filename):
    infile = open(filename, 'r', encoding='utf8') # Open the file
    word_index = dict() # Create an empty dictionary to store the words and line numbers
    counter = 0 # Set a counter to count the line we found the word
    for line in infile:
        wordlinelist = line.rstrip('\n').split() # remove \n and split the line into words.
        counter += 1 # advance the counter to reflect the line we are in
        for word in wordlinelist: # for every word in the line
            if word not in word_index: # If we haven't yet encountered it,
                word_index[word] = [str(counter)] # Start a key/value pair with value being a list with the line number.
            elif word in word_index: # If the word was found,
                word_index[word].append(str(counter)) # Append the line number to the list in the value
    infile.close() # Close the file since we are done reading.
    return word_index

def create_index_file(dict):
    outfile = open('index_{:%Y-%m-%d}.txt'.format(today), 'w', encoding='utf8') # create a file to store the word index.
    a_list = [] # Create a list to store the word the index.
    index = 0 # Create a counter to control the index we are checking.
    for key in dict.keys(): # Ever word found in the dictionary
        a_list.append(key) # Append it to the a_list
        for value in dict[key]: # Ever value found for that word/key
            a_list[index] = a_list[index] + ' ' + value # Add it to the a_list, in the same index, seperated by a space
        index += 1 # Advance the index by one to continue to the next word.
    a_list.sort() # Sort the finished list.
    for element in a_list:
        outfile.write(element + '\n') # Extract the list, element by element to the file index.txt.
    outfile.close() # Close the file
             
            
def main():
    print('This program creates a word index of the file you request.')
    print('----------------------------------------------------------')
    print()
    file = get_textname() # Ask the user for the file to create an index for.
    dictionary = create_dictionary(file) # Create the dictionary for the file.
    create_index_file(dictionary) # Write the the word index to a file.
    print('Word index is created. File name is: index.txt')

# Call the main function.
main()
