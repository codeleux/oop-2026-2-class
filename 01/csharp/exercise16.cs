class Circle
{
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }
    public double area()
    {
        return Math.PI * Math.Pow(radius, 2);
    }

    public double circumferenceLenght ()
    {
        return radius * 2 * Math.PI;
    }
}

class MainClass
{
    public static void Main()
    {
        Console.WriteLine("Ingrese el radio del circulo: ");
        double input = Convert.ToDouble(Console.ReadLine());
        Circle circle = new Circle(input);

        Console.WriteLine($"El área del circulo de radio {input} es de {circle.area()}");
        Console.WriteLine($"La longitud de la circunferencia del circulo de radio {input} es de {circle.circumferenceLenght()}");
    }
}