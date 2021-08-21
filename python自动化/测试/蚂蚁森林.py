import uiautomator2 as u2
import time
import random

d = u2.connect() #有线连接
#d = u2.connect("ip") #无线连接，同一局域网内

print("打开支付宝")
d.app_start("com.eg.android.AlipayGphone")
time.sleep(5) #休息5s，等待支付宝完全启动

print("打开蚂蚁森林")
d(text="蚂蚁森林").click() #蚂蚁森林放支付宝首页
time.sleep(5)

def collectEnergy(cnt):
    print("开始第%d次取能量"%cnt)

    for i in range(150, 1000, 150):
        for j in range(600, 900, 150):
            d.long_click(i + random.randint(10, 20), j + random.randint(10, 20),0.1)
            time.sleep(0.01)
            if cnt != 1:
		        d.click(536,1816)

cnt = 1
while 1:
    collectEnergy(cnt)
    a = d.xpath("//*[@resource-id='J_tree_dialog_wrap']").get().bounds
    d.click(1000,a[3]-88) #能量按钮坐标
    
    #出现“返回我的森林”，结束
    if d.xpath("//*[@text='返回我的森林']").click_exists(timeout=2.0):
        break
    cnt+=1
print("结束！！！")
d.app_stop("com.eg.android.AlipayGphone") #退出支付宝
