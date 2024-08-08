# -----------------------------------------------------------------------------
# © 2024 Kareem Mangood. All Rights Reserved.
# -----------------------------------------------------------------------------

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Shared in-memory state
current_number = 0
MAX_NUMBER = 100
support_numbers = {
    1: None,
    2: None,
    3: None
}

@app.route('/support/<int:support_id>')
def support_page(support_id):
    if support_id not in support_numbers:
        return 'Support ID not found', 404
    return render_template('support.html', support_id=support_id)

@app.route('/user')
def user_page():
    return render_template('user.html')

@app.route('/support/<int:support_id>/next', methods=['POST'])
def get_next_number(support_id):
    global current_number
    if support_id not in support_numbers:
        return 'Support ID not found', 404

    if current_number >= MAX_NUMBER:
        return 'No more numbers available.', 400

    current_number += 1
    support_numbers[support_id] = current_number
    return jsonify({'next_number': current_number})

@app.route('/current_numbers')
def get_current_numbers():
    return jsonify(support_numbers)

@app.route('/current_number')
def get_current_number():
    return jsonify({'current_number': current_number})

if __name__ == '__main__':
    app.run(debug=True)
