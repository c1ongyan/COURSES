import java.util.Arrays;

class Card{
	private String face;
	private String suit;

	public Card(String f,String s){
		this.face=f;
		this.suit=s;
	}

	protected String getFace(){
		return this.face;
	}

	protected String getSuit(){
		return this.suit;
	}

	public String toString(){
		return (this.suit+this.face);
	}
}

public class T_12204202_2_3{
	public static void main(String args[]){
		String f[] = { "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" };
		String s[] = { "黑桃", "红桃", "梅花", "方块" };
		Card[] deck = new Card[ 52 ];

		for ( int i = 0; i < deck.length; i++ ) {
			deck[ i ] = new Card( f[ i % 13 ], s[ i / 13 ] );
		}

		System.out.print("洗牌前的牌面:\n");
        System.out.print(Arrays.toString(deck));
        System.out.print("\n");

        //洗牌
		for ( int first= 0; first< deck.length; first++ ){
			int second =  ( int ) ( Math.random() * 52 );//Math.random()是令系统随机选取大于等于 0.0 且小于 1.0 的伪随机 double 值
			Card temp = deck[ first];
			deck[ first] = deck[ second ];
			deck[ second ] = temp;
		}

		System.out.print("洗牌后的牌面:\n");
        System.out.print(Arrays.toString(deck));




	}
}