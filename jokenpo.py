from random import randint
import sys

def gerar_mao():
	mao = ('tesoura', 'pedra', 'papel')
	mao = mao[randint(0,2)]
	return mao

if __name__ == '__main__':	
	
	ganhador = ''

	mao01 = gerar_mao()
	mao02 = gerar_mao()

	if mao01 == 'pedra' and mao02 == 'papel':
		ganhador = mao02
		
	if mao01 == 'papel' and mao02 == 'pedra':
		ganhador = mao01
		
	if mao01 == 'tesoura' and mao02 == 'papel':
		ganhador = mao01
		
	if mao01 == 'papel' and mao02 == 'tesoura':
		ganhador = mao02		

	if mao01 == 'pedra' and mao02 == 'tesoura':
		ganhador = mao01		

	if mao01 == 'tesoura' and mao02 == 'pedra':
		ganhador = mao02
	
print('As jogadas foram {} e {}\n'.format(mao01, mao02))
	
if mao01 == mao02:
	ganhador = 'infelizmente não houve vencedor, empate'
	print('{}\n'.format(ganhador))
	sys.exit(0)
	
print('vencedor {}\n'.format(ganhador))
