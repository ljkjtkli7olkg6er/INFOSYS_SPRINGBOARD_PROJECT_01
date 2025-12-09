public class MERGE_SORT {

    static void mergesort(int[] arr, int l, int r) {
        if (l >= r) return; // Base case
        int mid = (l + r) / 2;
        mergesort(arr, l, mid);
        mergesort(arr, mid + 1, r);
        merge(arr, l, mid, r);
    }

    static void merge(int[] arr, int l, int mid, int r) {
        int n1 = mid - l + 1;
        int n2 = r - mid;
        int[] left = new int[n1];
        int[] right = new int[n2];

        for (int i = 0; i < n1; i++) { // Fill left array
            left[i] = arr[l + i];
        }
        for (int j = 0; j < n2; j++) { // Fill right array
            right[j] = arr[mid + 1 + j];
        }

        int i = 0, j = 0, k = l;
        while (i < n1 && j < n2) {
            if (left[i] <= right[j]) {
                arr[k++] = left[i++];
            } else {
                arr[k++] = right[j++];
            }
        }

        while (i < n1) {
            arr[k++] = left[i++];
        }

        while (j < n2) {
            arr[k++] = right[j++];
        }
    }

    static void display(int[] arr) {
        for (int val : arr) {
            System.out.print(val + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] arr = {22, 5, 90, 789, 45, 51, 33};
        int n = arr.length;
        System.out.println("Array before sorting:");
        display(arr);
        mergesort(arr, 0, n - 1);
        System.out.println("Array after sorting:");
        display(arr);
    }
}


        