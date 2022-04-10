import pygame
from math import sqrt
from pandas import read_csv as rcv
import plotly.graph_objects as go
import test3 as t3

FW = 820 # 父画布宽度F
FH = 500 # 父画布高度
SW = 400 # 子画布宽度
SH = 400 # 子画布高度
RATIO = 400 / (t3.L) # 绘图比

gray = (128, 128, 128)
coloes = [
    (255, 0, 0),
    (255,255,0), #黄
    (255,165,0), #橙
    (0,255,0),   #绿
    (0,255,255), #青
    (128,0,128), #紫
    (0,191,255), #天蓝
    (0,0,255),
    (0,0,0)
]

# 初始化pygame模块
pygame.init()

# 设置窗口
screen = pygame.display.set_mode((FW, FH))

# 设置图标
# pygame.display.set_icon()

# 设置窗口标题
pygame.display.set_caption('毕业设计')

# 字体设置
font = pygame.font.Font("STXINGKA.TTF", 28)

# 文本处理
def drawText(content):
    score_text = font.render(content, True, gray)
    return score_text

# 图片
# def drawImage(pth):
#     surface_img = pygame.image.load(pth).convert()

# 网格线
def draw_wgx(face):
    for x in range(0, SW, 20):
        pygame.draw.line(face, gray, (x, 0), (x, 400))
    for y in range(0, SH, 20):
        pygame.draw.line(face, gray, (0, y), (400, y))

# 切面图
def draw_qm(face, i, arr):
    # 绘制网格线
    draw_wgx(face)
    # 优化处理
    x1 = -1
    for x, y, z in arr:
        # 非同一维度才计算
        if x1 != x:
            x1 = x
            # 圆心到切面距离
            l = i-x1
            # 半径
            r = sqrt(t3.R**2-l**2)
        pygame.draw.circle(face, coloes[l], (y*RATIO, z*RATIO), r*RATIO, width = 1)

# 子Surface
def sf(col, i, data):
    face = pygame.Surface(size=(400,400), flags=pygame.HWACCEL)
    face.fill(color=col)
    # 切面图
    draw_qm(face, i, data)
    return face

# 折线图
def sca_show(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['x'],
        y=df['f'],
        mode='lines+markers',
        name='覆盖率',
    ))
    fig.add_trace(go.Scatter(
        x = df['x'],
        y = df['n1'],
        mode = "lines+markers",
        name = "节点数目"
    ))
    fig.add_trace(go.Scatter(
        x = df['x'],
        y = df['n2'],
        mode = "lines+markers",
        name = "优化后节点数目"
    ))
    fig.update_layout(
        title = "栅栏情况折线统计图",
        xaxis_title = "栅栏面/x",
        yaxis_title = "(覆盖率)/(数目)"
    )
    fig.show()

def main():
    # 切面x
    n = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                screen.fill((0))
                if event.key == pygame.K_q:
                    exit()
                elif event.key == pygame.K_RIGHT:
                    if n < t3.L-1:
                        n+=1
                elif event.key == pygame.K_UP:
                    if n < t3.L-10:
                        n+=10
                elif event.key == pygame.K_LEFT:
                    if n > 0:
                        n-=1
                elif event.key == pygame.K_DOWN:
                    if n >= 10:
                        n-=10
                elif event.key == pygame.K_z:
                    # 优化数据
                    df1 = rcv.read_csv(r"data1.csv")
                    sca_show(df1)
                elif event.key == pygame.K_r:
                    # 重构数据
                    t3.reset()

                df_x = t3.read_zl_x(n)
                pre, arr_y = t3.cover_jd(n, df_x)
                # 栅栏面
                screen.blit(drawText(f'x={n}'), (10, 10))
                # 覆盖率
                screen.blit(drawText(f"覆盖率: {pre}%"), (300, 10))
                # 结点数目
                screen.blit(drawText(f'结点数目: {len(df_x)}个'), (0, 50))
                screen.blit(drawText(f'结点数目: {len(arr_y)}个'), (420, 50))
                # 子窗口
                screen.blit(sf("white", n, df_x.values), (0, 80))
                screen.blit(sf("white", n, arr_y), (420, 80))
                # 全局刷新
                pygame.display.flip()

if __name__ == '__main__':
    # t3.main()
    main()