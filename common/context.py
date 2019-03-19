from common.config import ReadConfig
import re

config = ReadConfig()

class Context():
    admin_user = config.get("data","admin_user")
    admin_pwd = config.get("data","admin_pwd")
    loan_member_id = config.get("data","loan_member_id")
    normal_user = config.get("data","normal_user")
    normal_pwd = config.get("data","normal_pwd")
    normal_member_id = config.get("data","normal_member_id")
def replace(s):
    p = "\$\{(.*?)}"
    while re.search(p, s):
        m = re.search(p,s)
        key = m.group(1)
        if hasattr(Context,key):
            value = getattr(Context,key)
            s = re.sub(p,value,s,count=1)
    return s