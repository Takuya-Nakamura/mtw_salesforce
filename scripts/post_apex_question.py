from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce
import sys
from util import * 


def main():
    """
    """

    args = sys.argv
    check_args(args, 1)
    content = args[1] #qid : { q1__c=n, q2__c=n...}のオブジェクト

    msf = LibMtSalesForce()
    
    api_path = 'simple_questionnaire/question/updater/' %(account_id)
    response = msf.apexecute(api_path, method='POST', data=content)
    p(response)
    
    return response


if __name__ == "__main__":
    main()



