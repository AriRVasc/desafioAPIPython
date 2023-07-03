from pydantic import BaseModel

class Simulacao(BaseModel):
    cpf: str
    valor: float
    parcelas: int
