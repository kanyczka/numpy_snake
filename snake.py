"""
Snake is a short applications that uses numpy array to calculate possible snake moves on a grid box.
The rules are: only forward moves are possile, the snake can't move backwards, it is allowed to
take the same paths though. The aim is to visit every point in the box.
The application calculates number of possible moves and takes random choice
(both the direction and the amount of steps are random).
The amount of steps equals the snakes length and can only be taken between positions with integer coordinates (x, y)
The result of calculation is returned and presented on a plot with matplotlib animation.
Every run returns the total number of steps and moves.

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


def choose_direction(steps=[]):
    # random choice of possible direction: up, down, left, right

    if len(steps) > 0:
        steps = np.array(steps)
        possible_moves = np.where(steps != 0)  # result is a tuple
        step = np.random.choice(possible_moves[0])
    else:
        step = 0
    return step


def choose_no_of_steps(move=(0,)):
    # random number of possible steps
    if move[1]:
        steps = random.randint(1, move[1])
    else:
        steps = 0
    return steps


def snake(rows=10, cols=10, position=(0, 0)):
    # calculates all positions taken by random moves and steps

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
    print("Executing", end='')

    while move_possible:
        print(".", end='')

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

        chosen_move = choose_direction(possible_moves_steps)
        chosen_move = moves[chosen_move]
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

    return {"plot_positions": plot_positions, "num_of_moves": num_of_moves, "num_of_steps": num_of_steps}

def line_coordinates(coordinates=()):
    x_point = coordinates[0]
    y_point = coordinates[1]
    num_of_points = coordinates[2] + 1  # number of steps + 1
    x_axis = np.linspace(x_point[0], x_point[1], num=num_of_points, dtype='int32')
    y_axis = np.linspace(y_point[0], y_point[1], num=num_of_points, dtype='int32')
    return x_axis, y_axis

# ==================================

rows = 50
cols = 50
s = snake(rows, cols, position=(0, 0))

print("\n Number of moves: ", s['num_of_moves'])
print("Number of steps: ", s['num_of_steps'])

plt.style.use('ggplot')
# plt.rc('grid', linestyle='-')
fig, ax = plt.subplots()
ax.yaxis.set_major_locator(plt.NullLocator())
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.set(xlim=(-1, rows + 1), ylim=(-1, cols + 1))
line, = ax.plot([], [], color='red', linewidth=4)

# ======== Animation ================

def init():
    line.set_data([], [])
    return line,


def animate(l):
    x, y = line_coordinates(l)
    line.set_data(x, y)
    return line,


all_lines = s['plot_positions']
ani = animation.FuncAnimation(fig, animate, all_lines, init_func=init, interval=50, repeat=False, blit=True)
plt.show()
