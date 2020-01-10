package gpsproject;

import java.awt.Color;
import java.awt.Graphics;

public class DrawComponents {
	private Object1 firstObj;
	private Object1 secondObj;
	private Object1 thirdObj;
	private ObjectMover objMover;
	private GPS gps;
	
	public DrawComponents(){
		firstObj = new Object1(20, 20, Color.BLUE);
		secondObj = new Object1(20, 20, Color.GREEN);
		thirdObj = new Object1(20, 20, Color.YELLOW);
		objMover = new ObjectMover(100, 100, new Object1(20, 20, Color.RED));
		objMover.setMovementVector(-5, 8);
		gps = new GPS(firstObj, secondObj, thirdObj, objMover);
		
	}
	
	public void draw(Graphics g){
		firstObj.draw(g, 25, 25);
		secondObj.draw(g, 25, 250);
		thirdObj.draw(g, 250, 250);
		objMover.draw(g);
		//simulated signal way
		new Signal(firstObj).pingSignal(objMover);
		new Signal(secondObj).pingSignal(objMover);
		new Signal(thirdObj).pingSignal(objMover);
		Signal.getLocation();
		//cheap way
		gps.receiveSignal();
		gps.giveLocation();
	}
}
