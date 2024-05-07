import java.security.SecureRandom;

public class RandomBinarySequence {
    /**
     * Generates a random binary sequence and prints it to the console.
     */
    public static void RandomBinarySequence() {

        SecureRandom random = new SecureRandom();

        System.out.println("The generated sequence:");
        for (int i = 0; i < 128; i++) {
            System.out.print(random.nextBoolean() ? "1" : "0");
        }
        System.out.println();
    }

    /**
     * The main function that generates a random binary sequence.
     * @param args Command-line arguments (not used)
     */
    public static void main(String[] args) {
       RandomBinarySequence();
    }
}
