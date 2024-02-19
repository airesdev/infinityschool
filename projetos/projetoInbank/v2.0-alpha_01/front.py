from back import banco
from functions.deposito import depositar
from functions.saque import sacar
from functions.consulta import consultar
from functions.transferencia import transferir

opcao = int(input(f'----- Menu Inicial ----- \n'
                  f'\n'
                  f'>>> Opções: \n'
                  f'    1 - Adicionar Cliente \n'
                  f'    2 - Pesquisar Cliente\n'
                  f'    3 - Editar Cliente \n'
                  f'    4 - update \n'
                  f'    5 - Deletar Cliente \n'
                  f'\n'
                  f'>>> Operações: \n'
                  f'    6 - Consultar Cliente \n'
                  f'    7 - Depositar \n'
                  f'    8 - Sacar \n'
                  f'    9 - Transferir \n'
                  f'    10 - Lista de clientes \n'
                  f'\n'
                  f'- Selecione sua opção: '))
