package gpsproject;
import java.awt.Graphics;

public interface Sprite {
	void draw(Graphics g, int x, int y);
	
	int getHeight();
	
	int getWidth();
}
