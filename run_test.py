import unittest
import HTMLTestRunnerNew
from loan_hanmei.common import contants

discover = unittest.defaultTestLoader.discover(start_dir="testcase",pattern="test_*.py")

with open(contants.report_html,"wb+") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        title="API",
        description="This is my first report!",
        tester="hanmei"
    )
    runner.run(discover)