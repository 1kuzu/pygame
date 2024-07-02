from random_walk import RandomWalk
import matplotlib.pyplot as plt

while 1==1:
    rw = RandomWalk()
    rw.fill_walk()
    plt.style.use('classic')
    fig,ax = plt.subplots()
    point_numbers  = range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,c = point_numbers ,cmap = plt.cm.Blues,edgecolors ='none',s=10)
    plt.show()
    keep_running = input('还要在来一次吗(y/n):')
    if keep_running == 'n':
        break