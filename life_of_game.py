def draw_board(board_arr,row,col):
 """A  function to print the generation board"""
 for  i in range(row):
    for j in range (col):        
         print(board_arr[i][j],end=' ')
    print('')
    

def apply_rules(cell,neighbours):
    """A function to apply game of life rules to the 
       corresponding cells"""
    if cell == "*":
        if neighbours in [2,3] :
            cell = '*'
        else:
            cell ='-'
    else:
        if neighbours == 3:
            cell = '*'
    
    return cell


def neighbour_index(row,col,tot_row,tot_col):
    """A function to return the neighbours index of the given cell"""
    if row == 0:
        if col == 0:
            index_lst = list(([row+1,col],[row+1,col+1],[row,col+1]))
            return index_lst

        if col == tot_col-1:
            index_lst = list(([row+1,col],[row+1,col-1],[row,col-1]))
            return index_lst
        else:
            index_lst = list(([row,col+1],[row+1,col+1],
                             [row+1,col],[row+1,col-1],[row,col-1]))
            return index_lst

    if col  == 0:
        if row == tot_row-1:
            index_lst = list(([row-1,col],[row-1,col+1],[row,col+1]))
            return index_lst
        else:    
            index_lst = list(([row-1,col],[row+1,col],[row+1,col+1],
                             [row-1,col+1],[row,col+1]))
            return index_lst

    if row == tot_row-1:
        if col == tot_col-1:
            index_lst = list(([row-1,col],[row-1,col-1],[row,col-1]))
            return index_lst
        else:
            index_lst = list(([row-1,col],[row,col-1],[row,col+1],
                             [row-1,col+1],[row-1,col-1]))
            return index_lst

    if col == tot_col-1:
        index_lst = list(([row-1,col],[row+1,col],[row+1,col-1],
                         [row-1,col-1],[row,col-1]))
        return index_lst
    
    else:
        index_lst = list(([row-1,col],[row-1,col-1],[row-1,col+1],
                         [row+1,col-1],[row+1,col],[row+1,col+1],
                         [row,col-1],[row,col+1]))  
        return index_lst


def no_of_neighbour(index_lst,board_arr):
    """"A function to return the number of neighbours of 
        the given generation board and neighbour index list"""
    count = 0
    for i in index_lst:
        a = i[0]
        b = i[1]
        if board_arr[a][b] == '*':
            count = count+1
    
    return count
 

def next_generation(row,col,gen_arr,neighbour_count_arr):
        """A function to print the nexrt generation using 
          the previous generation data"""
        for  i in range(row):
            for  j in range(col):
                neighbour_lst = neighbour_index(i,j,row,col)
                num  = no_of_neighbour(neighbour_lst,gen_arr)
    
                neighbour_count_arr[i][j] = num

        for i in range (row):
            for j in range(col):
                gen_arr[i][j] = apply_rules(gen_arr[i][j],neighbour_count_arr[i][j])

        print("\n")
        draw_board(gen_arr,row,col)


def main():
    # - indicates dead cells
    # * indicatees  live cells
    first_gen  = [['-','-','-','-','-'],
                  ['-','-','*','-','-'],
                  ['-','-','*','-','-'],
                  ['-','-','*','-','-'],
                  ['-','-','-','-','-']]
    
    row = len(first_gen)
    col = len(first_gen[0])

    neighbour_count_arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],
                           [0,0,0,0,0],[0,0,0,0,0]]
    draw_board(first_gen,row,col)

    for  i in range(10):
        next_generation(row,col,first_gen,neighbour_count_arr)
    

if __name__ == "__main__":
    main()





