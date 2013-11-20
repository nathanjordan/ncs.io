from flask import Flask, render_template, send_from_directory, send_file

app = Flask(__name__)

app.debug = True

# Serves homepage
@app.route('/')
def homepage():
	return render_template('index.html')	

# Serves user documentation
@app.route('/docs/')
def serve_documentation_homepage():
	# Return index page
	return send_file('static/docs/index.html')

@app.route('/docs/<path:resource>')
def serve_documentation(resource):
    # Return the static file
    if resource[len(resource)-1:] == '/':
        resource = resource + 'index.html'
    return send_from_directory('static/docs/', resource)

# Serves static resources like css, js, images, etc.
@app.route('/assets/<path:resource>')
def serve_static_content(resource):
    # Return the static file
    return send_from_directory('static/assets/', resource)

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
