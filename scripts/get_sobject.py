from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce

import sys
from util import * 


def main():
    """ Object名を指定して/sobjects/オブジェクト名/' のsf_apiを実行する。
    """

    args = sys.argv
    check_args(args, 2) 

    object_name = args[1]
    id = args[2] # idが不要な場合もある..?
    msf = LibMtSalesForce()

    api_path = 'sobjects/%s/%s' %(object_name,id)
    payload = {}
    response = msf.http_request(api_path, method='GET', data=payload)
    return response.content.decode() # byte->string


if __name__ == "__main__":
    main()



