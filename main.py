from flask import Flask, jsonify, request
import os

app = Flask(__name__)


@app.route('/', methods = ['POST'])
def index():
    order_data = request.get_json() # 

    mail = None

    if "机构管理员邮箱" in order_data:
        mail = order_data['机构管理员邮箱']
    
    if "管理员邮箱" in order_data:
        mail = order_data['管理员邮箱']

    return mail


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))