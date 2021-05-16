import remi.gui as gui
from remi import start, App
import pymongo

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)
    
    def main(self):
        container = gui.VBox(width=600, height=600)
        self.lbl = gui.Label('hello workd')
        self.bt = gui.Button("press me!")

        # self.bt.onclick.do(self.on_button_pressed)

        self.bt.onclick.do(self.rlt)

        container.append(self.lbl)
        container.append(self.bt)
        
        return container
    
    def on_button_pressed(self, widget):
        self.lbl.set_text('Button pressed')
        self.bt.set_text('Hi')
    
    def rlt(self, widget):
        cli = pymongo.MongoClient(host='127.0.0.1')

        db_list = cli.list_database_names()
        # print(db_list)

        db = cli.test1
        # print(db.)

        ct = db.c3

        result = ct.find({}, {"_id":0})

        a=''
        for i in result:
            a+=str(i)

        self.lbl.set_text(a)
        self.bt.set_text("hi")

con=start(MyApp)

try:
    while (1):
        con
except:
        print("hhh")