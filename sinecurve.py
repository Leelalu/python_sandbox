#/usr/bin/python3

import math
import numpy
import matplotlib.pyplot as pyplot

TIMESTEP = numpy.arange(0, 2*math.pi, math.pi/10)
TIMESTEP = TIMESTEP*2

COSAMPLITUDE = numpy.sin(TIMESTEP)
SINEAMPLITUDE = numpy.sin(TIMESTEP*-1)

pyplot.plot(TIMESTEP, COSAMPLITUDE)
pyplot.plot(TIMESTEP, SINEAMPLITUDE)
pyplot.show()
