from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce
import sys
from util import *


def main():
    """ optin_signup_cp
       :TODO DEBUG
    """

    args = sys.argv
    check_args(args, 1)
    product = args[1]

    msf = LibMtSalesForce()

    api_path = 'optin/signup/cp/'
    payload = {
        "product": product
    }
    response = msf.apexecute(api_path, method='POST', data=payload)
    p(response)

    return response


if __name__ == "__main__":
    main()
