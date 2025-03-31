import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int X = sc.nextInt();
        int Y = sc.nextInt();
        
        int count = 0;
        for (int num = X; num <= Y; num++) {
            if (is_interesting(num)) {
                count++;
            }
        }

        System.out.printf("%d", count);
    }

    public static boolean is_interesting(int num) {
        int[] freq = new int[10];
        int len = 0;
        int temp = num;

        while (temp > 0) {
            int digit = temp % 10;
            freq[digit]++;
            len++;
            temp /= 10;
        }

        if (len < 2) return false;

        int uniqueDigits = 0;
        int[] counts = new int[2];
        int idx = 0;

        for (int i = 0; i < 10; i++) {
            if (freq[i] > 0) {
                uniqueDigits++;
                if (idx < 2) {
                    counts[idx++] = freq[i];
                }
            }
        }

        if (uniqueDigits != 2) return false;

        int a = counts[0], b = counts[1];
        return ((a == 1 && b == len - 1) || (b == 1 && a == len - 1));
    }
}