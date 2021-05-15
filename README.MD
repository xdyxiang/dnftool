## 软件功能   旭旭宝宝，一阵雨  命运抉择ban选工具
- 随机：
1. dnf 全职业随机
2. 队员随机分组
3. 队员随机上次顺序

- ban选功能：
1. ban选职业，展示已经ban选，未ban选职业
2. 已ban选职业随机
3. 未ban选职业随机

-  期待功能
1. 随机禁用职业技能
2. 随机禁用道具，buff



### 环境安装：
- 安装python3
- pip install pyQT5  -i https://pypi.douban.com/simple
- pip install pyqt5_tools   -i https://pypi.douban.com/simple
- pip install pyinstaller   -i https://pypi.douban.com/simple

### 页面UI设计
- pyqt UI 绘制
   UiDesign程序启动页面：\site-packages\qt5_applications\Qt\bin\designer.exe
- UI代码文件输出
   \Scripts\pyuic5.exe -o mytool.py mytool.ui     # 在命令目录找到这两文件，放到工程下使用


### 打包成exe
* 使用打包工具：pyinstaller
* 打包： -w 无窗口   -F  生产一个exe文件  -i  添加图标   --add-data  打包静态资源
* pyinstaller -w  -i  ./res/icon.ico  -F app.py --add-data res;res


### 包文件
* dist文件夹下有可以运行的exe文件，下载可用