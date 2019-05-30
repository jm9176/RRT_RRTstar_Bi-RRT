'''
---------------RRT*--------------------

# Defining a region with radius r
Rad = r

# Creating a graph containing edges and vertices
G(V,E)

for i in range(vertices):

    # Generate a random Node
    Xnew = np.random.uniform(lower, upper)

    # check if the new point is in obstacle or not
    Polygon.contains(point), return True or False

    # Get the nearest node from the graph to the
    # generated random node
    Xnearest = Nearest(G(V,E), Xnew)

    # Get the cost between the nearest and teh random node
    Cost(Xnew) = distance(Xnew, Xnew)

    # Find the best node and its neighbors
    XBest, XNeighbors = findNeighbors(G(V,E), Xnew, Rad)

    # link the random node and the best node
    link = Chain(Xnew, XBest)

    for var in XNeighbors:
        if Cost(Xnew) + Distance(var, Xnew) < Cost(var):
            Cost(var) = Cost(XNew) + distance(XNew, var)
            Parent(var) = XNew
            G += {XNew, var}

    G += link

return G
'''
