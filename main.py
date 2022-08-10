from funcoes import Valida_cnpj
from time import time

inicial = time()
Valida_cnpj()
final = time()
print(float(final - inicial))

