"""
UI for tilegen. use PySide2
"""

from __future__ import division, unicode_literals, print_function, absolute_import

import sys
import os 
from PySide2 import QtGui, QtCore, QtWidgets, QtSvg
import tile_gen
import random
import time


def randomColor():
    """
    Generate a random tone deaf color
    """
    h = 360 * random.random()
    s = 10 + 25 * random.random()
    l = 35 + 10 * random.random()
    return "hsl(" + str(h) + ',' + str(s) + '%,' + str(l) + '%)', "hsl(" + str(h) + ',' + str(min(100, s + 5)) + '%,' + str(min(100, l + 6)) + '%)'


class MainWindowWidget(QtWidgets.QWidget):
    """
    Main widget
    """

    def __init__(self):

        super(MainWindowWidget, self).__init__()

        self.setWindowTitle("TileGen")
        self.loaded = False
        self.timer =  QtCore.QTimer(self)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.update)
        script_dir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(script_dir + os.path.sep + 'images' + os.path.sep + 'logo.png'))
        
        # Image viewing region
        self.main_render = QtWidgets.QLabel(self)
        
        self.label_load = QtWidgets.QLabel(self)
        self.label_load.setAlignment(QtCore.Qt.AlignCenter)
        self.label_load.setObjectName("btn")
        self.label_load.setStyleSheet("#btn {background-color:rgb(60, 65, 70); border-bottom: 1px solid #2d2d2d;} #btn:hover {background-color:rgb(83, 88, 94);}") 
        self.label_load.mousePressEvent = self.load_image_but

        self.label_load_background = QtWidgets.QLabel(self)
        self.label_load_background.setObjectName("btnbg")
        self.label_load_background.setAlignment(QtCore.Qt.AlignCenter)
        self.label_load_background.setStyleSheet("#btnbg {background-color:rgb(60, 65, 70); border-top: 1px solid #5a5a5a;  border-bottom: 1px solid #2d2d2d;} #btnbg:hover {background-color:rgb(83, 88, 94);}") 
        self.label_load_background.mousePressEvent = self.load_background

        self.clear(None)
        
        self.main_render.setMouseTracking(True)
        self.main_render.setObjectName("main")
        self.main_render.setMinimumWidth(314)
        self.main_render.setAlignment(QtCore.Qt.AlignCenter)
        rand, randhov = randomColor()
        self.main_render.setStyleSheet("#main:hover {background-color: " +randhov + ";} #main {border-right: 1px solid #2d2d2d; background-color: "+ rand  +";}") 
        
        frames_container = QtWidgets.QWidget(self)
        frames_label = QtWidgets.QLabel("Frames")
        frames_label.setObjectName("fr")
        frames_container.setStyleSheet("#fr {color: white;}")
        self.frames = QtWidgets.QLineEdit("1", frames_container)
        self.frames_value = 1
        self.frames.textChanged.connect(self.change_frames)
        self.frames.setValidator(QtGui.QIntValidator(0, 100, self.frames))
        self.frames.setFixedWidth(50)
        vlayout_frames = QtWidgets.QHBoxLayout()
        vlayout_frames.setSpacing(3)
        vlayout_frames.setContentsMargins(6, 6, 6, 6)
        self.frames.setAlignment(QtCore.Qt.AlignCenter)
        vlayout_frames.addWidget(frames_label)
        vlayout_frames.addWidget(self.frames)
        frames_container.setFixedHeight(40)
        frames_container.setLayout(vlayout_frames)

        self.containerUI = QtWidgets.QWidget()
        self.demo = None
        
        self.hlayout = QtWidgets.QHBoxLayout()
        self.hlayout.setSpacing(0)
        self.hlayout.setContentsMargins(0, 0, 0, 0)
        self.hlayout.addWidget(self.main_render)

        vlayoutmain = QtWidgets.QVBoxLayout()
        vlayoutmain.setSpacing(5)
        vlayoutmain.setContentsMargins(0, 0, 0, 0)

        vlayout = QtWidgets.QVBoxLayout()
        vlayout.setSpacing(0)
        vlayout.setContentsMargins(0, 0, 0, 0)
        self.containerUI.setLayout(vlayout)
        vlayout.addWidget(frames_container)
        vlayout.addWidget(self.label_load)
        vlayout.addWidget(self.label_load_background)

        self.hlayout.addWidget(self.containerUI)

        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.main_render.mousePressEvent = self.load_image_but

        self.add_toolbar()
        vlayoutmain.setMenuBar(self.tb)
        self.tb.show()

        mainview = QtWidgets.QWidget()
        mainview.setLayout(self.hlayout)
        vlayoutmain.addWidget(mainview)
        self.setLayout(vlayoutmain)

        # Enable dragging and dropping onto the GUI
        self.setAcceptDrops(True)
        self.setFixedSize(435, 298)
        self.setAutoFillBackground(True)
        self.setObjectName("mainwidget")
        self.setStyleSheet("#mainwidget {background-color:rgb(60, 65, 70);}") 
        self.show()

    def change_frames(self, new_value):
        """
        input frame management
        :return:
        """
        self.labelerror.setText("")
        if new_value is not None and new_value != "":
            self.frames_value = int(new_value)
            self.load_image()
        else:
            self.labelerror.setText("Invalid frames value")

    def add_toolbar(self):
        """
        toolbar management
        :return:
        """
        self.tb = QtWidgets.QToolBar(self)
        
        self.saveAction = QtWidgets.QAction(QtGui.QIcon("images" + os.path.sep +"error.png"), "&Save", self)
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.setStatusTip("Save file")
        self.saveAction.triggered.connect(self.save_image)

        self.clearAction = QtWidgets.QAction(QtGui.QIcon("images" + os.path.sep +"cancel.png"), "&Clear", self)
        self.clearAction.setShortcut("Ctrl+W")
        self.clearAction.setStatusTip("Clear")
        self.clearAction.triggered.connect(self.clear)

        self.tb.setAutoFillBackground(True)
        self.tb.setObjectName("tb")
        self.tb.setStyleSheet("#tb {background-color:rgb(40, 45, 50); color: white;border-bottom: 1px solid black;}") 
        self.tb.addAction(self.saveAction)
        self.tb.addAction(self.clearAction)
        self.labelerror = QtWidgets.QLabel("To start, load a tile", self.tb)
        self.labelerror.setObjectName("labelerror")
        self.labelerror.setStyleSheet("#labelerror { color: white;}") 
        self.tb.addWidget(self.labelerror)
        
    def clear(self, event):
        """
        Return ui to default state
        :return:
        """
        self.timer.stop()
        pixmap = QtGui.QPixmap("images" + os.path.sep + "drop.png")
        pixmap = pixmap.scaled(314, 278, QtCore.Qt.KeepAspectRatio)
        self.main_render.setPixmap(pixmap)
        self.label_load.setPixmap(QtGui.QPixmap())
        self.label_load_background.setPixmap(QtGui.QPixmap())
        self.clearButtonStyle()
        self.fname = None
        self.fbgname = None
        self.DirectoryWatcher = None

    def load_image_but(self, event):
        """
        Open a the tiles image button action
        :return:
        """
        
        self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open file")
        print(self.fname)
        if self.fname is not None and self.fname != "":
            self.load_image()

    def load_background(self, event):
        """
        Open a the background image button action
        :return:
        """
        
        self.fbgname, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open file")
        if self.fbgname is not None and self.fbgname != "":
            pixmap = QtGui.QPixmap(self.fbgname)
            pixmap = pixmap.scaled(116, 93, QtCore.Qt.KeepAspectRatio)
            self.label_load_background.setPixmap(pixmap)
            self.load_image()

    def save_image(self, event):
        """
        open a save dialog
        :parameter: event
        :return:
        """

        if not self.result:
            return            
        savefilename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save file",  "images" + os.path.sep + "atlas.png")
        tile_gen.save_result(self.result, savefilename)


    def clearButtonStyle(self):
        """
        clear label style to default
        :return:
        """

        rand, randhov = randomColor()
        self.main_render.setStyleSheet("#main:hover {background-color: " +randhov + ";} #main {border-right: 1px solid #2d2d2d; background-color: "+ rand  +";}") 
        self.label_load.setStyleSheet("#btn {border-bottom: 1px solid #2d2d2d;} #btn:hover {background-color:rgb(83, 88, 94);}") 
        self.label_load_background.setStyleSheet("#btnbg {border-bottom: 1px solid #2d2d2d;} #btnbg:hover {background-color:rgb(83, 88, 94);}") 

    def load_image(self):
        """
        run the tile generation and show it
        :return:
        """
        
        self.DirectoryWatcher = QtCore.QFileSystemWatcher([self.fname, self.fbgname])
        self.DirectoryWatcher.fileChanged.connect(self.load_image)

        self.labelerror.setText("")

        self.saveAction.setIcon(QtGui.QIcon("images" + os.path.sep + "save.png"))
        self.clearButtonStyle()
        self.loadUI()
        
        self.timer.stop()
        try:
            self.result, frames, bg, size = tile_gen.treat_image(self.fname, self.fbgname, self.frames_value)
            demo_images = tile_gen.create_demo_images(self.result, frames, bg, size, (int(345/2), int(280/2)))
        except ValueError as e:
            self.labelerror.setText(str(e))
            pixmaperror = QtGui.QPixmap("images" + os.path.sep + "error.png")
            self.saveAction.setIcon(QtGui.QIcon("images" + os.path.sep + "error.png"))
            self.label_load_background.setPixmap(pixmaperror)
            self.label_load_background.setStyleSheet("#btnbg {background-color:rgb(183, 88, 94);}") 
            return       
        except Exception as e:
            print(e)
            self.labelerror.setText(str(e))
            pixmaperror = QtGui.QPixmap("images" + os.path.sep + "error.png")
            self.label_load.setPixmap(pixmaperror)
            self.label_load.setStyleSheet("#btn {background-color:rgb(183, 88, 94);}")
            self.main_render.setPixmap(pixmaperror)
            self.saveAction.setIcon(QtGui.QIcon("images" + os.path.sep + "error.png"))
            self.main_render.setStyleSheet("#main {border-right: 1px solid #2d2d2d; background-color:rgb(183, 88, 94);}") 
            return 
        
        self.loaded = True
        
        self.pixmaps = []
        self.current_index = 0
        for i, image in enumerate(demo_images):
            self.pixmaps.append(QtGui.QPixmap.fromImage(image))
            self.pixmaps[i] = self.pixmaps[i].scaled(345, 280, QtCore.Qt.KeepAspectRatio)
            
        if len(demo_images) == 1:
            self.pixmaps[0] = self.pixmaps[0].scaled(345, 280, QtCore.Qt.KeepAspectRatio)
            self.main_render.setPixmap(self.pixmaps[0])
            return
        self.timer.start(200)

    def update(self):
        self.main_render.setPixmap(self.pixmaps[self.current_index])
        QtGui.qApp.processEvents()
        if self.current_index >= len(self.pixmaps) - 1:
            self.current_index = 0
        else:
            self.current_index = self.current_index + 1

    def loadUI(self):
        """
        Load the UI
        """
        pixmap = QtGui.QPixmap(self.fname)
        pixmap = pixmap.scaled(116, 93, QtCore.Qt.KeepAspectRatio)
        self.label_load.setPixmap(pixmap)
        self.label_load.show()
        self.label_load_background.show()
        # self.labelsave.show()

        
    # The following three methods set up dragging and dropping for the app
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        """
        Drop files directly onto the widget
        File locations are stored in fname
        :param e:
        :return:
        """
        if e.mimeData().hasUrls:
            e.setDropAction(QtCore.Qt.CopyAction)
            e.accept()
            # Workaround for OSx dragging and dropping
            for url in e.mimeData().urls():
                fname = str(url.toLocalFile())

            self.fname = fname
            self.load_image()
        else:
            e.ignore()

# Run if called directly
if __name__ == '__main__':
    # Initialise the application
    app = QtWidgets.QApplication(sys.argv)
    # Call the widget
    ex = MainWindowWidget()
    sys.exit(app.exec_())