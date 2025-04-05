from flask import Flask, render_template, request, jsonify
from TrafficManagement import TrafficManagementSystem

app = Flask(__name__)
tms = TrafficManagementSystem()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.get_json()
    density = data.get('density')
    emergency_route = data.get('emergency_route')

    result = tms.simulate(density, emergency_vehicle_route=emergency_route)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
