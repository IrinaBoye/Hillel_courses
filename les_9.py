import csv

counter = 1
with open("number.csv", "w", newline="") as file:
    while counter != 1001:
        csv_writer = csv.writer(file)
        csv_writer.writerow(range(counter, counter+10))
        counter += 10



with open("number.csv") as file:
    csv_reader = csv.reader(file)
    for number in csv_reader:
        print(number)



