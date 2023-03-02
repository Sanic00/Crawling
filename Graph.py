import matplotlib.pyplot as plt
import Homework as hw

def graph_painting():
    plt.subplot(2, 1, 1)
    plt.plot(hw.df.Date, hw.df.volume, '#4DD0E1')
    plt.xlabel('date')
    plt.ylabel('volume')
    plt.title('SAMSUNG')

    plt.subplot(2, 1, 2)
    plt.plot(hw.df.Date, hw.df.End, '#4DD0E1')
    plt.xlabel('date')
    plt.ylabel('price')
    plt.title('SAMSUNG')

    plt.tight_layout()
    plt.show()
