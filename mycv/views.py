from mycv.application import app

@app.route('/')
def entry_point():
    return 'Hello World!'