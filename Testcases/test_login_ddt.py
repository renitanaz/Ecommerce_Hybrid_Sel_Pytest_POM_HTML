import time

import pytest

from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen
from Utilities import XLUtils

class Test_001_DDT_Login:
        baseURL = ReadConfig.getApplicationURL()
        path=".//Testdata/LoginDetails.xlsx"
        logger=LogGen.loggen()

        @pytest.mark.sanity
        @pytest.mark.regression
        def test_login_ddt(self,setup):
            self.logger.info("********Test_001_DDT_Login**********")
            self.logger.info("********Verifying Login page Title**********")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.lp=LoginPage(self.driver)

            self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
            print('Number of rows...', self.rows)
            lst_status = []

            for r in range(2, self.rows + 1):
                self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
                self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
                self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

                self.lp.setUserName(self.user)
                self.lp.setPassword(self.password)
                self.lp.ClickLoginButton()
                time.sleep(5)

                act_title = self.driver.title
                exp_title = "Dashboard / nopCommerce administration"

                if act_title == exp_title:
                    if self.exp == 'Pass':
                        self.logger.info("**** passed ****")
                        self.lp.ClickLogoutButton()
                        lst_status.append("Pass")
                    elif self.exp == 'Fail':
                        self.logger.info("**** failed ****")
                        self.lp.ClickLogoutButton()
                        lst_status.append("Fail")

                elif act_title != exp_title:
                    if self.exp == 'Pass':
                        self.logger.info("**** failed ****")
                        lst_status.append("Fail")
                    elif self.exp == 'Fail':
                        self.logger.info("**** passed ****")
                        lst_status.append("Pass")
                print(lst_status)
            if "Fail" not in lst_status:
                self.logger.info("******* DDT Login test passed **********")
                self.driver.close()
                assert True
            else:
                self.logger.error("******* DDT Login test failed **********")
                self.driver.close()
                assert False

            self.logger.info("******* End of Login DDT Test **********")
            self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ");