class EvenOdd implements Runnable{
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

public class test10_2
{   public static void main(String[] args)          
    { 
     
        Thread t1 = new Thread(new EvenOdd(1,1));
        Thread t2 = new Thread( new EvenOdd(0,2));
         t1.start();
         t2.start();
}
}