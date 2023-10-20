package com.zhouzixin.homework3;

import java.util.ArrayList;
import javax.swing.table.AbstractTableModel;

public class PhoneBook {
	
	public static ArrayList<PhoneBookItem> BookList=new ArrayList<PhoneBookItem>();

	
	
	public PhoneBook() {
		//PhoneBookItem item1=new PhoneBookItem("周子欣","cumt","student","10086994444","16551","11555");
		//PhoneBookItem item2=new PhoneBookItem("小袁","cumt","student","15555594444","16551","54615");
		//BookList.add(item1);
		//BookList.add(item2);
		
	}
	
	//初始化
	public void init() {
		BookList.add(new PhoneBookItem("周子欣","cumt","student","10086994444","16551","11555"));
		BookList.add(new PhoneBookItem("小喻","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小袁","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小k","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小l","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小明","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小我","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小为","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小发","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小韬","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小普","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小人","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小黄","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小艾","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小兰","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小南","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小北","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小6","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小7","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小8","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小9","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小10","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小11","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小1","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小2","cumt","student","15555594444","16551","54615"));
		BookList.add(new PhoneBookItem("小3","cumt","student","15555594444","16551","54615"));
	}
	
	//追加
	public void add(String name,String workplace,String post,String mobiletelnumber,String officetelnumber,String homenumver) {
		PhoneBookItem item=new PhoneBookItem(name,workplace,post,mobiletelnumber,officetelnumber,homenumver);
		BookList.add(item);
	}
	
	//删除
	public void del(int index) {
		BookList.remove(index);
	}
	
	//修改
	public void modify(int index,PhoneBookItem item) {
		BookList.set(index,item);
	}
	
	//插入
	public void insert(int index,String name,String workplace,String post,String mobiletelnumber,String officetelnumber,String homenumver) {
		PhoneBookItem item=new PhoneBookItem(name,workplace,post,mobiletelnumber,officetelnumber,homenumver);
		BookList.add(index,item);
	}
		
}

class CustomModel extends AbstractTableModel {
	
	PhoneBook pb=new PhoneBook();
	ArrayList<PhoneBookItem> data = pb.BookList;
	//ArrayList<PhoneBookItem> BookList2=
    String[] columnNames = {"姓名", "工作单位","职务","手机号码","办公室电话","住宅电话"};
    
    public CustomModel() {
    	//data.add(new PhoneBookItem("周子欣","cumt","student","10086994444","16551","11555"));
    	//data.add(new PhoneBookItem("小袁","cumt","student","15555594444","16551","54615"));
    }
    
    public String getColumnName(int column) {
        return columnNames[column];
    }

    @Override
    public int getColumnCount() {
        return 6;
    }

    @Override
    public int getRowCount() {
        return data.size();
    }

    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
    	PhoneBookItem pbi = data.get(rowIndex);
        switch (columnIndex) {
        case 0:
            return pbi.getName();
        case 1:
            return pbi.getWorkplace();
        case 2:
            return pbi.getPost();
        case 3:
            return pbi.getMobiletelnumber();
        case 4:
            return pbi.getOfficetelnumber();
        case 5:
            return pbi.gethomenumver();
        default:
            return null;
        }
    }

}
