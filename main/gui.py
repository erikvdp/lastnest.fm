'''
Created on 21-mei-2012

@author: Erik
'''

from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon
from main.notegrabber import notegrabber
  
class HelloPython(QtGui.QWidget):
    def __init__(self, parent=None):  
        super(HelloPython, self).__init__(parent)
        btn = QtGui.QPushButton('Play', self)
        btn.resize(btn.sizeHint())
        btn.move(50, 300)         
        btn.clicked.connect(self.startAnimation)
        self.vert_gap = 15
        self.horz_gap = 15
        self.offset = 25
        self.blockx = -1
        self.blocky = 0
        self.currentnotes = []
        self.initUI()
        self.i = 0
        
    def initUI(self):
        self.notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.setGeometry(400, 400,400,400)
        self.center()
        
        "determine new position and new timeinterval"
    def newblock(self):
        length = self.keys[self.i+1][0]-self.keys[self.i][0]
        self.currentnotes = self.keys[self.i][1]
        self.blockx = (self.blockx+1) % 10
        for index, item in enumerate(self.currentnotes):
            self.currentnotes[index] = self.notes.index(item)#omzetten naar yco
        self.blocky = self.blocky+1
        self.i +=1
        self.update();
        print self.keys[self.i]
        QtCore.QTimer.singleShot(length*1000, self.newblock)

    def playsong(self):
        self.output = Phonon.AudioOutput(Phonon.MusicCategory)
        self.m_media = Phonon.MediaObject()
        Phonon.createPath(self.m_media, self.output)
        self.m_media.setCurrentSource(Phonon.MediaSource(self.path))
        self.m_media.play()            
        
    def startAnimation(self):
        self.path = QtGui.QFileDialog.getOpenFileName(self)#ask for mp3
        #fetch notes
        n = notegrabber(self.path)
        HelloPython.keys = n.parse()
        #start the timer & song
        self.playsong()
        QtCore.QTimer.singleShot(1000, self.newblock)
    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawNotes(e,qp)
        self.drawGrid(e,qp)
        self.drawRect(e, qp)
        qp.end()
        
    def drawNotes(self,event,qp):
        qp.setPen(QtCore.Qt.black)
        qp.setFont(QtGui.QFont('Decorative', 15))
        for i in range(1,12):
            qp.drawText(self.horz_gap-5, self.vert_gap + self.offset * i, self.notes[len(self.notes)-i])
    
    def drawGrid(self, event,qp):
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        #draw a 12x12 grid
        for i in range(0,len(self.notes)):
            qp.drawLine(10, self.vert_gap + i*self.offset, self.horz_gap+(len(self.notes)-1)*self.offset, self.vert_gap + i*self.offset) #horizontal lines
        for i in range(1,len(self.notes)):
            qp.drawLine(self.horz_gap+i*self.offset, self.vert_gap , self.horz_gap+i*self.offset, self.vert_gap + (len(self.notes)-1)*self.offset) #vertical lines
    
    def drawRect(self, event,qp):
        qp.setBrush(QtGui.QColor(200, 0, 0))
        for index, item in enumerate(self.currentnotes):
            xco = self.horz_gap+((self.blockx+1)*self.offset)
            yco = self.vert_gap +(item*self.offset)
            qp.drawRect(xco,yco,self.offset,self.offset)
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
  
if __name__ == '__main__':  
    import sys  
  
    app = QtGui.QApplication(sys.argv)  
  
    helloPythonWidget = HelloPython()  
    helloPythonWidget.show()  
    sys.exit(app.exec_())  