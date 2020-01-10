package gpsproject;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D; 
import java.awt.RenderingHints;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

import javax.swing.JFrame;
import javax.swing.JPanel;

import gpsproject.DrawComponents;
import gpsproject.DrawMap;

public class DrawMap extends JPanel implements Runnable{
	private static final long serialVersionUID = -7469734580960165754L;
	private final int FRAME_DELAY = 50; 
	public static final int WIDTH = 300;
	public static final int HEIGHT = 300;
	private DrawComponents draw;
	
	public DrawMap(DrawComponents draw){
		this.draw = draw;
	}
	
	@Override
	public void paintComponent(Graphics g) {
		super.paintComponent(g);
		Graphics2D g2 = (Graphics2D) g;
		g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
		draw.draw(g2);
	}

	@Override
	public void run() {
		while (true) {
			repaint();
			try {
				Thread.sleep(FRAME_DELAY);
			} catch (InterruptedException e) {
				throw new RuntimeException(e);
			}
		}
	}
	
	public static void main(String args[]){
		final DrawMap content = new DrawMap(new DrawComponents());
		content.setBackground(Color.white);
		content.setPreferredSize(new Dimension(WIDTH, HEIGHT));
		
		JFrame frame = new JFrame("GPS");
		frame.setBackground(Color.white);
		frame.setContentPane(content);
		frame.setResizable(false); // I wonder what settings we're going to have to mess around with to allow a frame to be resizable. Are we going to need to make the sizes of the sprites dynamic?  
		frame.pack(); // not sure what this method does
		frame.addWindowListener(new WindowAdapter() { //anonymous nested class ... why? Recall what anonymous nested classes are good for - creating a specific type of class that is typically only used once
			public void windowClosing(WindowEvent e) { System.exit(0); }
		});
		new Thread(content).start(); // We're throwing thread into runnable so that we can run it
		frame.setVisible(true);
	}	
}
