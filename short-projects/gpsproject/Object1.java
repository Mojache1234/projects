package gpsproject;

import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;

public class Object1 implements Sprite{
	private int height;
	private int width;
	private int x;
	private int y;
	private Color color;
	private double angle;
	private double distance;
	
	public Object1(int width, int height, Color color){
		this.height = height;
		this.width = width;
		this.color = color;
	}
	
	@Override
	public void draw(Graphics g, int x, int y){
		this.x = x;
		this.y = y;
		g.setColor(color);
		g.fillRect(x, y, width, height);
		g.setColor(Color.BLACK);
		((Graphics2D) g).setStroke(new BasicStroke(3.0f));
		g.drawRect(x, y, width, height);
	}
	
	@Override
	public int getHeight(){
		return height;
	}
	
	@Override 
	public int getWidth(){
		return width;
	}
	
	public int getX(){ //should replace with "emit signal" instead
		return x;
	}
	
	public int getY(){ //should replace with "emit signal" instead
		return y;
	}
	
	public void setProperties(double angle, double distance){
		this.angle = angle;
		this.distance = distance;
	}
	
	public double getAngle(){
		return angle;
	}
	
	public double getDistance(){
		return distance;
	}
	
}
