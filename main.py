import sys
print(sys.path)

from window import Window
from point import Point
from line import Line

def main():
    # Create a window instance
    window = Window(1200, 800)

    # Create points for the line
    start_point = Point(50, 50)
    end_point = Point(200, 200)

    # Create a line using the points
    line = Line(start_point, end_point)

    # Draw the line on the window canvas
    window.draw_line(line, "blue")

    # Wait for the user to close the window
    window.wait_for_close()

if __name__ == "__main__":
    print ("This script is running!")
    main()