import snake as sn

# file with 1 mln runs array
arr_file = '1mln_np_array_all.npy'

# plot descriptions
title = '1.000.000 RUNS EXAMPLES'
text = 'The snake function ran 1 mln times on google colab.\nIt took 50 minutes to execute it on GPU.\n" \
            "Output data was saved in an numpy array.\nEach run of the snake function appends to the list a number" \
            " of moves to fill the box'

# array from file
all_moves_arr = sn.array_from_file(arr_file)

# plot results
sn.plot_number_of_moves(all_moves_arr, text, title)


