# Column A = 1, B= 2, .. , Z = 26, AA = 27
# Create a base system of 26 using the letters A..Z
# AA = 1*26^1 + 1*26^0 = 27
# Z = 26^1 = 26
# ord('A') = 65 --> unicode 
# position of letter --> ord(letter) - ord('A') + 1 


def spreadsheet_column_encoding(column):
    code = 0
    count = len(column) -1
    for letter in column:
        code += (ord(letter) - ord('A') + 1) * (26**count)
        count = count - 1
    return code
        
print(spreadsheet_column_encoding("Z"))
print(spreadsheet_column_encoding("AA"))