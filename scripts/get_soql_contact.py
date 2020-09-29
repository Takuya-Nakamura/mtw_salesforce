from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce

import sys
from util import * 

def main():
    args = sys.argv
    check_args(args, 1)
    account_id = args[1]

    msf = LibMtSalesForce()
    soql = "SELECT Id From Contact Where AccountId='%s'" %(account_id)
    response =msf.query(soql)
    p(response)
    return response


if __name__ == "__main__":
    main()



