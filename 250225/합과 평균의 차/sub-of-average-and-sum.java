import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        int sum = A + B + C;
        int avg = sum / 3;
        int result = sum - avg;

        System.out.println(sum);
        System.out.println(avg);
        System.out.println(result);

    }
}