from selenium import webdriver
import pytest

@pytest.fixture()
def setup(request):
    browser_sel= request.config.getoption("--browser")
    if browser_sel =='chrome':
        driver = webdriver.Chrome()
    elif browser_sel == 'firefox':
        driver = webdriver.Firefox()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Type in browser name e.g. chrome OR firefox")

# @pytest.fixture()
# def browser(request): #this will return browser value to set up method
#     return request.config.getoption("--browser")

#pytest HTML Report
# hook to add environment info in HTML report
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Project Name'] = 'nop Commerce'
        config.stash[metadata_key]['Module Name'] = 'Customers'
        config.stash[metadata_key]['Tester'] = 'Ren'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)