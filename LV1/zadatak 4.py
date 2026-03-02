import string

rijecnik = {}

with open("song.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.translate(str.maketrans("", "", string.punctuation)) #gets rid of punctuations in each line
        words = line.split()

    for word in words:
        word = word.lower()
        rijecnik[word] = rijecnik.get(word, 0) + 1

singleWords = [(word,value) for word, value in rijecnik.items() if value == 1]
print("Broj riječi koje se pojavljuju jednom: ", len(singleWords))
print(singleWords)