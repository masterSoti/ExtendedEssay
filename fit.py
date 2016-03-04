import numpy
import math
"""
the findSSE function finds the sse value of any fit
xdata is an array of all of the points on thecount axis
ydata is an array of all of the points of the y axis
function is the function for which you are curve fitting
"""


def findSSE(xdata, ydata, function, *popt):
    if(len(xdata) is len(ydata)):
        # do this
        i = 0
        sse = 0
        while i < len(xdata):
            y = ydata[i] - function(xdata[i], *popt)
            y = y * y
            sse = sse + y
            i = i + 1
        return sse
    else:
        print "please make sure that the xdata and ydata",
        " array are the same size"


"""
the plan for the fitting is the brute force so this funcition increments
the fitting by some number ...you will see what it does, it is dificcult
to describe
"""


def fit(xdata, ydata):
    a = [0, 0, 0, 0]
    sse = numpy.array([])
    count = 0
    primeParameter = a
    smallest = findSSE(xdata, ydata, equation, a)
    a[0] = 0
    # beginning of the while loops
    while a[0] < 100:
        a[1] = 0
        while a[1] < 100:
            a[2] = 0
            while a[2] < 100:
                a[3] = 0
                while a[3] < 100:
                    # TODO: make a better algorithm for the fit
                    # find the sse
                    z = findSSE(xdata, ydata, equation, a)
                    # save the sse to an array
                    numpy.append(sse, z)
                    if z < smallest:
                        smallest = z
                        primeParameter = a
                    if z == 0:
                        print "sse = 0"
                        return primeParameter
                    # this is to make this printable
                    b = str(count) + " out of " + str(100**4) + ": " + str(z)
                    # The above are all part of a line
                    # print b
                    count = count + 1
                    a[3] = a[3] + 1
                a[2] = a[2] + 1
            a[1] = a[1] + 1
        a[0] = a[0] + 1
    print "sse = ", z
    return primeParameter

def fit_expo(xdata, ydata):
    a = numpy.zeros(3)
    primeParameter = a
    smallest = findSSE(xdata, ydata, equation_exponential, a)
    while a[0] < 100:
        a[1] = 0
        while a[1] < 100:
            a[2] = 0
            while a[2] < 100:
                z = findSSE(xdata, ydata, equation_exponential, a)
                if z < smallest:
                    smallest = z
                    primeParameter = a
                if z == 0:
                    print "sse = 0"
                    return primeParameter
                a[2] = a[2] + 1
            a[1] = a[1] + 1
        a[0] = a[0] + 1
    return primeParameter

def fitLog(xdata, ydata):
    a = numpy.ones(4)
    primeParameter = a
    smallest = findSSE(xdata, ydata, equation_log, a)
    while a[0] < 100:
        a[1] = 1
        while a[1] < 100:
            a[2] = 1
            while a[2] < 100:
                a[3] = 1
                while a[3] < 100:
                    z = findSSE(xdata, ydata, equation_log, a)
                    if z < smallest:
                        smallest = z
                        primeParameter = a
                    if z == 0:
                        print "sse = 0"
                        return primeParameter
                    a[3] = a[3] + 1
                a[2] = a[2] + 1
            a[1] = a[1] + 1
        a[0] = a[0] + 1
    return primeParameter

def fitTrig(xdata, ydata):
    a = numpy.zeros(4)
    primeParameter = a
    smallest = findSSE(xdata, ydata, equation_trig, a)
    while a[0] < 100:
        a[1] = 0
        while a[1] < 100:
            a[2] = 0
            while a[2] < 100:
                a[3] = 0
                while a[3] < 100:
                    z = findSSE(xdata, ydata, equation_trig, a)
                    if z < smallest:
                        smallest = z
                        primeParameter = a
                    if z == 0:
                        print "sse = 0"
                        return primeParameter
                    a[3] = a[3] + 1
                a[2] = a[2] + 1
            a[1] = a[1] + 1
        a[0] = a[0] + 1
    return primeParameter

# the name is descriptive enough
def equation(i, a):
    return a[0]*i**3 + a[1]*i**2 + a[2]*i + a[3]

# for the scipy.optimize.curve_fit function
def equation_scipy(i, a, b, c, d):
    return a*numpy.power(i, 3) + b*numpy.power(i, 2) + c*i + d

def equation_exponential(i, a):
    return numpy.exp(a[0]*i + a[1]) + a[2]

def equation_exponential_scipy(i, a, b, c):
    return numpy.exp(a*i + b) + c

def equation_log_scipy(i, a, b, c, d):
    return a*numpy.log(b*i + c) + d

def equation_log(i, a):
    return a[0]*numpy.log(a[1]*i + a[2]) + a[3]

def equation_trig_scipy(i, a, b, c, d):
    return a*numpy.sin(b*i + c) + d

def equation_trig(i, a):
    return a[0]*numpy.sin(a[1]*i + a[2]) + a[3]
# To make sure that people do not run this file
if __name__ == '__main__':
    print "this is not the main function, do not run this!!!!!!"
    print "run the main function with 'python main.py'"
