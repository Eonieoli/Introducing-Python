import webview

url = input("URL? ")

print(webview.create_window(f"webview display of {url}", url))
webview.start()