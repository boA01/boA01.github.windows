package com.ATM.vo;

import java.util.Scanner;

public class Test {
    Scanner sc = new Scanner(System.in);
    ATM a = new ATM();

    public void menu1(){
        System.out.println("########菜单#########\n"+
                "#      0.退出       #\n"+
                "#      1.登录       #\n"+
                "####################\n"+
                "你的选择：");
    }

    public void menu2(){
        System.out.println("########菜单#########\n"+
                "#      0.退出       #\n"+
                "#      a.存钱       #\n"+
                "#      b.取钱       #\n"+
                "#      c.转账       #\n"+
                "#      d.改密       #\n"+
                "#      e.挂失       #\n"+
                "#      f.注销       #\n"+
                "####################\n"+
                "你的选择：");
    }

    public void login(){
        while(true){
            menu1();

            boolean b = false;
            char c = sc.next().charAt(0);

            switch (c) {
                case '0':
                    System.out.println("Bye");
                    break;
                case '1':
                    System.out.println("请输入账号：");
                    People p = a.getUser(sc.next());
                    if(p != null){
                        for (int i = 0; i < a.getN(); i++){
                            System.out.println("请输入密码：");
                            String pwd = sc.next();
                            if(p.getPassWorld().equals(pwd)){
                                System.out.println("登录成功");
                                b = true;
                                break;
                            }
                        }
                        if (b){
                            System.out.println(p);
                            service(p);
                        }
                        else {
                            System.out.println("三次错误，账号冻结！！！");
                            p.setStatus(0);
                        }
                        break;
                    }
                    else
                        System.out.println("账号错误！！！");
                    break;
                default:
                    System.out.println("输入错误！！！");
                    break;
            }
        }
    }

    public void service(People p){
        while(true){
            menu2();
            char c = sc.next().charAt(0);
            switch(c){
                case '0':
                    System.out.println("Bye");
                    return;
                case 'a':
                    System.out.println("存入金额：");
                    float f1 = sc.nextFloat();
                    p.setMoney(p.getMoney()+f1);
                    System.out.println("存款成功");
                    System.out.println(p);
                    break;
                case 'b':
                    System.out.println("领取金额：");
                    float f2 = sc.nextFloat();

                    if(f2<p.getMoney()){
                        p.setMoney(p.getMoney()-f2);
                        System.out.println("领取成功");
                    }
                    else{
                        System.out.println("余额不足，领取失败！！");
                    }
                    System.out.println(p);
                    break;
                case 'c':
                    System.out.println("转账账号：");
                    People p1 = a.getUser(sc.next());
                    if (p1 != null && p1.getId() != p.getId()){
                        System.out.println("转账金额：");
                        float f3 = sc.nextFloat();
                        if(f3<p.getMoney()) {
                            p.setMoney(p.getMoney()-f3);
                            p1.setMoney(p1.getMoney()+f3);
                            System.out.println("转账成功");
                        }
                        else {
                            System.out.println("余额不足，转账失败！！");
                        }
                        System.out.println(p);
                    }
                    else
                        System.out.println("账号错误！！！");
                    break;
                case 'd':
                    System.out.println("输入密码：");
                    String pwd1 = sc.next();
                    System.out.println("确认密码：");
                    String pwd2 = sc.next();
                    if(pwd1.equals(pwd2)){
                        p.setPassWorld(pwd2);
                        System.out.println("修改成功");
                    }
                    else
                        System.out.println("修改失败！！！");
                    break;
                case 'e':
                    p.setStatus(0);
                    System.out.println("挂失成功");
                    break;
                case 'f':
                    a.popUser(p);
                    System.out.println("注销成功");
                    break;
                default:
                    System.out.println("输入错误！！！");
                    break;
            }
        }
    }
}
