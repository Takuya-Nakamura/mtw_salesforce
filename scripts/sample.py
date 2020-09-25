from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce  


def main():
    p("main")
    msf = LibMtSalesForce()
    
    p(msf.query("SELECT Id, Name FROM Organization"))


if __name__ == "__main__":
    main()
