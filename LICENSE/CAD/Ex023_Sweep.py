import cadquery as cq

# Points we will use to create spline and polyline paths to sweep over
pts = [
    (0, 1),
    (1, 2),
    (2, 4)
]

# Spline path generated from our list of points (tuples)
path = cq.Workplane("XZ").spline(pts)

# Sweep a circle with a diameter of 1.0 units along the spline path we just created
defaultSweep = cq.Workplane("XY").circle(1.0).sweep(path)

# Sweep defaults to making a solid and not generating a Frenet solid. Setting Frenet to True helps prevent creep in
# the orientation of the profile as it is being swept
frenetShell = cq.Workplane("XY").circle(1.0).sweep(path, makeSolid=True, isFrenet=True)

# We can sweep shapes other than circles
defaultRect = cq.Workplane("XY").rect(1.0, 1.0).sweep(path)

# Switch to a polyline path, but have it use the same points as the spline
path = cq.Workplane("XZ").polyline(pts)

# Using a polyline path leads to the resulting solid having segments rather than a single swept outer face
plineSweep = cq.Workplane("XY").circle(1.0).sweep(path)

# Switch to an arc for the path
path = cq.Workplane("XZ").threePointArc((1.0, 1.5), (0.0, 1.0))

# Use a smaller circle section so that the resulting solid looks a little nicer
arcSweep = cq.Workplane("XY").circle(0.5).sweep(path)

# Displays the result of this script
#show_object(result)

def show_object(result):
    shapes = result.objects
    for shape in shapes:
      display.DisplayShape(shape.wrapped, update=True)

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()

    #show_object(result)
    # Translate the resulting solids so that they do not overlap and display them left to right
    show_object(defaultSweep)
    show_object(frenetShell.translate((5, 0, 0)))
    show_object(defaultRect.translate((10, 0, 0)))
    show_object(plineSweep.translate((15, 0, 0)))
    show_object(arcSweep.translate((20, 0, 0)))
    start_display()
