"""Main module."""
import itertools
import time
import csv
import json
import requests
def process_data(getLink: str, outputfile: str, proxylist: str, limit: int):
    headers: list = getHeaders(getLink)
    createHeadersCsv(headers, outputfile)
    
    if not proxylist:
        nonProxyGetData(getLink, outputfile, limit, headers)
    else:
        _list: list = read_proxy_list(proxylist)
        proxyGetData(getLink, outputfile, limit, _list)

def read_proxy_list(filename: str):
    """
    Читает файл с прокси-серверами и возвращает список прокси.
    """
    try:
        with open(filename, 'r') as file:
            proxies = [line.strip() for line in file if line.strip()]
        return proxies
    except FileNotFoundError:
        print(f"Файл не найден: {filename}")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []

def write_to_csv(data, outputfile, headers: list):
    print(data)
    with open(outputfile, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerows(data)

def nonProxyGetData(getLink , outputfile: str, limit: int, headers: list):
    for page in range(1, limit + 1):
        try:
            response = requests.get(f"{getLink}?page={page}")
            response.raise_for_status()
            data = response.json()
            items = find_list_of_dicts(data)
            # Запись данных в CSV
            if items is not None:
                # Запись данных в CSV
                write_to_csv(items, outputfile, headers)
            else:
                print("Подходящие данные не найдены в ответе API.")

        except requests.RequestException as e:
            print(f"Ошибка запроса: {e}")
            break
        time.sleep(5)  # Пауза между запросами

def find_list_of_dicts(data):
    """
    Пытается найти и вернуть список словарей в данных.
    Возвращает None, если подходящий список не найден.
    """
    for key, value in data.items():
        if isinstance(value, list) and all(isinstance(item, dict) for item in value):
            return value
    return None

def proxyGetData(getLink: str, outputfile: str, limit: int, proxylist: list, headers: list):
    proxies_cycle = itertools.cycle(proxylist)
    for page in range(1, limit + 1):
        proxy = next(proxies_cycle)
        try:
            response = requests.get(f"{getLink}?page={page}", proxies={"http": proxy, "https": proxy})
            response.raise_for_status()
            data = response.json()
            items = find_list_of_dicts(data)
            if items is not None:
                # Запись данных в CSV
                write_to_csv(items, outputfile, headers)
            else:
                print("Подходящие данные не найдены в ответе API.")
            
        except requests.RequestException as e:
            print(f"Ошибка запроса через прокси {proxy}: {e}")
            continue



def createHeadersCsv(headers: list, outputfile: str):
    with open(outputfile, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        



def getHeaders(getLink: str) -> list:
    try:
        response = requests.get(getLink)
        response.raise_for_status()  # Проверяем, не вернул ли сервер код ошибки

        data = response.json()

        if isinstance(data, dict) and data:  
            items = next(iter(data.values()), [])
            if items and isinstance(items, list) and isinstance(items[0], dict):
                headers = items[0].keys()  # Получаем ключи из первого словаря в списке
            else:
                print("Данные не соответствуют ожидаемой структуре")
        
        return list(headers)

    except requests.exceptions.RequestException as e:
        print(f"Ошибка HTTP: {e}")
    except json.JSONDecodeError:
        print("Ошибка разбора JSON")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")

    return [] 