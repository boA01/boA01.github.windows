from tkinter import *
root = Tk()
root.title("hello world")
names = ('0','1','2','3','5','6','7','8','9','+','-','*','/','.','=')
for i in range(len(names)):
      b=Button(root, text = names[i],width=4)#按钮
      b.pack()
e = Entry(root, text = '555',width=4)#输入
l1 = Label(root, text = '666',width=4)#显示
#Menu#菜单
#Listbox#选择

e.pack() 
l1.pack()
root.mainloop()
      
