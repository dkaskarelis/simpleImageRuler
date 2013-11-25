#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  SimpleImageRuler.py
#  simpleImageRuler_ui.py
#  
#  Copyright 2013 Ingo Haase <haase@rolab.de>
#  Version 1.0 
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from PySide import QtCore, QtGui
import simpleImageRuler_ui, sys


class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui=simpleImageRuler_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.graphicsView.setScene(QtGui.QGraphicsScene(self))
        self.ui.graphicsView.setStyleSheet('border: 4px solid red;')
        self.ui.graphicsView.setSceneRect(QtCore.QRectF(self.ui.graphicsView.viewport().rect()))
        #self.ui.graphicsView.setSceneRect(QtCore.QRectF(0,0,500,500))

        self.f_press={'line':self.line_press, 'neutral':self.neutral_press,'cal':self.line_press, 'path':self.path_press}
        self.f_move={'line':self.line_move, 'neutral':self.neutral_move, 'cal':self.line_move, 'path':self.path_move}
        self.f_release={'line':self.line_release, 'neutral':self.neutral_release, 'cal':self.cal_release,'path':self.path_release}
        
        self.redirectMouseEvents('neutral')
        
        self.textedit=TextEditHandler(self.ui.textEdit)
        
        self.setStyleSheet('background:transparent')
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.groupBox.setStyleSheet('background:lightGray')
        self.ui.textEdit.setStyleSheet('background:lightGray')
        self.ui.statusbar.setStyleSheet('background:lightGray')
        self.ui.menubar.setStyleSheet('background:lightGray')
                
        self.calibration=Calibration(self)
        
        self.ui.toolButtonCal.clicked.connect(self.calibration.startCalibration)
        self.ui.toolButtonNeutral.clicked.connect(self.set_mode_neutral)
        self.ui.toolButtonLine.clicked.connect(self.set_mode_line)
        self.ui.toolButtonPath.clicked.connect(self.set_mode_path)
        self.ui.toolButtonClear.clicked.connect(self.set_clear)
        self.ui.toolButtonRed.clicked.connect(self.setStandardPenColor)
        self.ui.toolButtonYellow.clicked.connect(self.setStandardPenColor)
        self.ui.toolButtonBlack.clicked.connect(self.setStandardPenColor)
        self.ui.toolButtonWhite.clicked.connect(self.setStandardPenColor)
        
        self.imagefile=ImageFile(self, self.ui.graphicsView)
        self.ui.actionOpen.triggered.connect(self.imagefile.openFile)
        self.ui.toolButtonZoomIn.clicked.connect(self.imagefile.zoomin)
        self.ui.toolButtonZoomOut.clicked.connect(self.imagefile.zoomout)
        
        self.end=None   #Start und Ende der aktuellen Linie
        self.start=None 
        self.standardPen=QtGui.QPen()


    def redirectMouseEvents(self, mode):
        self.ui.graphicsView.mousePressEvent=self.f_press[mode]
        self.ui.graphicsView.mouseMoveEvent=self.f_move[mode]
        self.ui.graphicsView.mouseReleaseEvent=self.f_release[mode]
        self.ui.statusbar.showMessage(u'Aktueller Modus ist: %s'%mode)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.ui.graphicsView.setMouseTracking(False)
            self.redirectMouseEvents('neutral')
        elif e.key() == QtCore.Qt.Key_Delete:
            pass #Löschen einzelner Linien noch nicht möglich
 
    #Clicked-Events der toolBox-Buttons kommen hier an
    def set_mode_neutral(self):
        self.redirectMouseEvents('neutral')
    def set_mode_line(self):
        self.redirectMouseEvents('line')
        self.textedit.clear()
    def set_mode_path(self):
        self.redirectMouseEvents('path')
        self.textedit.clear()
    def set_clear(self):
        self.redirectMouseEvents('neutral')
        self.ui.graphicsView.scene().clear()
        self.imagefile.update()
        self.textedit.clear()
    def setStandardPenColor(self):
        if self.sender().objectName()=="toolButtonRed":
            color='red'
        elif self.sender().objectName()=="toolButtonWhite":
            color='white'
        elif self.sender().objectName()=="toolButtonYellow":
            color='yellow'
        else:
            color='black'
        col=QtGui.QColor(color)
        self.standardPen.setColor(col)
        
    #Mouse Event Bearbeitung im Modus "neutral"
    #*********************************************************************************
    def neutral_press(self,event):
        QtGui.QGraphicsView.mousePressEvent(self.ui.graphicsView, event)
    def neutral_move(self,event):
        QtGui.QGraphicsView.mouseMoveEvent(self.ui.graphicsView, event)
    def neutral_release(self,event):
        QtGui.QGraphicsView.mouseReleaseEvent(self.ui.graphicsView, event)
    

    #Mouse Event Bearbeitung im Modus "line"
    #*********************************************************************************
    def line_press(self,event):
        ep = event.pos()
        self.start = QtCore.QPointF(self.ui.graphicsView.mapToScene(ep))
        self.gummi=QtGui.QGraphicsLineItem(QtCore.QLineF(self.start, self.start))
        self.gummi.setPen(self.standardPen)
        self.tickA=QtGui.QGraphicsLineItem(QtCore.QLineF(self.start, self.start))
        self.tickA.setPen(self.standardPen)
        self.tickE=QtGui.QGraphicsLineItem(QtCore.QLineF(self.start, self.start))
        self.tickE.setPen(self.standardPen)
           
        self.ui.graphicsView.scene().addItem(self.gummi)
        self.ui.graphicsView.scene().addItem(self.tickA)
        self.ui.graphicsView.scene().addItem(self.tickE)
        
    def line_move(self, event):
        end = QtCore.QPointF(self.ui.graphicsView.mapToScene(event.pos()))
        self.gummi.setLine(QtCore.QLineF(self.start, end))
        x1=self.start.x()
        y1=self.start.y()
        x2=end.x()
        y2=end.y()
        dx=self.gummi.line().dx()
        dy=self.gummi.line().dy()
        length=self.gummi.line().length()
        if length==0:
            return
        dxneu=10/length*dy  # 10: Länge der End-Ticks in Scene-Units
        dyneu=10/length*dx
        p3=QtCore.QPointF(x1-dxneu,y1+dyneu)
        p4=QtCore.QPointF(x1+dxneu,y1-dyneu)
        self.tickA.setLine(QtCore.QLineF(p4, p3))
        p5=QtCore.QPointF(x2-dxneu,y2+dyneu)
        p6=QtCore.QPointF(x2+dxneu,y2-dyneu)
        self.tickE.setLine(QtCore.QLineF(p5, p6))

    def line_release(self, event):
        self.textedit.addlength(self.gummi.line().length())


    #Mouse Event Bearbeitung im Modus "path"
    #*********************************************************************************
    def path_press(self,event):
        if event.button()==QtCore.Qt.RightButton:
            self.gummi.setLine(QtCore.QLineF(self.start, self.start))
            self.ui.graphicsView.setMouseTracking(False)
            self.end=None
            self.textedit.memorizeOldText()
            return 
            
        if self.end:
            self.textedit.addlength(self.gummi.line().length())

        self.ui.graphicsView.setMouseTracking(True)
        self.start = QtCore.QPointF(self.ui.graphicsView.mapToScene(event.pos()))
        self.gummi=QtGui.QGraphicsLineItem(QtCore.QLineF(self.start, self.start))
        self.gummi.setPen(self.standardPen)
        self.ui.graphicsView.scene().addItem(self.gummi)
       
    def path_move(self, event):
        self.end = QtCore.QPointF(self.ui.graphicsView.mapToScene(event.pos()))
        self.gummi.setLine(QtCore.QLineF(self.start, self.end))

    def path_release(self, event):
        pass 

    #Mouse Event Bearbeitung im Modus "cal"
    #*********************************************************************************
    # press und move laufen über den modus line
    def cal_release(self, event):
        self.calibration.calcFactor(self.gummi.line().length())
        
     
