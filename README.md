# CS 361 Search Microservice

A Flask microservice to search a pre-determined list of entries.

## Search results

Search results are loaded from a plain text file given at startup. If no file is selected upon startup, a default demo
file will be used.

## API

Routes:

- Search

The API opens at the address <http://localhost:5155/> by default.

### Search

> POST `/search`

Given a search query and options, return back the query and options with a list of matched strings.

EXAMPLE CALL:

```py
requests.post("http://localhost:4820/search", json={"query": "sun"})
requests.post("http://localhost:4820/search", json={"query": "sun", "options": {"caseSensitive": false}})
```

EXAMPLE OUTPUTS:

```json
{
  "query": "sun",
  "options": {},
  "results": ["sun", "sunny"]
}
```

```json
{
  "query": "sun",
  "options": {
    "caseSensitive": false
  },
  "results": ["sun", "sunny", "Sunday"]
}
```

## Installation

This program requires additional libraries to function. This installation shows the steps to install the requirements
via pip inside a virtual environment.

> [!WARNING]  
> _The command to enter the Python Virtual environment differs by operating system. You can [check the full
> list](https://docs.python.org/3/library/venv.html#how-venvs-work) for your specific command. The POSIX version is listed
> in this example._

### Prerequisites

To run this program you must have Python 3 and pip installed. You can verify that the programs are installed with the
following command:

```bash
python3 --version
pip --version
```

### Initial setup

Create a virtual environment:

```bash
python3 -m venv env
```

Enter the virtual environment and install the dependencies:

```bash
source env/bin/activate
pip install -r requirements.txt
```

The requirements should now be installed into the virtual environment and the program can be run whenever you are within
this virtual environment.

### Running the program

Enter the virtual environment if not already inside:

```bash
source env/bin/activate
```

Run the program:

```bash
python3 src/main.py

```
