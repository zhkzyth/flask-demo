from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/', methods = ['POST'])
def index():
    order_data = request.get_json() # 
    return order_data['机构管理员邮箱']


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
