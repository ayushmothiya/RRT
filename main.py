import RRT
RRT = RRT.RRT()
### Add blocks here providing (starting_x_ coordinate, starting_y_ coordinate, height, width) as parameters ###
RRT.block(50,50,80,30)
RRT.block(5,30,60,30)

### Call the "run" function providing (x_coordinate_starting node, y_coordinate_starting node, x_coordinate_target node, y_coordinate_target node) as parameters ###
RRT.run(20,98,90,90)