using System;

class Payroll {
    public static int BaseSalary(int hours, int rate) 
    {
        return hours * rate;
    }

    public static double WithholdingTax(int salary) 
    {
        return salary * 0.125;
    } 

    public static double NetSalary(int amount, double tax) 
    {
        return amount - tax;
    }
}

class MainClass {
    public static void Main() {
        int BaseSalary = Payroll.BaseSalary(48, 5000);
        double Tax = Payroll.WithholdingTax(BaseSalary);
        double NetSalary = Payroll.NetSalary(BaseSalary, Tax);

        Console.WriteLine($"El salario bruto es {BaseSalary}");
        Console.WriteLine($"La retefuente es de {Tax}");
        Console.WriteLine($"El salario neto es {NetSalary}");
    }
}