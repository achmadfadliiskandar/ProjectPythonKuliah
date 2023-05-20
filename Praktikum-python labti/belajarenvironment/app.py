from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/about')
def about():
    nama = 'Achmad Fadli Iskandar\t'
    kelas = '1IA04'
    return nama + kelas

if __name__ == '__main__':
    app.run(debug=True)