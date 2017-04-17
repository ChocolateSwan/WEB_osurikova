
def app(environ, start_response):

	output = 'Hello, World !!!\n'
	output += 'Request Method: ' + environ['REQUEST_METHOD'] + '\n'

	# GET
	if environ['REQUEST_METHOD'] == 'GET' and environ['QUERY_STRING']:
		output += 'Options:\n' + environ['QUERY_STRING'].replace('&', '\n') +'\n'

	# POST
	if environ['REQUEST_METHOD'] == 'POST' and environ['wsgi.input'] :
		output+= 'Options:\n' + environ['wsgi.input'].read().decode('utf-8').replace('&', '\n') + '\n'

	start_response("200 OK", [
	    ("Content-Type", "text/plain"),
	    ("Content-Length", str(len(output)))
	])
	output = output.encode('utf-8')
	return [output]








