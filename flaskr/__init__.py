from flask import Flask, jsonify, request, abort
from models import setup_db, State
from flask_cors import CORS

STATES_PER_PAGE = 10

def paginate_states(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * STATES_PER_PAGE
    end = start + STATES_PER_PAGE

    states = [state.format() for state in selection]
    current_states = states[start:end]

    return current_states


def create_app(test_conf=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Acceess-Contrll-Allow-Methods', 'GET, POST, DELETE, PUT, OPTIONS')
        return response
    
    @app.route('/states')
    def get_states():
        selection = State.query.order_by(State.id).all()
        current_states = paginate_states(request, selection)

        if len(current_states) == 0:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'states': current_states,
                'total_states': len(State.query.all())
            })
        
    @app.route('/states', methods=['POST'])
    def create_state():
        body = request.get_json()

        try:
            new_governor = body.get('governor', None)
            new_name = body.get('name', None)
            new_capital = body.get('capital', None)
            
            state = State(name=new_name, capital=new_capital, governor=new_governor)
            state.insert()

            selection = State.query.order_by(State.id).all()
            current_states = paginate_states(request, selection)

            return jsonify({
                'success': True,
                'created': state.id,
                'states': current_states,
                'total_states': len(State.query.all())
            })

        except:
            abort(422)

        
    @app.route('/states/<int:state_id>')
    def get_specific_state(state_id):
        state = State.query.filter(State.id == state_id).one_or_none()
        if state:
            return jsonify({
                'success': True,
                'state': state.format()
            })
        else:
            abort(404)
            
    @app.route('/states/<int:state_id>', methods=['DELETE'])
    def delete_state(state_id):
        try:
            state = State.query.filter(State.id == state_id).one_or_none()

            if state:
                state.delete()
                selection = State.query.order_by(State.id).all()
                current_states = paginate_states(request, selection)
                total_states = State.query.all()

                return jsonify({
                    'success': True,
                    'deleted': state_id,
                    'states': current_states,
                    'total_states': len(total_states)
                })
        except BaseException:
            abort(404)

            
    @app.route('/states/<int:state_id>', methods=['PATCH'])
    def update_state(state_id):
        body = request.get_json()

        try:
            state = State.query.filter(State.id == state_id).one_or_none()
            if state is None:
                abort(404)

            if 'governor' in body:
                state.governor = body['governor']
                state.update()

                return jsonify({
                    'success': True,
                    'id': state.id
                })
        except:
            abort(400)

    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        jsonify({
            'success': False,
            'error': 422,
            'message': "unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        jsonify({
            'success': False,
            'error': 400,
            'message': "bad request"
        }), 400

        
    return app