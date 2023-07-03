# Desafio API em Python

Como desenvolvedor(a) do time de parcerias de crédito você precisa integrar APIs de
ofertas de diversos parceiros para servir a times internos.
Nesse desafio você precisa criar uma API HTTP com o endpoint /emprestimos .
Esse endpoint deve receber o valor e a parcela de uma simulação de crédito, buscar as ofertas na
API do parceiro e filtrar apenas uma oferta que tenha o valor e a parcela menor ou igual ao valor e
parcela simulados.
Em caso de não encontrar oferta, deve retornar o status code 204 (No Content) representando que
não encontrou oferta.
A oferta deve ser retornada no formato JSON com os atributos:

{

identificador: Identificador da oferta
parceiro: Nome do parceiro
parcelas: Quantidade de parcelas
valor: Valor total

}

