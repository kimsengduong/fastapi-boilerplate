from uvicorn import run


def main():
    run("src.app:app", host="0.0.0.0", port=8000, reload=True)
