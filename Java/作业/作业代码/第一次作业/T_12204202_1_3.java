public class T_12204202_1_3{
	public static void main(String[] args){
		int[] arr=new int[100];
		for(int i=1;i<=100;i++){
			arr[i-1]=i;
			//System.out.print(arr[i-1]);
		}
		arr[0]=0;
		for(int j=2;j<=10;j++){
			int k=2;
			while(k*j<=100){
				arr[k*j-1]=0;
				k++;
			}
		}
		for(int i=0;i<=arr.length-1;i++){
			if(arr[i]!=0)
				System.out.print(arr[i]+"\t");
		}
	}
}
