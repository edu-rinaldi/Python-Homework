from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *  

class PaintInfo:
    def __init__(self):
        self.mouse_pressed = False
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_px = 0
        self.mouse_py = 0
        self.key = ''
        self.size = (0, 0)

class _GWidget(QWidget):
    def __init__(self):
        super().__init__() 				# inizializzazione della superclasse
        self.image = QImage(self.width(), 
            self.height(), QImage.Format_ARGB32)	# immagine con canale alpha (trasparenza)
        self.paint_handler = None
        self.info = PaintInfo()
        self.info.size = self.width(), self.height()
        self.setMouseTracking(True)			# reagisce al movimento del mouse

    def drawing(self):
        painter = QPainter(self.image)
        painter.setRenderHints(
            QPainter.Antialiasing,True)			# bordi della linea con colore sfumato
        painter.setRenderHints(
            QPainter.SmoothPixmapTransform,True)
        painter.info = self.info
        self.paint_handler(painter)
        self.info.mouse_px = self.info.mouse_x
        self.info.mouse_py = self.info.mouse_y
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)

    def resizeEvent(self,event):
        prev_img = self.image				# immagine precedente
        self.image = QImage(self.width(), 
            self.height(), QImage.Format_ARGB32)	# nuova immagine ridimensionata
        self.image.fill(QColor(0,0,0).rgb())		# riempita di nero
        painter = QPainter(self.image)
        painter.drawImage(0, 0, prev_img)		# copio la vecchia sulla nuova
        self.info.size = self.width(), self.height()
        self.update()

    def mousePressEvent(self,event):
        ''' quando si clicca sul mouse settiamo mouse_pressed'''
        self.info.mouse_pressed = True

    def mouseReleaseEvent(self,event):
        ''' quando si lascia il tasto del mouse'''
        self.info.mouse_pressed = False

    def mouseMoveEvent(self,event):
        ''' quando il mouse si muove memorizziamo la nuova'''
        self.info.mouse_x = event.x()
        self.info.mouse_y = event.y()

    def keyPressEvent(self,event):
        ''' quando premiamo un tasto lo memorizziamo in key'''
        if not event.text():
            super().keyPressEvent(event)
        self.info.key = event.text()

    def keyReleaseEvent(self,event):
        ''' quando rilasciamo il tasto'''
        self.info.key = ''

    def clear(self,a=255):    
        '''Pulisce l'immagine della finestra con trasparenza a'''
        width, height = self.info.size     
        self.setPen(QColor(0,0,0,a))       
        self.setBrush(QColor(0,0,0,a))     
        self.drawRect(0, 0, width, height)    


def run_app(paint, w, h, time=1000/60):
    app = QApplication.instance()
    if not app: app = QApplication([])
    widget = _GWidget()
    widget.resize(w,h)
    widget.setWindowTitle('Fondamenti di Programmazione')
    widget.paint_handler = paint
    timer = QTimer()
    timer.setInterval(time)
    timer.timeout.connect(widget.drawing)
    widget.show()
    timer.start()
    app.exec_()

