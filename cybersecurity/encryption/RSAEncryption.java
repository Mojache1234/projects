package encryption;

public class RSAEncryption {
	public static void main(String args[]){
		User sender = new User("Sender");
		User receiver = new User("Receiver");
		EncryptedMessage senderMessage = sender.encryptMessage();
		System.out.println("Ciphertext: " + senderMessage.readMessage());
		receiver.decryptMessage(senderMessage);
	}
}
