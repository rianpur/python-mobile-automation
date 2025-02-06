from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android.uiautomator2.base import UiAutomator2Options

options = UiAutomator2Options()

options.udid = "2d211046"
options.platform_name = "Android"
options.app_package = "com.swaglabsmobileapp"
options.app_activity = "com.swaglabsmobileapp.MainActivity"

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

driver.implicitly_wait(10)

# enter some value button = acc id = Btn1
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-Username').send_keys('standard_user')

driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-Password').send_keys('secret_sauce')

# login butto
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-LOGIN').click()

