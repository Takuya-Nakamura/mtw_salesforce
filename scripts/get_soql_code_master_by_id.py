from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce
import sys
from util import * 


def main():
    """ CodeMasterからID指定でNameを取得 
    """

    args = sys.argv
    check_args(args, 1)
    id = args[1]
    
    msf = LibMtSalesForce()
    soql = "SELECT Name FROM CodeMaster__c WHERE Id='%s'" %(id)
    
    response =msf.query(soql)
    p(response)
    return response


if __name__ == "__main__":
    main()



