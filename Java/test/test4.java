//内部类

/*
public class test4 {
    class Destination {
        private String label;
        Destination(String whereTo) {
            label = whereTo;
        }
        String readLabel() {
            ship("test");
            return label;
        }
    } 
    // 在类的的函数中使用内部类,与使用普通类没多大区别
    public void ship(String dest) {
        Destination d = new Destination(dest);
        System.out.println(d.readLabel());
    }

    public static void main(String[] args) {
        test4 p = new test4();
        p.ship("Hello");
    }
}
*/
///*
public class test4{//这里外部类的权限修饰符只能使用public或者默认
	int bl1=4;
	private String bl2="zzx";
	public int bl3=5;
	static int bl4=6;
	private class Inner{//内部类不能与外部类同名
		private int x=1;
		public int y=2;

		final static double constnum=3.14;//实例内部类中想要创建static静态变量必需要带上final


		public void viewOut(){
			System.out.println(bl1);//内部类能访问各种访问类型的外部类成员
			System.out.println(bl2);
			System.out.println(bl3);
			System.out.println(bl4);
			System.out.println(test4.this.bl1);//对外部类用this需要 外部类.this
			System.out.println(this.x);//对内部类成员用this 直接用
		}
	}

	public void tryin(){
		System.out.println(Inner.constnum);//内部类的static变量可通过类名.成员名访问
		Inner in=new Inner();
		System.out.println(in.x);          //内部类的其他成员可通过实例访问，任何权限都可,不论是成员的还是类的
		System.out.println(in.y);
		System.out.println(in.constnum);
	}

	public static void main(String[] args){
		Inner in1=new test4().new Inner();//静态方法访问内部类需要创建实例
		in1.viewOut();
		System.out.println(in1.x); 
		test4 out1=new test4();
		out1.tryin();
		int mm=567;
		System.out.println(mm);

	}
}
//*/