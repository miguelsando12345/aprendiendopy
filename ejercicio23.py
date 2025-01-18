#Verifica si una palabra es palindromo
palabra = "radar"
es_pa = palabra == palabra[::-1]
print("Es palindromo ", es_pa)