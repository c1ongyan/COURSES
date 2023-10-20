import java.util.Scanner;

public class T_12204202_1_4 {
    public static void main(String[] args){
        // 输入系数
        System.out.print("请依次输入一元三次方程ax3+bx2+cx+d=0的系数a,b,c,d:");
        Scanner sc = new Scanner(System.in);
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double c = sc.nextDouble();
        double d = sc.nextDouble();
        T_12204202_1_4 t=new T_12204202_1_4();
        if(IsDangDiao(a,b,c,d)){
            System.out.print("使用二分法求根输入1,使用牛顿迭代法输入2,输入其他退出:");
            int mode =sc.nextInt();
            if(mode==1){
                t.ErFeng(a,b,c,d);
            }
            else if(mode==2){
                t.NewTon(a,b,c,d);
            }

        }
        
        

    }
    public static boolean IsDangDiao(double a, double b, double c, double d){
        System.out.print("请输入用于判断单调性的x1,x2:");
        Scanner sc2 = new Scanner(System.in);
        double x1 = sc2.nextDouble();
        double x2 = sc2.nextDouble();
        if(f(x1,a,b,c,d)*f(x2,a,b,c,d)<0){
            System.out.print("该函数的根存在\n");
            return true;
        }   
        else{
            System.out.print("该函数的根可能不存在\n");
            return false;
        }
    }

    public static double f(double x, double a, double b, double c, double d){
        return a*x*x*x + b*x*x + c*x + d;
    }

    public static double fi(double x, double a, double b, double c, double d){
        return 3*a*x*x + 2*b*x + c;
    }

    public double ErFeng(double a,double b,double c,double d){
        System.out.print("输入近似根区间x1,x2:");
        Scanner sc2 = new Scanner(System.in);
        double x1 = sc2.nextDouble();
        double x2 = sc2.nextDouble();
        while (Math.abs(f(x1,a,b,c,d))>1e-5) {
            double xx = (x1 + x2) / 2;
            if (f(xx, a, b, c, d) * f(x1, a, b, c, d) < 0) {
                x2 = xx;
            } else {
                x1 = xx;
            }
            }
            // x1是根
        System.out.print("用二分法求出的近似根x1为"+x1+"\n");
        return 0;
    }

    public double NewTon(double a,double b,double c,double d){
        System.out.print("输入初始测试根值x0:");
        Scanner sc3 = new Scanner(System.in);
        double x1=sc3.nextDouble();
        double q=fi(x1,a,b,c,d);
        double p=f(x1,a,b,c,d)-fi(x1,a,b,c,d)*x1;
        double x2=-p/q;
        while(Math.abs(x2-x1)>1e-5){
            x1=x2;
            q=fi(x1,a,b,c,d);
            p=f(x1,a,b,c,d)-fi(x1,a,b,c,d)*x1;
            x2=-p/q;
        }
        System.out.print("用牛顿迭代法求出的近似根x1为"+x1+"\n");
        return 0;
    }

}


