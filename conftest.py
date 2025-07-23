import os

import pytest
from selenium import webdriver
driver = None

def pytest_addoption(parser):
    parser.addoption("--browser_name",action = "store",default = "chrome",help ="browser selection")
@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")


    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--disable-password-manager-reauthentication")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)


    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    driver.implicitly_wait(5)
    driver.get("https://www.saucedemo.com/v1/")
    request.node._driver = driver
    yield driver
    driver.quit()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when in ('call', 'setup'):
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = getattr(item, "_driver", None)
            if driver:
                reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
                file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
                _capture_screenshot(driver, file_name)

                if os.path.exists(file_name):
                    html = (
                        f'<div><img src="{file_name}" alt="screenshot" '
                        f'style="width:304px;height:228px;" '
                        f'onclick="window.open(this.src)" align="right"/></div>'
                    )
                    extra.append(pytest_html.extras.html(html))

        report.extra = extra


def _capture_screenshot(driver, file_name):
    if driver:
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        driver.save_screenshot(file_name)

