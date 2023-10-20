//接口和接口实现


interface A{//实际上 public abstract
	int key=1;//public static final int key=1
	void show();//public abstract void show()
}

interface B{
	int bkey=2;
	void show();
}

class test3 implements A,B{
	public void show(){ //必需加上public
		//key=2;  不合法key为final变量
		System.out.println(key);
		System.out.println(bkey);
	}
	public static void main(String[] args){
		test3 t1=new test3();
		t1.show();
	}
}