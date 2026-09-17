package Experiments.arrays;
import java.util.Arrays;
import java.util.Stack;

public class Main {

    public static String ReverseArray(int arr[]) {

        Stack<Integer> stack = new Stack<>();
        for (int val : arr) {
            stack.push(val);
        }

        int[] ReversedArray = new int[stack.size()];

        for (int i = 0; i < stack.size(); i++) {
            ReversedArray[i] = stack.pop();
        }

        return Arrays.toString(ReversedArray);
    }

    public static void main(String[] args) {
        int b[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        String s  = ReverseArray(b);
        System.out.println(s);
    }
}
