import snake as sn
import numpy as np

# file with 1 mln runs array
arr_file = '1mln_np_array_all.npy'

# plot descriptions
title = '1.000.000 RUNS EXAMPLES'
text = 'The snake function ran 1 mln times on google colab.\nIt took 50 minutes to execute it on GPU.\nOutput data was' \
       ' saved in an numpy array.'

# array from file
all_moves_arr = sn.array_from_file(arr_file)

# prepare array with number of moves and number of occurences
all_moves, counts = np.unique(all_moves_arr, return_counts=True)
all_moves_arr = np.array(list(zip(all_moves, counts)))

# plot results
sn.plot_number_of_moves(all_moves_arr, text, title, save=True)
