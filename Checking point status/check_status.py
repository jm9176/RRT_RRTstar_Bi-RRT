'''
To check if the randomly selected or a newly generated point
lies inside the polygon or on its boundary edges.

polygon.contains(point) only tells about if the point lies inside
polygon obstacle. It provides no status if the point lies on the
boundary edges.

In order to check the status for the boundary edges, LineString
method is used, which stores the points assigned for the
polygon and checks if the point to be verified lies on the
edges or not.
'''

import matplotlib.pyplot as plt
from shapely.geometry.polygon import Polygon
from shapely.geometry import Point, LineString

# Initializing the figure
plt.figure()
plt.axis([0,6,0,6])

# Defining the points for the obstacle
obs_pt = [[2,2],[2,4],[4,4],[4,2]]
obs_poly = Polygon(obs_pt)
plt.gca().add_patch(plt.Polygon(obs_pt, fill = True, color = 'lightgrey'))

# Inside point
pt_i = [3,3]
plt.plot(pt_i[0], pt_i[1], 'ok')

# Point on the boundary
pt_b = [2,3]
plt.plot(pt_b[0],pt_b[1],'ob')

# Point outside
pt_o = [1,3]
plt.plot(pt_o[0],pt_o[1],'or')

# Condition to check if point lies inside polygon
# using polygon.contains(point)
print(obs_poly.contains(Point(pt_i[0],pt_i[1])),
      obs_poly.contains(Point(pt_b[0],pt_b[1])),
      obs_poly.contains(Point(pt_o[0],pt_o[1])))

# Creating a linestring to verify the same
line = LineString(obs_pt)
print(line.contains(Point(pt_i[0],pt_i[1])),
      line.contains(Point(pt_b[0],pt_b[1])),
      line.contains(Point(pt_o[0],pt_o[1])))

plt.show()



