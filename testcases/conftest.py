import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="class")
def setup(request, browser):
    global driver
    if browser == "chrome":
        # options = Options()
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser == "firefox":
        options = Options()
        options.add_argument("start-maximized")
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "edge":
        options = Options()
        options.add_argument("start-maximized")
        driver = webdriver.Edge(options=options, service=Service(EdgeChromiumDriverManager().install()))
        # driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())

    driver.get("https://www.yatra.com/")
    # driver.get(url)
    # driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")
@pytest.fixture(scope='class', autouse=True)
def browser(request):
    return request.config.getoption('--browser')
@pytest.fixture(scope='class', autouse=True)
def url(request):
    return request.config.getoption('--url')

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.rcvacademy.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time() * 1000))) + ".png"
            # file_name = report.nodeid.replace("::","_") + ".png"
            destination_file = os.path.join(report_directory, file_name)
            driver.save_screenshot(destination_file)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height:200px"'\
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra

def pytest_html_report_title(report):
    report.title = "RCV Academy Automation Report"