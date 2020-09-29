from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce

import sys
from util import *


def main():
    args = sys.argv
    check_args(args, 2)
    msf = LibMtSalesForce()
    id = args[1]
    session_id__c = args[2]
    api_path = 'sobjects/Account/%s?_HttpMethod=PATCH' % (id)
    payload = {
        "SessionId__c": session_id__c
    }
    response = msf.http_request(api_path, method='POST', data=payload)
    return response.content.decode()  # byte->string


if __name__ == "__main__":
    main()
