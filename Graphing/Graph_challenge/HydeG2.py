import matplotlib.pyplot as plt

def graph(to):
    g = []
    for i in range(to):
        g.append(i<<2|i)
    plt.scatter(range(len(g)), g , s=1)
    plt.show()

if __name__ == "__main__":
    graph(10000)