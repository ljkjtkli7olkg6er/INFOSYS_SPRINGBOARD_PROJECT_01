//  class method {
//      int multiplication(int a,int b){
//         return a*b;
//     }
//    public static void main(String[] args) {
//     method B= new method();
//     int c=B.multiplication(2,5);
//     System.out.println(c);
//    

// class Overloading {
//    int multiply(int a, int b) {
//        return a * b;
//    }

//    double multiply(double a, double b) {
//        return a * b;
//    }

//    public static void main(String[] args) {
//        Overloading obj = new Overloading();
//        int c = obj.multiply(5, 4);
//        double d = obj.multiply(5.1, 4.2);
//        System.out.println("Multiply: returns integer: " + c);
//        System.out.println("Multiply: returns double: " + d);
//    }
// }


class Overloading{
    static void gm(){
        System.out.println(" good morning:");
    }
    static void gm(int n){
        System.out.println("Good morning "+n);
    }
    static int power (int a,int b){
        int z=1;
        for(int i=0;i<b;i++){
            z=a*z;
        }
        return z;

    }
    public static void main(String[] args) {
       
        gm( 50);
        gm( );
         int j=power(2,3);
         System.out.println(j);
    
    }
}
