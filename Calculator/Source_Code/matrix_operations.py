# matrix_operations.py
import numpy as np

def calculate(operation, matrices):
    try:
        mat1 = np.array(matrices[0])
        mat2 = np.array(matrices[1]) if len(matrices) > 1 else None

        if operation == 'add':
            result = mat1 + mat2
        elif operation == 'subtract':
            result = mat1 - mat2
        elif operation == 'multiply':
            result = np.dot(mat1, mat2)
        elif operation == 'invert':
            result = np.linalg.inv(mat1)
        elif operation == 'determinant':
            result = np.linalg.det(mat1)
        else:
            return 'Invalid operation'

        return result.tolist()

    except ValueError as e:
        return f'ValueError: {str(e)}'
    except Exception as e:
        return str(e)
