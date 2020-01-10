package gpsproject;

import gpsproject.DrawMap;
import java.awt.Graphics;

public class ObjectMover {
	private int x;
	private int y;
	private int xDirection;
	private int yDirection;
	private Object1 object;
	
	public ObjectMover(int x, int y, Object1 object){
		this.x = x;
		this.y = y;
		this.object = object;
	}
	
	public void setMovementVector(int xDirection, int yDirection){
		this.xDirection = xDirection;
		this.yDirection = yDirection;
	}
	
	public void draw(Graphics g){
		object.draw(g, x, y); 
		x += xDirection;
		y += yDirection;
		
		System.out.println("Actual location: (" + x + ", " + y + ")");
		
		if ((x <= 0 && xDirection < 0) || (x + object.getWidth() >= DrawMap.WIDTH && xDirection > 0)) {
			xDirection = -xDirection;
		}
		if ((y <= 0 && yDirection < 0) || (y + object.getHeight() >= DrawMap.HEIGHT && yDirection > 0)) {
			yDirection = -yDirection;
		}
	}
	
	public int signalX(){
		return x;
	}
	
	public int signalY(){
		return y;
	}
}
