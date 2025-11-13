from flask import Flask
import sys

app = Flask(__name__)

search_values: list[str] = []


@app.route("/")
def home():
    # Just for reference
    return search_values


def load_search_values():
    file_path = "./example.txt"  # Default
    if len(sys.argv) > 1:
        file_path = sys.argv[1]

        with open(file_path, "r") as file:
            global search_values
            search_values = file.read().splitlines()


def main():
    try:
        load_search_values()
    except Exception as e:
        print(e)
        return

    app.run(host="localhost", port=5155)


if __name__ == "__main__":
    main()
