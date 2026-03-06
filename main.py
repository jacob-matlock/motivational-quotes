from flask import Flask, jsonify
import random


app = Flask(__name__)

quotes_used = set()


def generate_quotes(num: int) -> list:
    """
    This function selects a number of quotes randomly from quotes.txt based on the num provided. The function is
    responsible for communicating with the global set quotes_used to ensure that no quote is used twice before
    each quote is used once.
    """

    quotes_list = []
    with open("quotes.txt", "r", encoding="utf-8") as file:
        content = file.read()

    global quotes_used
    quotes = content.splitlines()

    if len(quotes_used) >= len(quotes):
        quotes_used.clear()

    quotes_available = list(set(quotes).difference(quotes_used))
    quotes_list = random.sample(quotes_available, num)
    quotes_used.update(quotes_list)

    return quotes_list

@app.get('/quotes/<int:num_quotes>')
def get_quotes(num_quotes):
    """
    This is an endpoint for a GET request from a client requesting quotes. An integer must be provided in order for the
    microservice to do any work.

    Return number of quotes to client.
    """

    if not isinstance(num_quotes, int) or num_quotes <= 0:
        return jsonify({"error": "Number of Quotes Must Be a Positive Integer"}), 400

    quote_list = generate_quotes(num_quotes)

    return jsonify(quote_list), 200




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1400, debug=True)
