from models.endereco import Endereco
from models.enum.sexo import Sexo
from models.enum.setor import Setor

class Funcionario:
    def __init__(self, id: int, nome: str, cpf: str, rg: str, matricula: str, dataNascimento: str, sexo: Sexo, setor: Setor, salario: float, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.dataNascimento = dataNascimento
        self.sexo = sexo
        self.setor = setor
        self.salario = salario
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return ( 
            f"\nId: {self.id}"
            f"\nNome: {self.nome}"
            f"\nCpf: {self.cpf}"
            f"\nRg: {self.rg}"
            f"\nMatricula: {self.matricula}"
            f"\nData de nascimento: {self.dataNascimento}"
            f"\nSexo: {self.sexo}"
            f"\nSetor: {self.setor}"
            f"\nSalario: {self.salario}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nEndereço: {self.endereco}"
        )
    
           
