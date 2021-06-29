import pandas as pd
import pyautogui, time, pyperclip


def out(MM):
    table = pd.read_excel("邓超.xls",header=MM,usecols=[1,2,3])
    f=open('xxx.txt','a+')

    for i in table.values.tolist():
        x=0
        #鼠标移动
        pyautogui.moveTo(397,230,duration = 1)
        # 鼠标点击
        pyautogui.click()
        pyperclip.copy(i[1])
        pyautogui.hotkey("ctrl","v")
        # print(i[1])
        # 鼠标相对移动
        pyautogui.moveRel(0,49,duration=1) #397,279
        pyautogui.click()
        pyperclip.copy(i[0])
        pyautogui.hotkey("ctrl","v")
        pyautogui.press('enter')
        # print(i[0])
        time.sleep(0.5)
        #pyautogui.press('enter')
        # 鼠标相对移动
        # pyautogui.moveRel(-221,220,duration=1) #176,489
        # 获得指定区域坐标
        try:
            help_pos1 = pyautogui.locateOnScreen("flag2.png")

            pyautogui.moveTo(help_pos1.left+help_pos1.width//2,help_pos1.top+help_pos1.height//2)
            pyautogui.click()
        except:
            pass
        finally:
            try:
                help_pos = pyautogui.locateOnScreen("Flag.png")
                pyautogui.moveTo(help_pos.left+help_pos.width,help_pos.top+help_pos.height+6)
                pyautogui.mouseDown(button="left")#247
                pyautogui.moveRel(71,0)
                pyautogui.hotkey("ctrl","c")
                pyautogui.mouseUp(button="left")

                a=pyperclip.paste()
                if "米" in a:
                    x=round(int(a.split("米")[0])/1000,2)
                elif "里" in a:
                    x=float(a.split("公")[0])
            except:
                pass
            finally:
                print(x)
                f.write(str(x)+" ")
    f.close()


out(431)

# with open("xxx.txt","r") as f:
#     a = f.read().split(" ")
#     # print(list(a),end="\n")
#     for i in list(a)[500:1000]:
#         print(eval(i))
   乾县
    
    # time.sheep()

# pd.DataFrame(table).to_excel("邓超.xls")
# print(table.head(3))



# pyautogui.moveTo(397,230,duration = 1)
# if help_pos1 := pyautogui.locateOnScreen("flag2.png"):
#             pyautogui.moveTo(help_pos1.left+help_pos1.width//2,help_pos1.top+help_pos1.height//2)
#             pyautogui.click()
# else:
#     pass
# help_pos1 = pyautogui.locateOnScreen("flag2.png")
# pyautogui.moveTo(help_pos1.left,help_pos1.top)
# pyautogui.click()
# print(help_pos1)

# help_pos = pyautogui.locateOnScreen("Flag.png")
# print(help_pos.left+help_pos.width,help_pos.top+help_pos.height+6)





# class PyAutoGUIPlugs:
    
#     def __init__(self):
#         #保护措施，避免失控
#         pyautogui.FAILSAFE = True
#         #为所有的PyAutoGUI函数增加延迟。默认延迟时间是0.1秒。
#         pyautogui.PAUSE = 0.5

#     #鼠标操作
#     #当前屏幕的分辨率（宽度和高度）
#     def screeSize(self):
# 	    return pyautogui.size()

#     #  (x,y)是否在屏幕上
#     def onScreen(self, X, Y):
# 	    return pyautogui.onScreen(X, Y)

#     # 获取鼠标位置
#     def get_mouse_positon(self):
#         time.sleep(5) # 准备时间
#         print('开始获取鼠标位置')
#         x = None
#         y = None 
#         try:
#             for i in range(5):
#                 # Get and print the mouse coordinates.
#                 x, y = pyautogui.position()
#                 positionStr = '鼠标坐标点（X,Y）为：{},{}'.format(str(x).rjust(4), str(y).rjust(4))
#                 pix = pyautogui.screenshot().getpixel((x, y)) # 获取鼠标所在屏幕点的RGB颜色
#                 positionStr += ' RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(3) + ')'
#                 print(positionStr)
#                 time.sleep(1) # 停顿时间
#                 del i
#         except:
#             print('获取鼠标位置失败')
#         return x, y
    
#     #num_seconds秒钟鼠标移动坐标为X, Y位置  绝对移动,duration为持续时间
#     def moveTo(self, X, Y, num_seconds):
# 	    pyautogui.moveTo(X, Y, duration=num_seconds, tween=pyautogui.easeInOutQuad)
    
#     #右击
#     def rightClick(self, moveToX, moveToY):
# 	    pyautogui.rightClick(x=moveToX, y=moveToY)

#     def middleClick(self, moveToX, moveToY):
# 	    pyautogui.middleClick(x=moveToX, y=moveToY)
    
#     # 鼠标moveToX, moveToY位置，0间隔，左击两下
#     def doubleClick(self, moveToX, moveToY):
# 	    pyautogui.doubleClick(x=moveToX, y=moveToY, button="left", interval=0.0)

#     # 鼠标moveToX,moveTo位置左击三下
#     def tripleClick(self, moveToX, moveToY):
# 	    pyautogui.tripleClick(x=moveToX, y=moveToY)    

#     #鼠标移动到moveToX, moveToY位置按下（左键）
#     def mouseDown(self, moveToX, moveToY):
# 	    pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')

#     #鼠标移动到( moveToX, moveToY)位置再向上滚动10格
#     def scrollXY(self, moveToX, moveToY):
#         pyautogui.scroll(10, x=moveToX, y=moveToY) # 10表示：向上滚动10格；-10表示：向下滚动10格；
#         pyautogui.scroll()
    
#     #amount_to_scroll参数表示滚动的格数
#     def scroll(self, amount_to_scroll):
# 	    pyautogui.scroll(amount_to_scroll) # 10表示：向上滚动10格；-10表示：向下滚动10格；
    
#     #鼠标水平滚动（Linux）
#     def hscroll(self):
# 	    pyautogui.hscroll()
	
#     #鼠标左右滚动（Linux）
#     def vscroll(self):
# 	    pyautogui.vscroll()
    
#     # 按住鼠标左键，把鼠标拖拽到(100, 200)位置
#     def dragTo(self, moveToX, moveToY):
# 	    pyautogui.dragTo(moveToX, moveToY, button='left')
    
#     # 按住鼠标左键，用2秒钟把鼠标拖拽到(moveToX, moveToY)位置
#     def dragToNum(self, moveToX, moveToY, num_seconds):
# 	    pyautogui.dragTo(moveToX, moveToY, num_seconds, button='left')

#     # 按住鼠标左键，用0.2秒钟把鼠标向上拖拽（其中,moveToY为负值；）
#     def dragRel(self, moveToY, num_seconds):
# 	    pyautogui.dragRel(0, moveToY, duration=num_seconds)
    
# #++++++键盘操作+++++我们在pyautogui库对于键盘的使用方法大体如下：++++++++++++++
	
#     #模拟输入信息,每次输入间隔0.5秒
#     def typewrite(self, Str):
# 	    pyautogui.typewrite(message=Str, interval=0.5)
    
#     #  PyAutoGUI输入【中文】需要用粘贴实现
#     #  Python 2版本的pyperclip提供中文复制
#     def paste(self, foo):
#         pyperclip.copy(foo)
#         pyautogui.hotkey('ctrl', 'v')
	
#     # 按下并松开（轻敲）回车键
#     def pressEnter(self, Str):
# 	    pyautogui.press('enter') 
    
#     #点击ESC
#     def pressESC(self, Str):
# 	    pyautogui.press('esc')
	
#     # 按住shift键
#     def keyDownShift(self, Str):
# 	    pyautogui.keyDown('shift')
    
#     # 放开shift键
#     def keyUpShift(self, Str):
# 	    pyautogui.keyUp('shift')
    
#     # 模拟组合热键（复制；）
#     def hotkeyCtrlC(self, Str):
# 	    pyautogui.hotkey('ctrl', 'c')
    
#     # 组合按键（Ctrl+V），粘贴功能，按下并松开'ctrl'和'v'按键
#     def hotkeyCtrlV(self):
# 	    pyautogui.hotkey('ctrl', 'v') 

#     #同时按下shift和某个数字键；
#     def keyUpShiftNumber(self, number):
#         pyautogui.keyDown('shift')
#         pyautogui.press(str(number))
#         pyautogui.keyUp('shift') # 输出 $ 符号的按键
