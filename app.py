from flask import Flask, render_template, request, jsonify
from utils import filtrar_transacciones, validar_fecha

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    data = request.json
    codigo_tienda = data.get('codigo_tienda')
    tid = data.get('tid')
    tarjeta = data.get('tarjeta')
    monto_desde = data.get('monto_desde')
    monto_hasta = data.get('monto_hasta')
    fecha_desde = data.get('fecha_desde')
    fecha_hasta = data.get('fecha_hasta')

    if fecha_desde and not validar_fecha(fecha_desde):
        return jsonify({"error": "La fecha desde ingresada no es válida. Por favor, ingrese una fecha en formato DD/MM/AAAA."}), 400
    if fecha_hasta and not validar_fecha(fecha_hasta):
        return jsonify({"error": "La fecha hasta ingresada no es válida. Por favor, ingrese una fecha en formato DD/MM/AAAA."}), 400

    resultados = filtrar_transacciones(codigo_tienda, tid, tarjeta, monto_desde, monto_hasta, fecha_desde, fecha_hasta)

    return jsonify(resultados.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)
