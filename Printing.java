public class Printing {
    public static void main(String[] args) {
        // Prints string argument, along with an extra empty line
        System.out.println("I");
        System.out.println("Know");
        // When no argument is passed prints empty line
        System.out.println();
        System.out.println("Java");
        System.out.println("Well");
        System.out.println();
        // Prints string passed and places cursor of the console right after, no extra
        // lines are printed.
        System.out.print("I ");
        System.out.print("Know ");
        System.out.print("Java ");
        System.out.print("Well ");
        System.out.println();

        // You can tell the cursor to go to the next line using escape characters
        System.out.print("Hello\nWorld");

        // You can also print integers and characters
        System.out.println(49);
        System.out.println('H');

        String name = "John";

        // Concatenate strings literals and variables contianing them use the + operator
        System.out.println("Hey, " + name);

        // You can also concatenate strings with other data types such as integers. The
        // non string data type will be converted
        // to a string.
        int num = 26;
        System.out.println("I'm " + 2 + 6 + " years old tomorrow. ");
    }
}
