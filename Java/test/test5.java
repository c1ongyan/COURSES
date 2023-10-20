//静态内部类

class Out{
	int oa=3;
	static int ob=4;

	static class StaticInner{
		int a=1;
		static int b=2;

		static void show(){
			//System.out.println(a); 静态方法中引用非静态变量需要实例对象
			System.out.println(b);
			System.out.println(ob);
			Out out1=new Out();
			System.out.println(out1.oa);
		}
	}

	public void show2(){
		System.out.println(Out.StaticInner.b);
		Out.StaticInner m=new Out.StaticInner();
		System.out.println(m.a);
	}
}

public class test5{
	public static void main(String[] args){
		Out.StaticInner m=new Out.StaticInner();
		//m.show();
		Out out1=new Out();
		out1.show2();
	}
}