"""Main module."""
import csv
import json
import requests
def process_data(getLink: str, outputfile: str, proxylist: str, limit: int) -> list:
    headers: list = getHeaders(getLink)
    createHeadersCsv(headers, outputfile)
    if not proxylist:
        nonProxyGetData(getLink, outputfile)
    else:
        print("proxylist не пустой")

def write_to_csv(data, outputfile):
    if not data:
        return
    with open(outputfile, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writerows(data)

def nonProxyGetData(getLink, outputfile, limit):
    pass
def proxyGetData(getLink, outputfile, limit):
    pass

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