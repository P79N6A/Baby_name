#!usr/bin/env python
# coding:GB18030

import urllib
import urllib2
from bs4 import BeautifulSoup


url = "http://life.httpcn.com/xingming.asp"

params = {}

# �������ͣ�0��ʾ������1��ʾũ��
params['data_type'] = "0"
params['year'] = "%s" % str(1985)
params['month'] = "%s" % str(12)
params['day'] = "%s" % str(24)
params['hour'] = "%s" % str(22)
params['minute'] = "%s" % str(23)
params['pid'] = "%s" % str("����")
params['cid'] = "%s" % str("����")
# ϲ�����У�0��ʾ�Զ�������1��ʾ�Զ�ϲ����
params['wxxy'] = "0"
params['xing'] = "%s" % "��"
params['ming'] = "־ǿ"
# ��ʾŮ��1��ʾ��
params['sex'] = "1"
params['act'] = "submit"
params['isbz'] = "1"

paramsData = urllib.urlencode(params)
request = urllib2.Request(url, paramsData)
response = urllib2.urlopen(request)
content = response.read()

soup = BeautifulSoup(content, 'html.parser')
print(soup)




