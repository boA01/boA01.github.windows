from pywebio.input import input, FLOAT
from pywebio.output import put_text

def bmi(height, weight):
    bmi_value = weight/(height/100)**2

    top_status = [(14.9, '极瘦'),
    (18.4, '偏瘦'),
    (22.9, '正常'),
    (27.5, '过重'),
    (40.0, '肥胖'),
    (float('inf'), '非常肥胖')
    ]
    # (float('inf'):'非常肥胖')}

    for k, v in top_status:
        if bmi_value <= k:
            return bmi_value,v

def main():
    height = input("身高(cm)：", type=FLOAT)
    weight = input("体重(kg)：", type=FLOAT)

    bmi_value, status = bmi(height, weight)

    #输出文本
    put_text(f"你的BMI：{bmi_value:.2f}，身体状况：{status}")

    #输出表格
    put_table([
        ['Product', 'Price'],
        ['Apple', '$5.5'],
        ['Banner', '$6']
    ])
    
    #输出图像
    put_image(open('./image/AC.png', 'rb').read())

    #输出MarkDown
    put_markdown('**Blod text')

    #输出通知消息
    toast('Awesome PyWebIO!!')

    #输出文件
    put_file('hello_world.txt', b'hello world')

    #输出html
    put_html("<h1>hello html</h1>")

    #输出弹窗
    with popup('Popu title'):
        put_text('hwllo world')


    #点击按钮
    def on_click(btn):
        put_markdown("You click `%s` button" %btn)

    #使用行布局
    put_row([put_code('A'), None, put_code('B')])

    #输出进度条
    import time
    put_processbar('bar1')
    for i in range(1, 11):
        set_processbar('bar', i/10)
        time.sleep(0.1)

if __name__ == '__main__':
    main()