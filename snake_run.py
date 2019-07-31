import time
import snake as sn
import numpy as np


# Starting parameters:
rows = 10
cols = 10
start_position = (0,0)
no_of_runs = 5000

moves_list = []   # number of moves needed to fill the box

print("Counting... ")
start_time = time.time()

runs = 0
for i in range(no_of_runs):
    runs += 1
    print(f"Run number: {runs}")
    _, n_moves, _ = sn.snake(rows, cols, position=start_position, verbose=False)
    moves_list.append(n_moves)

end_time = time.time()
executing_time = end_time - start_time
print(f"Executing time of {no_of_runs} runs in seconds: ", executing_time)


# prepare array with all moves
moves_arr = np.array(moves_list)
sorted_moves = np.sort(moves_arr)

# save array to file
arr_file_name = 'all_moves_arr.npy'
sn.array_to_file(sorted_moves, arr_file_name)
# saved_array = sn.array_from_file(arr_file_name)

# prepare array with number of moves and number of occurences
all_moves, counts = np.unique(sorted_moves, return_counts=True)
all_moves_arr = np.array(list(zip(all_moves, counts)))

# min
print("Minimal number of moves: ", np.min(sorted_moves))
# max
print("Maximal number of moves: ", np.max(sorted_moves))
# mean
print("Mean: ", np.mean(sorted_moves))
# median:
print("Median: ", np.median(sorted_moves))
# arithmetic variance
print("Variance: ", np.var(sorted_moves))
# arithmetic standard deviation
print("Standard deviation: ", np.std(sorted_moves))


# prepare data for plotting and plot
text = f'Total number of runs: {no_of_runs}'
title = f'{no_of_runs} RUNS EXAMPLES'
sn.plot_number_of_moves(all_moves_arr, text, title)

