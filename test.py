from PyQt4.QtGui import *
from PyQt4.QtCore import *
from UI import Ui_MainWindow
from multiprocessing import Process, Manager
import pypylon
import cv2
from cv2 import cv
import time
from ctypes import *
import numpy as np
import os
import psutil
import math

def Z_coordinate(pixel_x, pixel_y, x, y, z, Name,data_3D_Z):
    #3D Camera
    dll = cdll.LoadLibrary('HEELO_API.dll')
    height = 480
    width = 640
    count = width*height
    data_3D_x = (c_float*count)()
    data_3D_y = (c_float*count)()
    data_3D_z = (c_float*count)()
    dll.save.restype = POINTER(c_ubyte)
    data_Intensity = (c_uint16*count)()
    ret = dll.save(data_3D_x, data_3D_y, data_3D_z, data_Intensity)
    list = []
    for n in range(255):
        if ret[n] == 0:
            break;
        list.append(chr(ret[n]))
    list = ''.join(list)
    print type(list)
    Name[1] = list
    # p = psutil.Process(os.getpid())
    # if p.status() == psutil.STATUS_WAITING:
    #     print "22"
    data_3D_Z[0] = data_3D_z
    if pixel_x > 0 and pixel_y > 0:
        x = data_3D_x[pixel_y * width + pixel_x]
        y = data_3D_y[pixel_y * width + pixel_x]
        z = data_3D_z[pixel_y * width + pixel_x]
    # print("after call save with  C++ class, output x:")
    # create a 0 list
    # l = np.array([0, 0, 0], dtype=np.float)
    # matrix = [[l for i in range(width)] for i in range(height)]
    # matrix1= [[0 for i in range(width)] for i in range(height)]
    # matrix_3D = np.array(matrix)
    # matrix_Intensity = np.array(matrix1, dtype=np.uint16)


def ShowPic(out, name, pid):
    #2D camera
    #Nblocks = 1000  # arbitrary number of frames to plot

    print type(out)
    devices = pypylon.factory.find_devices()

    def connect(camdev, camind=0):
        cam = pypylon.factory.create_device(camdev[camind])
        name[0] = str(cam.device_info)
        cam.open()
        cam.properties['PixelFormat'] = 'RGB8'
        return cam

    print os.getpid()
    p = psutil.Process(pid)
    if p.status() == psutil.STATUS_RUNNING:
        print "ok"
    cam = connect(devices, 0)

    check = True
    while check:
        p = psutil.Process(pid)
        check = (p.status() == psutil.STATUS_RUNNING)
        images = cam.grab_images(1)
        img = [o for o in images][0]
        outt = np.zeros((img.shape[0], img.shape[1] / 3, 3), dtype=np.uint8)
        for m in range(img.shape[1]):
            c = int(m / 3)
            outt[:, c, 2 - (m % 3)] = img[:, m]
        out[0] = outt
    cam.close()


def data_process(out, lst_bbox, Points, data_3D_z ):

    # set red thresh
    lower_red = np.array([156, 40, 40])  # sunshine
    upper_red = np.array([180, 255, 255])
    lower_red1 = np.array([0, 40, 40])  # shandow
    upper_red1 = np.array([10, 255, 255])
    time = 0
    points = []
    # points.append([0, 0, 0, 0])
    index = 0
    # Arrays to store object points and image points from all the images.
    # Make a list of calibration images

    img_size = (out.shape[0], out.shape[1])
    img_combine = np.zeros((out.shape[0], out.shape[1], 3), np.float32)
    # P_2d_pixel stores the corresponding pixel of 2d image;
    # e.g pixel (5,5) in 2d image is the same pixel with that in P_2d_pixel[5,5] in 3d image
    P_2d_pixel = np.zeros((out.shape[0], out.shape[1], 2), np.int32)

    mtx_Hscale = np.array(
        [[0.867562, 0.0767659, 20.0037], [-0.0767659, 0.867562, 31.1582], [0, 0, 1]])

    def Validate_pixel(coord):
        if math.isinf(coord[0]) == 0 and \
                        math.isinf(coord[1]) == 0 and \
                        coord[0] > 0 and \
                        coord[1] > 0 and \
                        coord[0] < 480 and \
                        coord[1] < 640:
            return True

    while True:
        if time != lst_bbox[1]:  # new

            for i in range(img_size[0]):
                for j in range(img_size[1]):

                    # Halcon calculate the matrix as row first, then column;
                    # This is opposite with what openCV does, so putting the coordinate as P_2d_pixel[i,j,1], P_2d_pixel[i,j,0]
                    pp = [i, j, 1]
                    p_array = np.array(pp)
                    p_trans = np.dot(mtx_Hscale, p_array)
                    P_2d_pixel[i, j, :] = p_trans[0:2]
                    # validate if the coordinate in P_2d_pixel is reasonable coordinate
                    val = Validate_pixel(P_2d_pixel[i, j])
                    if val:
                        img_combine[i, j, :] = out[P_2d_pixel[i, j, 0], P_2d_pixel[i, j, 1]]

            if any(lst_bbox[0][0]):  # not null
                for i in range(lst_bbox[0]):
                    # get a frame and show
                    frame = out[i[0]:i[2], i[1]:i[3]]
                    # h, w = frame.shape[:2]
                    blured = cv2.blur(frame, (5, 5))  # remove noise

                    hsv = cv2.cvtColor(blured, cv2.COLOR_BGR2HSV)
                    binary = cv2.inRange(hsv, lower_red, upper_red)
                    binary1 = cv2.inRange(hsv, lower_red1, upper_red1)
                    binary = cv2.bitwise_or(binary, binary1)

                    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    len = 0
                    for c in contours:
                        if c.size > len:
                            len = c.size
                            a = c
                    # compute the center of the contour
                    M = cv2.moments(a)
                    cX = 0
                    cY = 0
                    if M["m00"] != 0:
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])
            # cv2.drawContours(frame, [a], -1, (0, 0, 255), 3)
            # cv2.circle(frame, (cX, cY), 7, (255, 255, 255), -1)
            # cv2.putText(frame, "center", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                        width = img_size[1]
                        z = data_3D_z[P_2d_pixel[cY, cX, 1] * width + P_2d_pixel[cY, cX, 0]]  # from 2D to 3D
                    if points.size == 0:
                            points.append([cX, cY, z, 1])
                    else:
                        flag = 0
                        for j in range(points):
                            if i[0] < j[0] < i[0] + i[2] \
                                    and i[1] < j[1] < i[1] + i[3] \
                                    and j[2]-1 < z < j[2]+1:
                                j[0] = cX
                                j[1] = cY
                                j[2] = z
                                j[3] = j[3]+1
                                flag = 1
                        if flag == 0:
                            points.append([cX, cY, z, 1])
            if index == 4:
                Points[0] = points
                points.clear()
                index = -1
            index = index + 1
        time = lst_bbox[1]
    # end


