from modal import App
from utils.helper import example_function

app = App(name="test-modal-app")

@app.function()
def main():
    print("Hello, Modal!")
    print(example_function())

if __name__ == "__main__":
    app.local_entrypoint()
