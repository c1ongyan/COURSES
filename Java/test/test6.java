import java.io.IOException;
public class test6{
	public static void main(String[] args){
		byte[] b;
		int i=0,result=0;
		System.out.println("please input an int digital");
		while(true){
			b=new byte[5];
			try{
				System.in.read(b);//IOException
				i=Integer.parseInt((new String(b).trim()));//NumberFormatException
				result=25/i;//ArithmeticException
				System.out.println("25/i is:"+result);
				break; 
			}catch(IOException e){
				System.out.println("io error");
			}catch(NumberFormatException e1){
				System.out.println("NumberFormat error");
			}catch(ArithmeticException e2){
				System.out.println("Arithmetic error");
			}
		}
	}
}