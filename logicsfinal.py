import random
def start_game():
    matrix=[]
    #creating a matrix of size 4*4
    for i in range(4):
        matrix.append([0]*4)
    return matrix

#add a new 2 where it is empty
def add_new_2(matrix):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while(matrix[r][c]!=0):
         r=random.randint(0,3)
         c=random.randint(0,3)
    matrix[r][c]=2

#to get the current state of the game
def get_current_state(matrix):
    for i in range(4):
        for j in range(4):
            if(matrix[i][j]==2048):
                return 'WON'
    
    for i in range(4):
        for j in range(4):
            if(matrix[i][j]==0):
                return 'GAME NOT OVER'
            
    for i in range(3):
        for j in range(3):
            if(matrix[i][j]==matrix[i][j+1] or matrix[i][j]==matrix[i+1][j]):
                return 'GAME NOT OVER'
    
    for j in range(3):
        if(matrix[3][j]==matrix[3][j+1]):
            return 'GAME NOT OVER'
    
    for i in range(3):
        if(matrix[i][3]==matrix[i+1][3]):
            return 'GAME NOT OVER'
        
    return 'LOST'

#now we will compress the matrix
def compress(matrix):
    changed=False
    mat=[[0]*4 for i in range(4)]
    for i in range(4):
        pos=0
        for j in range(4):
            if(matrix[i][j]!=0):
                mat[i][pos]=matrix[i][j]
                pos=pos+1
    if(mat!=matrix):
        changed=True
    return mat,changed

#merge the matrix
def merge(matrix):
    changed=False
    for i in range(4):
        for j in range(3):
            if(matrix[i][j]==matrix[i][j+1] and matrix[i][j]!=0):
                changed=True
                matrix[i][j]=2*matrix[i][j]
                matrix[i][j+1]=0
    return matrix,changed

#reverse a matrix
def reverse(matrix):
    mat=[]
    for i in range(4):
        mat.append([])
        for j in range(4):
            mat[i].append(matrix[i][4-j-1])
    return mat

#transpose the matrix
def transpose(matrix):
    mat=[]
    for i in range(4):
        mat.append([])
        for j in range(4):
            mat[i].append(matrix[j][i])
    return mat
            

#move left
def move_left(matrix):
    c1,changed1=compress(matrix)
    m,changed2=merge(c1)
    changed=changed1 or changed2
    c2,changed3=compress(m)
    return c2,changed

#move right
def move_right(matrix):
    r1=reverse(matrix)
    c1,changed1=compress(r1)
    m,changed2=merge(c1)
    changed=changed1 or changed2
    c2,changed3=compress(m)
    r2=reverse(c2)
    return r2,changed

#move up
def move_up(matrix):
    t1=transpose(matrix)
    c1,changed1=compress(t1)
    m,changed2=merge(c1)
    changed=changed1 or changed2
    c2,changed3=compress(m)
    t2=transpose(c2)
    return t2,changed

#move down
def move_down(matrix):
    t1=transpose(matrix)
    r1=reverse(t1)
    c1,changed1=compress(t1)
    m,changed2=merge(c1)
    changed=changed1 or changed2
    c2,changed3=compress(m)
    r2=reverse(c2)
    t2=transpose(r2)
    return t2,changed
    

    