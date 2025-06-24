public class TwinPrime {
    static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i <= n / 2; i++)
            if (n % i == 0) return false;
        return true;
    }
    public static void main(String[] args) {
        int a = 11, b = 13;
        System.out.println((isPrime(a) && isPrime(b) && Math.abs(a - b) == 2) ? "Twin Primes" : "Not Twin Primes");
    }
}
