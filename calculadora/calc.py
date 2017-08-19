from funcoes import soma, subtracao, divisao, multiplicacao

if __name__ == '__main__':
	
	valor01 = float(input('Digite o primeiro valor '))
	valor02 = float(input('Digite o segundo valor '))
	operacao = input('Digite a operação ')

	if operacao == '+':
		resultado = soma(valor01, valor02)
	elif operacao == '-':
		resultado = subtracao(valor01,valor02)
	elif operacao == '/':
		resultado = divisao(valor01, valor02)
	elif operacao == '*':
		resultado = multiplicacao(valor01, valor02)
	else:
		resultado = 'Erro na operação'

print(resultado)
