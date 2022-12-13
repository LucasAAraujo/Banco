from models.cliente import Cliente
from models.conta import Conta

lucas: Cliente = Cliente('Lucas Alves', 'lucasalves@hotmail.com', '757476501-49', '02/09/2000')
julia: Cliente = Cliente('Julia', 'julia@gamil.com', '12345678989', '05/10/1994')

# print(lucas)
# print(julia)


contal: Conta = Conta(lucas)
contaj: Conta = Conta(julia)

print(contaj)
print(contal)
