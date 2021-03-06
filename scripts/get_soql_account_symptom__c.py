from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce

import sys
from util import *


def main():
    args = sys.argv
    check_args(args, 1)

    msf = LibMtSalesForce()
    soql = "SELECT Id,Name,MstSymptom__c,Other__c FROM AccountSymptom__c WHERE AccountSymptom2Account__c='%s'" % (
        args[1])

    response = msf.query(soql)
    p(response)
    return response


if __name__ == "__main__":
    main()
