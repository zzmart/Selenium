num_esperado = 3
num_obtido = 0
assert num_esperado == num_obtido, f"esperado = {num_esperado} atual = {num_obtido}"

text_esperado = "gelo"
text_obtido = "Gelo"
assert  text_esperado.lower() == text_obtido.lower(), f'esperado = {text_esperado} obtido = {text_obtido}'

texto_esperado = "Gelo"
texto_obtido = "Gelo"
assert  texto_esperado.lower() in text_obtido.lower(), f'esperado = {texto_esperado} obtido = {texto_obtido}'

