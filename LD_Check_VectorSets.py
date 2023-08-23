from sympy import symbols, Eq, solve
from sympy.matrices import Matrix

# Definindo os símbolos para os coeficientes
a, b, c, d, e = symbols('a b c d e')

# Vetores da base
base_vectors = [(1, 2, 3), (4, 5, 6)]

# Vetores extras que formam um conjunto com mais de m vetores
extra_vectors = [(7, 8, 9), (10, 11, 12), (13, 14, 15)]

# Montando equações de combinações lineares para vetores extras em termos da base
equations = [Eq(a*v[0] + b*v[1], d*v[0] + e*v[1]) for v in extra_vectors]

# Resolvendo o sistema de equações para a, b, d e e
solutions = solve(equations, (a, b, d, e))

# Verificando se existem soluções, o que indicaria que os vetores extras são LD
if solutions:
    print("Contradição encontrada! Vetores extras são LD.")
else:
    print("Não foi encontrada contradição. Vetores extras podem ser LI.")
