from tkinter import *
import tkinter.messagebox as messagebox

'''
GUI中，每个button（按钮），label（标签），输入框等，
都是以一个widget（部件）。Frame就是
可以容纳其他widget的widget，所有的
widget组合起来就是一棵树。
'''

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        #pack()把widget加到容器中，并实现布局，grid()可以实现更复杂的布局
        # self.pack()
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text="输入姓名：")
        self.helloLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text="登陆", command=self.hello)
        self.alertButton.pack()
        # self.quitButton = Button(self,text='quit',command=quit)
        # self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo("Message",f"hello {name}")

if __name__=="__main__":
    app = Application()
    #设置窗口标题
    app.master.title("new window")
    #主消息循环
    app.mainloop()
    
