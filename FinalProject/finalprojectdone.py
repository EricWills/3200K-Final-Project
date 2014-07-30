##import xlrd
##workbook = xlrd.open_workbook('bravesstats.xlsx')
##worksheet = workbook.sheet_by_name()
##num_rows = worksheet,nrows - 1
##curr_row = -1
##while curr_row < num_rows:
##    curr_row += 1
##    row = worksheet.row(curr_row)
##    print row


##f = open('bravesstats.csv', 'r')
##data = f.readlines()
##
##del f
##
##for line in data:
##    print(line.strip())

##
##f = open('bravesstats.csv', 'r')
##data = f.readlines()

##f = 'bravesstats.csv'
##"Evan" in f
##if "Evan" in f:
##    print("Gattis")

""" Returns individual player statistics based on raw input entry of player names"""
### Used an excel worksheet with statistics as a csv as my data pool ###

f = open('bravesstats.csv', 'r')
data = f.readlines()

player = raw_input("Enter player name: ")
for line in data:
    if player in line:
        print(line)
print("NAME", "GP", "AB", "R", "H", "2B", "3B", "HR", "RBI", "TB", "BB", "SO", "SB", "BA", "OBP", "SLG", "OPS", "OWAR")

     
