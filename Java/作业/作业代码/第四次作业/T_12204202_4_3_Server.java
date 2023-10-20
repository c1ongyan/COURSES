//T_12204202_4_3_Server

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;
 
 
import java.io.*;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
 

public class T_12204202_4_3_Server {
 
    public static void main(String[] args) {
 
        try {
            //1、创建一个服务器端Socket,即ServerSocket, 指定绑定的端口，并监听此端口
            ServerSocket serverSocket = new ServerSocket(8888);
            Socket socket = null;
            //记录客户端的数量
            int count = 0;
            System.out.println("***服务器即将启动，等待客户端的链接***");
            //循环监听等待客户端的链接
            while (true){
                //调用accept()方法开始监听，等待客户端的链接
                socket = serverSocket.accept();
                //创建一个新的线程
                ServerThread serverThread = new ServerThread(socket);
                //启动线程
                serverThread.start();
 
                count++; //统计客户端的数量
                System.out.println("客户端的数量: " + count);
                InetAddress address = socket.getInetAddress();
                System.out.println("当前客户端的IP ： " + address.getHostAddress());
            }
 
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

 
//服务器端线程处理类
class ServerThread extends Thread {
 
    //和本线程相关的Socket
    Socket socket = null;
    public ServerThread(Socket socket){
        this.socket = socket;
    }
 
    //线程执行的操作，响应客户端的请求
    public void run(){
 
        InputStream is = null;
        InputStreamReader isr = null;
        BufferedReader br = null;
 
        OutputStream os = null;
        PrintWriter pw = null;
        try {
 
            //获取一个输入流，并读取客户端的信息
            is = socket.getInputStream();
            isr = new InputStreamReader(is); //将字节流转化为字符流
            br = new BufferedReader(isr); //添加缓冲
            String info = null;
            //循环读取数据
            while ((info = br.readLine()) != null){
                System.out.println("我是服务器，客户端说: " +info);
            }
 
            socket.shutdownInput(); //关闭输入流
 
            //获取输出流，响应客户端的请求
            os = socket.getOutputStream();
            pw = new PrintWriter(os); //包装为打印流
            pw.write("欢迎你");
            pw.flush();  //将缓存输出
 
 
        } catch (IOException e) {
            e.printStackTrace();
        }finally {
 
 
                try {
                    //关闭资源
                    if (pw != null)
                        pw.close();
                    if (os != null)
                        os.close();
                    if (is != null)
                        is.close();
                    if (isr != null)
                        isr.close();
                    if (br != null)
                        br.close();
                    if (socket != null)
                        socket.close();
                } catch (IOException e) {
                    e.printStackTrace();
 
                }
 
        }
 
 
 
    }
}