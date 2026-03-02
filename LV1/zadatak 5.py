import string

count_ham = 0
count_spam = 0

word_count_ham = 0
word_count_spam = 0

count_spamExclamation = 0

with open("SMSSpamCollection.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        
        type, data = line.split(maxsplit=1) #splits first word from others
        words = data.split()

        if(type == "ham"):
            count_ham += 1
            word_count_ham += len(words)
        elif(type == "spam"):
            count_spam += 1
            word_count_spam += len(words)

            if(data.endswith("!")):
                count_spamExclamation += 1

average_word_count_ham = word_count_ham / count_ham if count_ham > 0 else 0
average_word_count_spam = word_count_spam / count_spam if count_spam > 0 else 0

print("Prosječan broj riječi(ham): ", round(average_word_count_ham, 2))
print("Prosječan broj riječi(spam): ", round(average_word_count_spam, 2))
print("Broj poruka sa uskličnikom(spam): ", count_spamExclamation)