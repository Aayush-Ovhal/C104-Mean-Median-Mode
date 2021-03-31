import csv

def median():
    with open("SOCR-HeightWeight.csv", newline = '') as f:
        reader = csv.reader(f)
        fileData = list(reader)

    fileData.pop(0)

    newData = []

    for i in range(len(fileData)):
         n_num = fileData[i][2]
         newData.append(n_num)

    n = len(newData)
    newData.sort()

    if n % 2 == 0:
         median1 = float(newData[n//2])
         median2 = float(newData[n//2 - 1])

         finalMedian = (median1 + median2)/2
    else:
         finalMedian = newData[n//2]

    print("Median is: " + str(finalMedian))

median()
