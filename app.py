import json
from flask import Flask, request, Response

import DeerIO

app = Flask(__name__)


@app.route('/', methods=['GET'])
def search():
	query = request.args.get('q')
	out_of_stock = request.args.get('outofstock', False)

	search_result = DeerIO.search(query, out_of_stock=out_of_stock)
	response = Response(json.dumps(search_result))

	response.headers['Access-Control-Allow-Origin'] = '*'

	return response


if __name__ == '__main__':
	try:
		app.run(host='0.0.0.0', port=8080)
	except KeyboardInterrupt as e:
		pass
