//常用类 
import java.lang.Math;


public class test7{
	public static void change(String str,int x,char[] c){
		str="changed";
		x=6666;
		c[0]='C';
	}

	public static void main(String args[]){

		//String类
		int x=1;
		String str1="abc";
		String str2="aaa";
		String str3="abc";
		char c[]={'z','z','x'};
		//str1="cccc";
		change(str2,x,c);
		System.out.println("str1="+str1);
		System.out.println("str2="+str2);
		System.out.println("str3="+str3);
		System.out.println("x="+x);
		System.out.println(c);
		System.out.println(str1.equals(str3));
		System.out.println(str1==str3);//str1和str3指向同一堆


/*

		//封装类
		//int和字符串的转化
		int num=10;
		String str4=Integer.toString(num);//可以按一定进制转换
		int num2=Integer.valueOf("5");
		System.out.println(str4);
		System.out.println(num2);

		//math
		int a=Math.pow(1.1,2.1);
		System.out.println(a);
*/
		
	}
}