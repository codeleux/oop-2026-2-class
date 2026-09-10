class Payroll:
    @staticmethod
    def baseSalary(hours, rate):
        return hours * rate

    @staticmethod
    def withholdingTax(salary):
        return salary * 0.125

    @staticmethod
    def netSalary(amount, tax):
        return amount - tax


baseSalary = Payroll.baseSalary(48, 5000)
tax = Payroll.withholdingTax(baseSalary)
netSalary = Payroll.netSalary(baseSalary, tax)

print(f"El salario bruto es {baseSalary}")
print(f"La retefuente es de {tax}")
print(f"El salario neto es {netSalary}")