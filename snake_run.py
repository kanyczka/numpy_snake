import time
import snake as sn
import numpy as np
import matplotlib.pyplot as plt


# Starting parameters:
rows = 10
cols = 10
start_position = (0,0)
no_of_runs = 5000

moves_list = []   # number of moves needed to fill the box

print("Counting... ")
start_time = time.time()

for i in range(no_of_runs):
  _, n_moves, _ = sn.snake(rows, cols, position=start_position, verbose=True)
  moves_list.append(n_moves)

end_time = time.time()
executing_time = end_time - start_time
print(f"Executing time of {no_of_runs} runs: ", executing_time)


# prepare array with number of moves and number of occurences
moves_arr = np.array(moves_list)
np.sort(moves_arr)
all_moves, counts = np.unique(moves_arr, return_counts=True)
all_moves_arr = np.array(list(zip(all_moves, counts)))


# save array to file
arr_file_name = 'all_moves_arr.npy'
sn.array_to_file(all_moves_arr, arr_file_name)
# saved_array = sn.array_from_file(arr_file_name)


# prepare data for plotting and plot
text = f'Total number of runs: {no_of_runs}'
title = f'{no_of_runs} RUNS EXAMPLES'
sn.plot_number_of_moves(all_moves_arr, text, title)

