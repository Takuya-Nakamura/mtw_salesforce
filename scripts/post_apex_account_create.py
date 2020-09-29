from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce
import sys
from util import *


def main():
    """ Account作成
    """

    # args = sys.argv
    # check_args(args, 0)
    msf = LibMtSalesForce()

    api_path = 'account/create/'
    payload = {}
    response = msf.apexecute(api_path, method='POST', data=payload)
    p(response)

    return response


if __name__ == "__main__":
    main()
