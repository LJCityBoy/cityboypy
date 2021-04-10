import cadquery as cq

# Create a plate with 4 rounded corners in the Z-axis.
# 1.  Establishes a workplane that an object can be built on.
# 1a. Uses the X and Y origins to define the workplane, meaning that the
#     positive Z direction is "up", and the negative Z direction is "down".
# 2.  Creates a plain box to base future geometry on with the box() function.
# 3.  Selects all edges that are parallel to the Z axis.
# 4.  Creates fillets on each of the selected edges with the specified radius.
result = cq.Workplane("XY").box(3, 3, 0.5).edges("|Z").fillet(0.125)

# Displays the result of this script
#show_object(result)

def show_object(result):
    shapes = result.objects
    for shape in shapes:
      display.DisplayShape(shape.wrapped, update=True)

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()

    show_object(result)

    start_display()
