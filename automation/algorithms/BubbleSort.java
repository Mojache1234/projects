package algorithms;

import java.util.Arrays;

public class BubbleSort {
	public static void main(String args[]){
		int sortMe[] = {8, 3, 5, -2, 9, 1, 2, -1, 9, 0, 4, 6, 7};
		int sortMe2[] = {8, 3, 5, -2, 1, 2, -1, 9, 0, 4, 6, 7};
		bubbleSort(sortMe);
		System.out.println("\n--------------------------------------\n");
		bubbleSort2(sortMe2);
	}
	
	static void bubbleSort(int[] s){
		System.out.println(Arrays.toString(s));
		int n = s.length;
		for (int in = 0; in < n; in++) {
			for (int i = 1; i <= n-1; i++) {
				int placeholder;
				if (s[n-i] < s[n-i-1]){
					placeholder = s[n-i];
					s[n-i] = s[n-i-1];
					s[n-i-1] = placeholder;
				} else if (s[n-i] > s[n-i-1] || s[n-i] == s[n-i-1]) continue;
				else {
					System.out.println("An error has occurred");
				}
			}
		}
		
		System.out.println(Arrays.toString(s));
	}
	
	static void bubbleSort2(int[] s){
		System.out.println(Arrays.toString(s));
		int n = s.length;
		boolean sorted = false;
		done:
		while (!sorted) {
			for (int i = 0; i < n-1; i++) {
				if (s[i] > s[i+1]) break;
				else if (i+2 == n) {
					sorted = true;
					break done;
				}
			}
			
			for (int i = 1; i <= n-1; i++) {
				int placeholder;
				if (s[n-i] < s[n-i-1]){
					placeholder = s[n-i];
					s[n-i] = s[n-i-1];
					s[n-i-1] = placeholder;
				} else if (s[n-i] > s[n-i-1] || s[n-i] == s[n-i-1]) {
					continue;
				} else {
					System.out.println("An error has occurred");
				}
			}
		}
		System.out.println(Arrays.toString(s));
	}
}
