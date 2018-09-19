from appium import webdriver

desired_caps = desired_caps = {
'platformName': 'Android',
'platformVersion': '5.1',
'deviceName': 'Y15QKCPH278J4',
"noReset":True,
"appPackage":"org.cnodejs.android.md",
"appActivity":".ui.activity.LaunchActivity"
# 'automationName': 'Appium',
# 'app': r'C:\\Users\\nellia\\Desktop\\cnode.apk'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
