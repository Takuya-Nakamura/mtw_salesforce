from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce
import sys
from util import *


def main():
    """ AccountIDを指定して、Account情報を取得する
    """

    # https://cs6.salesforce.com/services/apexrest/account/with_relations/?id=001N000001HsLSUIA3
    args = sys.argv
    check_args(args, 1)

    account_id = args[1]
    msf = LibMtSalesForce()

    api_path = 'account/with_relations?id=%s' % (account_id)
    payload = {}
    response = msf.apexecute(api_path, method='GET', data=payload)
    p("Debug:")
    p(response)

    return response


if __name__ == "__main__":
    main()
