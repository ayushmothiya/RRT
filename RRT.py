import matplotlib.pyplot as plt
import random
import matplotlib.patches as patches


class RRT:
    def __init__(self):
        self.x_block = []
        self.y_block = []
        self.w_block = []
        self.h_block = []
        fig = plt.figure()
        self.ax = fig.add_subplot(111)
        self.ax.set_xlim([0, 100])
        self.ax.set_ylim([0, 100])

    def block(self, x, y, h, w):
        self.ax.add_patch(
            patches.Rectangle(
                xy=(x, y),
                width=w, height=h, linewidth=1,
                color='black', fill=True))
        self.x_block.append(x)
        self.y_block.append(y)
        self.w_block.append(w)
        self.h_block.append(h)

    def check_point_clearance(self, x, y):
        for j in range(len(self.x_block)):
            if x < self.x_block[j] or x > self.x_block[j] + self.w_block[j]:
                continue
            if y < self.y_block[j] or y > self.y_block[j] + self.h_block[j]:
                continue
            else:
                return False
        return True

    def random_points(self):
        x_dot = random.randint(1, 100)
        y_dot = random.randint(1, 100)
        while (self.check_point_clearance(x_dot, y_dot) == False):
            x_dot = random.randint(1, 100)
            y_dot = random.randint(1, 100)
        return x_dot, y_dot

    def distance_clearance(self, x1, y1, x2, y2):
        if x2 == x1:
            if y2 < y1:
                y1, y2 = y2, y1
            for y in range(y1, y2):
                if self.check_point_clearance(x1, y) == False:
                    return False
        elif y2 == y1:
            if x2 < x1:
                x1, x2 = x2, x1
            for x in range(x1, x2):
                if self.check_point_clearance(x, y1) == False:
                    return False
        else:
            slope = (y2 - y1) / (x2 - x1)
            b = y1 - slope * x1
            if abs(slope) > 1:
                if y2 < y1:
                    y1, y2 = y2, y1
                for y in range(y1, y2):
                    x = (y - b) / slope
                    if self.check_point_clearance(x, y) == False:
                        return False
            else:
                if x2 < x1:
                    x1, x2 = x2, x1
                for x in range(x1, x2):
                    y = slope * x + b
                    if self.check_point_clearance(x, y) == False:
                        return False
        return True

    def run(self, curr_node_x, curr_node_y, end_node_x, end_node_y):
        if self.check_point_clearance(curr_node_x, curr_node_y) == False:
            return ("Start point falling on block!")
        if self.check_point_clearance(end_node_x, end_node_y) == False:
            return ("End point falling on block!")

        path_list_x = []
        path_list_y = []
        path_list_x.append(curr_node_x)
        path_list_y.append(curr_node_y)
        while (self.distance_clearance(curr_node_x, curr_node_y, end_node_x, end_node_y) == False):
            new_node_x, new_node_y = self.random_points()
            if self.distance_clearance(curr_node_x, curr_node_y, new_node_x, new_node_y) == True:
                curr_node_x, curr_node_y = new_node_x, new_node_y
                path_list_x.append(curr_node_x)
                path_list_y.append(curr_node_y)
                plt.plot(curr_node_x, curr_node_y, 'go')

        path_list_x.append(end_node_x)
        path_list_y.append(end_node_y)
        plt.plot(path_list_x, path_list_y, 'go', linestyle="--")
        plt.plot(path_list_x[0], path_list_y[0], 'ro')
        self.ax.add_patch(
            patches.Circle(
                xy=(path_list_x[0], path_list_y[0]),
                radius=5, linewidth=1,
                color='green', fill=False))
        plt.plot(end_node_x, end_node_y, 'ro')
        self.ax.add_patch(
            patches.Circle(
                xy=(end_node_x, end_node_y),
                radius=5, linewidth=1,
                color='green', fill=False))
        plt.show()
        return
