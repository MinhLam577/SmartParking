from flask import Flask, render_template, request, jsonify
from controllers.biensoxe_controller import product_bp
from controllers.user_controller import user_bp
from controllers.led_controller import led_bp
from flask_mail import Message
import os
from auth.autho import configure_jwt
from flask_mail import Mail
from models.user import User
from flask_cors import CORS, cross_origin
import requests
app = Flask(__name__)
CORS(app, supports_credentials=True)

# Cấu hình đối tượng
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'nguyenhuynhan.dn@gmail.com'
app.config['MAIL_PASSWORD'] = 'rkif gdqq cdwk tqmj'
app.config['MAIL_USE_TLS'] = True
model = User()
# Khởi tạo đối tượng Mail
mail = Mail(app)
configure_jwt(app)
# app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(product_bp, url_prefix='/biensoxe')
app.register_blueprint(led_bp, url_prefix='/led')
# đăng kí


@app.route('/user/adduser', methods=['POST'])
def register():
    gmail = request.json['gmail']
    password = request.json['password']
    role = 'user'
    if model.check_user_existence(gmail):
        return jsonify({'message': 'User already exists'}), 409
    else:
        try:
            role = "user"
            model.create_user(gmail, password, role)
            msg = Message("Đăng kí Tài Khoản Website Thành Công ",
                          sender='nguyenhuynhan.dn@gmail.com', recipients=[gmail])
            msg.body = f"Username:{gmail}  \nPassword: {password} "
            mail.send(msg)
            # send_registration_email(gmail, password)
            return jsonify({'message': 'User registered successfully'}), 201
        except Exception as e:
            return jsonify({'error': 'Failed to register user', 'details': str(e)}), 500


# Hàm tiện ích để cung cấp đối tượng mail cho controller
app.register_blueprint(user_bp, url_prefix='/')
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 4000))
    app.run(debug=True, host='localhost', port=port)
