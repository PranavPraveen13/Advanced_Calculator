from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from pymongo import DESCENDING, ASCENDING
from Source_Code import complex_numbers
from Source_Code.basic_calculator import calculate as calculate_basic
from Source_Code.matrix_operations import calculate as calculate_matrix  # Import matrix calculations
from Source_Code.symbolic_computation import differentiate, integrate_expression, simplify_expression
from Source_Code.unit_conversion import convert_units

app = Flask(__name__)

# Configure MongoDB connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/calculatorDB"
mongo = PyMongo(app)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Basic calculator page route
@app.route('/basic_calculator')
def basic_calculator():
    return render_template('basic_calculator.html')

# Endpoint to handle basic calculator calculations
@app.route('/calculate_basic', methods=['POST'])
def calculate_basic_route():
    data = request.json
    expression = data['expression']
    result = calculate_basic(expression)

    # Store calculation in MongoDB
    mongo.db.calculations.insert_one({
        'type': 'basic',
        'expression': expression,
        'result': result
    })

    return jsonify(result=result)

# Complex calculator page route
@app.route('/complex_calculator')
def complex_calculator():
    return render_template('complex_calculator.html')

# Endpoint to handle complex calculator calculations
@app.route('/calculate_complex', methods=['POST'])
def calculate_complex():
    data = request.json
    real_part1 = float(data['real_part1'])
    imaginary_part1 = float(data['imaginary_part1'])
    real_part2 = float(data['real_part2'])
    imaginary_part2 = float(data['imaginary_part2'])
    operation = data['operation']

    # Perform complex number operation based on operation type
    if operation == 'add':
        result_real, result_imaginary = complex_numbers.add_complex(real_part1, imaginary_part1, real_part2,
                                                                    imaginary_part2)
    elif operation == 'subtract':
        result_real, result_imaginary = complex_numbers.subtract_complex(real_part1, imaginary_part1, real_part2,
                                                                         imaginary_part2)
    elif operation == 'multiply':
        result_real, result_imaginary = complex_numbers.multiply_complex(real_part1, imaginary_part1, real_part2,
                                                                         imaginary_part2)
    elif operation == 'divide':
        result_complex = complex_numbers.divide_complex(real_part1, imaginary_part1, real_part2, imaginary_part2)
        if result_complex is None:
            return jsonify(error="Division by zero error")
        result_real, result_imaginary = result_complex
    else:
        return jsonify(error="Invalid operation")

    # Store calculation in MongoDB
    mongo.db.calculations.insert_one({
        'type': 'complex',
        'complex_number1': {'real_part': real_part1, 'imaginary_part': imaginary_part1},
        'complex_number2': {'real_part': real_part2, 'imaginary_part': imaginary_part2},
        'operation': operation,
        'result': {'real': result_real, 'imaginary': result_imaginary}
    })

    return jsonify(real_part1=real_part1, imaginary_part1=imaginary_part1,
                   real_part2=real_part2, imaginary_part2=imaginary_part2,
                   result_real=result_real, result_imaginary=result_imaginary)

# Matrix calculator page route
@app.route('/matrix_calculator')
def matrix_calculator():
    return render_template('matrix_calculator.html')

# Endpoint to handle matrix calculator calculations
@app.route('/calculate_matrix', methods=['POST'])
def calculate_matrix_route():
    data = request.json
    matrices = data['matrices']
    operation = data['operation']

    # Perform matrix operation based on operation type
    result = calculate_matrix(operation, matrices)

    # Store calculation in MongoDB
    mongo.db.calculations.insert_one({
        'type': 'matrix',
        'matrices': matrices,
        'operation': operation,
        'result': result
    })

    return jsonify(result=result)

# Symbolic calculator page route
@app.route('/symbolic_calculator')
def symbolic_calculator():
    return render_template('symbolic_calculator.html')

# Endpoint to handle symbolic calculator calculations
@app.route('/calculate_symbolic', methods=['POST'])
def calculate_symbolic():
    data = request.json
    expression = data['expression']
    operation = data['operation']

    # Perform symbolic computation based on operation type
    if operation == 'differentiate':
        result = differentiate(expression)
    elif operation == 'integrate':
        result = integrate_expression(expression)
    elif operation == 'simplify':
        result = simplify_expression(expression)
    else:
        result = 'Invalid operation'

    # Store calculation in MongoDB (assuming symbolic computations do not have complex data structures)
    mongo.db.calculations.insert_one({
        'type': 'symbolic',
        'expression': expression,
        'operation': operation,
        'result': result
    })

    return jsonify(result=result)

# Unit conversion page route
@app.route('/unit_conversion')
def unit_conversion():
    return render_template('unit_conversion.html')

# Endpoint to handle unit conversion calculations
@app.route('/convert_unit', methods=['POST'])
def convert_unit():
    data = request.json
    result = convert_units(data)

    # Store calculation in MongoDB
    mongo.db.calculations.insert_one({
        'type': 'unit_conversion',
        'conversion_data': data,
        'result': result
    })

    return jsonify(result=result)

# History page route to display all calculations or filtered by type
@app.route('/history')
def history():
    calculation_type = request.args.get('calculation_type', '')  # Get the selected calculation type filter
    sort_order = request.args.get('sort', 'latest')  # Get the selected sort order, default to latest

    sort_key = '_id'  # Sort by MongoDB ObjectId by default
    if sort_order == 'oldest':
        sort_direction = ASCENDING
    else:
        sort_direction = DESCENDING

    filters = {}

    # Apply calculation type filter if selected
    if calculation_type:
        filters['type'] = calculation_type

    # Retrieve calculations from MongoDB based on filters and sort order
    calculations = mongo.db.calculations.find(filters).sort(sort_key, sort_direction)

    return render_template('history.html', calculations=calculations)


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
