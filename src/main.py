from typing import Dict
from flask import Flask, request
import sys

app = Flask(__name__)

search_values: list[str] = []


def load_search_values():
    file_path = "./example.txt"  # Default
    if len(sys.argv) > 1:
        file_path = sys.argv[1]

    with open(file_path, "r") as file:
        global search_values
        search_values = file.read().splitlines()


@app.route("/all-values")
def home():
    return {
        "values": search_values,
        "count": len(search_values),
    }


@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    if not isinstance(data, dict):
        return "Invalid request", 400

    query = data.get("query", "")
    options = data.get("options", {})

    case_sensitive = options.get("caseSensitive", True)
    caseless_query = query.lower()
    results = []
    for line in search_values:  # search Iteration
        if case_sensitive:  # Case sensitivity true
            if query in line:
                results.append(line)
        else:  # Case sensitive false
            if caseless_query in line.lower():
                results.append(line)

    return {"query": query, "options": options, "results": results}


def main():
    try:
        load_search_values()
    except Exception as e:
        print(e)
        return

    app.run(host="localhost", port=5155)


if __name__ == "__main__":
    main()
