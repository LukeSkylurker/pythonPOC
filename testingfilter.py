import csv
results = []
average1 = 0
sum1 = 0
with open('fone.csv', encoding="utf-8-sig", newline='') as inputfile:
    for row in csv.reader(inputfile):
        results.append(row[0])
        mylist = [s for s in results if s.isdigit()]
    for i in range(0, len(mylist)):
        mylist[i] = int(mylist[i])
        average1 = (int(mylist[0]) + int(mylist[1])) / int(len(mylist))
        sum1 = (int(mylist[0]) + int(mylist[1]))
    f = open("demofile3.txt", "w")
    f.write("the average of the filtered list was: " + str(average1) + " and the sum of the filtered list was " + str(sum1))
    print(average1)
    print(sum1)
