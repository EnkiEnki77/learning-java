import java.util.Scanner;

public class HiAdaLovelace {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            String name = "Ada Lovelace";

            System.out.println("What would you like to say to " + name.split(" ")[0] + "?");

            String message = scanner.nextLine();

            System.out.println(message + " " + name);
        }
    }
}
