//字节流
import java.io.*;

/*
public class test8{
	public static void main(String[] args){

		try{
			//InputStream流的用法
		FileInputStream fi=new FileInputStream("file1.txt");

		int size=fi.available();
		byte[] b=new byte[size];
		fi.read(b); //常用用法  int read(byte[] b)
		fi.close();

		FileOutputStream fo=new FileOutputStream("file2.txt");
		fo.write(b);//void write(byte b[])
		fo.close();
	}catch(IOException e){
		System.out.print("IO error");
	}

	}
}
*/

//上下两种异常处理方式都可以

public class test8{
	public static void main(String[] args) throws IOException{


			//InputStream流的用法
		FileInputStream fi=new FileInputStream("file1.txt");

		int size=fi.available();
		byte[] b=new byte[size];
		fi.read(b); //常用用法  int read(byte[] b)
		fi.close();

		FileOutputStream fo=new FileOutputStream("file2.txt");
		fo.write(b);//void write(byte b[])
		fo.close();

	}
}





