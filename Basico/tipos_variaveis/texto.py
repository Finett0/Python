# Delcaração de strings

nome_completo = "Giovanni Finetto" 

nome_completo_aspas = """ Giovanni

finetto"""

print(nome_completo)
print(nome_completo_aspas)

nome = 'Giovanni'
sobrenome = "Finetto"

#formatação
print("\nNome completo (1 forma):", nome_completo)
print("\nNome completo (2 forma): " + nome_completo) #concatenação com mais
print("\nNome completo (3 forma):" + " Giovanni" + " Santos")
print(f"\nNome completo (4 forma): {nome} {sobrenome}")

