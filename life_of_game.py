from typing import List
import numpy as np
def draw(arr,m,n):
 for  i in range(m):
    for j in range (n):        
         print(arr[i][j],end=' ')
    print('')
    

def rules(cell,neighbours):
    if cell == "*":
        if neighbours in [2,3] :
            cell = '*'
        else:
            cell ='-'
    else:
        if neighbours == 3:
            cell = '*'
    
    return cell


def neighbour_indent(row,col,tot_row,tot_col):#get the neighbour indentations
    if row == 0:
        if col == 0:
            lst = list(([row+1,col],[row+1,col+1],[row,col+1]))
            return lst

        if col == tot_col-1:
            lst = list(([row+1,col],[row+1,col-1],[row,col-1]))
            return lst
        else:
            lst = list(([row,col+1],[row+1,col+1],
                             [row+1,col],[row+1,col-1],[row,col-1]))
            return lst

    if col  == 0:
        if row == tot_row-1:
            lst = list(([row-1,col],[row-1,col+1],[row,col+1]))
            return lst
        else:    
            lst = list(([row-1,col],[row+1,col],[row+1,col+1],
                             [row-1,col+1],[row,col+1]))
            return lst

    if row == tot_row-1:
        if col == tot_col-1:
            lst = list(([row-1,col],[row-1,col-1],[row,col-1]))
            return lst
        else:
            lst = list(([row-1,col],[row,col-1],[row,col+1],
                             [row-1,col+1],[row-1,col-1]))
            return lst

    if col == tot_col-1:
        lst = list(([row-1,col],[row+1,col],[row+1,col-1],
                         [row-1,col-1],[row,col-1]))
        return lst
    
    else:
        lst = list(([row-1,col],[row-1,col-1],[row-1,col+1],
                         [row+1,col-1],[row+1,col],[row+1,col+1],
                         [row,col-1],[row,col+1]))
        
        return lst

def no_of_neighbour(lst,arr):
    count = 0
    for i in lst:
        a = i[0]
        b = i[1]
        if arr[a][b] == '*':
            count = count+1
        else:
            continue
    
    return count
 
    
def main():
    # - indicates dead cells
    # * indicatees  live cells
    arr  = [['-','-','-','-','-'],
            ['-','-','*','-','-'],
            ['-','-','*','-','-'],
            ['-','-','*','-','-'],
            ['-','-','-','-','-']]
    row    = len(arr)
    col    = len(arr[0])
    arr1 = np.zeros((row,col))
    lst1 = []
    draw(arr,row,col)
    for  i in range(row):
        for  j in range(col):
            lst1       = neighbour_indent(i,j,row,col)
            num        = no_of_neighbour(lst1,arr)
            arr1[i][j] = num
            # arr[i][j]  =  rules(arr[i][j],num)
    for i in range (row):
        for j in range(col):
            arr[i][j] = rules(arr[i][j],arr1[i][j])

    print("\n")
    draw(arr,row,col)

if __name__ == "__main__":
    main()





