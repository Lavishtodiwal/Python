import csv

with open("demo.csv", mode="r") as f:
    # f.write(str(["name: Lavish", "class: BCA"]))
    a = csv.reader(f)
    for i in a:
        print(i)
