"""
Recebe uma lista com números inteiros e devolve um número
inteiro correspondente à soma dos elementos da lista recebida.
"""
def soma_elementos(a: [int]):
	soma = 0
	for i in a:
		soma = soma + i
	return soma

