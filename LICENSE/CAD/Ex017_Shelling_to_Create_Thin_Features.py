import cadquery as cq

# Create a hollow box that's open on both ends with a thin wall.
# 1.  Establishes a workplane that an object can be built on.
# 1a. Uses the named plane orientation "front" to define the workplane, meaning
#     that the positive Z direction is "up", and the negative Z direction
#     is "down".
# 2.  Creates a plain box to base future geometry on with the box() function.
# 3.  Selects faces with normal in +z direction.
# 4.  Create a shell by cutting out the top-most Z face.
result = cq.Workplane("front").box(2, 2, 2).faces("+Z").shell(0.05)

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