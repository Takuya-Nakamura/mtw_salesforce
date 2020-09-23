from pprint import pprint as p
from lib.mt_salesforce import MtSalesForce
import sys
from util import * 

# AccountCategory2Address__c = a01N000000MSHP8IAP
def main():
    """ account_category2_address__c_id指定で、account_categoryを取得する
    """

    args = sys.argv
    check_args(args, 1)
    account_category2_address_id = args[1]
    
    msf = MtSalesForce()
    soql = "SELECT Id,Name,MstCategory__c,Other__c,IsPrimary__c FROM AccountCategory__c WHERE AccountCategory2Address__c='%s'" %(account_category2_address_id)
    
    response =msf.query(soql)
    p(response)
    return response


if __name__ == "__main__":
    main()



