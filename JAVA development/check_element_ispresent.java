
   
public class check_element_ispresent{
    public static void main(String[] args) {
    int[]marks={43,56,78,97,100};
    int target=4;
    int index;
    boolean yes=false;
    for( int i=0;i<marks.length;i++){
        if(marks[i]==target){ 
            yes=true;
       
       
    }
    }
    if(yes){
        
        System.out.println("the element is present at index :");
    }
    else{
        
        System.out.println("the element is not present ");
    }
}
}




