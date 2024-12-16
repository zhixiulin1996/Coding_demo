"""
File: babygraphics.py
Name: Zhi-Xiu Lin
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    space = (width - GRAPH_MARGIN_SIZE * 2) // len(YEARS)
    return year_index * space + GRAPH_MARGIN_SIZE


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for index in range(len(YEARS)):
        x_axis = get_x_coordinate(CANVAS_WIDTH, index)
        canvas.create_line(x_axis, 0, x_axis, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x_axis + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[index], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #

    for j in range(len(lookup_names)):  # iterate all names in the lookup_names
        coordinate = []  # To record the point and the rank of each year
        # Record every point coordination and label the text beside the points
        for i in range(len(YEARS)):
            # rank<=1000
            if (lookup_names[j] in name_data) and (str(YEARS[i]) in name_data[lookup_names[j]]):
                x = get_x_coordinate(CANVAS_WIDTH, i)
                rank = int(name_data[lookup_names[j]][str(YEARS[i])])  # remember to change data type here...
                y = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * rank // 1000 + GRAPH_MARGIN_SIZE
                canvas.create_text(x + TEXT_DX, y, text=f"{lookup_names[j]} {rank}", anchor=tkinter.SW,
                                   fill=COLORS[j % len(COLORS)])  # To make color repeat
                coordinate.append([x, y])  # record the data point in the list
            # rank>1000
            else:
                x = get_x_coordinate(CANVAS_WIDTH, i)
                y = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
                canvas.create_text(x + TEXT_DX, y, text=f"{lookup_names[j]} *", anchor=tkinter.SW,
                                   fill=COLORS[j % len(COLORS)])  # To make color repeat
                coordinate.append([x, y])  # record the data point in the list
        # Start connecting point to point recorded in coordinate
        for i in range(len(coordinate) - 1):  # i.e. 12 point only need 11 lines to connect them
            canvas.create_line(coordinate[i][0], coordinate[i][1], coordinate[i + 1][0], coordinate[i + 1][1],
                               width=LINE_WIDTH, fill=COLORS[j % len(COLORS)])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
