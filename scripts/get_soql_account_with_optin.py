from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce
import sys
from util import * 


def main():
    """ 指定Accountのオプトイン情報取得
        001N000001HsLSUIA3
    """

    args = sys.argv
    check_args(args, 1)
    
    msf = LibMtSalesForce()
    soql = "SELECT (SELECT Id, OptinCP2CP__c FROM AccountOptinCPs__r) " \
        "FROM Account WHERE Id ='%s'" %(args[1])
    
    response =msf.query(soql)
    p(response)
    return response


if __name__ == "__main__":
    main()



