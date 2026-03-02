numbers = []

while True:
    data = input()

    if(data == "Done"):
        break

    try:
        number = float(data)
        numbers.append(number)
    except:
        print("Unos nije broj. Zanemareno")

numbers.sort()
print(numbers)
print("Broj elemenata: ", len(numbers))
print("Srednja vrijednost: ", sum(numbers)/len(numbers))
print("Minimalna vrijednost: ", min(numbers))
print("Maksimalna vrijednost: ", max(numbers))