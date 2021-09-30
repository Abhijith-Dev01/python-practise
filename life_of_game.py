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

def no_of_neighbour(row,col,tot_row,tot_col):
    if (row == 0) or (row == tot_row -1):
        if (col == 0) or (col == tot_col-1):
            return 3
        else:
            return 5
    elif (col == 0) or (col == tot_col-1):
        if (row == 0) or (row == tot_row-1):
            return 3
        else:
            return 5
    else:
        return 8 




def main():
    # - indicates dead cells
    # * indicatees  live cells
    m    = int(input("enter the number of rows"))
    n    = int(input("enter the number of columns"))
    arr  = np.full((m,n),'*')
    arr1 = np.zeros((m,n))
    draw(arr,m,n)
    for  i in range(m):
        for  j in range(n):
            num        = no_of_neighbour(i,j,m,n)
            arr1[i][j] = num
            arr[i][j]  =  rules(arr[i][j],num)
        
    print("\n")
    draw(arr,m,n)

if __name__ == "__main__":
    main()





