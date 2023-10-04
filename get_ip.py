import socket
import requests
COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m", 
    "GREEN": "\033[32m",     
    "YELLOW": "\033[93m",    
    "RED": "\033[31m",       
    "CYAN": "\033[36m",     
    "BOLD": "\033[01m",        
    "PINK": "\033[95m",
    "URL_L": "\033[36m",       
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m",     
}

def get_ip():
    ip = input(f'{COLOR_CODE["GREEN"]}[!]Введите айпи:' )

    try:
        ip = socket.gethostbyname(ip)
        
        infoList1 = requests.get(f"http://ipwho.is/{ip}")
        infoList = infoList1.json()
        
        if infoList.get("success"):
            print(f'{COLOR_CODE["GREEN"]}╔══════════════                     ══════════════╗\n')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Айпи адресс:{COLOR_CODE["YELLOW"]}  {infoList["ip"]}')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Успех:{COLOR_CODE["YELLOW"]}  {infoList["success"]}  ')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Тип:{COLOR_CODE["YELLOW"]}   {infoList["type"]}     ')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Континент:{COLOR_CODE["YELLOW"]}   {infoList["continent"]}')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Страна:{COLOR_CODE["YELLOW"]}   {infoList["country"]}')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Регион:{COLOR_CODE["YELLOW"]}   {infoList["region"]}')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Город:{COLOR_CODE["YELLOW"]}   {infoList["city"]}')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Почтовый код:{COLOR_CODE["YELLOW"]}   {infoList["postal"]}')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Столица:{COLOR_CODE["YELLOW"]}  {infoList["capital"]}\n')
            print(f'{COLOR_CODE["RED"]}╚══════════════                     ══════════════╝\n')

            
        else:
            print(f'{COLOR_CODE["RED"]}╔══════════════                     ══════════════╗\n')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} IP:{COLOR_CODE["YELLOW"]}  {infoList["ip"]}')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Success:{COLOR_CODE["YELLOW"]}   {infoList["success"]}')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["PINK"]}{COLOR_CODE["GREEN"]} Message:{COLOR_CODE["YELLOW"]}  {infoList["message"]}')
            print(f'{COLOR_CODE["RED"]}╚══════════════                     ══════════════╝\n')
    except Exception as e:
        print(f'An error occurred: {e}')



