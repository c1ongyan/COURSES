//多线程


//继承thread类重写类方法

class EvenOdd extends Thread{
	private int i0;
	private int m;

	public EvenOdd(int first,int order){
		i0=first;
		m=order;
	}

	//	重写run方法
	public void run(){
		for(int i=i0;i<=100;i+=2){
			System.out.println("in the "+m+"thread :"+i);
		}
	}
}

public class test10
{   public static void main(String[] args)       
    { 
         EvenOdd ot = new EvenOdd(1,1);//创建线程
         EvenOdd et = new EvenOdd(0,2);
         ot.start();//启动线程
         et.start();
        System.out.println("Main thread done");

    }
}