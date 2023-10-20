public class T_12204202_1_2 {
public static void main(String[] args) {
	int max = 5;
	new T_12204202_1_2().p(max,max);
}
void p(int i,int m){
	if(i>0){
		p(i-1,m);
		String s = "";
		for(int k=0; k<i; k++)
			s+=k+1+" ";
		System.out.println(s);
		}
}
}