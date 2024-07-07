from funcionario import funcionario

funcionario = funcionario('Matheus','matheus@blabla.com.br')
funcionario.cadastro_horas('JAN',300)
funcionario.cadastro_horas('FEV',200)
funcionario.cadastro_salario_horas('JAN',30)
funcionario.cadastro_salario_horas('FEV',20)
print(funcionario)
print(funcionario.calcula_salario('JAN'))
print(funcionario.calcula_salario('FEV'))