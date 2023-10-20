package com.zhouzixin.homework3;

public class PhoneBookItem{
	public  String name;
	public  String workplace;
	public  String post;
	public  String homenumver;
	public  String mobiletelnumber;
	public  String officetelnumber;

	public  PhoneBookItem(String name,String workplace,String post,String mobiletelnumber,String officetelnumber,String homenumver){
		this.name=name;
		this.workplace=workplace;
		this.post=post;
		this.mobiletelnumber=mobiletelnumber;
		this.officetelnumber=officetelnumber;
		this.homenumver=homenumver;
	}

	//相应get方法
	public String getName(){
		return this.name;
	}
	public String getWorkplace(){
		return this.workplace;
	}
	public String getPost(){
		return this.post;
	}
	public String getMobiletelnumber(){
		return this.mobiletelnumber;
	}
	public String getOfficetelnumber(){
		return this.officetelnumber;
	}
	public String gethomenumver(){
		return this.homenumver;
	}
	

	//相应set方法
	public void setName(String name){
		this.name=name;
	}
	public void setWorkplace(String workplace){
		this.workplace=workplace;
	}
	public void setPost(String post){
		this.post=post;
	}
	public void setMobiletelnumber(String mobiletelnumber){
		this.mobiletelnumber=mobiletelnumber;
	}
	public void setOfficetelnumber(String officetelnumber){
		this.officetelnumber=officetelnumber;
	}
	public void sethomenumver(String homenumver){
		this.homenumver=homenumver;
	}

}