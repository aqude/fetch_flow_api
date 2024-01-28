"""Console script for fetch_flow_api."""
import argparse
import sys

from fetch_flow_api import process_data


def main():
    """Console script for fetch_flow_api."""
    parser = argparse.ArgumentParser()
    parser.add_argument('getLink', type=str, help='URL для получения данных')
    parser.add_argument('outputfile', type=str, help='Имя файла для сохранения данных')
    parser.add_argument('proxylist', type=str, help='Имя файла с прокси')
    parser.add_argument('limit', type=int, help='Лимит запросов')

    args = parser.parse_args()
    getLink, outputfile, proxylist, limit = args.getLink, args.outputfile, args.proxylist, args.limit
  
    data = process_data(getLink, outputfile, proxylist, limit)
    print(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
