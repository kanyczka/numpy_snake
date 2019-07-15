import time
import snake as sn
import numpy as np
import matplotlib.pyplot as plt


# Box parameters:
rows = 10
cols = 10
start_position = (0,0)

no_of_runs = 10
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

arr_file_name = 'all_moves_arr.npy'
sn.array_to_file(all_moves_arr, arr_file_name)
# saved_array = sn.array_from_file(arr_file_name)

# prepare data for plotting and plot
array_of_runs_split = np.hsplit(all_moves_arr, 2)
x = array_of_runs_split[0]
y = array_of_runs_split[1]
plt.rcParams["figure.figsize"] = (20, 10)
plt.plot(x, y)
plt.xlabel("NUMBER OF MOVES")
plt.ylabel("NUMBER OF OCCURENCES")
plt.title("1.000.000 RUNS EXAMPLES")
text_x = 2 / 3 * np.amax(x)
text_y = 4 / 5 * np.amax(y)
plot_text = "The snake function ran 1 mln times on google colab.\n'It took 50 minutes to execute it on GPU.\n" \
            "Output data was saved in an numpy array.\nEach run of the snake function appends to the list a number" \
            " of moves to fill the box"
plt.text(text_x, text_y, plot_text)
plt.plot(x, y)
plt.savefig("snake_plot.png")




