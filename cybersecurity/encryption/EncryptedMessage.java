package encryption;
import java.util.ArrayList;

public class EncryptedMessage {
	private final ArrayList<Integer> message;
	EncryptedMessage(ArrayList<Integer> ciphertext){
		message = ciphertext;
	}
	
	public ArrayList<Integer> readMessage(){
		return message;
	}
}
