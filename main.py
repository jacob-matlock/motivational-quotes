from flask import Flask, request, jsonify
import random


app = Flask(__name__)

quotes_used = set()


def generate_quotes(num) -> list:
    """select num of quotes randomly from quotes.txt"""

    quotes_list = []
    with open("quotes.txt", "r") as file:
        content = file.read()

    global quotes_used
    quotes = content.splitlines()

    if len(quotes_used) <= len(quotes):
        quotes_used.clear()

    quotes_available = list(set(quotes).difference(quotes_used))
    quotes_list = random.sample(quotes_available, num)
    quotes_used.update(quotes_list)

    return quotes_list

@app.get('/quotes/<int:num_quotes>')
def get_quotes(num_quotes):
    """ GET request from client requesting quotes
        Return number of quotes to client 
    """
    quote_list = generate_quotes(num_quotes) #implement func

    return jsonify(quote_list), 200




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1400, debug=True)
