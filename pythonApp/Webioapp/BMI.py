from pywebio.input import *
from pywebio.output import *

def bmi(height, weight):
    bmi_value = weight/(height/100)**2

    top_status = [(14.9, '极瘦'),
    (18.4, '偏瘦'),
    (22.9, '正常'),
    (27.5, '过重'),
    (40.0, '肥胖'),
    (float('inf'), '非常肥胖')
    ]

    for k, v in top_status:
        if bmi_value <= k:
            return bmi_value,v

def mai():
# 输入函数
    # 输入框（不能有name）
    password = input("Input password", type=PASSWORD)
    
    # 输入组（必须有name）
    info = input_group("User info",[
        input('Input your name', name='name'),
        input('Input your age', name='age', type=NUMBER)
    ])
    print(info['name'], info['age'])

    # 文本输入
    text = textarea('Text Area', rows=3, placeholder='Some text')
    
    # 代码输入
    code = textarea('Code Edit',
            code={
                'mode':'python',
                'theme':'darcula'}
            )

    # 下拉列表
    gift = select('Which gift you want?', options=['keyboard', 'ipad'])

    # 单选框
    answer = radio("Choose one", options=['A', 'B', 'C', 'D'])

    # 复选框
    agree = checkbox("User Term", options=['I agree to terms and conditions'])
    
    # 按钮
    bt = actions()

    # 文件上传
    img = file_upload("Select a image:", accept="image/*")
    if img:    
        put_image(img['content'], title=img['filename']) 
    
# 输出函数
    #输出文本
    put_text(f'passwd{password}')
    
    #输出表格
    put_table([
        ['Product', 'Price'],
        ['Apple', '$5.5'],
        ['Banner', '$6']
    ])
    
    # 输出图像
    put_image(open(r'image/AC.png', 'rb').read())

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

    # 点击事件
    put_buttons()
    
    #使用行布局
    put_row([put_code('A'), None, put_code('B')])

    #输出进度条
    import time
    put_processbar('bar1')
    for i in range(1, 11):
        set_processbar('bar', i/10)
        time.sleep(0.1)

def main():
    height = input("身高(cm)：", type=FLOAT)
    weight = input("体重(kg)：", type=FLOAT)
    bmi_value, status = bmi(height, weight)
    put_text(f"你的BMI：{bmi_value:.2f}，身体状况：{status}")

if __name__ == '__main__':
    main()