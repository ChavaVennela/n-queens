import random

# compute random initial state

def get_random_state(n):
    state=[]
    for i in range(n):
        state.append(random.randint(1, n))
    return state

#generate board

def generate_board(state):
    board=[]
    for i in range(len(state)):
        temp=[]
        for j in range(len(state)):
            temp.append(0)
        board.append(temp)
    for i in range(len(state)):
        board[state[i]-1][i]=1
    return board

#compute number of attacking or conflicting pairs

def compute_attacking_pairs(state):
    number_attacking_pairs = 0
    board=generate_board(state) 
    for i in range(len(state)):
        #check upper left diagonal
        row=state[i]-2
        col=i-1
        while(row>=0 and col>=0 and board[row][col]!=1):
            row-=1
            col-=1
        if(row>=0 and col>=0):
            number_attacking_pairs+=1
        #check left part of the row
        row=state[i]-1
        col=i-1
        while(col>=0 and board[row][col]!=1):
            col-=1
        if(col>=0):
            number_attacking_pairs+=1
        #check right part of the row
        row=state[i]-1
        col=i+1
        while(col<len(state) and board[row][col]!=1):
            col+=1
        if(col<len(state)):
            number_attacking_pairs+=1
        #check upper right diagonal
        row=state[i]-2
        col=i+1
        while(row>=0 and col<len(state) and board[row][col]!=1):
            row-=1
            col+=1
        if(row>=0 and col<len(state)):
            number_attacking_pairs+=1
        #check lower left diagonal
        row=state[i]
        col=i-1
        while(row<len(state) and col>=0 and board[row][col]!=1):
            row+=1
            col-=1
        if(row<len(state) and col>=0):
            number_attacking_pairs+=1
        #check lower right diagonal
        row=state[i]
        col=i+1
        while(row<len(state) and col<len(state) and board[row][col]!=1):
            row+=1
            col+=1
        if(row<len(state) and col<len(state)):
            number_attacking_pairs+=1
    number_attacking_pairs=number_attacking_pairs/2
    return number_attacking_pairs

#Basic hill-climbing algorithm for n queens

def hill_descending_n_queens(state, comp_att_pairs):
    while(1):
        initial_state=comp_att_pairs(state)
        optimum_state=initial_state
        optimum_pos=[-1, -1]
        for i in range(len(state)):
            for j in range(len(state)):
                if(state[i]-1!=j):
                    temp=state[i]
                    state[i]=j+1
                    current_state=comp_att_pairs(state)
                    state[i]=temp
                    if(current_state<optimum_state):
                        optimum_state=current_state
                        optimum_pos[0]=i
                        optimum_pos[1]=j
        if(optimum_state<initial_state):
            state[optimum_pos[0]]=optimum_pos[1]+1
        else:
            break
    return state

#Hill-Climbing algorithm for n queens with restart

def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
    final_state = get_rand_st(n)
    while(compute_attacking_pairs(final_state)>0):
        final_state=hill_descending(get_rand_st(n), comp_att_pairs)
    return final_state