public class T_12204202_1_1{
	public static void main(String[] args){
		int cnt=0;
		for(int i=1;i<5;i++){
			for(int j=1;j<5;j++){
				for(int k=1;k<5;k++){
					if(i!=j&&i!=k&&j!=k){
						int num=i*100+j*10+k;
						cnt++;
						System.out.print(num+"\t");
						if(cnt==4){
							System.out.print("\n");
							cnt=0;
						}
					}
				}
			}
		}
	}
}