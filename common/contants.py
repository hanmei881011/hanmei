import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir,"datas")
case_file = os.path.join(data_dir,"loantest.xlsx")

conf_dir = os.path.join(base_dir,"config")
global_dir = os.path.join(conf_dir,"global.conf")
loan_dir = os.path.join(conf_dir,"loan.conf")
test_dir = os.path.join(conf_dir,"test2.conf")

logs_dir = os.path.join(base_dir,"logs")
log_dir = os.path.join(logs_dir,"case.log")

testcase_dir = os.path.join(base_dir,"testcase")

reports_dir = os.path.join(base_dir,"report")
report_html = os.path.join(reports_dir,"report.html")

if __name__ == '__main__':
    print(base_dir)
    print(data_dir)
    print(case_file)