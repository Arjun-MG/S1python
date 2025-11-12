from graphics.rectangle import area as ra, perimeter as rp
from graphics.circle import area as ca, circumference as cp
from graphics.graphics_3d.cuboid import volume as cua, surface_area as cup
from graphics.graphics_3d.sphere import volume as sa, surface_area as sp

print("rectangle area:", ra(10,5))
print("rectangle perimeter:", rp(10,5))

print("\nCircle area:", ca(7))
print("circle perimeter:", cp(7))

print("\ncuboid area:", cua(2,3,4))
print("cuboid perimeter:", cup(2,3,4))

print("\nSphere area:", sa(5))
print("sphere perimeter", sp(5))