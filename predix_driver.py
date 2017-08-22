import os


class PredixDriver():
    """Predix driver for Bofo project

    """
    def __init__(self):
        username = 'zhi.zhao@ge.com'
        password = 'CTC1349sso~'
        os.system('cf login -a https://api.system.aws-usw02-pr.ice.predix.io -u zhi.zhao@ge.com -p CTC1349sso~')


    def power_on(self):



