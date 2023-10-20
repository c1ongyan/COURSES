//过滤流
import java.io.*;
public class test8_3{
	public static void main(String[] args){
		System.out.println("input");
	try(BufferedReader bufr =new BufferedReader(new FileReader("file2.txt"));
		BufferedWriter bw=new BufferedWriter(new FileWriter("a.txt"));){
		char[] ch=new char[1024];
		bufr.read(ch);
		String str=new String(ch);
		System.out.print(str);
		//String str=null;
		while((str=bufr.readLine())!=null&&str.length()>0){
			bw.write(str);
			bw.newLine();
		}
		bw.flush();
		System.out.println("ending");
	}catch(IOException e){
		System.out.println(e.getMessage());
	}
	}
}