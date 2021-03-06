import argparse

from flask import jsonify, Flask
# from flask_cors import CORS
from simulations import Environment, SimulationEngine

# global
app = Flask(__name__)
# CORS(app)


@app.errorhandler(500)
def internal_error():
    return "Oops, apologies! We encountered a problem. Please try again later.", 500


@app.route('/heartbeat', methods=['GET'])
@app.route('/support/heartbeat', methods=['GET'])
def heartbeat():
    return 'ok'


@app.route('/get_simulation_frames', methods=['GET', 'POST'])
def api_get_simulation_frames():
    result = get_simulation_frames()
    return jsonify(result), 200


def get_simulation_frames() -> dict:
    engine = SimulationEngine(100, 50)
    engine.initialize_simulation(num_actors=100, num_food=80)
    result = [engine.export_state_json()]

    for i in range(100):
        engine.step()
        result.append(engine.export_state_json())

    return result


def main():
    parser = argparse.ArgumentParser()
    # Required arguments
    parser.add_argument('--port', type=int, default=9999, help='Port number where this API should listen.')
    args = parser.parse_args()

    app.run(host='0.0.0.0', port=args.port, debug=True, use_reloader=True)


if __name__ == '__main__':
    main()
