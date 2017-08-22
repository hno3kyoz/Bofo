
"""
init
"""
# INIT
import leancloud
leancloud.init("BCgp3kbWFgbelbNAVQASIJj5-gzGzoHsz",'YTmPEIiCypdathSkOzWMbCPR')
leancloud.use_region('CN') # 'US'
# using DEBUG MODEL
import logging
logging.basicConfig(level=logging.DEBUG)
# import os

# def get_Pi_IP():
#     response = os.popen('hostname -I')
#     ip_address = response.read()
#     return ip_address



# creat object
# TestObject = leancloud.Object.extend('BofoGauges')
# test_object= TestObject()
# test_object.set('IP_address','100.1.1.1')
# test_object.set('Gauge_NO','00001')
# test_object.save()



TestObject = leancloud.Object.extend('GaugeInfo')
test_object = TestObject.create_without_data('594c921a0ce463005750450e')
# 这里修改 location 的值
test_object.set('GaugeIP', '1.1.1.1')
test_object.save()
