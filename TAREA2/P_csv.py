import csv
with open('names.csv') as file:
    csvss = csv.reader(file)
    print(file)
    for reg in csvss:
        print(reg[0], reg[1], reg[2], reg[3])
print("tipo: ", type(csvss))
#https://python-para-impacientes.blogspot.com/2015/05/operaciones-con-archivos-csv.html
