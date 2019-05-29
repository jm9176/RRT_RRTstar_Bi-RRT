# Function for retracing the path
def retrace_path(dict_parent, curr_var, start):
    # path list storing the trace of path from
    # start to goal
    path = [curr_var]

    while curr_var != start:
        for var in dict_parent:
            if var == curr_var:
                curr_var = dict_parent[var]
                path.append(curr_var)

    return path[::-1]
