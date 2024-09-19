from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_email_id="Email"
    textbox_password_id="Password"
    button_login_Xpath="//button[normalize-space()='Log in']"
    link_logout_linktext="Logout"

    # capture driver from TC and assign it to the class variable, driver.
    def __init__(self,driver):
        self.driver=driver


    def setUserName(self,email_id):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID,self.textbox_email_id).send_keys(email_id)

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def ClickLoginButton(self):
        self.driver.find_element(By.XPATH,self.button_login_Xpath).click()

    def ClickLogoutButton(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()