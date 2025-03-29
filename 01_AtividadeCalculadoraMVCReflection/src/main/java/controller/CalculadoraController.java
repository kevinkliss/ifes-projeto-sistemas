package controller;

import model.Operacao;

public class CalculadoraController {

    public double calcular (String op, double value1, double value2){

        try {
            String nomeClasse = "model." + op;
            Class<?> classe = Class.forName(nomeClasse);
            Operacao instancia = (Operacao) classe.getDeclaredConstructor().newInstance();

            return instancia.calcular(value1, value2);
        }
        catch(ClassNotFoundException e) {
            System.out.println("Operador inválido.");
        }
        catch(Exception e){
            System.out.println("Erro ao calcular: " + e.getMessage());
        }
        return 0;
    }
}