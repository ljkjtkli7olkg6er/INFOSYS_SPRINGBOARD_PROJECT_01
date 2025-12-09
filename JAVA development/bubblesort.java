// public class bubblesort {
//     static void bubble(int[] arr){
//         int n=arr.length;
//         for(int i=0;i<n-1;i++){
//            for(int j=0;i<n-i-1;j++){
//             if(arr[j]>arr[j+1]){
//                 int temp = arr[j];
//                 arr[j] = arr[j+1];
//                 arr[j+1] = temp;
//             }
//            }
//         }
// }


// public static void main(String[] args){
//     int[]arr={100,5,9,67,9,2,4,5,7};
//     bubble(arr);
//     for(int i:arr){
//         System.out.println(i+"  ");
//     }

// }
// }
public class bubblesort {
    static void bubble(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {//for passes i++
            for (int j = 0; j < n - i - 1; j++) {// sorting within passes
                if (arr[j] > arr[j + 1]) {//swapping
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {100, 5, 9, 67, 9, 2, 4, 5, 7};//arr declaration
        bubble(arr);//function call
        for (int i : arr) {
            System.out.print(i + "  ");//to print
        }
    }
}
