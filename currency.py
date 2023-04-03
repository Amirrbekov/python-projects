import requests


api_key = "2QvwSImI3rMywZ1kgz3wQZkmJyDERxrM"

url ="http://data.fixer.io/api/latest?access_key=" + api_key
    

first_currency = input("From currency :") # Ex : USD
second_currency = input("To currency :") # Ex : EUR
amount = int(input("Miktar:")) # Ex : 15

response = requests.get(url)

infos = response.json()


firstValue = infos["rates"][first_currency]
secondValue = infos["rates"][second_currency]

print((secondValue / firstValue) * amount)