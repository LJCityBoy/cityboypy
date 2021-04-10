import cadquery as cq

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCone
from OCC.Core.TopLoc import TopLoc_Location
from OCC.Core.TopoDS import TopoDS_Shape
from OCC.Core.gp import gp_Pnt, gp_Trsf, gp_Vec, gp_Ax1, gp_Dir
from OCC.Display.OCCViewer import rgb_color
from OCC.Display.SimpleGui import init_display

display, start_display, add_menu, add_function_to_menu = init_display()

# Displays the result of this script
#show_object(result)
def show_object(result):
    shapes = result.objects  # cq.occ_impl.shapes
    for shape in shapes:
      display.DisplayShape(shape.wrapped, update=True) #cq.Shape.wrapped

# These can be modified rather than hardcoding values for each dimension.
length = 80.0               # Length of the block
height = 60.0               # Height of the block
thickness = 10.0            # Thickness of the block
center_hole_dia = 22.0      # Diameter of center hole in block

# Create a block based on the dimensions above and add a 22mm center hole.
# 1.  Establishes a workplane that an object can be built on.
# 1a. Uses the X and Y origins to define the workplane, meaning that the
# positive Z direction is "up", and the negative Z direction is "down".
# 2.  The highest (max) Z face is selected and a new workplane is created on it.
# 3.  The new workplane is used to drill a hole through the block.
# 3a. The hole is automatically centered in the workplane.
result = cq.Workplane("XY").box(length, height, thickness) \
    .faces(">Z").workplane().hole(center_hole_dia)



if __name__ == "__main__":

    # Displays the result of this script
    show_object(result)

    start_display()