package encryption;

import java.math.BigInteger;
import java.util.ArrayList;

public class Encryptor {
	private static final BigInteger modulus = new BigInteger("582311175997456733");
	private static final BigInteger ePow = new BigInteger("961748941");
	//private static final BigInteger p = new BigInteger("694847539");
	//private static final BigInteger q = new BigInteger("838041647");
	private static final BigInteger dPow = new BigInteger("582311174464567548000000000000").add(ePow);
	//private static final BigInteger modulus = BigInteger.valueOf(143);
	//private static final BigInteger ePow = BigInteger.valueOf(7);
	//private static final BigInteger dPow = BigInteger.valueOf(103);
	public EncryptedMessage encrypt(String plaintext){
		char[] array = plaintext.toCharArray();
		ArrayList<Integer> encoded = new ArrayList<>();
		for (char letter : array){
			int x = (int) letter;
			if (x >= 97 && x <= 122){
				x = x-96;
			} else if (x >= 65 && x <= 90){
				x = x-38;
			} else {
				switch (x) {
				case 160: 
					x = 52; //space
					break;
				case 39:
					x = 53; //single quote
					break;
				case 44:
					x = 54; //comma
					break;
				case 45:
					x = 55; //hyphen
					break;
				case 46:
					x = 56; //period
				default: 
					x = 0; //NULL
					break;
				}
			}
			x = new BigInteger(""+x).modPow(ePow, modulus).intValue();
			encoded.add(x);
		}
		
		return new EncryptedMessage(encoded);
	}
	
	public String decrypt(ArrayList<Integer> ciphertext){
		StringBuilder b = new StringBuilder();
		for (int x : ciphertext){
			x = new BigInteger(""+x).modPow(dPow, modulus).intValue();
			if (x >= 1 && x <= 26){
				x = x + 96;
			} else if (x >= 27 && x <= 52){
				x = x + 38;
			} else {
				switch (x) {
				case 52: 
					x = 160; //space
					break;
				case 53:
					x = 39; //single quote
					break;
				case 54:
					x = 44; //comma
					break;
				case 55:
					x = 45; //hyphen
					break;
				case 56:
					x = 46; //period
				default: 
					x = 0; //NULL
					break;
				}
			}
			b.append((char) x);
		}
		return b.toString();
	}
}

/*
* N = 582311175997456733
* e = 961748941
* d = 605471084.646161881234
*/