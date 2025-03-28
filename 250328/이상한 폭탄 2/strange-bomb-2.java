import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int[] bombs = new int[N];
        for (int i = 0; i < N; i++) {
            bombs[i] = sc.nextInt();
        }
        
        int boom = -1;
        for (int i = 0; i < N; i++) {
            for (int j = 1; j <= K; j++) {
                if (i + j >= N) break;
                if (bombs[i] == bombs[i + j]) {
                    boom = Math.max(boom, bombs[i]);
                }
            }
        }

        System.out.printf("%d", boom);
    }
}