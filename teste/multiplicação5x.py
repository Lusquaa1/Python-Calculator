from time import sleep
ma = float(input('Digite o valor de a:'))

mb = float(input('Digite o valor de b:'))

mc = float(input('Digite o valor de c:'))

md = float(input('Digite o valor de d:'))

me = float(input('Digite o valor de e:'))

mabcde = (ma*mb*mc*md*me)

print('Para receber um resultado arredondado digite a'), sleep(0.25)
print('Para um resultado completo digite b')
opm = str(input('Opção selecionada :'))
if opm in 'Aa':
    print('O resultado arredondado da multiplicação entre a = {},\n'
          'b = {}, c={}, d={} e e={} é igual a {:.0f}'.format(ma, mb, mc, md, me, mabcde))
elif opm in 'Bb':
    print('O resultado completo da multiplicação entre a = {},\n'
          'b = {}, c={}, d={} e={} é igual a {}'.format(ma, mb, mc, md, me, mabcde))
