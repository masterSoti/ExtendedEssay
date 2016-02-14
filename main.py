import fit as fit
import matplotlib as plt


def main():
    print "Hello world"
    xdata = [1, 2, 3, 4, 5]
    ydata = xdata
    a = fit.fit(xdata, ydata)
    # TODO: make a graph with the array of constant the fit.fit returns
    yfunc = xdata
    for i in xdata:
        yfunc = fit.equation(i, a)


if __name__ == "__main__":
    main()
