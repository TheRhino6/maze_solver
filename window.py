from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    def __init__(self, width, height):
        # Create a new root widget
        self.__root = Tk()

        # Set the title of the window
        self.__root.title("Maze Solver")

        # Create a canvas widget with specified width and height
        self.__canvas = Canvas(self.__root, width=width, height=height)
        
        # Pack the canvas so it's ready to be drawn
        self.__canvas.pack(fill=BOTH, expand=1)

        # Create a data member to represent if the window is running
        self.__running = False

        # Set the protocol for window close event
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        # Set the running state to True
        self.__running = True
        while self.__running == True:
            self.redraw()

    def close(self):
        # Close the window
        self.__root.destroy()
        # Set the running state to False
        self.__running = False

    def draw_line(self, line, fill_color):
        # Draw a line on the canvas from start to end
        line.draw(self.__canvas, fill_color)
        