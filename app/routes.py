from flask import Blueprint, render_template, abort
import json

# 1. Definir el blueprint
main = Blueprint('main', __name__)

# 2. Función para cargar productos desde productos.json
def cargar_productos():
    with open('productos.json', 'r', encoding='utf-8') as f:
        productos = json.load(f)
    return productos

# 3. Función para buscar producto por SKU
def buscar_producto_por_sku(sku):
    productos = cargar_productos()
    for producto in productos:
        if producto.get('sku') == sku:
            return producto
    return None

# 4. Ruta principal "/"
@main.route('/')
def index():
    productos = cargar_productos()
    return render_template('index.html', productos=productos)

# 5. Ruta detalle "/producto/<sku>"
@main.route('/producto/<sku>')
def detalle(sku):
    producto = buscar_producto_por_sku(sku)
    if producto is None:
        abort(404)
    return render_template('detalle.html', producto=producto)
