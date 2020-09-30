from pprint import pprint as p
from lib_mt_salesforce import LibMtSalesForce
import sys
import json
from util import *


def main():
    """ Account作成
    """
    # TODO: パラメータでjson取得
    # dev ダミーデータ
    file = open('./data/post_apex_account_create.json', 'r')
    data = json.load(file)

    # args = sys.argv
    # check_args(args, 0)

    msf = LibMtSalesForce()

    api_path = 'account/create_with_relations/'
    payload = data
    response = msf.apexecute(api_path, method='POST', data=data)
    p(response)
    # 001N000001ypTXaIAM
    return response


if __name__ == "__main__":
    main()
