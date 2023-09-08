with open("story.txt", "r") as f:
    story = f.read()
# print(story)
 
words =  set()  #create set with unique words
target_start = "<"
target_end = ">"
start_of_word = -1 

for i, char in enumerate(story): #access to the position as well as element at that position
    if char == target_start:
        start_of_word = i #marking the start of word i.e '<'

    if char == target_end and start_of_word != -1 : #if end ">" and start of word is already found
        word = story[start_of_word : i + 1]  #using slice syntax, get  the whole word
        words.add(word)
        start_of_word = -1 #reset start of word

# print(words)

answers = {}

 # replace all instances of word with user input
for word in words :
    answer = input("Enter a word" + word + ": ")
    answers[word] = answer

for word in words :
   story = story.replace(word, answers[word])

print(story)