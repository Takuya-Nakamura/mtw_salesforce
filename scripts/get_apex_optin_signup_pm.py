from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce
import sys
from util import *


def main():
    """ optin_signup
    apexはOptinStatus__cをtrueにして、その後の値を返す
    """

    args = sys.argv
    check_args(args, 1)
    account_id = args[1]

    msf = LibMtSalesForce()

    api_path = 'optin/signup/pm/?id=%s' % (account_id)
    payload = {}
    response = msf.apexecute(api_path, method='GET', data=payload)
    p(response)

    return response


if __name__ == "__main__":
    main()
