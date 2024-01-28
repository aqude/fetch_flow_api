"""Console script for fetch_flow_api."""
import argparse
import sys

from fetch_flow_api.fetch_flow_api import process_data


def main():
    """Console script for fetch_flow_api."""
    parser = argparse.ArgumentParser()
    parser.add_argument('getLink', type=str, help='URL для получения данных')
    parser.add_argument('outputfile', type=str, nargs='?', default='customs_data.csv', help='Имя файла для сохранения данных')
    parser.add_argument('limit', type=int, nargs='?', default=10, help='Лимит запросов (необезательный (10))')
    parser.add_argument('proxylist', type=str, nargs='?', default='', help='Имя файла с прокси (необязательный)')
    

    args = parser.parse_args()
    getLink, outputfile, proxylist, limit = args.getLink, args.outputfile, args.proxylist, args.limit
  
    process_data(getLink, outputfile, proxylist, limit)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
