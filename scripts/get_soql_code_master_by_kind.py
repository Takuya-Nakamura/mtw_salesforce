from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce

import sys
from util import * 


def main():
    """  codeKindを指定してCodeMasterを取得する
        # code_kindの例
        akasatana
        position
        work_division
    """


    args = sys.argv
    check_args(args, 1)
    
    msf = LibMtSalesForce()
    soql = "SELECT Id, CodeKind__c, Code__c, Kubun__c, Name, ValueKana__c, ValueEng__c FROM CodeMaster__c " \
        "WHERE CodeKind__c = '%s'" %(args[1])

    response =msf.query(soql)
    p(response)
    return response


if __name__ == "__main__":
    main()



