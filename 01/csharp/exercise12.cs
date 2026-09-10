using System;

class Payroll {
    public static int baseSalary(int hours, int rate) {
        return hours * rate;
    }

    public static double withholdingTax(int salary) {
        return salary * 0.125;
    } 

    public static double netSalary(int amount, double tax) {
        return amount - tax;
    }
}

class MainClass {
    public static void Main() {
        int baseSalary = Payroll.baseSalary(48, 5000);
        double tax = Payroll.withholdingTax(baseSalary);
        double netSalary = Payroll.netSalary(baseSalary, tax);

        Console.WriteLine($"El salario bruto es {baseSalary}");
        Console.WriteLine($"La retefuente es de {tax}");
        Console.WriteLine($"El salario neto es {netSalary}");
    }
}