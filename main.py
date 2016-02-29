import numpy as np
import fit as fit
import matplotlib.pyplot as plt


def main():
    print "Hello world"
    xdata = [1, 2, 3, 4, 5]
    temp = xdata
    ydata = np.square(temp)
    a = fit.fit(xdata, ydata)
    yfunc = xdata
    print ("xdata", xdata)
    # for i in range(1, 6):
        # yfunc[i - 1] = fit.equation(i, a)
    print ("xdata", xdata)
    print a
    print yfunc
    plt.title("Fitted Plot in red vs Actual points in black")
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    xx = np.linspace(np.min(xdata), np.max(xdata))
    #plt.xlim([xdata[0]-20, xdata[-1] + 20])
    #plt.ylim([ydata[0]-2000, ydata[-1] + 2000])
    plt.plot(xx, fit.equation(xx, a), 'r-')
    #, label="Fitted Curve")
    plt.plot(xdata, ydata, 'ko')
    plt.show()


if __name__ == "__main__":
    main()
else:
    print()
