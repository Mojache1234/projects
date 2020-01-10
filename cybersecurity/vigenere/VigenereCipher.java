package vigenere;
import java.util.Scanner;
import java.util.ArrayList;

public class VigenereCipher {
	private static ArrayList<Integer> key = new ArrayList<>();
	private static int counter = 0;
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		//int i = 0;
		StringBuilder m = new StringBuilder();
		System.out.print("/> Enter Key: \n/> ");
		String keyString = scan.nextLine().toUpperCase();
		for (int i = 0; i < keyString.length(); i++){
			for (int a : keyString.toCharArray()){
				if (a >= 65 && a <= 90){
					key.add(a-65);
				}
			}
		}
		System.out.println("/> Type message: ");
		while(true){
			counter = counter%key.size();
			System.out.print("/> ");
			String message = scan.nextLine().toUpperCase();
			char[] line = message.toCharArray();
			int x;
			for (int i = 0; i < message.length(); i++){
				if ((int)line[i] >= 65 && (int)line[i] <= 90){
					x = ((((int) line[i] + key.get(counter))-64)%26);
					switch(x){
					case 0:
						x = x + 90;
						break;
					default:
						x = x + 64;
						break;
					}
					counter = (counter+1)%key.size();
				} else {
					x = (int) line[i];
				}
				m.append((char) x);
			}
			
			
			/*
			for (int x : line.toCharArray()){
				if ((x >= 97 && x <= 122) || (x >= 65 && x <= 90)){
					switch (i){
					case 0: 
						i++;
						break;
					case 1:
						x = x + 7;
						i++;
						break;
					case 2:
						x = x + 18;
						i++;
						break;
					case 3:
						i++;
						break;
					case 4:
						x = x + 13;
						i = 0;
						break;
					}
					if ((x >= 97 && x <= 122) || (x >= 65 && x <= 90)){
						m.append((char)x);
					} else {
						x=x-26;
						m.append((char)x);
					}
				} else {
					m.append((char)x);
				}
			}
			*/
			System.out.println("/> Ciphertext: "+m.toString().toLowerCase());
			m = new StringBuilder();
		}
	}
}