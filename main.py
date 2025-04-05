numeros = [1, 7, 12, 18, 4, 52, 11, 37]

numeros_pares= [
    numero
    for numero 
    in numeros 
    if numero % 2 == 0
]

print(numeros_pares)

# List comprehension é uma forma de manipularmos uma lista e seus itens, permitindo filtrar os elementos para reduzir a quantidade inicial, além de manipulá-los para modificar seus valores e realizar algumas transformações.

# Expression, na linha 4. essa é a parte em que iremos definir a transformação do item.

# Item, na linha 5. É aqui que definimos um nome para chamar cada item da lista. Esse nome dado será usado nos segmentos Expression e condition

# Iterable, na linha 6. É aqui que definimos a lista que queremos manipular. Também pode ser uma string.

# Condition, na linha 7. É aqui que definimos a condição que queremos aplicar para filtrar os itens da lista. Essa parte é opcional, mas se não for utilizada, a lista resultante será igual à original. Pode ter quantas condições forem necessárias, mas apenas um if.