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

@app.route("/search", methods=["GET"])
def search():
    data= request.args
    query = request.args.get("query", "")
    caseless_query = query.lower()
    
    case_option = data.get("caseSensitive", "false") # If none in URL, then the default is false
    case_sensitive = case_option.lower() == "true" 
    req_options = {
        "caseSensitive":case_sensitive
    }

    results = []
    for line in search_values:   #search Iteration
        if case_sensitive:        # Case sensitivity true
            if query in line:
                results.append(line)
        else:                    # Case sensitive false
            if caseless_query in line.lower():
                results.append(line)
                
    return {
        "query": query,
        "options": req_options,
        "results": results
    }
    


def main():
    try:
        load_search_values()
    except Exception as e:
        print(e)
        return

    app.run(host="localhost", port=5155)


if __name__ == "__main__":
    main()
