from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce
import sys
from util import * 


def main():
    """ 指定Accountの勤務先取得
    """

    args = sys.argv
    check_args(args, 1)
    
    msf = LibMtSalesForce()
    
    soql = "SELECT (SELECT Name, AddressClass__c, MstWorkClassId__c, EmpName__c, EmpClass__c, Zip__c, Pref__c, City__c, Address__c, Building__c, Tel__c FROM AccountAddresses__r)  " \
        "FROM Account WHERE Id ='%s'" %(args[1])
    
    response =msf.query(soql)
    p(response)
    return response


if __name__ == "__main__":
    main()



