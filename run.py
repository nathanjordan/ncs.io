from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

app.debug = True

# Serves homepage
@app.route('/')
def homepage():
	return render_template('index.html')	

# Serves static resources like css, js, images, etc.
@app.route('/assets/<path:resource>')
def serveStaticResource(resource):
    # Return the static file
    return send_from_directory('static/assets/', resource)

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
