def sudokuChk(x):
    for i in x:
        rs=0
        for j in i:
            rs+= int(j)
        print("Row Sum is for row number :",rs)
        if rs != 45:
            my_val="No"
            break
        else:
            continue
    for i in range(9):
        cs=0
        for j in range(9):
            cs += int(x[i][j])
        print("Column ",i ,":", cs)
        if cs !=45:
            my_val="No"
            break
        else:
            my_val="Yes"
    return my_val

row=0
x=[]
while row<9:
    x.append(input("Enter 9 digits between 1 to 9 to check the sudoku entries"))
    #print(x[row])
    row+=1

print(x)


print(sudokuChk(x))
