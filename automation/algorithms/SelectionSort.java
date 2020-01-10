package algorithms;

import java.util.Arrays;

public class SelectionSort {
	public static void main(String args[]){
		int sortMe[] = {8, 3, 5, -2, 1, 2, -1, 9, 0, 4, 6, 7};
		sort(sortMe);
	}
	
	static void sort(int[] s){
		System.out.println("Original array: " + Arrays.toString(s));

		boolean sorted = false;
		int lowest = s[0];
		int placeholder;
		int n = s.length - 1;
//		
//		while (!sorted) {
//			for (int i = 1; i <= n; i++) {
//				if (s[i-1] > s[i]) break;
//				else if (i == n) {
//					sorted = true;
//				}
//				
//				for (int a = 0; a < n; a++){
//					lowest = s[a];
//					for (int i2 = a+1; i2 <= n; i2++) {
//						if (lowest > s[i2]) {
//							placeholder = s[a];
//							s[a] = lowest;
//							lowest = placeholder;
//						}
//						else if (lowest < s[i2] || lowest == s[i2]) continue;
//						else System.out.println("An error has occurred.");
//					}
//					
//				}
//				
//			}
//		}
//		
//		System.out.println("Sorted array: " + Arrays.toString(s));
		
		for (int i = 0; i < n; i++) {
			lowest = i;
			
//			System.out.println("\n-------------------Round " + i + "---------------------\n");
			
			for (int i2 = i+1; i2 <= n; i2++){
				
//				System.out.println("\nIndex i: " + i + " and s[i] = " + s[i] + " and s[lowest] = " + s[lowest]);
//				System.out.println("lowest = " + lowest);
//				System.out.println("     Index i2: " + i2 + " and s[i2] = " + s[i2]);
				
				if (s[lowest] > s[i2])	lowest = i2;
				else if (s[lowest] <= s[i2]) continue;
				else System.out.println("An error has occurred, my dudes!\n");
			}
			
			placeholder = s[i];
			s[i] = s[lowest];
			s[lowest] = placeholder;
			
//			System.out.println("NEW s[i] = " + s[i] + " where i = " + i);
//			System.out.println("NEW s[lowest] = " + s[lowest] + " where lowest = " + lowest);
//			
//			System.out.println("\n------------------END OF ROUND-----------------\n");
			
		}
		
		System.out.println(Arrays.toString(s));
		
	}
}
