class IdadeInvalida(Exception):
    def __init__(self, idade_cliente, classificacao_etaria):
        super().__init__(f"A idade do cliente ({idade_cliente} anos) não atende à classificação etária mínima de {classificacao_etaria} anos para este filme.")
