import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        int k;
        int[] k_count = new int[101];

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                int total = arr[i] + arr[j];
                if (total % 2 != 0) {
                    continue;
                }

                k = total / 2;
                if (k <= 100) {
                    k_count[k]++;
                }
            }
        }

        int max_count = 0;
        for (int i = 0; i <= 100; i++) {
            if (k_count[i] > max_count) {
                max_count = k_count[i];
            }
        }

        System.out.printf("%d", max_count);
    }
}