from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QButtonGroup, QFrame, QToolButton, QStackedLayout,\
    QWidget, QStatusBar,QAction
from PyQt5.QtGui import QFont,QIcon

import sys,random,json,copy
from mytool import Ui_MainWindow as Ui_Main1
from mytool1 import Ui_MainWindow as Ui_Main2
from data import data,emptydata

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.ui1 = Ui_Main1()
        self.ui2 = Ui_Main2()
        self.__setup_ui__()

    def __setup_ui__(self):

        self.setWindowTitle('DNF tool')  # 设置窗口标题
        # 获取据对路径
        self.setWindowIcon(QIcon('./res/icon.ico'))
        self.resize(650, 700)
        # 2. 工作区域
        self.main_frame = QFrame(self)
        self.main_frame.setGeometry(0, 0, self.width(), self.height())
        # self.main_frame.setStyleSheet("background-color: rgb(65, 95, 255)")

        # 创建堆叠布局
        self.stacked_layout = QStackedLayout( self.main_frame)

        # # 第一个布局界面
        self.main_frame1 = QMainWindow()
        # # 第二个布局界面
        self.main_frame2 = QMainWindow()
        self.ui1.setupUi(self.main_frame1)   
        self.ui2.setupUi(self.main_frame2)   
        # 把两个布局界面放进去
        self.stacked_layout.addWidget(self.main_frame1)
        self.stacked_layout.addWidget(self.main_frame2)


        action1=QAction('&随机',self)
        action1.triggered.connect(self.click_window1) 
        action2=QAction('&ban职业',self)
        action2.triggered.connect(self.click_window2) 

        self.ui1.menu.addAction(action1)
        self.ui2.menu.addAction(action1)
        self.ui1.menuban.addAction(action2)
        self.ui2.menuban.addAction(action2)

        self.ui1.pushButton.clicked.connect(self.do_group)
        self.ui1.pushButton_2.clicked.connect(self.do_random)
        self.ui1.pushButton_3.clicked.connect(self.all_random)
        self.ui2.pushButton.clicked.connect(self.ban)
        self.ui2.pushButton_2.clicked.connect(self.resetdata)
        self.ui2.pushButton_3.clicked.connect(self.left_random)
        self.ui2.pushButton_4.clicked.connect(self.ban_random)
        

        # 初始化UI2数据
 
        self.leftdata=copy.deepcopy(data)
        self.show_log2(json.dumps(self.leftdata,ensure_ascii=False,indent=4))
        self.emptydata=copy.deepcopy(emptydata)
        self.show_log3(json.dumps(self.emptydata,ensure_ascii=False,indent=4))


    def click_window1(self):
        if self.stacked_layout.currentIndex() != 0:
            self.stacked_layout.setCurrentIndex(0)

    def click_window2(self):
        if self.stacked_layout.currentIndex() != 1:
            self.stacked_layout.setCurrentIndex(1)
   
    def show_log1(self,text):
        self.ui1.textBrowser.setText(text)

    def show_log2(self,text):
        self.ui2.textBrowser.setText(text)
    # 已ban选职业展示
    def show_log3(self,text):
        self.ui2.textBrowser_2.setText(text)

    def show_log4(self,text):
        self.ui2.textBrowser_3.setText(text)


    # 随机分组
    def do_group(self):
        textvalue = self.ui1.lineEdit.text()
        result = []
        for i in textvalue.replace(",","，").split("，"):
            if i:
                result.append(i.strip())
        random.shuffle(result)
        n = int(self.ui1.spinBox.text()) #分成n组
        list2 = []
        if len(result) > 0 and n > 0:
            m = int(len(result)/n)
            for v in range(0, len(result), m):
                list2.append(result[v:v+m])
        self.show_log1(json.dumps(list2,ensure_ascii=False,indent=4))
    # 随机
    def do_random(self):
        textvalue = self.ui1.lineEdit_2.text()
        result = []
        for i in textvalue.replace(",","，").split("，"):
            if i:
                result.append(i.strip())
        random.shuffle(result)
        self.show_log1(json.dumps(result,ensure_ascii=False,indent=4))
    # 全职业随机
    def all_random(self):
        occupationlist = []
        for k in data:
            occupationlist.extend(data[k])
        n = int(self.ui1.spinBox_2.text()) # 随机个数
        if len(occupationlist)>n:
            textvalue = random.sample(occupationlist,n)
        else:
            textvalue = occupationlist
        self.show_log1(json.dumps(textvalue,ensure_ascii=False,indent=4))

    def ban(self):
        textvalue = self.ui2.lineEdit.text()
        for i in textvalue.replace("\"",",").replace(",","，").split("，"):
            i = i.strip()
            if i:
                for k in self.leftdata:
                    if i in self.leftdata[k]:
                        self.leftdata[k].remove(i)
                        self.emptydata[k].append(i)
        self.show_log2(json.dumps(self.leftdata,ensure_ascii=False,indent=4))
        self.show_log3(json.dumps(self.emptydata,ensure_ascii=False,indent=4))

    def resetdata(self):
        self.leftdata=copy.deepcopy(data)
        self.show_log2(json.dumps(self.leftdata,ensure_ascii=False,indent=4))
        self.emptydata=copy.deepcopy(emptydata)
        self.show_log3(json.dumps(self.emptydata,ensure_ascii=False,indent=4))
    
    # 剩余职业随机
    def left_random(self):
        leftlist = []
        for k in self.leftdata:
            leftlist.extend(self.leftdata[k])
        n = int(self.ui2.spinBox.text()) # 随机个数
        if len(leftlist)>n:
            textvalue = random.sample(leftlist,n)
        else:
            textvalue = leftlist
        self.show_log4(json.dumps(textvalue,ensure_ascii=False,indent=4))

    def ban_random(self):
        banlist = []
        for k in self.emptydata:
            banlist.extend(self.emptydata[k])
        n = int(self.ui2.spinBox.text()) # 随机个数
        if len(banlist)>n:
            textvalue = random.sample(banlist,n)
        else:
            textvalue = banlist
        self.show_log4(json.dumps(textvalue,ensure_ascii=False,indent=4))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Demo()
    window.show()
    sys.exit(app.exec_())

