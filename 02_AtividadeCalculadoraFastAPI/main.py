from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Operacao(BaseModel):
    valor1: float
    valor2: float


@app.post("/soma")
def somar(dados: Operacao):
    return {"Resultado": dados.valor1 + dados.valor2}

@app.post("/subtracao")
def subtrair(dados: Operacao):
    return {"Resultado": dados.valor1 - dados.valor2}

@app.post("/multiplicacao")
def multiplicar(dados: Operacao):
    return {"Resultado": dados.valor1 * dados.valor2}

@app.post("/divisao")
def dividir(dados: Operacao):
    if dados.valor2 == 0:
        return "Não é possível dividir por 0."
    return {"Resultado": dados.valor1 / dados.valor2}

