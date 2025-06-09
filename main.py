import os
from flask import Flask, jsonify
from flask_cors import CORS  # 解决跨域问题

app = Flask(__name__)
CORS(app)  # 允许所有域名访问（开发环境用，生产环境需限制）

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Railway!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
