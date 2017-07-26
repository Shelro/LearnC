import java.util.Arrays;
import java.util.Scanner;

public class BinarySearch {
	public static int rank(int key, int[] a) {
		int first = 0;
		int last = a.length - 1;
		
		while(first < last) {
			int mid = ( first + last ) / 2;
			if(key < a[mid]) last = mid - 1;
			else if(key > a[mid]) first = mid + 1;
			else return mid;
		}
		
		return -1;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		 Scanner x=new Scanner(System.in);
	     //while(x.hasNext()){
	     int m=x.nextInt();
	         //System.out.println(m);
	     int[] number=new int[m];
	     for(int i=0;i<m;i++){
	         number[i]=x.nextInt();
	     }
	     //}
		Arrays.sort(number);
		
		int key = x.nextInt();
		
		x.close();
		
		if(rank(key,number)<0) System.out.println(key);
		else System.out.println("Found it.");
	}

}
