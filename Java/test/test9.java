import java.awt.*;
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class test9{
	public static void main(String[] args){
		JFrame jf=new JFrame("test");
		jf.setBounds(400,400,400,400);

		JButton jb1=new JButton("按钮1");
		JButton jb2=new JButton("按钮2");

		//JFrame 默认Border布局

		//更改布局

		jf.setLayout(new FlowLayout(FlowLayout.CENTER,50,20));
		//jb1.setSize(30,40);
		//jb2.setSize(30,40);
		
		JLabel jl=new JLabel("输入");
		JTextField jt1=new JTextField(25);

		JLabel jl2=new JLabel("结果");

		JTextField jt2=new JTextField(25);


		jf.add(jl);
		jf.add(jt1);
		jf.add(jl2);
		jf.add(jt2);

		//jf.add("South",jb1);
		//jf.add("South",jb2);
		jf.add(jb1);
		jf.add(jb2);

		//监听事件
		jb1.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e){
				String input=jt1.getText();
				jt2.setText(input);

			}
		});

		jf.setVisible(true);

	}
}
