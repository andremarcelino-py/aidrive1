def calcular_frete(valor_compra: float, cliente_premium: bool) -> float:
    """
    Calcula o valor do frete de uma compra.
    """
    if valor_compra < 0:
        raise ValueError("valor_compra não pode ser negativo")

    # >= no lugar >
    if cliente_premium and valor_compra >= 200:
        return 0.0

    return 20.0
