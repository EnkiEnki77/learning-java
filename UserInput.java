import java.util.Scanner;

public class UserInput {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Write a message: ");

            String message = scanner.nextLine();

            System.out.println("You wrote: " + message);
        }
    }
}
