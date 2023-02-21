import helper_func as hf

n=20

# get a random initial state

state=hf.get_random_state(n)
print("The Initial random state: "+str(state)+", Number of conflicting pairs or attacking pairs: "+str(hf.compute_attacking_pairs(state)))

#calling hill descending once

optimum_state=hf.hill_descending_n_queens(state, hf.compute_attacking_pairs)
print("State after running hill-descending once: "+str(optimum_state)+", Number of conflicting pairs: "+str(hf.compute_attacking_pairs(optimum_state)))

#Fully solved state for a given n

print("A solution for "+str(n)+" queens: "+str(hf.n_queens(n, hf.get_random_state, hf.compute_attacking_pairs, hf.hill_descending_n_queens)))