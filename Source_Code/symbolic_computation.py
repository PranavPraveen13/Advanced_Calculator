from sympy import sympify, diff, integrate, simplify

def differentiate(expression, variable='x'):
    try:
        expr = sympify(expression)
        result = diff(expr, variable)
        return str(result)
    except Exception as e:
        return str(e)

def integrate_expression(expression):
    expr = sympify(expression)
    result = integrate(expr)
    return str(result)

def simplify_expression(expression):
    expr = sympify(expression)
    result = simplify(expr)
    return str(result)
