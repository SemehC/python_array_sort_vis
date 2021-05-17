import time
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.animation as animation
from PyQt5.QtGui import QIcon, QPixmap
import PyQt5.QtGui
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtWidgets, QtCore
import cv2 as cv
import sys
import functions as fn
import webbrowser
import arrayVis
import random
from drawtree import draw_bst

class designWindow(QtWidgets.QMainWindow,arrayVis.Ui_MainWindow):
    def __init__(self):

        super(designWindow,self).__init__()
        self.setupUi(self)
        self.errorColors=["red","green","yellow","blue","pink",]
        self.array=None
        self.generator=None
        self.formul = " "
        self.illus = " "
        self.vidlink = " "
        self.link = " "
        self.infos = self.picViewer
        #self.input.returnPressed.connect(self.getInput)
        self.input.textChanged.connect(self.getInput)
       # self.done.clicked.connect(self.getInput)
        self.errorText = self.textBrowser
        self.result = self.textBrowser_2
        self.bblsort.clicked.connect(self.selectBubbleSort)
        self.insertsort.clicked.connect(self.selectInsertionSort)
        self.selectsort.clicked.connect(self.selectSelectionSort)
        self.fusionsort.clicked.connect(self.selectMergeSort)
        self.quicksort.clicked.connect(self.selectQuickSort)
        self.triArbre.clicked.connect(self.selectTreeSort)

        self.triArbre.setEnabled(False)
        self.bblsort.setEnabled(False)
        self.insertsort.setEnabled(False)
        self.selectsort.setEnabled(False)
        self.fusionsort.setEnabled(False)
        self.quicksort.setEnabled(False)
        self.done_2.setEnabled(False)
        self.illustration.setEnabled(False)
        self.formule.setEnabled(False)
        self.lien.setEnabled(False)
        self.video.setEnabled(False)
        self.save.hide()
        self.graph.hide()
        self.save.hide()

        self.graph.clicked.connect(self.graphShow)
        self.done_2.clicked.connect(self.displaySort)
        self.illustration.clicked.connect(self.showIllustration)
        self.formule.clicked.connect(self.showFormule)
        self.lien.clicked.connect(self.moreInfo)
        self.video.clicked.connect(self.showVideo)

        self.result.setStyleSheet("font-size:20px")

        self.errorText.setText("Insert values separated by a white space ' ' ! ")
        self.isSorted=False

        #Set input Styles
        self.input.setStyleSheet("font-size:20px;")
        self.errorText.setStyleSheet("font-size:20px;")

    def getInput(self):
        self.array=[]
        txt=self.input.text()
        try:
            l=list(map(int,txt.split()))
            if(len(l)==0):
                raise Exception
            self.errorText.setStyleSheet("color: cyan; font-size:20px;")
            self.errorText.setText("List verified, your list is : "+str(l))
            self.bblsort.setEnabled(True)
            self.insertsort.setEnabled(True)
            self.selectsort.setEnabled(True)
            self.fusionsort.setEnabled(True)
            self.quicksort.setEnabled(True)
            self.triArbre.setEnabled(True)
            self.done_2.setEnabled(False)
            self.illustration.setEnabled(False)
            self.formule.setEnabled(False)
            self.lien.setEnabled(False)
            self.video.setEnabled(False)



        except:
            self.graph.setEnabled(False)
            self.bblsort.setEnabled(False)
            self.insertsort.setEnabled(False)
            self.selectsort.setEnabled(False)
            self.fusionsort.setEnabled(False)
            self.quicksort.setEnabled(False)
            self.done_2.setEnabled(False)
            self.triArbre.setEnabled(False)
            self.illustration.setEnabled(False)
            self.formule.setEnabled(False)
            self.lien.setEnabled(False)
            self.video.setEnabled(False)
            self.errorText.setText("List error ")
            self.errorText.setStyleSheet("color: Red;font-size:20px")
        else:
            self.errorText.setStyleSheet("color: cyan; font-size:20px;")
            self.errorText.setText("List verified, your list is : " + str(l))
            self.array=l
            print(self.array)



    def graphShow(self):
        fn.createGraph( self.graphDict)
        img = "Graph.gv.png"
        w = self.infos.width()
        h = self.infos.height()
        self.infos.setPixmap(PyQt5.QtGui.QPixmap(img).scaled(w, h, PyQt5.QtCore.Qt.KeepAspectRatio))

    def selectTreeSort(self):
        self.errorText.setText("Tree sort")
        self.done_2.setEnabled(True)

        self.illustration.setEnabled(True)
        self.formule.setEnabled(True)
        self.lien.setEnabled(True)
        self.video.setEnabled(True)
        self.save.show();
        self.graph.show();
        self.graph.setEnabled(True)
        l = fn.treesort(self.array)[0]
        d = fn.treesort(self.array)[1]
        self.graphDict=d;
        self.illus = "TreeSort/illus.png"
        self.formul = "TreeSort/algo.png"
        self.link = "https://fr.wikipedia.org/wiki/Tri_par_tas"
        self.vidlink = "TreeSort/vid.mp4"
        self.title = "Tree sort"
        self.result.setText(str(l))
        self.generator = fn.bubblesort(self.array)


    def selectBubbleSort(self):
        if ( self.array==None ):
            self.errorText.setText("No list to verify ! ")
            self.errorText.setStyleSheet("color: "+self.errorColors[(random.randint(0,len(self.errorColors)-1))]+";font-size:20px")
        else:

            self.done_2.setEnabled(True)
            self.illustration.setEnabled(True)
            self.formule.setEnabled(True)
            self.lien.setEnabled(True)
            self.video.setEnabled(True)
            self.illus = "bubbleSort/bubblesort.png"
            self.formul = "bubbleSort/algowiki.png"
            self.link = "https://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles"
            self.vidlink = "bubbleSort/bubbleSort.mp4"
            self.title="Bubble sort"
            self.errorText.setText("Bubble sort")

            x=self.array.copy()
            self.generator = fn.bubblesort(self.array)
            self.result.setText(str(fn.bubblesortNoAnim(x)))

    def selectInsertionSort(self):
        if ( self.array==None ):
            self.errorText.setText("No list to verify ! ")
            self.errorText.setStyleSheet("color: "+self.errorColors[(random.randint(0,len(self.errorColors)-1))]+";font-size:20px")
        else:
            self.done_2.setEnabled(True)
            self.illustration.setEnabled(True)
            self.formule.setEnabled(True)
            self.lien.setEnabled(True)
            self.video.setEnabled(True)
            self.illus = "InsertSort/illus.png"
            self.formul = "InsertSort/algo.png"
            self.link = "https://fr.wikipedia.org/wiki/Tri_par_insertion"
            self.vidlink = "InsertSort/insert.mp4"
            self.iteration = [0]
            self.errorText.setText("Insert sort")
            self.title="Insert sort"
            x = self.array.copy()
            self.generator = fn.insertionSort(self.array)
            self.result.setText(str(fn.insertionSortNoAnim(x)))


    def selectMergeSort(self):
        if ( self.array==None ):

            self.errorText.setText("No list to verify ! ")
            self.errorText.setStyleSheet("color: "+self.errorColors[(random.randint(0,len(self.errorColors)-1))]+";font-size:20px")
        else:
            self.done_2.setEnabled(True)
            self.illustration.setEnabled(True)
            self.formule.setEnabled(True)
            self.lien.setEnabled(True)
            self.video.setEnabled(True)
            self.illus = "MergeSort/illus.png"
            self.formul = "MergeSort/algo.png"
            self.link = "https://fr.wikipedia.org/wiki/Tri_fusion"
            self.vidlink = "MergeSort/Merge.mp4"

            self.errorText.setText("Merge sort")
            self.title = "Merge sort"
            x = self.array.copy()
            self.generator = fn.mergesort(self.array,0,len(self.array)-1)
            self.result.setText(str(fn.mergeSortNoAnime(x)))


    def selectQuickSort(self):
        self.done_2.setEnabled(True)
        self.illustration.setEnabled(True)
        self.formule.setEnabled(True)
        self.lien.setEnabled(True)
        self.video.setEnabled(True)
        self.illus = "QuickSort/illus.png"
        self.formul = "QuickSort/algo.png"
        self.link = "https://fr.wikipedia.org/wiki/Tri_rapide"
        self.vidlink = "QuickSort/Quick.mp4"

        self.errorText.setText("Quick sort")
        self.title = "Quick sort"
        x = self.array.copy()
        self.generator = fn.quicksort(self.array,0,len(self.array)-1)
        self.result.setText(str(fn.quickSortNoAnime(x,0,len(x)-1)))

    def selectSelectionSort(self):
        self.done_2.setEnabled(True)
        self.illustration.setEnabled(True)
        self.formule.setEnabled(True)
        self.lien.setEnabled(True)
        self.video.setEnabled(True)
        self.illus = "SelectionSort/illus.png"
        self.formul = "SelectionSort/algo.png"
        self.link = "https://fr.wikipedia.org/wiki/Tri_par_s%C3%A9lection"
        self.vidlink = "SelectionSort/Selection.mp4"
        self.errorText.setText("Selection sort")
        self.title = "Selection sort"
        x = self.array.copy()
        self.generator = fn.selectionsort(self.array)
        self.result.setText(str(fn.selectionSortNoAnime(x)))

    def showFormule(self):
        if(self.formul == " "):
            self.errorText.setText("No sorting method selected ! ! ")
            self.errorText.setStyleSheet("color: "+self.errorColors[(random.randint(0,len(self.errorColors)-1))]+";font-size:20px")
        else:

          #  self.infos.clf()

           # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
          #  ax = self.infos.add_subplot(111)
          #  ax.imshow(img)

           # pmap = QPixmap(img)

          #  ax.axis("off")
           # self.infos.canvas.draw()
            img = self.formul
            w = self.infos.width()
            h = self.infos.height()
            # pmap = QPixmap(img)
            self.infos.setPixmap(PyQt5.QtGui.QPixmap(img).scaled(w,h,PyQt5.QtCore.Qt.KeepAspectRatio))


    def showVideo(self):
        if(self.vidlink == " "):
            self.errorText.setText("No sorting method selected ! ! ")
            self.errorText.setStyleSheet("color: "+self.errorColors[(random.randint(0,len(self.errorColors)-1))]+";font-size:20px")
        else:
            cap = cv.VideoCapture(self.vidlink)

            while (cap.isOpened()):
                ret, frame = cap.read()
                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

                cv.imshow('frame', gray)
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv.destroyAllWindows()

    def showIllustration(self):
        if(self.illus == " "):
            self.errorText.setText("No sorting method selected ! ! ")
            self.errorText.setStyleSheet("color: "+self.errorColors[(random.randint(0,len(self.errorColors)-1))]+";font-size:20px")
        else:
         #   self.infos.clf()
            img = self.illus
            w=self.infos.width()
            h=self.infos.height()
           # pmap = QPixmap(img)
            self.infos.setPixmap(PyQt5.QtGui.QPixmap(img).scaled(w,h,PyQt5.QtCore.Qt.KeepAspectRatio))

          #  img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
          #  ax = self.infos.add_subplot(111)
          #  ax.imshow(img)
          #  ax.axis("off")
          #   self.infos.canvas.draw()


    def moreInfo(self):
        if(self.link ==" "):
            self.errorText.setText("No sorting method selected ! ! ")
            self.errorText.setStyleSheet("color: "+self.errorColors[(random.randint(0,len(self.errorColors)-1))]+";font-size:20px")
        else:
            webbrowser.open_new(self.link)



    def displaySort(self):
        if(self.generator == None):
            self.errorText.setText("No sorting method selected ! ")
            self.errorText.setStyleSheet("color: "+self.errorColors[(random.randint(0,len(self.errorColors)-1))]+";font-size:20px")
        else:
            title = self.title
            generator = self.generator
            A=self.array.copy()
            N = max(A)
            print(A)
            fig, ax = plt.subplots()
            ax.set_title(title)

            bar_rects = ax.bar(range(len(A)), A, align="edge")

            #ax.set_xlim(0, N)
            #ax.set_ylim(0, int(1.07 * N))

            text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
            iteration = [0]

            def update_fig(A, rects, iteration):
                for rect, val in zip(rects, A):
                    rect.set_height(val)
                iteration[0] += 1
                text.set_text("# Iterations : {}".format(iteration[0]))

            anim = animation.FuncAnimation(fig, func=update_fig,
                                           fargs=(bar_rects, iteration), frames=generator, interval=self.horizontalSlider.value(),
                                           repeat=False)
            plt.show()




def main():
    matplotlib.use('TkAgg')
    app=QtWidgets.QApplication(sys.argv)
    form = designWindow()
    form.show()
    form.update()
    app.exec_()
if __name__ == "__main__":
    main()