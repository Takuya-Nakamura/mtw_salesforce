from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce
import sys
from util import * 


def main():
    """ 指定Account項目一通り取得
    """

    args = sys.argv
    check_args(args, 1)
    
    msf = LibMtSalesForce()
    
    soql = "SELECT Id, MstMemberClassId__c, Name, LastName__c, FirstName__c, Kana__c, KanaSei__c, KanaMei__c, MailAddr__c, Sex__c, Birthday__c, Nickname__c, MstLicenseId__c, LicenseNumber__c, LicenseYear__c, MstUniversityId__c, UniversityOther__c, StudentMstUniversityId__c, StudentUniversityOther__c, StudentGraduationDay__c, StudentInternHospital__c, StudentWorkingForm__c, StudentHospitalDepartment__c, ImsMonitor__c, MailStatus__c, ResearchStatus__c, ConfStatus__c, MtPostFlag__c, PaidStatus__c, MtwMemberFlag__c, MtNumber__c, DcfNumber__c, DeliveryIds__c, Point__c, OptinStatus__c " \
    "FROM Account WHERE Id = '%s' AND deleteFlag__c = FALSE " %(args[1]) 

    
    response =msf.query(soql)
    p(response)
    return response


if __name__ == "__main__":
    main()



