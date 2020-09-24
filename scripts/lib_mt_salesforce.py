# import setting
from pprint import pprint as p
import os
import pickle  # object serialize
from simple_salesforce import Salesforce
from simple_salesforce.exceptions import *
import lib_mt_salesforce_settings as settings
import sys
import requests
import json
import functools
import time
from pathlib import Path

# from  util import *

""" clientの中身
{'apex_url': 'https://cs6.salesforce.com/services/apexrest/',
 'api_usage': {},
 'auth_site': 'https://test.salesforce.com',
 'auth_type': 'password',
 'base_url': 'https://cs6.salesforce.com/services/data/v42.0/',
 'bulk_url': 'https://cs6.salesforce.com/services/async/42.0/',
 'domain': 'test',
 'headers': {'Authorization': 'Bearer '
                              '00DN0000000AQ1U!AQQAQMx.fQbWJyJfnoBEIxSb5r2sbkOXh6JdVb8hkBgsTbMHGzWIOKOJWEEEVVHFnRwPedad2WylAZZTxswqmkF.HZu5LYjH',
             'Content-Type': 'application/json',
             'X-PrettyPrint': '1'},
 'proxies': {},
 'session': <requests.sessions.Session object at 0x10d95bb50>,
 'session_id': '00DN0000000AQ1U!AQQAQMx.fQbWJyJfnoBEIxSb5r2sbkOXh6JdVb8hkBgsTbMHGzWIOKOJWEEEVVHFnRwPedad2WylAZZTxswqmkF.HZu5LYjH',
 'sf_instance': 'cs6.salesforce.com',
 'sf_version': '42.0'}

"""


class LibMtSalesForce():
    """simple_salesforceを使うためのクラス
    """

    def __init__(self):
        self.token_expires = 100000  # tokenの有効期限秒
        self.load_wait = 3  # token_更新待ちの待機時間 
        
        file_dir = os.path.dirname(os.path.realpath(__file__))
        self.client_instance_file = '%s/access_object' % (file_dir)
        self.lock_file = '%s/access_object_lock' % (file_dir)
        self.load_client()

    ############################################
    # authnticatoion
    ############################################

    def load_client(self):
        """set simple_salesforce instance
        """
        #lockファイルが有る場合は一定秒wait
        if os.path.exists(self.lock_file):
            p("wait")
            time.sleep(self.load_wait)

        # ファイルが存在する。作成日からexpires秒経過していたら再認証する。
        p("self.isTokenExpired()")
        p(self.isTokenExpired())

        if os.path.exists(self.client_instance_file) == False or self.isTokenExpired():
            p("[Log]]Auth from Salesforce")
            self.authenticate()
            self.load_client()
        else:
            with open(self.client_instance_file, 'rb') as f:
                p("[Log]Auth from File")
                self.client = pickle.load(f)

    def authenticate(self):
        Path(self.lock_file).touch() #create lockfile
        sf = Salesforce(
            username=settings.SALESFORCE_USERNAME,
            password=settings.SALESFORCE_PASSWORD,
            security_token=settings.SALESFORCE_SECURITY_TOKEN,
            organizationId=settings.SALESFORCE_ORGANIZATION_ID,
            domain=settings.DOMAIN
        ) 
        with open(self.client_instance_file, 'wb') as f:
            pickle.dump(sf, f)
        os.remove(self.lock_file)

        

    def file_created_at(self, file):
        return os.path.getctime(file)


    def isTokenExpired(self):
        created_at = int(os.path.getctime(self.client_instance_file))
        now = int(time.time())
        return now - created_at > self.token_expires

    ############################################
    # public
    ############################################

    def query(self, soql, retry=0):
        func = functools.partial(self.client.query, soql)
        res = self._request_with_retry(func)
        return self.to_json(res['records'])  # dataだけ返す

    def apexecute(self, api_path, method, data):
        func = functools.partial(self.client.apexecute, api_path, method, data)
        return self.to_json(self._request_with_retry(func))

    # 戻り値はResponseオブジェクトを返すので、
    # 利用側でcontetnsからデータを取得する
    def http_request(self, api_path, method, data):
        func = functools.partial(self._http_request, api_path, method, data)
        return self._request_with_retry(func)

    ############################################
    # private
    ############################################


    # 関数(引数固定済み)を受け取ってそれを実行、
    # 認証失敗の場合、認証を取得し直して一定回数リトライする
    def _request_with_retry(self, func, *args, retry=0):
        try:
            return func()
        except SalesforceExpiredSession as e:
            p("[Log]SalesforceExpiredSession")
            if(retry < 2):
                os.remove(self.client_instance_file)
                self.load_client()
                return self._request_with_retry(func, retry=retry + 1)
            else:
                # TODO: log出力と通知
                p("[Log]retry stop")
                p(e)
        except Exception as e:
            # TODO: log出力と通知
            p("[Log]query Exception2")
            p(e)

    # simple_salesforceを使わない、リクエスト
    #
    def _http_request(self, api_path, method, data):
        """ ライブラリを使わないでシンプルにrequestを送る
        """
        path = self.client.base_url + api_path
        p("path")
        p(path)

        with requests.session() as s:
            response = s.request(
                method,
                path,
                headers=self.client.headers,
                cookies={'sid': self.client.session_id},
                json=data
            )
        # p(vars(response))
        return response

    def to_json(self, dict):
        return json.dumps(dict, ensure_ascii=False)
