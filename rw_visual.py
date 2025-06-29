import matplotlib.pyplot as plt
from random_walk import RandomWalk

#Keep creating random walks while the program be active
while True:

    #Creates a instance of random walk and fill the X and Y lists
    rw = RandomWalk(50000)
    rw.fill_walk()

    #Set plot window size
    plt.figure(figsize=(10, 6))

    #Scatter the X and Y random walk values and show it.
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1)

    #Enfatizes first and last point
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    #Hide the axis
    plt.axis('off')

    #Brings the graphic
    plt.show()

    #Leave the user decides if he wants to make a new random walk
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break