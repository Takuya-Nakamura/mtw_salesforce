from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce

import sys
from util import *


def main():
    args = sys.argv
    check_args(args, 1)

    msf = LibMtSalesForce()
    soql = "SELECT Id,AddressClass__c,EmpDepartment__c,MstWorkClassId__c,EmpName__c,EmpClass__c,Zip__c,Pref__c,City__c,Address__c,Tel__c,isShippingAddressOfMT__c,shisetsu_code__c,checkFlag__c FROM Address__c WHERE AccountId__c='%s'" % (
        args[1])

    response = msf.query(soql)
    p(response)
    return response


if __name__ == "__main__":
    main()
