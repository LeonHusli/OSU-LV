try:
    grade = float(input("Unesite ocjenu između 0 i 1: "))

    if(grade < 0 or grade > 1):
        print("Greška! Uneseni broj nije u dobrom obliku.")
    elif(grade >= 0.9):
        print("A")
    elif(grade >= 0.8):
        print("B")
    elif(grade >= 0.7):
        print("C")
    elif(grade >= 0.6):
        print("D")
    else: print("F")

except ValueError:
    print("Greška! Nije unesen broj.")
