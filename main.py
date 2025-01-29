############################  IMPORT  #######################################################################
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
############################  VARIABLES  #######################################################################-
global is_blocked
is_blocked = False

############################  CLASS  #######################################################################

class AnimatedButton(QPushButton):
    def __init__(self, text, parent=None, hover_color="red"):
        super().__init__(text, parent)
        self.default_color = "transparent"  # Default background color
        self.hover_color = hover_color  # Hover color

        self.setStyleSheet(f"""
            background-color: {self.default_color}; 
            border-radius: 7px;+
            font-weight: bold; 
            font-size: 18px; 
            border: none;
            color:black;
        """)

        self.effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.effect)

        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(100)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)

    def enterEvent(self, event):
        global is_blocked
        if is_blocked:
            if self.text() == "X":
                self.setStyleSheet(f"background-color: {self.hover_color}; border-radius: 7px; font-weight: bold; font-size: 18px; border: none;color:black;")
                self.animation.setStartValue(0.5)
                self.animation.setEndValue(1.0)
                self.animation.start()
        else:
            if self.text() == "🖈":
                self.setStyleSheet(f"background-color: {self.hover_color}; border-radius: 7px; font-weight: bold; font-size: 18px; border: none;color:black;")
                self.animation.setStartValue(0.5)
                self.animation.setEndValue(1.0)
                self.animation.start()
            elif self.text() == "X" or self.text() == "-":
                self.setStyleSheet(f"background-color: {self.hover_color}; border-radius: 7px; font-weight: bold; font-size: 18px; border: none;color:black;")
                self.animation.setStartValue(0.5)
                self.animation.setEndValue(1.0)
                self.animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        global is_blocked
        if is_blocked:
            if self.text() == "X":
                self.setStyleSheet(f"background-color: transparent; border-radius: 7px; font-weight: bold; font-size: 18px; border: none;color:black;")
                self.animation.setStartValue(1.0)
                self.animation.setEndValue(0.5)
                self.animation.start()
        else:
            if self.text() == "🖈":
                self.setStyleSheet(f"background-color: transparent; border-radius: 7px; font-weight: bold; font-size: 18px; border: none;color:black;")
                self.animation.setStartValue(1.0)
                self.animation.setEndValue(0.5)
                self.animation.start()
            elif self.text() == "X" or self.text() == "-":
                self.setStyleSheet(f"background-color: transparent; border-radius: 7px; font-weight: bold; font-size: 18px; border: none;color:black;")
                self.animation.setStartValue(1.0)
                self.animation.setEndValue(0.5)
                self.animation.start()
        super().leaveEvent(event)

