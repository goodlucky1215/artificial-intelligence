import openpyxl

filename = "stats_104102.xlsx"
book = openpyxl.load_workbook(filename)


#첫번째 방법
#print(book.get_sheet_names())
#print(book.get_sheet_by_name("stats_104102"))

#두번째방법
sheet = book.worksheets[0]
for row in sheet.rows:
    for data in row:
        print(data.value,end="  ")
    print(data,end="\n")    
