from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    if not data or 'product_id' not in data or 'description' not in data or 'customer_name' not in data or 'email' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    if 'price' not in data or not isinstance(data['price'], (int, float)) or data['price'] > 1000:
        return jsonify({'error': 'Price must be a number no greater than 1000.00'}), 400
    print('Received data:', data)
    return jsonify({'status': 'ok', 'received': data}), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)

    