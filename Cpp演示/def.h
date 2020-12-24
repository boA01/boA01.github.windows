#include <iostream>
#include <graphics.h>
#include "clas.h"
#include <vector>
using namespace std;

G::G(int x, int y) : m_x(x), m_y(y){}

void G::display(){}

void G::move(int x, int y){}

void G::scale(float n){}


C::C(int x, int y, int r) : G(x, y), m_r(r){}

C::~C()
{
	closegraph();
}
		
void C::display()
{
//	setcolor(YELLOW);
	cleardevice();
	circle(m_x, m_y, m_r);
}

void C::move(int x, int y)
{
	m_x += x;
	m_y += y;
	cleardevice();
	circle(m_x, m_y, m_r);
}
		
void C::scale(float n)
{
	m_r += (int) 50*n;
	cleardevice();
	circle(m_x, m_y, m_r );
}
	

B::B(int x, int y, int x1, int y1) : G(x, y), m_x1(x1), m_y1(y1){}

B::~B()
{
	closegraph();
}
		
void B::display()
{
	cleardevice();
	setfillcolor(YELLOW);
	bar(m_x, m_y, m_x1, m_y1);
}
		
void B::move(int x, int y)
{
	m_x += x;
	m_y += y;
	m_x1 += x;
	m_y1 += y;
	cleardevice();
	setfillcolor(YELLOW);
	bar(m_x, m_y, m_x1, m_y1);
}

void B::scale(float n)
{
	int ch_x = (int) n*((m_x1 - m_x)/4);
	int ch_y = (int) n*((m_y1 - m_y)/4);
	m_x -= ch_x;
	m_y -= ch_y
	m_x1 += ch_x;
	m_y1 += ch_y
	cleardevice();
	setfillcolor(YELLOW);
	bar(m_x, m_y, m_x1, m_y1);
}


void menu()
{
	setfont(20, 0, "楷体");
	xyprintf(400, 220, "      菜单     ");
	xyprintf(400, 240, "###############");
	xyprintf(400, 260, "#     选绘    #");
	xyprintf(400, 280, "#     c.圆    #");
	xyprintf(400, 300, "#    b.矩形   #");
	xyprintf(400, 320, "###############");
	xyprintf(400, 340, "#     移动    #");
	xyprintf(400, 360, "#    w.上移   #"); 
	xyprintf(400, 380, "#    x.下动   #");
	xyprintf(400, 400, "#    a.左动   #");
	xyprintf(400, 420, "#    d.右动   #");
	xyprintf(400, 440, "###############");
	xyprintf(400, 460, "#     缩放    #");
	xyprintf(400, 480, "#     -.缩    #");
	xyprintf(400, 500, "#     +.放    #");
	xyprintf(400, 520, "###############");
	xyprintf(400, 540, "#   q.退出    #");
	xyprintf(400, 560, "# space.暂停  #");
	xyprintf(400, 580, "###############");
}

void test2()
{
	initgraph(1000, 800, INIT_RENDERMANUAL);//创建窗口 
	setbkcolor(WHITE);
	setcolor(BLACK);
	setfont(40, 0, "楷体");
	
	MUSIC music;
	music.OpenFile("雷军 - Are You OK.mp3");
	xyprintf(0, 0, "%s\n", music.IsOpen() ? "音乐打开成功 q:退出  m:菜单" : "音乐打开失败");
	music.Play();//music.Play(开始时间, 结束时间);
	menu();
	
	B b2(350,300,650,500);
	C c2(500, 400, 100);
//	G *p[2];
//	p[0] = &b2;
//	p[1] = &c2;
	vector<G*> V;
	V.push_back(&b2);
	V.push_back(&c2);
	
	int exit = 1;
	int n = 0;
	
	while(exit)
	{
		key_msg keyMsg = getkey();
		DWORD status = music.GetPlayStatus();
		char key = keyMsg.key;
		switch (key) 
		{
			case 'q':
				exit = 0;
				break;
			case ' ':
				if (status == MUSIC_MODE_PLAY)
					music.Pause();
				else if (status == MUSIC_MODE_PAUSE)
					music.Play();
				else if (status == MUSIC_MODE_STOP)
					music.Play(0);
				break;
			case 'm':
				cleardevice();
				menu();
				break;
			case 'b':
				b2.display();
				n = 0;
				break;
			case 'c':
				c2.display();
				n = 1;
				break;
			
			case 'w':
				V[n]->move(0, -100);
//				c2.move(0, -100);
				break;
			case 's':
				V[n]->move(0, 100);
//				c2.move(0, 100);
				break;
			case 'a':
				V[n]->move(-100, 0);
//				c2.move(-100, 0);
				break;
			case 'd':
				V[n]->move(100, 0);
//				c2.move(100, 0);
				break;
			case '-':
				V[n]->scale(-1.0);
//				b2.scale(0.5);
				break;
			case '+':
				V[n]->scale(1.0);
//				b2.scale(2);
				break;
			default:
				cout << "please agen!!!" << endl;
		}
	}
	music.Close();
}
