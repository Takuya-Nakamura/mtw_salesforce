from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce

import sys
from util import * 

def main():
    args = sys.argv
    check_args(args, 1)
    
    msf = LibMtSalesForce()
    soql = "Select CreatedDate, AccountPoint2Account__c, Point_i__c, Comment_c__c FROM AccountPoint__c WHERE IsDeleted = FALSE AND AccountPoint2Account__c = '%s' AND CreatedDate >= 2018-04-01T00:00:00+09:00 order by CreatedDate" %(args[1])
    
    response =msf.query(soql)
    p(response)
    return response


if __name__ == "__main__":
    main()



