from flask import Flask, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/soma', methods=['POST'])
def soma():
    """
    Soma dois números
    ---
    parameters:
      - name: num1
        in: formData
        type: number
        required: true
      - name: num2
        in: formData
        type: number
        required: true
    responses:
      200:
        description: Resultado da soma
    """
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    return {"resultado": num1 + num2}

@app.route('/multiplicacao', methods=['POST'])
def multiplicacao():
    """
    Multiplica dois números
    ---
    parameters:
      - name: num1
        in: formData
        type: number
        required: true
      - name: num2
        in: formData
        type: number
        required: true
    responses:
      200:
        description: Resultado da multiplicação
    """
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    return {"resultado": num1 * num2}
