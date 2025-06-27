from fastapi import FastAPI
from pydantic import BaseModel
from calculadora import operacoes

app = FastAPI()

class Operacao(BaseModel):
    valor1: float
    valor2: float

@app.post("/soma")
def somar(dados: Operacao):
    return {"Resultado": operacoes.somar(dados.valor1, dados.valor2)}

@app.post("/subtracao")
def subtrair(dados: Operacao):
    return {"Resultado": operacoes.subtrair(dados.valor1, dados.valor2)}

@app.post("/multiplicacao")
def multiplicar(dados: Operacao):
    return {"Resultado": operacoes.multiplicar(dados.valor1, dados.valor2)}

@app.post("/divisao")
def dividir(dados: Operacao):
    return {"Resultado": operacoes.dividir(dados.valor1, dados.valor2)}
