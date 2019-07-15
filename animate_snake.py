import snake as sn
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Box parameters:

rows = 10
cols = 10
start_position = (0,0)

plot_positions, num_of_moves, num_of_steps = sn.snake(rows, cols, position=start_position)

print("\nNumber of moves: ", num_of_moves)
print("Number of steps: ", num_of_steps)


with plt.style.context('ggplot'):

    fig, ax = plt.subplots()
    ax.yaxis.set_major_locator(plt.NullLocator())
    ax.xaxis.set_major_formatter(plt.NullFormatter())
    ax.set(xlim=(-1, rows + 1), ylim=(-1, cols + 1))
    line, = ax.plot([], [], color='red', linewidth=6)


# ======== Animation ===================================

def line_coordinates(coordinates=()):
    # changes plot positions into line coordinates

    x_point = coordinates[0]
    y_point = coordinates[1]
    num_of_points = coordinates[2] + 1  # number of steps + 1
    x_axis = np.linspace(x_point[0], x_point[1], num=num_of_points, dtype='int32')
    y_axis = np.linspace(y_point[0], y_point[1], num=num_of_points, dtype='int32')
    return x_axis, y_axis


def init():
    line.set_data([], [])
    return line,


def animate(l):
    x, y = line_coordinates(l)
    line.set_data(x, y)
    return line,


all_lines = plot_positions
ani = animation.FuncAnimation(fig, animate, all_lines, init_func=init, interval=200, repeat=False, blit=True)
# ani.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()
