from pprint import pprint as p
from lib.mt_salesforce import MtSalesForce
import sys
from util import * 


def main():
    """ CodeMasterからID指定でNameを取得 
    """

    args = sys.argv
    check_args(args, 1)
    id = args[1]
    
    msf = MtSalesForce()
    soql = "SELECT Name FROM CodeMaster__c WHERE Id='%s'" %(id)
    
    response =msf.query(soql)
    p(response)
    return response


if __name__ == "__main__":
    main()



