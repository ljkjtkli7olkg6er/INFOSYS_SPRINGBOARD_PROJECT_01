

// # program for sum of  n numbers

// public class recursion {
//     static int sum(int n){// n where is parameter
//         if(n==1){
//             return 0;
//         }
//         else{
//             return n +sum(n-1);// it will recall function again
//         }
//     }
//     public static void main(String[] args) {
//         int c=sum(5);//n=5 is actual parameter
//         System.out.println(c);
//     }
    
// }

//# febonnocci series

// public class recursion{
//     static int febo(int n){
//         if(n==0||n==1){
//             return n;
//         }
//         else{
//             return  febo(n - 1) + febo(n - 2);
//         }
//     }
//     public static void main(String[] args) {
//         int d= febo(9);
//         System.out.println(d);
//     }
    
// }


// # factorial for n number



// public class recursion{
//     static int factorial(int n){
//         if(n==0||n==1){
//             return 1;
//         }
//         else{
//             return n*factorial(n -1);
//         }
//     }
//     public static void main(String[] args) {
//         int j=factorial(5);
//         System.out.println(j);
//     }
// }
  

//  print an array from index 0 to last index
// public class recursion{

// static void printarray(int[]arr,int idx){
//     if(idx==arr.length){
//         return;
//     }
//     System.out.println(arr[idx]);
//     printarray(arr,idx+1);
// }
// public static void main(String[] args) {
//     int[]arr={1,2,3,4,5,6,7,8};
//     printarray(arr,0);
// }
// }


//print max of element