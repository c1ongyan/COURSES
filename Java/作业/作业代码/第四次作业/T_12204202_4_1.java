import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.Optional;


public class T_12204202_4_1 {
    public static void main(String[] args) throws Exception{
        FileManager a = new FileManager("intfile1.txt");
        FileWriter c = new FileWriter("intfile2.txt");

        String aWordsum = null;

        while ((aWordsum = a.nextlinesum())!=null){
            c.write(aWordsum+"\n");
        }

        c.close();

    }
}


class FileManager{

    String[] words = null;

    int pos = 0;


    public FileManager(String pathe)throws Exception{
        //传入文件路径,new File 对象
        File f = new File(pathe);
        //new FileReder对象,获取文件内容
        FileReader reader = new FileReader(f);
        //length()方法获取文件的长度
        char[] buf= new char[(int)f.length()];
        //将读取到的字符写入buf,并返回长度
        int len = reader.read(buf);
        // 通过使用平台的默认字符集解码指定的 byte 子数组，构造一个新的 String。
        String results = new String (buf,0,len);

        //最后将每一行拆分到words数组中
        words=results.split("\r|\n|\r\n");

    }

    //读取下一行
    public String nextlinesum(){
        if(pos == words.length){
            return null;
        }
        else{
            if (words[pos]==""){  //由于拆分后每一行的分隔在数组words占一个""的位置，故要略过
                pos++;
            }
            int sum=0;
            String[] temp=words[pos++].split(" ");
            for(int i=0;i<temp.length;i++){
                
                int foo;

                try{
                    foo=Integer.parseInt(temp[i]);
                }
                catch (NumberFormatException e) {
                    foo=0;
                }
                System.out.print(temp[i]+"*");
                sum+=foo;
            }
           return Integer.toString(sum);
        }

    }
}