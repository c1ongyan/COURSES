public class T_12204202_4_2 {
    public static void main(String[] args) {
        Bridge bridge = Bridge.getInstance();
        //南5
        for (int i = 1; i <= 5; i++) {
            Thread t = new Thread(new Person(1,i,bridge));
            t.start();
        }
        //北6
        for (int i = 1; i <= 6; i++) {
            Thread t = new Thread(new Person(2,i,bridge));
            t.start();
        }

        //谁先上桥
        bridge.state = true;
        Thread t = new Thread(new Person(2,6,bridge));  //南边第一个开始上桥
    }
}

class Person implements Runnable{
    public Bridge bridge;
    private String side;    //桥的哪端
    private String direction;    //走的方向
    int no; //序号
    public Person(int s,int i,Bridge bridge) {  //s代表桥的哪端
        this.no = i;
        this.bridge = bridge;
//        if (bridge.state) {
//            System.out.println("第"+i+"个人已过桥");
//        }
        //1为南，2为北
        if (s == 1) {
            this.side = new String("南");
            this.direction=new String("从南向北");
        }else {
            this.side = new String("北");
            this.direction=new String("从北向南");
        }
    }

    //过桥
    public synchronized void through() throws InterruptedException {
        if (bridge.state) {
            System.out.println(side+"边第"+no+"个人在过桥，"+"走向："+direction);
            bridge.open(no);
        }else {
            bridge.lock(no);
        }
    }

    @Override
    public void run() {
        try {
            Thread.sleep(1000);
            through();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

//桥
class Bridge {
    //桥的状态,true为可用
    public boolean state = false;
    //实例化
    public static Bridge getInstance(){
        return new Bridge();
    }
    //放行
    public synchronized void open(int i) throws InterruptedException {
        if (state) {    //桥可用
            Thread.sleep(1000);
            this.state = true;
            notify();
        }
    }
    //加锁
    public synchronized void  lock(int i) throws InterruptedException {
        if (!state) {   //state为false，即桥不可用
            this.state = false;
            System.out.println(i+"在等待");
            wait();
        }
    }
}
