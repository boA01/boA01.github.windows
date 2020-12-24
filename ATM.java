package com.ATM.vo;

public class ATM {
    final int N = 10;
    private People[] users = new People[N];
    private int n = 3;

    public ATM(){
        users[0] = new People("fff",'男',"123456","123",999.9f,1);
        users[1] = new People("ggg",'男',"124356","123",999.9f,1);
        users[2] = new People("hhh",'女',"123654","123",999.9f,1);
    }

    public void setN(int n){
        this.n += n;
    }

    public int getN(){
        return this.n;
    }

    public People getUser(String s){
        for (int i= 0;i < n; i++)
            if(this.users[i].getId().equals(s) && this.users[i].getStatus()==1)
                return this.users[i];
        return null;
    }

    public void popUser(People p){
         p.setStatus(0);
        this.n--;
    }
}

/*
     public String toString(){
         for(People i:this.users){
             System.out.println(i);
         }
     }

    void stopUser(People p){
        p.setStatus(0);
    }

     private void addUser(People user) {
         if(this.n<this.N){
             this.users[this.n] = new People();
             this.users[this.n] = user;
         }
         else
             System.out.println("is Full!!!");
     }
    public void addOperate(People p, float f){
        p.setMoney(p.getMoney()+f);
    }

    public void subOperate(People p, float f){
        p.setMoney(p.getMoney()-f);
    }

    public void sendOperate(People p1, People p2, float f){
        subOperate(p1,f);
        addOperate(p2,f);
    }

    public void rePwd(People p, String pwd){
        p.setPassWorld(pwd);
    }

 */