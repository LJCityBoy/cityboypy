from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCone
from OCC.Core.TopLoc import TopLoc_Location
from OCC.Core.TopoDS import TopoDS_Shape
from OCC.Core.gp import gp_Pnt, gp_Trsf, gp_Vec, gp_Ax1, gp_Dir
from OCC.Display.OCCViewer import rgb_color

import cadquery as cq

# These can be modified rather than hardcoding values for each dimension.
length = 80.0                               # Length of the block
width = 60.0                                # Width of the block
height = 100.0                              # Height of the block
thickness = 10.0                         # Thickness of the block
center_hole_dia = 22.0             # Diameter of center hole in block
cbore_hole_diameter = 2.4     # Bolt shank/threads clearance hole diameter
cbore_inset = 12.0                    # How far from the edge the cbored holes are set
cbore_diameter = 4.4              # Bolt head pocket hole diameter
cbore_depth = 2.1                   # Bolt head pocket hole depth

# Create a 3D block based on the dimensions above and add a 22mm center hold
# and 4 counterbored holes for bolts
# 1.  Establishes a workplane that an object can be built on.
# 1a. Uses the X and Y origins to define the workplane, meaning that the
# positive Z direction is "up", and the negative Z direction is "down".
# 2.  The highest(max) Z face is selected and a new workplane is created on it.
# 3.  The new workplane is used to drill a hole through the block.
# 3a. The hole is automatically centered in the workplane.
# 4.  The highest(max) Z face is selected and a new workplane is created on it.
# 5.  A for-construction rectangle is created on the workplane based on the
#     block's overall dimensions.
# 5a. For-construction objects are used only to place other geometry, they
#     do not show up in the final displayed geometry.
# 6.  The vertices of the rectangle (corners) are selected, and a counter-bored
#     hole is placed at each of the vertices (all 4 of them at once).

result = cq.Workplane("XY").box(length, height, thickness) \
    .faces(">Z").workplane().hole(center_hole_dia) \
    .faces(">Z").workplane() \
    .rect(length - cbore_inset, height - cbore_inset, forConstruction=True) \
    .vertices().cboreHole(cbore_hole_diameter, cbore_diameter, cbore_depth) \
    .edges("|Z").fillet(2.0)

# Displays the result of this script
#show_object(result)

def show_object(result):
    shapes = result.objects  # cq.occ_impl.shapes
    for shape in shapes:
      display.DisplayShape(shape.wrapped, update=True) #cq.Shape.wrapped

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()

   # my_cone = BRepPrimAPI_MakeCone(1, 0, 4).Shape()

    #cone = TopoDS_Shape(my_cone)
    #T = gp_Trsf()
    #T.SetTranslation(gp_Vec(0, 5, 0))
    #loc = TopLoc_Location(T)
    #cone.Location(loc)

    #display.DisplayShape(my_cone, update=True,color=rgb_color(1,0,0))
    #display.DisplayShape(cone, update=True,color=rgb_color(0,0,1))
    #shape = to_compound(obj)
   # shapes=result.objects  #cq.occ_impl.shapes
   # for shape in shapes:
    #    context.Display(ais)
       #display.DisplayShape(shape.wrapped, update=True) #cq.Shape.wrapped
       #display.DisplayShape(shape.wrapped, update=True, color=rgb_color(0, 0, 1))
       #display.DisplayShape(shape.wrapped, update=True, color=rgb_color(1, 0, 0))
   # cq.Workplane("XY").ctx.
    show_object(result)

    start_display()