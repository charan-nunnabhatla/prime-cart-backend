from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import sqlite3

path = './prime_cart_products.db'
conn = sqlite3.connect(path, check_same_thread=False)


app = Flask(__name__)
CORS(app)

#post methods to return selected products form db
@app.post('/about' )
def getTitle():
    data = request.json
    # data = json.loads(data)
    title = data['title']
    print(title)
    df = pd.read_sql(f'select * from amazon_products where title like "%{title}%" limit 10', conn)
    # conn.close()
    print(len(df.to_dict(orient='records')))
    # print(df.to_dict())
    df = df.astype(object).to_dict()
    products = []
    for i in range(len(df['asin'])):
        product = {key: df[key][i] for key in df}
        products.append(product)
    print(products)
    
    return jsonify(products)

app.run('0.0.0.0', 5000, True)

