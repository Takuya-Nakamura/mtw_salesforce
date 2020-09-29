from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce
import sys
from util import *


def main():
    """ Pointの更新
        id:001N000001HsLSUIA3
        displacement:-100 // 変更する値 (現在のポイントから-100)とか
        bikou: Amazon
    """

    args = sys.argv
    check_args(args, 3)

    msf = LibMtSalesForce()

    api_path = 'accountpoint/?id=%s&displacement=%s&bikou=%s' % (
        args[1], args[2], args[3])
    payload = {}
    response = msf.apexecute(api_path, method='GET', data=payload)
    p(response)

    return response


if __name__ == "__main__":
    main()
