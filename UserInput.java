import java.util.Scanner;

public class UserInput {
    public static void main(String[] args) {

        Scanner scanner = null;
        try {
            scanner = new Scanner(System.in);

            System.out.println("Write something: ");

            String message = scanner.nextLine();

            System.out.println("You typed: " + message);
        } finally {
            if (scanner != null)
                scanner.close();
        }
    }
}
