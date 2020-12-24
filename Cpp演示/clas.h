class G
{
	public:
		G(int, int);
		virtual void display();
		virtual void move(int x, int y);
		virtual void scale(float n);
		
		int m_x, m_y;
		
};

class C : public G
{
	public:
		C(int, int, int);
		~C();
		void display();
		void move(int, int);
		void scale(float);
		
		int m_r;
};

class B : public G
{
	public:
		B(int, int , int , int);
		~B();
		void display();
		void move(int, int);
		void scale(float);
	
		int m_x1, m_y1;
};
