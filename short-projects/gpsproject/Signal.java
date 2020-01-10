package gpsproject;

public class Signal{
	private static double xAverage = 0;
	private static double yAverage = 0;
	//starting point
	private int x;
	private int y;
	
	public Signal (Object1 o){
		this.x = o.getX();
		this.y = o.getY();
	}
	
	public void pingSignal(ObjectMover om){
		double selectorX = 0;
		double selectorY = 0;
		int r = 0;
		int a;
		signalReached:
		while (r <= 425){
			a = -180;
			while (a<=180){
				selectorX = x+r*Math.cos(Math.toRadians(a));
				selectorY = y+r*Math.sin(Math.toRadians(a));
				if (Math.sqrt( Math.pow((selectorX-om.signalX()),2) + Math.pow((selectorY-om.signalY()),2) ) <= 5){
					xAverage = xAverage + selectorX;
					yAverage = yAverage + selectorY;
					break signalReached;
				}
				a++;
			}
			r++;
		}
	}
	
	static void getLocation(){
		System.out.println("Estimated GPS location: (" + (int)(xAverage/3) + ", " + (int)(yAverage/3) + ")");
		xAverage = 0;
		yAverage = 0;
	}
}
