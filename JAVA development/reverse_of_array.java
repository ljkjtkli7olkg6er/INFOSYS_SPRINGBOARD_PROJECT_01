public class reverse_of_array{
    public static void main(String[] args) {
    int[]marks={43,56,78,97,100};
     int l=marks.length;
     int a=Math.floorDiv(l,2);
    for(int i=0;i<a;i++){
        int temp=0;
        temp=marks[i];
        marks[i]=marks[l-1-i];
        marks[l-1-i]=temp;
        
    }
    
    for(int element:marks){
        System.out.print(element+  " ");
    }
}
}

