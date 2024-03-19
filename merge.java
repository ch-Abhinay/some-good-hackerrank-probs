@SuppressWarnings("unchecked")
public class merge {

    public static <T extends Comparable<T>> void sort(T[] a) {
        if (a.length > 1) {
            int mid = a.length / 2;
            T[] left = (T[]) new Comparable[mid];
            T[] right = (T[]) new Comparable[a.length - mid];

            System.arraycopy(a, 0, left, 0, mid);
            System.arraycopy(a, mid, right, 0, a.length - mid);

            sort(left);
            sort(right);

            merge(a, left, right);
        }
    }

    private static <T extends Comparable<T>> void merge(T[] result, T[] left, T[] right) {
        int leftIndex = 0;
        int rightIndex = 0;
        int i = 0;

        while (leftIndex < left.length && rightIndex < right.length) {
            // Copy the smaller element to the result array
            if (left[leftIndex].compareTo(right[rightIndex]) < 0) {
                result[i] = left[leftIndex];
                leftIndex++;
            } else {
                result[i] = right[rightIndex];
                rightIndex++;
            }
            i++;
        }

        // Copy remaining elements from the left array
        while (leftIndex < left.length) {
            result[i] = left[leftIndex];
            leftIndex++;
            i++;
        }

        // Copy remaining elements from the right array
        while (rightIndex < right.length) {
            result[i] = right[rightIndex];
            rightIndex++;
            i++;
        }
    }

    public static void main(String[] args) {
        // Create a random table of 20 integers with values between 10 and 99
        Integer[] table = new Integer[20];
        for (int i = 0; i < 20; i++)
            table[i] = (int) (Math.random() * 90) + 10;

        // Output original array
        System.out.println("ORIGINAL ARRAY:");
        for (Integer i : table)
            System.out.print(i + " ");
        System.out.println();

        // Sort the array
        sort(table);

        // Output sorted array
        System.out.println("SORTED ARRAY:");
        for (Integer i : table)
            System.out.print(i + " ");
        System.out.println();
    }
}
