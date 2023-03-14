import pylab as lab
import scipy.interpolate as inp

x= [0, 0.3, 0.5, 0.8, 1,  2,  3 ]
y= [0, 0.1, 0.5, 1,   3, 10, 30]

x= "0 0.3 0.5 0.8 1  2  3".split()
y= "0 0.1 0.5 1   3 10 30".split()

x = list(map(float,x))
y = list(map(float,y))
lab.plot(x,y, '-o', label="původní hodnoty")

funkce = inp.CubicSpline(x, y)
newX= lab.linspace(0, 3, 99)
newY= funkce(newX)
lab.plot(newX, newY, label="CubicSpline")

lab.legend()
lab.grid(1)
lab.show()