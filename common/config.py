import configparser
from common import contants

class ReadConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()  # 实例化一个对象
        self.config.read(contants.global_dir)
        open = self.config.getboolean("switch", "open")
        if open:
            self.config.read(contants.loan_dir)
            # value1 = config.get("api", "pre_url")
        else:
            self.config.read(contants.test_dir)
    def get(self,section,option):
        return self.config.get(section,option)
    def getboolean(self,section,option):
        return self.config.get(section,option)

if __name__ == '__main__':
    read = ReadConfig()
    pre_url = read.get("api","pre_url")
    print(pre_url)