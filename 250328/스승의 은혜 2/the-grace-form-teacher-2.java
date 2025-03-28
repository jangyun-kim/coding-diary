import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int B = sc.nextInt();
        int[] P = new int[N];
        for (int i = 0; i < N; i++) {
            P[i] = sc.nextInt();
        }
        
        int max_gifted = 0;

        for (int k = 0; k < N; k++) {
            int[] temp = new int[N];
            for (int i = 0; i < N; i++) {
                temp[i] = P[i];
            }

            temp[k] /= 2;
            Arrays.sort(P);

            int total = 0;
            int count = 0;
            for (int i = 0; i < N; i++) {
                total += temp[i];

                if(total > B) break;
                count++;
            }

            max_gifted = Math.max(max_gifted, count);
        }

        System.out.printf("%d", max_gifted);
    }
}