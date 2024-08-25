from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/bfhl', methods=['POST'])
def create_user_id():
    try:
        data = request.get_json().get('data', [])
        num = []
        alphabets = []

        for item in data:
            if item.isdigit():
                num.append(item)
            elif item.isalpha():
                if len(item) > 1:
                    return jsonify({"user_id": "ashar_ismail_06082001",
                                    "email": "ashar.681.ismail@gmail.com",
                                    "roll_number": "21BCE2216", "is_success": False}), 400
                alphabets.append(item)
            else:
                return jsonify({"user_id": "ashar_ismail_06082001",
                                "email": "ashar.681.ismail@gmail.com",
                                "roll_number": "21BCE2216", "is_success": False}), 400
        lowercase_alphabets = sorted(
            [char for char in alphabets if char.islower()])
        highest = lowercase_alphabets[-1] if lowercase_alphabets else None

        response = {
            "is_success": True,
            "user_id": "ashar_ismail_06082001",
            "email": "ashar.681.ismail@gmail.com",
            "roll_number": "21BCE2216",
            "numbers": num,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest] if highest else []
        }
        return jsonify(response)
    except:
        return jsonify({"user_id": "ashar_ismail_06082001",
                        "email": "ashar.681.ismail@gmail.com",
                        "roll_number": "21BCE2216", "is_success": False}), 400


@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({
        "operation_code": 1
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
