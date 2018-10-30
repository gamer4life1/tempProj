from flask import Flask, request, jsonify
 
app = Flask(__name__)
@app.route('/pi', methods=['POST'])
def pi():
    pi_data = request.json
    print(f'Values: {pi_data}') #--> Value on server {'temp': 100, 'temp_1': 150}
    return jsonify(pi_data)
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