class Calibration(object):
    def __init__(self,mainwidget):
        self.main=mainwidget
        
    def startCalibration(self):
        self.main.redirectMouseEvents('cal')
        self.main.ui.statusbar.showMessage(u'Aktueller Modus ist: cal  Bitte bekannte Länge auswählen')
        # hierauf muss der User einen mouse drag machen, dann geht es weiter mit self.calcFactor
        # Abbruch mit ESC ist möglich

    def calcFactor(self,length):
        d, ok = QtGui.QInputDialog.getDouble(self.main, self.main.tr("Kalibrierung"),
                                             self.main.tr(u"Länge:"), 1., -10000, 10000, 3)
        if ok:
            scale=self.main.imagefile.getScale()
            factor=d*scale/length  #Faktor normiert auf scale=1
            self.main.textedit.setfactor(factor)
        self.main.redirectMouseEvents('neutral')
        self.main.ui.graphicsView.scene().clear()
        self.main.imagefile.update()
        self.main.textedit.clear()


class TextEditHandler(object):
    def __init__(self, tew):
        self.tew=tew #TextEditWidget
        self.lengthlist=[] #länge in scene-units, skaliert auf scale=1
        self.factor=1.
        self.text=''
        self.oldtext=''
        self.currentscale=1.
        
    def addlength(self,length): # add length and show it, length in Scene-Units
        self.lengthlist.append(length/self.currentscale*self.factor)
        summe=0
        for f in self.lengthlist:
            summe=summe+f
        strlist=[str(round(x,1)) for x in self.lengthlist]
        text='<br>'.join(strlist)
        mw=summe/len(self.lengthlist)
        mw=round(mw,1)
        summe=round(summe,1)
        self.text=u"%s %s <br>=======<br>Σ %s <br> MW: %s <br><br>"%(self.oldtext,text,summe,mw)
        textF=u'<div  align="right">%s</div>'%(self.text)
        self.tew.setHtml(textF)
        
    def setfactor(self,f):   #Faktor zum Umrechen von Scene-Units auf kalibrierte Strecke
        self.factor=f
                
    def setcurrentscale(self, f):  #aktueller Scale-Faktor (zoom)
        self.currentscale=f
        #print "Aktueller Scale:", self.currentscale
        
    def memorizeOldText(self):
        self.oldtext="%s %s"%(self.oldtext,self.text)
        self.text=''
        self.lengthlist=[]

    def clear(self):
        self.lengthlist=[]
        self.text=''
        self.oldtext=''
        self.tew.setPlainText('')
        

