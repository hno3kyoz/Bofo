import os



#login with predix

class predixAPI():

    def __init__(self):
        username='zhi.zhao@ge.com'
        password='CTC1349sso~'


    def login_in(self):
        os.system('cf login -a https://api.system.aws-usw02-pr.ice.predix.io -u zhi.zhao@ge.com -p CTC1349sso~')


    def check_apps(self):
        output = os.popen('cf apps')
        print(output.read())

    def upload_to_predix(self,message):



# import subprocess
#
# pipe = subprocess.Popen('ping 127.0.0.1', stdout=subprocess.PIPE)
# for line in iter(pipe.stdout.readline, ''):
#     print(line.rstrip())


PredixAPI.login_in()
PredixAPI.check_apps()
#关于微服务UAAtest
#
# zhideMacBook-Pro:~ zhizhao$ cf service UAAtest --guid
# 8e37919a-2d3f-4a43-b82b-c605f9130da6
