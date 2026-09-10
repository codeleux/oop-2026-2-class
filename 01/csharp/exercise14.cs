class Operations {
    public static double squared(double num) {
        return Math.Pow(num, 2);
    }
    
    public static double cubed(double num) {
        return Math.Pow(num, 3);    
    }
}

class MainClass {
    public static void Main() {
        Console.WriteLine("Escriba un número: ");
        double input =  Convert.ToDouble(Console.ReadLine());
        double squaredNum = Operations.squared(input);
        double cubedNum = Operations.cubed(input);

        Console.WriteLine($"{input}^2 = {squaredNum}");
        Console.WriteLine($"{input}^3 = {cubedNum}");
    }
}