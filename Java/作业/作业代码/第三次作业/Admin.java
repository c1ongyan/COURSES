package com.zhouzixin.homework3;

public class Admin {
    private String name="admin";           //姓名
    private String password="123456";      //密码
    
    void setName(String name) {
        this.name=name;
    }
    void setPassword(String password) {
        this.password=password;
    }
    
    
    String getName() {
        return this.name;
    }
    String getPassword() {
        return this.password;
    }
}