class SysUI():
    def toggle_block(self):
        global is_blocked
        if is_blocked == True:
            is_blocked = False
            self.minimize.setStyleSheet(f"background-color: transparent; border-radius: 7px; font-weight: bold; font-size: 18px; border: none;color:black;")
            self.minimize.setEnabled(True)
            self.block.setStyleSheet(f"background-color: transparent; border-radius: 7px; font-weight: bold; font-size: 18px; border: none;color:black;")
        else:
            is_blocked = True
            self.minimize.setStyleSheet(f"background-color: #D3D3D3; border-radius: 7px; font-weight: bold; font-size: 18px; border: none;color:black;")
            self.minimize.setEnabled(False)
            self.block.setStyleSheet(f"background-color: orange; border-radius: 7px; font-weight: bold; font-size: 18px; border: none;color:black;")

        self.parent.setWindowFlag(Qt.WindowStaysOnTopHint, is_blocked)
        self.parent.show()


    def __init__(self, parent):
        self.parent = parent
        super().__init__()

        self.stop = AnimatedButton("X", self.parent.mainCanvas, hover_color="red")
        self.stop.setFixedSize(35, 23)
        self.stop.setStyleSheet(f"""
            border-radius: 7px;
            font-weight: bold; 
            font-size: 18px; 
            border: none;
        """)
        self.stop.clicked.connect(self.parent.close)
        self.minimize = AnimatedButton("-", self.parent.mainCanvas, hover_color="#69f5c2")
        self.minimize.setFixedSize(35, 23)
        self.minimize.setStyleSheet(f"""
            border-radius: 7px;
            font-weight: bold; 
            font-size: 18px; 
            border: none;
        """)
        self.minimize.clicked.connect(self.parent.showMinimized)
        self.minimize.setEnabled(not is_blocked)
        
        self.block = AnimatedButton("🖈", self.parent.mainCanvas, hover_color="#69f5c2")
        self.block.setFixedSize(35, 23)
        self.block.setStyleSheet(f"""
            border-radius: 7px;
            font-weight: bold; 
            font-size: 18px; 
            border: none;
        """)

        self.block.clicked.connect(self.toggle_block)


        self.header = QWidget(self.parent.mainCanvas)
        self.header.setGeometry(0, 0, self.parent.w, 30)
        self.header.setStyleSheet("""
            background-color: #93adac;
            border-top-left-radius: 15px;   
            border-top-right-radius: 15px;  
            border-bottom-left-radius: 0px;
            border-bottom-right-radius: 0px;
        """)

        #---------------------HEADER-----------------------------#
        header_title = QLabel("Home Flight Sim Controller", self.header)
        header_title.setFont(QFont("Arial", 11))
        header_title.setStyleSheet("color: black; font-weight: bold;")

        header_icon = QLabel(self.header)
        pixmap = QPixmap("FSC_icon.png")
        header_icon.setPixmap(pixmap.scaled(22, 22, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        header_icon.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)


        header_layout = QHBoxLayout(self.header)
        header_layout.setContentsMargins(5, 0, 5, 0)
        header_layout.setSpacing(20)

        title_layout = QHBoxLayout()
        title_layout.setSpacing(10)
        header_layout.setContentsMargins(10, 0, 0, 0)
        title_layout.addWidget(header_icon)
        title_layout.addWidget(header_title)
        title_layout.addStretch()

        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 10, 0)
        button_layout.setSpacing(12)
        button_layout.addWidget(self.block)
        button_layout.addWidget(self.minimize)
        button_layout.addWidget(self.stop)
        

        header_layout.addLayout(title_layout)
        header_layout.addLayout(button_layout)  

        self.header.mousePressEvent = self.start_drag
        self.header.mouseMoveEvent = self.move_window

    def start_drag(self, event):
        if self.stop.underMouse() or self.minimize.underMouse() or self.block.underMouse():
            return
        if event.button() == Qt.LeftButton:
            self.parent.drag_position = event.globalPos() - self.parent.frameGeometry().topLeft()
            event.accept()

    def move_window(self, event):
        if self.stop.underMouse() or self.minimize.underMouse() or self.block.underMouse():
            return
        if event.buttons() == Qt.LeftButton:
            self.parent.move(event.globalPos() - self.parent.drag_position)
            event.accept()

class Labels():
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.test = QLabel("TEST", self.parent.mainCanvas)
        self.test.setFont(QFont("Arial", 50))
        self.test.setGeometry(0, 50, self.parent.w, 100)
        self.test.setStyleSheet("""
            color: #D0A1DB; 
            font-weight: bold; 
        """)
        self.test.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

class Images():
    def __init__(self, parent):
        self.parent = parent
        super().__init__()
        self.logo = QLabel(self.parent.mainCanvas)
        self.logo.setGeometry(0, 0, self.parent.w, self.parent.h)
        self.logo.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        pixmap = QPixmap("FSC_icon.png")
        self.logo.setPixmap(pixmap)
        self.logo.setAttribute(Qt.WA_TranslucentBackground, True)
        self.logo.setScaledContents(False)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = 1792
        self.h = 1092
        self.resize(self.w, self.h)
        self.setWindowTitle("Home Flight Sim Controller")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.setStyleSheet("""
        * {
            background-color: transparent;
        } """)

        self.mainCanvas = QFrame(self)
        self.mainCanvas.resize(self.w, self.h)
        self.mainCanvas.setObjectName("mainCanvas")
        self.setStyleSheet("""
            QWidget#mainCanvas {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #D1E8DB, stop:1 #BCDBE9);
                border-radius: 25px;
            }
        """)

        self.center()
        self.initUI()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick)
        self.timer.start(100)

############################  SYSTEM  #######################################################################

    def center(self):
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.w) // 2
        y = (screen.height() - self.h) // 2
        self.move(x, y)

    def tick(self):
        pass
    


############################  INIT  #######################################################################

    def initUI(self):
        self.labels = Labels(self)
        self.images = Images(self)
        self.sysUI = SysUI(self)



############################  Mainloop  #######################################################################

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
