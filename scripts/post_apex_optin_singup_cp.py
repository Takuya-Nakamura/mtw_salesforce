from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce
import sys
from util import *


def main():
    """
    """

    args = sys.argv
    check_args(args, 1)
    content = args[1]

    msf = LibMtSalesForce()

    api_path = 'optin/signup/cp/'
    response = msf.apexecute(api_path, method='POST', data=content)
    p(response)

    return response


if __name__ == "__main__":
    main()
