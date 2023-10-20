# java第二次作业

## 1.第一题

### 1.1题目

编写一个整数矩阵类，并实现如下功能：

(1) 矩阵元素用一个二维整数数组存储；

(2) 两个构造函数：

不带参数的构造函数：为3*3的矩阵分配存储空间

带两个参数的构造函数：两个参数row、col分别表示矩阵的行数和列数，为矩阵分配row*col个元素的存储空间；

(3) 输入函数：输入矩阵中的每一个元素；

(4) 输出函数：按行输出矩阵的每一个元素；

(5) 转置函数：即行列互换，得到另一个矩阵；

(6) 输出每一行的平均值；

### 1.2代码

```Java

```

### 1.3运行结果



## 2.第二题

### 2.1题目

 编写一个完整的Java Application 程序。包含接口ShapeArea，类MyRectangle及类Test，具体要求如下：

(1) 接口ShapeArea：

double getArea()：求一个形状的面积

double getPerimeter ()：求一个形状的周长

(2) 类MyRectangle：实现ShapeArea接口，另有以下属性和方法：

① 属性width：double类型，表示矩形的长 

属性height：double类型，表示矩形的高

② 方法MyRectangle(double w, double h)：构造方法 

方法toString()：输出矩形的描述信息，如“width=1.0,height=2.0, perimeter=6.0, area=2.0”

(3) Test类作为主类要完成测试功能

① 生成MyRectangle对象

② 调用对象的toString方法，输出对象的描述信息

### 2.2代码

```Java

```

### 2.3运行结果

## 3.第三题

### 3.1题目

定义一个名为Card的扑克牌类并进行测试

(1) 扑克牌类Card满足：

① 有两个private访问权限的字符串变量face和suit：分别描述一张牌的牌面值（A、K、Q、J、10、9、…、3、2等）和花色（“黑桃”、“红桃”、“梅花”和“方块”）。

② 定义public访问权限的构造方法，为类中的变量赋值；

③ 定义protected访问权限的方法getFace()，得到扑克牌的牌面值;

④ 定义protected访问权限的方法getSuit()，得到扑克牌的花色;

⑤ 定义方法toString()，返回表示扑克牌的花色和牌面值字符串（如“红桃A”、“梅花10”等）。

(2) 定义主函数，满足：

① 定义字符串数组f和s：分别表示扑克牌的牌面值和花色；

② 定义52个元素的Card类型数组deck，用来存放4个花色的52张牌。如下所示。

String f[] = { "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" };

String s[] = { "黑桃", "红桃", "梅花", "方块" };

Card deck = new Card[ 52 ];

③ 用Card对象给deck数组的52张牌赋值，要求数组中先存放黑桃花色的A、2、3、…、K；然后是红桃花色的A、2、3、…、K；梅花花色的A、2、3、…、K；方块花色的A、2、3、…、K。

for ( int i = 0; i < deck.length; i++ ) {

deck[ i ] = new Card( faces[ i % 13 ], suits[ i / 13 ] );

}

④ 编写模拟洗牌的程序段，即把数组deck中的扑克牌随机打乱存放顺序。

(看懂如下的核心代码并加入到程序中)

for ( int first= 0; first< deck.length; first++ ) {

int second = ( int ) ( Math.random() * 52 );

Card temp = deck[ first];

deck[ first] = deck[ second ];

deck[ second ] = temp;

}

### 3.2代码

```Java

```

### 3.3运行结果

## 4.第四题

### 4.1题目

编写一个方法Search()，要求该方法有一个字符串参数s，方法的功能是统计s中连续相同的字符构成的子串的最大长度，方法返回这个最大长度值，若没有，则返回1。例如s="103300002222223333"，其中连续相同的字符构成的子串有4个，长度依次为2、4、6、4，则最大长度为6。

### 4.2代码

```Java

```

### 4.3运行结果

