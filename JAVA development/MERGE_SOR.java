public class MERGE_SOR{
    
        static void mergesort(int[]arr,int l,int r){
            if(l>=r)
            return;
            int mid=(l+r)/2;
            mergesort(arr,l,mid);
            mergesort(arr,mid+1,r);
            merge(arr,l,mid,r);
            
            
        }
        static void merge(int[]arr,int l,int mid,int r){
            int n1=mid-l+1;
            int n2=r-mid;
            int[]left= new int[n1];
            int[]right= new int[n2];
            int i,j,k=0;
            for(i=0;i<n1;i++){// In this stage we put elements in left array
                left[i]=arr[l+i];
            }
            for( j=0;j<n2;j++){// In this stage we put elements in right array
                right[j]=arr[mid+1+j];
            }
            while(  i<n1 &&  j<n2){
                if(left[i]<right[j])
               { 
                arr[k++]=left[i++];}
                else
               { arr[k++]=right[j++];
            }
            while(i<n1){
                arr[k++]=left[i++];}

            }
            while(j<n2){
                arr[k++]=left[j++];   
            }
        }
        static void display(int[]arr){
            for(int val:arr){
                System.out.print(val+"  ");
            }
        }
public static void main(String[] args){
    int[]arr={22,5,90,789,45,51,33};
    int n=arr.length;
    System.out.println("array before sorting:");
    display(arr);
    mergesort(arr,0,n-1);
    System.out.println("array after sorting:");
    display(arr);
    
}
}