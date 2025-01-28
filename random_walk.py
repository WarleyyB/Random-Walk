from random import choice

class RandonWalk():
    """A class to create random walks"""
    def __init__(self, num_steps=5000, distance_steps=[0, 1, 2, 3, 4]):
        self.num_steps = num_steps
        self.distance_steps = distance_steps
        self.x_values = [0]
        self.y_values = [0]
        self.z_values = [0]

    def fill_steps(self):
        """Calculate all the random walk moves"""

        #Keep stepping until the random walk ends
        while len(self.x_values) < self.num_steps:

            #Decides direction, and distance to be followed in this direction
            x_direction = choice([1, -1])
            x_distance = choice(self.distance_steps)
            x_steps = x_direction * x_distance

            y_diretion = choice([1, -1])
            y_distance = choice(self.distance_steps)
            y_steps = y_diretion * y_distance

            z_diretion = choice([1, -1])
            z_distance = choice(self.distance_steps)
            z_steps = z_diretion * z_distance

            #Reject moves going to nowhere
            if x_steps == 0 and y_steps == 0 and z_steps == 0:
                continue

            #Calculates next x and y values
            next_x = self.x_values[-1] + x_steps
            next_y = self.y_values[-1] + y_steps
            next_z = self.z_values[-1] + z_steps

            #Concatenate the result of the steps to all self lists
            self.x_values.append(next_x)
            self.y_values.append(next_y)
            self.z_values.append(next_z)