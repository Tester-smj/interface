import json,python_utils
def __get_token_header(self):
    """
    生成token头部
    :return:
    """
    des = self.__get_token_des()
    arr = (des, self.conf['systemType'], self.conf['Model'], self.conf['Release'], self.conf['DeviceId'],
           self.conf['versionCode'], self.conf['versionName'], self.conf['AppBuild'], self.conf['DeviceOS'], "0")
    authorization = self.AUTHORIZATION_TOKEN % arr
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'Authorization': authorization}
    response = self.session.post(self.conf['getTokenHost'], headers=headers)
    if json.loads(response.text)['StatsCode'] == 200:
        data1 = json.loads(response.text)['Data']
        self.time = data1['Time']
        self.TOKEN_NAME = data1['TokenName']
        self.TOKEN_VALUE = data1['TokenValue']
    else:
        print("GetToken失败，请手动检查")
        utils.HandleJson.HandleJson.print_json(response.text)

def __login_session(self):
    """
    调用登录接口，这样后面的接口都能正常访问了
    :return:
    """
    url_login = self.conf['loginHost']
    headers = self.__get_session_header(url_login.split('api/')[-1])
    data_login = r'%s' % self.conf['loginInfo']
    response = self.session.post(url_login, headers=headers, data=data_login)
    if json.loads(response.text)['StatsCode'] == 200:
        data1 = json.loads(response.text)['Data']
        self.uId = data1[self.head_uid]
        self.uName = data1['NickName']
        self.uPhone = data1['Phone']
        self.SessionId = data1['Sid']
        self.uType = data1['UserType']
        self.uuid = data1['UID']
    else:
        print("登录失败，请手动检查")
        utils.HandleJson.HandleJson.print_json(response.text)