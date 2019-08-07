"""
Snake is a short applications that uses numpy array to calculate possible snake moves on a grid box.
The rules are: only forward moves are possible, the snake can't move backwards, it is allowed to
take the same paths though. The aim is to visit every point (every coordinate) in the box.
The application calculates number of possible moves and steps and takes random choices -
both the direction and the amount of steps are random.
The amount of steps during one move equals the snakes length and can only be taken between positions
with integer coordinates (x, y)
The result of calculation is returned and presented on a plot with matplotlib animation.
Every run returns the total number of steps and moves.

"""
import numpy as np
import matplotlib.pyplot as plt
import os
import random


def snake(rows=10, cols=10, position=(0, 0), verbose=False):
    """
        Creates a box with given rows and columns and calculates the path
        that was taken to fill all box points. The function ends when all
        points have been visited. Moves and steps are chosen randomly.

        Parameters
        ----------
        rows : int, optional, default: 10

        cols : int, optional, default: 10

        position : tuple of integers in range position[0]: (0, row-1), position[1]: (0, col-1), optional, default: (0,0)


        Returns:
        --------
        plot_positions : coordinates of all vectors that describe each move taken from one point to the next one

        num_of_moves : total number of moves

        num_of_steps : total number of steps (one move consists of possible range of steps
    """

    def choose_no_of_steps(move=(0,'')):
        # random number of possible steps

        if move[1]:
            steps = random.randint(1, move[1])
        else:
            steps = 0
        return steps

    box = np.zeros((rows, cols), dtype=int)
    row_position = position[0]
    col_position = position[1]
    box[row_position][col_position] = 1
    move_possible = True
    vorbidden_move = ''
    plot_positions = []
    opposite_moves = {'steps_right': 'steps_left',
                      'steps_left': 'steps_right',
                      'steps_up': 'steps_down',
                      'steps_down': 'steps_up'}
    num_of_moves = 0
    num_of_steps = 0
    if verbose:
        print("Executing snake... ")

    while move_possible:
        num_of_moves += 1
        possible_moves_names = ['steps_up', 'steps_down', 'steps_right', 'steps_left']
        max_steps_up = row_position
        max_steps_down = (rows - 1) - row_position
        max_steps_right = (cols - 1) - col_position
        max_steps_left = col_position
        possible_moves_steps = [max_steps_up, max_steps_down, max_steps_right, max_steps_left]

        if vorbidden_move:
            index_to_delete = possible_moves_names.index(vorbidden_move)
            del possible_moves_steps[index_to_delete]
            del possible_moves_names[index_to_delete]

        moves = list(zip(possible_moves_names, possible_moves_steps))
        # choose move only from possible moves - possible_moves_steps != 0
        moves = [possible_move for possible_move in moves if possible_move[1] != 0]
        chosen_move = random.choice(moves)
        steps = choose_no_of_steps(chosen_move)
        num_of_steps += steps

        if chosen_move[0] == 'steps_up':
            row_position -= steps

        if chosen_move[0] == 'steps_down':
            row_position += steps

        if chosen_move[0] == 'steps_right':
            col_position += steps

        if chosen_move[0] == 'steps_left':
            col_position -= steps

        if position[0] == row_position and col_position > position[1]:  # right
            move_path = box[position[0], position[1]: col_position + 1]

        if position[0] == row_position and col_position < position[1]:  # left
            move_path = box[position[0]: row_position + 1, col_position: position[1]]

        if position[1] == col_position and row_position < position[0]:  # up
            move_path = box[row_position: position[0], position[1]: col_position + 1]

        if position[1] == col_position and row_position > position[0]:  # down
            move_path = box[position[0]: row_position + 1, position[1]: col_position + 1]

        move_path[:] = 1

        starting_point = [position[0], row_position]  # x1, x2
        ending_point = [position[1], col_position]  # y1, y2

        vorbidden_move = opposite_moves[chosen_move[0]]
        plot_positions.append((starting_point, ending_point, steps))
        position = (row_position, col_position)

        any_zeros = np.where(box == 0)
        if any_zeros[0].size == 0:
            move_possible = False

    if verbose:
        print(f"Number of moves: {num_of_moves}")
        print(f"Number of steps: {num_of_steps}")

    return plot_positions, num_of_moves, num_of_steps


def array_to_file(array, outfile):
    if isinstance(array, np.ndarray):
        np.save(outfile, array)
        return True
    else:
        raise ValueError("Not a numpy array")


def array_from_file(outfile):
    if os.path.isfile(outfile):
        return np.load(outfile)
    else:
        raise FileNotFoundError("No such file found")


def plot_number_of_moves(array_of_runs, text='', title='', save=False):
    array_of_runs_split = np.hsplit(array_of_runs, 2)
    x = array_of_runs_split[0]
    y = array_of_runs_split[1]
    text_x = 2 / 3 * np.amax(x)
    text_y = 4 / 5 * np.amax(y)
    plt.rcParams["figure.figsize"] = (20, 10)
    plt.plot(x, y)
    plt.xlabel("NUMBER OF MOVES")
    plt.ylabel("NUMBER OF OCCURENCES")
    plt.title(title)
    plt.text(text_x, text_y, text)
    plt.plot(x,y)
    if save:
        plt.savefig(f"snake_plot.png")
    plt.show()