class ImageFile(object):
    def __init__(self, mainwidget, view):
        self.view=view
        self.mainwidget=mainwidget
        self.pixmap=None
        self.scale=1.
        
    def openFile(self):
        fileName,filt = QtGui.QFileDialog.getOpenFileName(self.mainwidget,self.mainwidget.tr("Open File"), None, self.mainwidget.tr("Image Files (*.png *.jpg *.jpeg)"))
        self.view.scene().clear()
        self.pixmap=QtGui.QPixmap(fileName)
        item=self.view.scene().addPixmap(self.pixmap)
        self.view.setSceneRect(self.pixmap.rect())
        self.scale=1.
        
    def getScale(self):
        return self.scale 
        
    def update(self):
        if self.pixmap:
            self._setscaledpixmap(self.scale)
            
    def zoomin(self):
        if self.pixmap:
            self.scale=self.scale+0.1
            self._setscaledpixmap(self.scale)
            
    def zoomout(self):
        if self.pixmap:
            self.scale=self.scale-0.1
            self._setscaledpixmap(self.scale)

    def _setscaledpixmap(self, scale):
        w=self.pixmap.width()
        h=self.pixmap.height()
        w=int(w*scale)
        h=int(h*scale)
        self.mainwidget.textedit.setcurrentscale(scale)
        scaledpixmap=self.pixmap.scaled(w,h, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.view.scene().clear()
        self.view.scene().addPixmap(scaledpixmap)
        self.view.setSceneRect(scaledpixmap.rect())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    translator_qt = QtCore.QTranslator()
    translator_qt.load('qt_de.qm')
    app.installTranslator(translator_qt)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())

