package gpsproject;

public class GPS {
	private Object1 ob1;
	private Object1 ob2;
	private Object1 ob3;
	private ObjectMover objMover;
	
	public GPS(Object1 ob1, Object1 ob2, Object1 ob3, ObjectMover objMover){
		this.ob1 = ob1;
		this.ob2 = ob2;
		this.ob3 = ob3;
		this.objMover = objMover;
	}
	
	public void receiveSignal(){ //this is the cheating way of doing it (using the coordinates of the moving object to determine the distance and angle which are used to determine the coordinates of the moving object through gps mathematics)
		ob1.setProperties(Math.toDegrees(Math.atan2((double)(objMover.signalY()-ob1.getY()), (double)(objMover.signalX()-ob1.getX()))), Math.sqrt( Math.pow((double)(objMover.signalX()-ob1.getX()), 2) + Math.pow((double)(objMover.signalY()-ob1.getY()), 2) ));
		ob2.setProperties(Math.toDegrees(Math.atan2((double)(objMover.signalY()-ob2.getY()), (double)(objMover.signalX()-ob2.getX()))), Math.sqrt( Math.pow((double)(objMover.signalX()-ob2.getX()), 2) + Math.pow((double)(objMover.signalY()-ob2.getY()), 2) ));
		ob3.setProperties(Math.toDegrees(Math.atan2((double)(objMover.signalY()-ob3.getY()), (double)(objMover.signalX()-ob3.getX()))), Math.sqrt( Math.pow((double)(objMover.signalX()-ob3.getX()), 2) + Math.pow((double)(objMover.signalY()-ob3.getY()), 2) ));
	}
	
	public void giveLocation(){
		double xAverage = 0;
		double yAverage = 0;
		
		Object1 obj[] = {ob1, ob2, ob3};
		
		for (Object1 o : obj){
				xAverage = xAverage + o.getX() + o.getDistance()*Math.cos(Math.toRadians(o.getAngle()));
				yAverage = yAverage + o.getY() + o.getDistance()*Math.sin(Math.toRadians(o.getAngle()));
		}
		
		double xC = xAverage/3;
		double yC = yAverage/3;
		System.out.println("Cheated GPS Coordinates: (" + (int) xC + ", " + (int) yC + ")\n");
	}
}