class Timer(QThread):

    def __init__(self, signal="updateTime()", parent=None):
        super(Timer, self).__init__(parent)
        self.stoped = False
        self.signal = signal
        self.mutex = QMutex()

    def run(self):
        with QMutexLocker(self.mutex):
            self.stoped= False
        while True:
            if self.stoped:
                return
            self.emit(SIGNAL(self.signal))
            time.sleep(0.04)

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stoped= True

    def isStoped(self):
        with QMutexLocker(self.mutex):
            return self.stoped


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.m = Manager()

        self.out = self.m.list()  # the image
        array_dim = (480, 640, 3)
        img_ndarray = np.zeros(array_dim)
        self.out.append(img_ndarray.tolist())

        self.name = self.m.dict()  # camera name
        self.name[0] = " "
        self.name[1] = " "

        self.applePoints = self.m.list()  # the apple
        self.applePoints.append([[0, 0, 0, 0]])

        self.data_3D_Z = self.m.list()  # range data
        # array_dim = (480, 640, 1)
        img_ndarray = np.zeros(640*480)
        self.data_3D_Z.append(img_ndarray.tolist())

        self.Point = self.m.list()  # 3D coordinate of the mouse
        self.Point.append([0, 0, 0])

        self.pid = os.getpid()
        self.p = Process(target=ShowPic, args=(self.out, self.name, self.pid,))  #2D process
        self.p1 = Process(target=Z_coordinate, args=(self.label.pixel_x, self.label.pixel_y, self.x, self.y, self.z, self.name, self.pid)) #3D process
        self.p2 = Process(target=frame_detect_fasterRCNN, args=(self.out[0], self.label.lst_bbox,))  # Test process
        self.p3 = Process(target=data_process, args=(self.out[0], self.label.lst_bbox, self.applePoints, self.data_3D_Z,))  # data process
        self.playTimer = Timer("updateTime()")
        self.connect(self.playTimer, SIGNAL("updateTime()"), self.updatePlay)
        self.connect(self.Opencamera, SIGNAL("clicked()"), self.startPlay)
        self.connect(self.Test,SIGNAL("clicked()"), self.startTest)
        self.p.start()
        self.p1.start()

    def startPlay(self):
        self.playTimer.start()

    def updatePlay(self):
        #show = self.out[..., ::-1]
        #img = cv2.imread("alpha.png")
        #height, width, bytesPerComponent = img.shape
        #bytesPerLine = bytesPerComponent * width;
        img = np.array(self.out[0])
        # Convert to RGB for QImage.
        cv2.cvtColor(img, cv.CV_BGR2RGB, img)
        showImage = QImage(img.data, 640, 480, QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(showImage))

        newItem = QTableWidgetItem(self.name[0])
        self.tableWidget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem(self.name[1])
        self.tableWidget.setItem(1, 0, newItem)
        if self.label.pixel_x > 0 and self.label.pixel_y > 0:
            newItem = QTableWidgetItem(str(self.label.pixel_x))
            self.tableWidget_2.setItem(0, 0, newItem)
            newItem = QTableWidgetItem(str(self.label.pixel_y))
            self.tableWidget_2.setItem(1, 0, newItem)
            newItem = QTableWidgetItem(str(self.x))
            self.tableWidget_2.setItem(2, 0, newItem)
            newItem = QTableWidgetItem(str(self.y))
            self.tableWidget_2.setItem(3, 0, newItem)
            newItem = QTableWidgetItem(str(self.z))
            self.tableWidget_2.setItem(4, 0, newItem)

    def startTest(self):
        self.p2.start()
        self.p3.start()



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())