import csv, codecs

filename = "test.csv"
file = codecs.open(filename, "r" , "euc_kr")# r로 바로 읽고 euc로 인코딩 형식

reader = csv.reader(file,delimiter=",")
for cells in reader:
    print(cells[1],cells[2])
