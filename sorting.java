import java.util.Arrays;

public class sorting {  
    public static void selectionSort( int[] arr){ 
        int comp=0; 
        for (int i = 0; i < arr.length - 1; i++)  
        {  
            int index = i;  
            for (int j = i + 1; j < arr.length; j++){  
                if (arr[j] < arr[index]){  
                    index = j;  
                }
                comp++;  
            }  
            int temp= arr[index];   
            arr[index] = arr[i];  
            arr[i] = temp;
        }
        System.out.println("\n comparissions are "+comp);
        System.out.println("Sorted array: " + Arrays.toString(arr));  
    }  
    public static void insertionSort(int[] arr){
        int comp=0;
        for(int i=1;i<arr.length;i++){
            int key = arr[i];
            int j=i-1;
            //comp++;
            while(j>=0 && arr[j]>key){
                arr[j+1]=arr[j];
                j--;
                comp++;
            }
            arr[j+1]=key;
        }
        System.out.println(" \n comparissions are "+comp);
        System.out.println("Sorted array: " + Arrays.toString(arr));
    } 
    public static void main(String[] args){  
        int[] input = {8, 7, 2, 5, 4, 3, 6, 1};
        System.out.println("Original array: " + Arrays.toString(input));

        System.out.println("\nSelection Sort:");
        selectionSort(input.clone());

        System.out.println("\nInsertion Sort:");
        insertionSort(input.clone()); 
    }  
}  