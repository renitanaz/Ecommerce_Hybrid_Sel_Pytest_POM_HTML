import time

import pytest

from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customlogger import LogGen

class Test_001_Login:
        baseURL = ReadConfig.getApplicationURL()
        username =ReadConfig.getUseremail()
        password =ReadConfig.getPassword()

        logger=LogGen.loggen()

        @pytest.mark.sanity
        @pytest.mark.regression
        def test_homepage_title(self,setup):
            self.logger.info("**********************Test_001_Login ***************")
            self.logger.info("********Verifying Home page Title**********")
            self.driver=setup
            self.driver.get(self.baseURL)
            act_title=self.driver.title
            if act_title=="Your store. Login":
                assert True
                self.driver.close()
                self.logger.info("********Home page Title TC is passed **********")
            else:
                self.driver.save_screenshot(".\\Screenshots\\"+"test_homepage_title.png")
                self.driver.close()
                self.logger.error("********Home page Title TC is failed **********")
                assert False

        @pytest.mark.regression
        def test_login(self,setup):
            self.logger.info("********Verifying Login page Title**********")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.lp=LoginPage(self.driver)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.ClickLoginButton()
            time.sleep(10)
            act_title=self.driver.title
            print(act_title)
            if act_title == "Dashboard / nopCommerce administration":
                assert True
                self.driver.close()
                self.logger.info("******** Login page Title TC is passed **********")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
                self.driver.close()
                self.logger.error("******** Login page Title TC is failed **********")
                assert False