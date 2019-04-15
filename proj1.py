import sys
from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QWidget, QApplication, QGridLayout, QColorDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from projekt1 import  przeciecie
class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'matplotlib example'
        self.initInterface()
        self.initWidgets()
        
    def initInterface(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 300, 400)
        self.show()
    
    def initWidgets(self):
        btnclear = QPushButton('czysc', self)
        btn = QPushButton('rysuj', self)
        btnCol = QPushButton('kolor AB', self)
        btnCol1 = QPushButton('kolor CD', self)
        XALabel = QLabel('XA', self)
        YALabel = QLabel('YA', self)
        XBLabel = QLabel('XB', self)
        YBLabel = QLabel('YB', self)
        XCLabel = QLabel('XC', self)
        YCLabel = QLabel('YC', self)
        XDLabel = QLabel('XD', self)
        YDLabel = QLabel('YD', self)
        XPLabel = QLabel('XP', self)
        YPLabel = QLabel('YP', self)
        ODLabel = QLabel('Polozenie punktu', self)
        self.XAEdit = QLineEdit()
        self.YAEdit = QLineEdit()
        self.XBEdit = QLineEdit()
        self.YBEdit = QLineEdit()
        self.XCEdit = QLineEdit()
        self.YCEdit = QLineEdit()
        self.XDEdit = QLineEdit()
        self.YDEdit = QLineEdit()
        self.XPEdit = QLineEdit()
        self.YPEdit = QLineEdit()
        self.ODEdit = QLineEdit()
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        #wyswietlanie
        grid = QGridLayout()
        grid.addWidget(XALabel, 1, 0)
        grid.addWidget(XBLabel, 1, 2)
        grid.addWidget(XCLabel, 1, 4)
        grid.addWidget(XDLabel, 1, 6)
        grid.addWidget(XPLabel, 1, 8)
        grid.addWidget(ODLabel, 3, 1)
        
        grid.addWidget(self.XAEdit, 1, 1)
        grid.addWidget(self.XBEdit, 1, 3)
        grid.addWidget(self.XCEdit, 1, 5)
        grid.addWidget(self.XDEdit, 1, 7)
        grid.addWidget(self.XPEdit, 1, 9)
        grid.addWidget(self.ODEdit, 3, 3, 1, 3)
        
        #grid.addWidget(self.xEdit, 1, 1)
        grid.addWidget(YALabel, 2, 0)
        grid.addWidget(YBLabel, 2, 2)
        grid.addWidget(YCLabel, 2, 4)
        grid.addWidget(YDLabel, 2, 6)
        grid.addWidget(YPLabel, 2, 8)
        
        
        grid.addWidget(self.YAEdit, 2, 1)
        grid.addWidget(self.YBEdit, 2, 3)
        grid.addWidget(self.YCEdit, 2, 5)
        grid.addWidget(self.YDEdit, 2, 7)
        grid.addWidget(self.YPEdit, 2, 9)
        grid.addWidget(btnclear, 5, 1, 1, 1 )

        grid.addWidget(btn, 4, 2, 1, 3)
        grid.addWidget(btnCol, 4, 4, 1, 3)
        grid.addWidget(btnCol1, 4, 6, 1, 3)
        grid.addWidget(self.canvas, 5, 2, -1, -1)
        
        self.setLayout(grid)
        
        btn.clicked.connect(self.oblicz)
        btnCol.clicked.connect(self.zmienKolor)
        btnCol1.clicked.connect(self.zmienKolor1)
        btnclear.clicked.connect(self.czysc)
        
    def czysc(self):
        self.XAEdit = QLineEdit()
        self.YAEdit = QLineEdit()
        self.XBEdit = QLineEdit()
        self.YBEdit = QLineEdit()
        self.XCEdit = QLineEdit()
        self.YCEdit = QLineEdit()
        self.XDEdit = QLineEdit()
        self.YDEdit = QLineEdit()
        self.XPEdit = QLineEdit()
        self.YPEdit = QLineEdit()
        self.ODEdit = QLineEdit()
    
    def zmienKolor(self):
        kolor = QColorDialog.getColor()
        if kolor.isValid():
            print(kolor.name())
            self.rysuj(kol = kolor.name())
            
    def zmienKolor1(self):
        kolor = QColorDialog.getColor()
        if kolor.isValid():
            print(kolor.name())
            self.rysuj(kol1 = kolor.name())
    
    
    
    def sprawdzLiczbe(self, element):
        if element.text().lstrip('-').replace(',','',1).isdigit():
                return float(element.text())
        else:
                element.setFocus()
                return None
    
    def oblicz(self):
        self.rysuj()
    
    
    def rysuj(self, kol = 'red', kol1='pink'):
        XA = self.sprawdzLiczbe(self.XAEdit)
        YA =  self.sprawdzLiczbe(self.YAEdit)
        XB = self.sprawdzLiczbe(self.XBEdit)
        YB =  self.sprawdzLiczbe(self.YBEdit)
        XC = self.sprawdzLiczbe(self.XCEdit)
        YC =  self.sprawdzLiczbe(self.YCEdit)
        XD = self.sprawdzLiczbe(self.XDEdit)
        YD =  self.sprawdzLiczbe(self.YDEdit)
        
        
        if None not in [XA, YA, XB, YB, XC, YC, XD, YD]:
            XA = float(self.XAEdit.text())
            YA = float(self.YAEdit.text())
            XB = float(self.XBEdit.text())
            YB = float(self.YBEdit.text())
            XC = float(self.XCEdit.text())
            YC = float(self.YCEdit.text())
            XD = float(self.XDEdit.text())
            YD = float(self.YDEdit.text())
            
            (roz, XP, YP, t1, t2) = przeciecie(XA, YA, XB, YB, XC, YC, XD, YD)
            
            self.XPEdit.setText(str(XP))
            self.YPEdit.setText(str(YP))
            self.ODEdit.setText(str(roz))

        
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot([YA,YB],[XA, XB], color = kol, marker = 'o', label = 'Odcinkek AB')
            ax.plot([YC,YD],[XC, XD], color = kol1, marker = 'o', label = 'Odcinkek CD')
            if 0<=t1 and t1<=1:
                if 0<=t2 and t2<=1 :
                    pass
                else:
                    ax.plot([YP, YC], [XP, XC], ':')
                    
            else: 
            
                if 0<=t2 and t2<=1:
                    ax.plot([YP, YA], [XP, XA], ':')
            
                else:
                    ax.plot([YP, YC], [XP, XC], ':')
                    ax.plot([YP, YA], [XP, XA], ':')
                    
            
            ax.legend()
            ax.scatter(YP,XP)
            self.canvas.draw()
    
def main():
    app = QApplication(sys.argv)
    window = AppWindow()
    app.exec_()
    
if __name__ == '__main__':
    main()