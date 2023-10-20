//字符流

import java.io.*;
public class test8_2{
	public static void main(String[] args) throws IOException {
		FileReader fr=new FileReader("file1.txt");

		char[] buf=new char[1024];
		int len=0;

		len=fr.read(buf);//int read(char[] ch)

		fr.close();

		FileWriter fw=new FileWriter("file3.txt");

		fw.write(buf);//void write(char[] ch)

		fw.close();





	}
}
