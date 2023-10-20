import java.util.Scanner;
public class T_12204202_2_1{
		public static void main(String[] args){
			System.out.print("输入创建矩阵的行列数\n");
			Scanner sc=new Scanner(System.in);
			int row=sc.nextInt();
			int col=sc.nextInt();
			MatrixType M1=new MatrixType(row,col);
			M1.InputData();
			M1.OutputData();
			M1.LineAvg();
			M1.Trans();
			M1.OutputData();
		}

}

class MatrixType{
	public int row;
	public int col;
	public int[][] Matrix;
	public MatrixType(){ //不带参数构造函数
		this.row=3;
		this.col=3;
		this.Matrix=new int[3][3];
	}

	public MatrixType(int x,int y){ //带参数构造函数
		this.row=x;
		this.col=y;
		this.Matrix=new int[x][y];
	}

	public void InputData(){
		Scanner sc=new Scanner(System.in);
		int x=this.row;
		int y=this.col;
		System.out.print("请输入"+x+"行"+y+"列的矩阵值\n");
		for(int i=0;i<x;i++){
			for(int j=0;j<y;j++){
				this.Matrix[i][j]=sc.nextInt();
			}
		}
	}

	public void OutputData(){
		System.out.print("当前矩阵数据为\n");
		int x=this.row;
		int y=this.col;
		for(int i=0;i<x;i++){
			for(int j=0;j<y;j++){
				System.out.print(this.Matrix[i][j]+"\t");
			}
			System.out.print("\n");
		}
	}

	public void Trans(){
		int x=this.row;
		int y=this.col;
		int[][] Matrix_T=new int[y][x];
		for(int i=0;i<y;i++){
			for(int j=0;j<x;j++){
				Matrix_T[i][j]=this.Matrix[j][i];
			}
		}
		this.Matrix=Matrix_T;
		this.row=y;
		this.col=x;
		System.out.print("矩阵转置成功\n");
	}

	public void LineAvg(){
		int x=this.row;
		int y=this.col;
		for(int i=0;i<x;i++){
			int tmp=0;
			for(int j=0;j<y;j++){
				tmp+=this.Matrix[i][j];
			}
			System.out.print("第"+i+"行的平均值为"+tmp/y+"\n");
			tmp=0;
		}
	}
}