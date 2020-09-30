from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce
import sys
import json
from util import *


def main():
    """ 
    """
    # TODO: パラメータでjson取得
    file = open('./data/post_sobject.json', 'r')
    data = json.load(file)

    args = sys.argv
    check_args(args, 1)
    object_name = args[1]
    msf = LibMtSalesForce()

    api_path = 'sobjects/%s/' % (object_name)
    response = msf.http_request(api_path, method='POST', data=data)
    p(response)
    return response.content.decode()  # byte->string


if __name__ == "__main__":
    main()
