from fastapi import FastAPI


app = FastAPI(debug=True)


@app.get('/')
def pong():
    return {'message': 'pong'}
