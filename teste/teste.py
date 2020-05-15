from time import sleep

print('VERIFYING'), sleep(0.5)
print('.', end=''), sleep(0.5)
print('.', end=''), sleep(0.5)
print('.\n', end=''), sleep(0.5)
print('VERIFY COMPLETED'), sleep(0.5)
print(8*'='+'LANGUAGES'+8*'='+'\n'
                              'A) PORTUGUES\n'
                              'B) ENGLISH (em desenvolvimento)\n'
                              'C) ESPANISH (em desenvolvimento)')
linguagem = str(input('PLEASE SELECT LANGUAGE: '))

int = int(input('testando'))