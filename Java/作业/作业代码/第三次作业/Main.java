package com.zhouzixin.homework3;

import javax.swing.*;
//import java.awt.FlowLayout;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.BorderLayout;
//import java.awt.event.MouseListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;
import javax.swing.table.AbstractTableModel;

public class Main{

	public static void main(String[] args){
	//初始化电话簿
		 PhoneBook book=new PhoneBook();
		 book.init();
	//构建窗体 
		JFrame jf=new JFrame();
		jf.setSize(600,500);
		jf.setLocation(400,300);
		jf.setTitle("c1ongyan's gui");
		
		//底层画板
		JPanel panel=new JPanel();
		//设置为流布局
		//jf.setLayout(new FlowLayout());
		JPanel panel1=new JPanel();

		//设置登录，退出，输入，显示，删除,帮助按钮


		JButton jb_login=new JButton("登录");
		JButton jb_exit=new JButton("退出");
		jb_exit.setEnabled(false);
		JButton jb_input=new JButton("输入");
		jb_input.setEnabled(false);
		JButton jb_show=new JButton("显示");
		jb_show.setEnabled(false); 
		JButton jb_del=new JButton("删除");
		jb_del.setEnabled(false);
		JButton jb_help=new JButton("关于");

		panel1.add(jb_login);
		panel1.add(jb_exit);
		panel1.add(jb_input);
		panel1.add(jb_show);
		panel1.add(jb_del);
		panel1.add(jb_help);
		
		panel.add(panel1);
		jf.setContentPane(panel);
		
		//输入页面面板
		JPanel panel2=new JPanel(new GridLayout(7,2,2,8));
		JLabel name = new JLabel("姓名:");
		JLabel work = new JLabel("工作单位:");
		JLabel post = new JLabel("职务:");
		JLabel mobiletel = new JLabel("手机号码:");
		JLabel offtel = new JLabel("办公室电话:");
		JLabel hometel = new JLabel("住宅电话:");
		
		JTextField jT_1 = new JTextField();
		JTextField jT_2 = new JTextField();
		JTextField jT_3 = new JTextField();
		JTextField jT_4 = new JTextField();
		JTextField jT_5 = new JTextField();
		JTextField jT_6 = new JTextField();
		
		//字体
		name.setFont(new Font("宋体",Font.PLAIN,20));
		work.setFont(new Font("宋体",Font.PLAIN,20));
		post.setFont(new Font("宋体",Font.PLAIN,20));
		mobiletel.setFont(new Font("宋体",Font.PLAIN,20));
		offtel.setFont(new Font("宋体",Font.PLAIN,20));
		hometel.setFont(new Font("宋体",Font.PLAIN,20));
		
		//输入框大小
		//jT_1.setSize(new Dimension(60,240));
		jT_1.setPreferredSize(new Dimension(200,30));
		
		//按钮 确认 返回
		JButton jb_1=new JButton("确认");
		JButton jb_2=new JButton("返回");
		
		
		
		panel2.add(name);
		panel2.add(jT_1);
		panel2.add(work);
		panel2.add(jT_2);
		panel2.add(post);
		panel2.add(jT_3);
		panel2.add(mobiletel);
		panel2.add(jT_4);
		panel2.add(offtel);
		panel2.add(jT_5);
		panel2.add(hometel);
		panel2.add(jT_6);
		panel2.add(jb_1);
		panel2.add(jb_2);
		
		//显示页面面板
		JPanel panel3=new JPanel(new BorderLayout());
		
		CustomModel model = new CustomModel();
        JTable table = new JTable();
        table.setModel(model);
        //table.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);

        JScrollPane scorllPane=new JScrollPane(table,ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS,ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
        
        JButton jb_back=new JButton("返回");
        
        panel3.add(scorllPane,BorderLayout.CENTER);
        panel3.add(jb_back,BorderLayout.SOUTH);
        
        //删除页面面板
        JPanel panel4=new JPanel(new BorderLayout());
        JTable table2 = new JTable();
        table2.setModel(model);
        JScrollPane scorllPane2=new JScrollPane(table2,ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS,ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);

        //table.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);
        //table.setPreferredScrollableViewportSize(new Dimension(500,300));
        //JScrollPane scorllPane2=new JScrollPane(table2,ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS,ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
        
        JButton jb_delete=new JButton("删除");
        JButton jb_back2=new JButton("返回");
        
        panel4.add(scorllPane2,BorderLayout.CENTER);
        panel4.add(jb_delete,BorderLayout.SOUTH);
        panel4.add(jb_back2,BorderLayout.EAST);
        
        
        
		

		//监听事件，鼠标点击登录按钮进入登录界面
		jb_login.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e){
				JDialog jd_login=new JDialog(jf,"登录");
				jd_login.setBounds(450,350,500,400);

				JPanel panel=new JPanel();

				panel.setLayout(null);

				JLabel nameStr = new JLabel("用户名:");
        		nameStr.setBounds(120, 50, 100, 25);
        		nameStr.setFont(new Font("宋体",Font.PLAIN,15));
        		panel.add(nameStr);

        		JTextField username = new JTextField();
    		    username.setBounds(180, 52, 200, 22);
    		    panel.add(username);
        
        		JLabel passwordStr = new JLabel("密码:");
        		passwordStr.setBounds(120, 100, 100, 25);
        		passwordStr.setFont(new Font("宋体",Font.PLAIN,15));
        		panel.add(passwordStr);

    		    JPasswordField password = new JPasswordField();
    		    password.setBounds(180, 102, 200, 22);
    		    panel.add(password); 
    		    
    		    JButton jb_login2=new JButton("登录");
    		    jb_login2.setBounds(235,150,60,35);
    		    
    		    panel.add(jb_login2);
    		    
    		    JLabel tip = new JLabel("默认用户名:admin    默认密码:123456");
    		    tip.setBounds(150,150,300,100);
    		    panel.add(tip);
    		    

    		    jd_login.setContentPane(panel);
    		    
    		    jb_login2.addActionListener(new ActionListener() {
    		    	public void actionPerformed(ActionEvent e) {
    		    		String name = username.getText();
    	                String passwd = new String (password.getPassword());
    	                
    	                Admin admin=new Admin();
    	                if(name.equals(admin.getName())&&passwd.equals(admin.getPassword())) {
    	                	//弹出登录成功的窗口
    	                    JOptionPane.showMessageDialog(null, "登陆成功", "登陆成功", JOptionPane.NO_OPTION);
    	                    //点击确定后会跳转到主窗口
    	                	jd_login.dispose();
    	                }
    	                else {
    	                	//弹出账号或密码错误的窗口
    	                    JOptionPane.showMessageDialog(null, "账号或密码错误", "账号或密码错误", JOptionPane.WARNING_MESSAGE);
    	                    //清除密码框中的信息
    	                    password.setText("");
    	                    //清除账号框中的信息
    	                    username.setText("");
    	                }
    	                jb_del.setEnabled(true);
    	                jb_input.setEnabled(true);
    	                jb_show.setEnabled(true);
    	                jb_exit.setEnabled(true);
    		    		
    		    	}
    		    });

				jd_login.setVisible(true);
				jd_login.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
			}
		});
		
		//监听 输入按钮
		jb_input.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				panel.removeAll();
				panel.add(panel2);
				panel.validate();
				panel.repaint();
				//jf.setContentPane(panel2);
			}
		});
		
		jb_help.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				JOptionPane.showMessageDialog(null,"作者：周子欣\n从属：2022_java第3次作业");
               
			}
		});
		
		//监听 提交按钮
		jb_1.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
            	//获取输入数据
            	String nametxt=jT_1.getText();
            	String worktxt=jT_2.getText();
            	String posttxt=jT_3.getText();
            	String milteltxt=jT_4.getText();
            	String offteltxt=jT_5.getText();
            	String hometeltxt=jT_6.getText();
            	//追加到数组中
            	book.add(nametxt, worktxt, posttxt, milteltxt, offteltxt, hometeltxt);
            	
            	JOptionPane.showMessageDialog(null,"输入成功");
            	//置空为了继续输入
            	jT_1.setText("");
            	jT_2.setText("");
            	jT_3.setText("");
            	jT_4.setText("");
            	jT_5.setText("");
            	jT_6.setText("");
            }
        });
		//监听 输入——返回
		jb_2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
            	panel.removeAll();
				panel.add(panel1);
				panel.validate();
				panel.repaint();
            }
        });
		
		//监听 显示
		jb_show.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
            	panel.removeAll();
				panel.add(panel3);
				panel.validate();
				panel.repaint();

            }
        });
		
		//监听 显示——返回
		jb_back.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
            	panel.removeAll();
				panel.add(panel1);
				panel.validate();
				panel.repaint();
            }
        });
		
		//监听 删除
		jb_del.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				panel.removeAll();
				panel.add(panel4);
				panel.validate();
				panel.repaint();
				//jf.setContentPane(panel2);
			}
		});
		
		//监听 删除——单选
		table2.addMouseListener(new MouseAdapter() {
			public void mousePressed(MouseEvent e) {
				int row=table2.getSelectedRow();//获得行号
				//监听 删除——删除
				jb_delete.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						book.del(row);
						//刷新表格
						
						panel4.remove(table2);
						CustomModel model3 = new CustomModel();
				        JTable table3 = new JTable();
				        table3.setModel(model3);
				        //table.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);

				        JScrollPane scorllPane3=new JScrollPane(table3,ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS,ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
				        panel4.add(scorllPane3,BorderLayout.CENTER);
				        panel4.validate();
						panel4.repaint();
				        
						
					}
				});
			}
			
		});
		
		//监听 删除——返回
		jb_back2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
            	panel.removeAll();
				panel.add(panel1);
				panel.validate();
				panel.repaint();
            }
        });
		
		//监听 退出
		jb_exit.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
            	System.exit(0);
            }
        });

		jf.setVisible(true);
		jf.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
	}


}




