board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]

#solves for the value using valid function and backtracking
def solve(no):
    find =find_empty(no)
    if not find:
        return True
    else:
        row,col = find
    
    for i in range (1,10):
        if valid(no,i,(row,col)):
            no[row][col] = i
            #recurssive solving 
            if solve(no):
                return True
            
            no[row][col]=0
    
    return False


#checks if the number is valid for the block 
def valid(no,num,pos):
    #check row
    for i in range(len(no[0])):
        if no[pos[0]][i]== num and pos[1] !=i:
            return False
    #check columns
    for i in range(len(no)):
        if no[i][pos[1]]== num and pos[0] !=i:
            return False
    #check Box
    box_x=pos[1] // 3
    box_y=pos[0] // 3 

    for i in range(box_y * 3 ,box_y * 3 + 3 ):
        for j in range(box_x * 3 ,box_x * 3 + 3 ):
            if no[i][j] == num and (i,j) !=pos:
                return False
    
    return True 

#just prints the board in a good layout(OCD)
def print_board(no):
    for i in range(len(no)):
        if i % 3 == 0 and i != 0:
            print(".......................")
            #prints this line after every three rows 
        for j in range (len(no[0])):
            if j % 3 == 0 and j !=0:
                print(" | ",end="")
                #doesnt go to the next line 

            if j == 8:
                print(no[i][j])
            else :
                print(str(no[i][j]) + " ",end="")

#find the empty spaces on the board ready to be filled 
def find_empty(no):
    for i in range(len(no)):
        for j in range(len(no[0])):
            if no[i][j] == 0:
                return (i,j)  #return row , column

    return None


print_board(board)
solve(board)
print("_______________________\n")
print_board(board)
