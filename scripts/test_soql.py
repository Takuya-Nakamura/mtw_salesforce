from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce
import sys
from util import * 


def main():
    """ SOQLのテスト実行用。データの確認もこれが手っ取りばやい
    """

    
    msf = LibMtSalesForce()
    # soql = "SELECT Name FROM CodeMaster__c WHERE Id='%s'" %(id)    
    # soql = "SELECT Name, CodeKind__c FROM CodeMaster__c" 
    soql = "SELECT id FROM AccountSymptom__c"

    response =msf.query(soql)
    p(response)
    return response

if __name__ == "__main__":
    main()



