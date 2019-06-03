import matplotlib.pyplot as plt
from shapely.geometry.polygon import Polygon
from shapely.geometry import Point

plt.figure()
plt.axis([0,8,0,8])

# Defining the set of points to form the
# obstacle polygon
point = [[2,2], [2,4], [4,4], [4,2]]
polygon = Polygon(point)

# Plotting the obstacles
plt.gca().add_patch(plt.Polygon(point, fill = True, color = 'lightgrey'))

# To check if the point lies inside the polygon or not
if polygon.contains(Point(2.1,3.2)):
   print(True)
else:
    print(False)

plt.show()
