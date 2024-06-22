def calculate(expression):
    try:
        result = eval(expression)  # Evaluate the expression
        return str(result)
    except Exception as e:
        return str(e)  # Return error message if there's an exception
