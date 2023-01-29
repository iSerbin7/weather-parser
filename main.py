import requests
import json

def read_json_file(file_name):
    try:
       with open(file_name, "r") as file:
            return json.load(file)
    except IOError:
        print("An IOError has occurred!")
    finally:
        file.close


link = read_json_file("settings.json")["url"]



response = requests.get(link).text

if __name__ == "__main__":
    print(response)