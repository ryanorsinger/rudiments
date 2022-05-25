import matplotlib.pyplot as plt


def visualize():
    x = range(1, 100)
    y = [n**2 for n in x]
    plt.scatter(x, y)

    plt.show() 
