# -*- coding: utf-8 -*-
"""
This example demonstrates the use of GLSurfacePlotItem.
"""

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
from collections import deque
import pyqtgraph.opengl as gl
import numpy as np
import datetime

numberOfData = 1000
widthOfData = 500

## Create a GL View widget to display data
app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()
w.setWindowTitle('PAS Surfaceplot')
w.setGeometry(100, 100, 1500, 800)  # distance && resolution
w.setCameraPosition(distance=50)


## Create axis
#axis = pg.AxisItem('left', pen=None, linkView=None, parent=None, maxTickLength=-5, showValues=True)
#axis.show()
#axis = pg.AxisItem('left', pen = None)
# xAxis.paint()
#Axis.setSize(self.valueNumber, self.valueNumber, self.valueNumber)
#axis.setStyle(showValues = True)
#axis.show()
#--------------------
axis = gl.GLAxisItem()
# xAxis.paint()
#axis.setSize(self.valueNumber, self.valueNumber, self.valueNumber)
w.addItem(axis)

## Add a grid to the view
g = gl.GLGridItem()
g.scale(2,2,1)
g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
w.addItem(g)

## Animated example
## compute surface vertex data
x = np.linspace(0, widthOfData, widthOfData)
y = np.linspace(0, numberOfData, numberOfData)

## precompute height values for all frames
data = np.random.randint(5, size=(widthOfData, numberOfData))

## create a surface plot, tell it to use the 'heightColor' shader
## since this does not require normal vectors to render (thus we 
## can set computeNormals=False to save time when the mesh updates)
p4 = gl.GLSurfacePlotItem(x, y, shader='heightColor', computeNormals=False, smooth=False)
p4.shader()['colorMap'] = np.array([0.2, 2, 0.5, 0.2, 1, 1, 0.2, 0, 2])
p4.translate(10, 10, 0)
w.addItem(p4)

index = 0
def update():
    global p4, data, index
    timeBeforeUpdate = datetime.datetime.now()
    data = np.delete(data, 0, 0)
    print('popped')
    newValues = np.random.randint(5, size=(1, numberOfData))
    print('newvalues created')
    data = np.concatenate((data, newValues))
    print('numpied')
    p4.setData(z = data)
    print('set')
    timeAfterUpdate = datetime.datetime.now()
    timeDiff = timeAfterUpdate - timeBeforeUpdate
    elapsed_ms = (timeDiff.days * 86400000) + (timeDiff.seconds * 1000) + (timeDiff.microseconds / 1000)
    print(elapsed_ms + ' ms')


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(20)

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
