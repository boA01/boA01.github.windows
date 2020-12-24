package com.ATM.vo;

public class People {
    private String name;
    private char sex;
    private String id;
    private String pwd;
    private float money;
    private int status;

    public People(){}

    public People(String name, char sex, String id, String pwd, float money, int status) {
        this.name = name;
        this.sex = sex;
        this.id = id;
        this.pwd = pwd;
        this.money = money;
        this.status = status;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public char getSex() {
        return sex;
    }

    public void setSex(char sex) {
        this.sex = sex;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getPassWorld() {
        return pwd;
    }

    public void setPassWorld(String pwd) {
        this.pwd = pwd;
    }

    public float getMoney() {
        return money;
    }

    public void setMoney(float money) {
        this.money = money;
    }

    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }

    @Override
    public String toString() {
        return "People{" +
                "姓名='" + name + '\'' +
                ", 性别=" + sex +
                ", 卡号='" + id + '\'' +
//                ", 密码='" + pwd + '\'' +
                ", 金额=" + money +
                ", 状态=" + status +
                '}';
    }
}
