public class SelectionSort {
static void selection(int[]a){
    int n =a.length;
    for (int i = 0; i < n - 1; i++) {//i-->current index
        int min_index=i;
        for (int j = i+1; j < n ; j++) {
            if (a[j] < a[min_index]) {
            min_index=j;
            } 
        }

            int temp = a[i];
                a[i] = a[min_index];
                a[min_index] = temp;
        }
    }
    



    
    public static void main(String[] args) {
        int[]a={3,5,2,60,5,44,99,200,1000,22,38};
        selection(a);
        for(int i:a){
            System.out.print(i+"  ");
        }
      
    }
}

