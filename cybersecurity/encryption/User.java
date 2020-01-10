package encryption;
import java.util.Scanner;

public class User {
	private final String name;
	public User (String name){
		this.name = name;
	}
	
	public EncryptedMessage encryptMessage(){
		System.out.println(name + " is encrypting a message. What will the message contain?");
		Scanner x = new Scanner(System.in);
		EncryptedMessage em = new Encryptor().encrypt(x.nextLine());
		x.close();
		return em;
	}
	
	public void decryptMessage(EncryptedMessage message){
		System.out.println(name + " has decrypted the following message: ");
		String x = new Encryptor().decrypt(message.readMessage());
		System.out.println(x);
	}
}
