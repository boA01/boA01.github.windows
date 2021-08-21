import pyautogui as pg
import time as t 

if __name__ == "__main__":
    t.sleep(3)
    last_pos = pg.position()
    try:
        while 1:
            new_pos = pg.position()
            if last_pos != new_pos:
                print(pg.screenshot().getpixel(new_pos))
                last_pos = new_pos
    except:
        print("over!!!")
