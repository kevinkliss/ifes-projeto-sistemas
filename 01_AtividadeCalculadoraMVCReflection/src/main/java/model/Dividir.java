package model;

public class Dividir implements Operacao{

    public double calcular(double value1, double value2) {
        if (value2 == 0) throw new ArithmeticException("Não é possível dividir por 0.");
        return value1 / value2;
    }
}
