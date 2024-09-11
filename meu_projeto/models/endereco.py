from models.enum.unidade_federativa import unidadeFederativa
class Endereco:
    def __init__(self, logadouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: unidadeFederativa ) -> None:
        self.logadouro = logadouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf

    def __str__(self) -> str:
        return (

            f"\nLogadouro: {self.logadouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCep: {self.cep}"
            f"\nCidade: {self.cidade}"
            f"\nUnidade Federativa: {self.uf}"
        )    