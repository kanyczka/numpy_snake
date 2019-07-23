# numpy_snake

snake() is a function that uses **numpy** array to calculate possible moves on a grid box (numpy array).<br>
The rules are: 
- only forward moves are possible, backwards moves are vorbidden 
- it is allowed to take the same paths
- the aim is to visit every point (every coordinate) in the box. Coordinates are integer numbers.

The application calculates number of possible moves and steps and takes random choices - 
both the direction and the amount of steps are random.
The amount of steps during one move equals the snakes length and can only be taken between positions 
with integer coordinates (x, y).<br>
The result of calculation is returned and presented on a plot with **matplotlib** plot animation - _animate_snake.py_ <br>
Every run returns the total number of steps and moves.

##### Parameters: 

- rows, columns of the box - must be integers
- starting position: some box coordinates, e.g. (0, 1)

Example:
```
rows = 10
cols = 10
start_position = (1,4)
snake(rows, cols, position=start_position, verbose=True)
```
----
- snake.py - function module
- animate_snake.py - animation of all moves - _snake_red.mp4_ is an example of such animation
- snake_run.py - short application which collects data and plots graph from many runs of the snake function (like the graph at the end of the page)
----
After finishig the application I checked

**HOW MANY MOVES DOES THE APPLICATION NEED TO VISIT ALL THE BOX (ARRAY) POSITIONS.**

To find the answer I took the 10 x 10 dimention's array to collect data from 1 mln runs (_snake_run.py_).
To calculate all 1 mln moves I used Google Colab's GPU. It took 50 minutes to execute and collect data.<br>
The output array with all the results is saved in _all_moves_arr.npy_<br>
It seems, that the most frequent number of moves is around 150 - occured more than 8.000 times.<br>
6000 times the application needed between 110 and 200 moves.

The **minimum** number of moves the program needed - **42.**<br>
The **maximum** number of moves done to cover the box -  **794**

The graph below shows all 1 mln results:

![Number of moves plot](snake_plot_1mln.png)

