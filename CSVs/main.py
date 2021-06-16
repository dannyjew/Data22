import csv

with open("user_details.csv", newline='\n') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(list(csvreader))
    # counter = 0
    # for row in csvreader:
    #     counter += 1
    #     if counter > 1:
    #         print(row[-1])
    #     else:
    #         continue


