import java.util.Scanner;
public class array1d {
    public static void main(String[] args) {
    
       int[] name = new int[5];
       Scanner sc = new  Scanner(System.in);   
        for(int i=0;i<4;i++){
            System.out.println("enter the array :"+    i);
            name[i] =  sc.nextInt();
      
  }
  for(int i=0;i<name.length-1;i++){
      
    System.out.println(name[i]);


  
}
    }
    
}
