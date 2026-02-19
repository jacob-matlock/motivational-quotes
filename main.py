from flask import Flask, request, jsonify

app = Flask(__name__)

def generate_quotes(num):
    """select num of quotes randomly from quotes.txt""" 
    return 0

@app.get('/quotes/<num_quotes>')
def get_quotes():
    """ GET request from client requesting quotes
        Return number of quotes to client 
    """
    quote_list = generate_quotes(num_quotes) #implement func

    return jsonify(quote_list), 200




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1400, debug=True)
