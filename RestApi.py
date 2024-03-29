from flask import request, Flask, jsonify, abort, make_response

app = Flask(__name__)

notes = [
    {
        'id': 1,
        'note': 'Aufgaben',
        'done': False
    },
    {
        'id': 2,
        'note': 'Einkaufen',
        'done': False
    }
]

# GET-Request fuer alle Notizen
@app.route("/notes", methods=['GET'])
def get_notes():
    return jsonify({'notes' : notes})

# GET-Request fuer jede einzelne Notiz
@app.route("/notes/<int:id>", methods=['GET'])
def get_note(id):
    note = [note for note in notes if note['id'] == id]
    if len(note) == 0:
        abort(404)
    return jsonify({'note' : note[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}),404)

# POST-Request
@app.route("/notes", methods=['POST'])
def create_note():
    if not request.json or not 'note' in request.json:
        abort(400)
    note = {
        'id': notes[-1]['id'] + 1,
        'note': request.json['note'],
        'done': False
    }
    notes.append(note)

    return jsonify({'note' : note}), 201

# PUT-Request
# Statuscode 405 - Server erlaubt die Methode nicht
@app.route("/notes/<int:id>", methods=['PUT'])
def update_note(id):
    note = [note for note in notes if note['id'] == id]
    print(note[0])
    if len(note) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    note[0]['done'] = request.json.get('done', note['done'])
    return jsonify({'note' : note[0]})

# DELETE-Request
# Statuscode 405 - Server erlaubt die Methode nicht
@app.route("/notes/<int:id>", methods=['DELETE'])
def delete_note(id):
    note = [note for note in notes if note['id'] == id]
    if len(note) == 0:
        abort(404)
        notes.remove(note[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(port=1337, debug=True)