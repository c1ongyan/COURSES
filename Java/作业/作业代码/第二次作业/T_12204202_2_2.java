interface ShapeArea{
	public double getArea();
	public double getPerimeter();
}

class MyRectangle implements ShapeArea{
	double width;
	double height;
	public MyRectangle(double w,double h){
		this.width=w;
		this.height=h;
	}

	public double getArea(){
		return this.width*this.height;
	}

	public double getPerimeter(){
		return 2*(this.width+this.height);
	}

	public String toString(){
		return ("width="+this.width+",height="+this.height+",perimeter="+getPerimeter()+", area="+getArea());
	}
}

public class T_12204202_2_2{
	 public static void main(String[] args){
		MyRectangle rg=new MyRectangle(21.2,45.56);
		System.out.print(rg.toString());
	}
}