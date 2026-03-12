import sys
import webbrowser
import requests

def search(title):
    search_url = "https://archive.org/advancedsearch.php"
    params = {
        "q": "title:({}) AND mediatype:(movies)".format(title),
        "fl[]": ["identifier", "title", "description"],
        "output": "json",
        "rows": 10,
        "page": 1,
    }
    resp = requests.get(search_url, params=params)
    data = resp.json()
    docs = [(doc["identifier"], doc["title"], doc["description"]) for doc in data["response"]["docs"]]
    return docs

def choose(docs):
    last = len(docs) - 1
    for num, doc in enumerate(docs):
        print(f"{num}: ({doc[1]}) {doc[2][:30]}")
    index = input(f"Which would you like to see (0 to {last})?")
    try:
        return docs[int(index)][0]
    except:
        return None
    
def display(identifier):
    details_url = "https://archive.org/details/{}".format(identifier)
    print("Loading", details_url)
    webbrowser.open(details_url)

def main(title):
    identifiers = search(title)
    if identifiers:
        identifier = choose(identifiers)
        if identifier:
            display(identifier)
        else:
            print("Nothing selected")
    else:
        print("Nothing found for", title)

if __name__ == "__main__":
    main(sys.argv[1])