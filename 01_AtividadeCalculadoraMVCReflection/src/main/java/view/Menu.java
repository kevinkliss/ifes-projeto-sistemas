package view;

import controller.CalculadoraController;
import java.util.Scanner;

public class Menu {

    public double getValue(String mensagem){
        Scanner input = new Scanner(System.in);

        System.out.println(mensagem);
        return input.nextDouble();
    }

    public String getOperator(){
        Scanner input = new Scanner(System.in);

        System.out.println("***** Operadores disponíveis *****");
        System.out.println("Somar");
        System.out.println("Subtrair");
        System.out.println("Multiplicar");
        System.out.println("Dividir");
        System.out.println("Digite o operador desejado: ");

        String op = input.nextLine();
        return op.substring(0,1).toUpperCase() + op.substring(1).toLowerCase();
    }

    public void iniciar(){

        double value1 = getValue("Digite o primeiro valor:");
        String op = getOperator();
        double value2 = getValue("Digite o segundo valor:");

        CalculadoraController calculadora = new CalculadoraController();
        double resultado = calculadora.calcular(op, value1, value2);
        System.out.println("Resultado: " + resultado);
    }

}
