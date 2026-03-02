def total_euro(hours, payPerHour):
    return hours * payPerHour

workHours = float(input("Radni sati: "))
payPerHour = float(input("Satnica: "))

total = total_euro(workHours, payPerHour)

print("Ukupno: ", total)