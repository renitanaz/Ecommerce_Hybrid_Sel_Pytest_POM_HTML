import configparser
config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        pwd = config.get('common info','password')
        return pwd