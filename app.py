# This app uses Laurence's API to give users information on a variety of food items. 
# PLEASE RERUN THE APP TO USE IT AGAIN.


import requests

url = "https://192.168.1.29:8000/"

usr_input = input("Welcome to the ultimate food compendium, what information may you seek today? \n a -- a full list of all available foods \n b -- specific info on one food only (PLEASE PROVIDE THE NAME WITH THE FIRST LETTER CAPITALIZED) \n > ")


if usr_input == "a":
    source = "https://192.168.1.29:8000/foodname?api_key=alicealice"
    response = requests.get(url=source)
    data = response.json()
    print(data)

elif usr_input == "b":
    prompt = input("What food would you like to view? \n> ")
    source = f"https://192.168.1.29:8000/foodname/{prompt}?api_key=alicealice"
    response = requests.get(url=source)
    data = response.json()
    print(data)