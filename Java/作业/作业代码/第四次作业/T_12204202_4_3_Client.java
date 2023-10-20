//T_12204202_4_3_Client
 
import java.io.*;
import java.net.Socket;

public class T_12204202_4_3_Client {
 
    public static void main(String[] args) {
 
        try {
            //1、创建客户端Socket，指定服务器端口号和地址
            Socket socket = new Socket("localhost",8888);
            //2、获取输出流,向服务器发送信息
            OutputStream os = socket.getOutputStream(); //字节输出流
            PrintWriter pw  = new PrintWriter(os); //将输出流包装为打印流
            pw.write("用户名:tom; 密码：456");
            pw.flush();
            socket.shutdownOutput(); //关闭输出流
 
            InputStream is = socket.getInputStream();
            InputStreamReader isr = new InputStreamReader(is);
            BufferedReader br = new BufferedReader(isr);
 
            String info = null;
            //循环读取
            while ((info = br.readLine()) != null){
                System.out.println("我是客户端:服务器说:" + info);
            }
 
            br.close();
            is.close();
            isr.close();
 
 
            pw.close();
            os.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}