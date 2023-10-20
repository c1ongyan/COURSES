import java.io.*;

public class test8_4{
	public static void main(String[] args){
		double r=4.0d;
		String str="this is test";
		try(DataOutputStream dos=new DataOutputStream(new FileOutputStream("a.data"));
			DataInputStream dis=new DataInputStream(new FileInputStream("a.data"))){

			dos.writeDouble(r);
			dos.writeUTF(str);
			dos.close();

			double tempR=dis.readDouble();
			String tempStr=dis.readUTF();
			System.out.printf("r=%f,str=%s",tempR,tempStr);



		}catch(IOException e){
			System.out.println("io error");
			e.printStackTrace();//输出栈区情况
		}
	}
}