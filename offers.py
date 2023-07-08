from fastapi import APIRouter, Depends, HTTPException
from typing import Dict
import requests
from cachetools import TTLCache

from authentication import verificar_jwt_token
from models import Simulacao

router = APIRouter()
cache = TTLCache(maxsize=1000, ttl=3600) 
    

@router.get("/emprestimo")
def get_emprestimos(simulacao: Simulacao, username: str = Depends(verificar_jwt_token)):
    if simulacao.cpf in cache:
        oferta_cache = cache[simulacao.cpf]
        return oferta_cache

    aut_url = "https://f0e60216-6218-46d2-ae59-a5c0ea8102fa.mock.pstmn.io/autenticar"
    aut_headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    aut_data = {
        "client_id": "serasa",
        "client_secret": "senha" #alterar senha para a correta
    }

    aut_response = requests.post(aut_url, data=aut_data, headers=aut_headers)
    if aut_response.status_code == 200:
        access_token = aut_response.json().get("access_token")
        ofertas_url = "https://f0e60216-6218-46d2-ae59-a5c0ea8102fa.mock.pstmn.io/ofertas"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        params = {
            "installments": simulacao.parcelas,
            "value": simulacao.valor
        }

        ofertas_response = requests.get(ofertas_url, headers=headers, params=params)
        if ofertas_response.status_code == 200:
            ofertas = ofertas_response.json()

            oferta_adequada = None
            for oferta in ofertas:
                if oferta["installments"] <= simulacao.parcelas and oferta["value"] <= simulacao.valor:
                    oferta_adequada = oferta
                    break

            if oferta_adequada:
                cache[simulacao.cpf] = oferta_adequada
                return oferta_adequada
            else:
                raise HTTPException(status_code=204, detail="Oferta não encontrada")
        else:
            raise HTTPException(status_code=ofertas_response.status_code, detail="API do parceiro indisponível")
    else:
        raise HTTPException(status_code=aut_response.status_code, detail="Falha na autenticação do parceiro")


