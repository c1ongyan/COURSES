class a{
	int i=4,j=1;
	a(){
		//this.i=m;
		//this.j=n;
		System.out.println("a构造函数调用");
	}

	void tostring(){
		System.out.println("i="+i);
		System.out.println("j="+j);
	}
}

class B extends a{
	int k=3;
	int j=2;
	//B(int x,int y){
	//	//super(x,y);
	//	this.k=x;
	//	this.i=y;
	//	System.out.println("b构造函数调用");
	//}
	//void tostring(){
	//	System.out.println("k="+k);
	//	System.out.println("j="+j);
	//	//super.tostring();
	//}
	
}

class test2{
	public static void main(String[] args){
		a a1=new B();
		B b1=new B();
		b1.tostring();
		System.out.println(a1.j);
	}
}

