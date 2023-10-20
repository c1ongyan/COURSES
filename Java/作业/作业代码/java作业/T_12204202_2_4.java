import java.util.Arrays;
import java.util.Scanner;

public class T_12204202_2_4{
	public static int Search(String S){
		int len=S.length();
		int MaxLen=0;
		if(len<=1) return 1;
		String[] strs=new String[len];
		for(int i=0;i<len;i++){
			strs[i]=S.substring(i,i+1);
		}
		int tmp=1;
		//System.out.print(Arrays.toString(strs));
		for(int i=0;i<len-1;i++){
			int result=strs[i].compareTo(strs[i+1]);
			if(result==0){
				tmp++;
			}
			else{
				tmp=1;
			}
			if(tmp>=MaxLen) MaxLen=tmp;
		}
		return MaxLen;
	}

	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
		String str=sc.next();
		//System.out.print(str+"\n");
		System.out.print("最长重复子段的长度为"+Search(str));

	}
}