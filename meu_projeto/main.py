from models.funcionario import Funcionario
from models.enum.sexo import Sexo
from models.enum.setor import Setor
from models.endereco import Endereco
from models.enum.unidade_federativa import unidadeFederativa


funcionario = Funcionario(123,"Wagner","123-444","9282","hwdh7","05/06/2005",Sexo.MASCULINO.value,Setor.ENGENHARIA.value,2020,"7171717","wag@gmail",Endereco("Drena","93","sla","43900-000","sfc",unidadeFederativa.BAHIA.nome))


print(funcionario)