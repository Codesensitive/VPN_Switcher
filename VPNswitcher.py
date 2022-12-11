if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service

    s = Service('C:/Users/{User}/Desktop/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    def ShutVPN(self):
        print('Stopping VPN')
        os.popen("taskkill /F /IM ProtonVPN.exe /T")
        os.popen("taskkill /F /IM ProtonVPN.WireGuardService.exe /T")
        os.popen("taskkill /F /IM ProtonVPNService.exe /T")

    def StartVPN(self):
        print('Staring VPN')
        os.popen("start C:\\Users\\{User}\\Desktop\\ProtonVPN\\ProtonVPN.exe")

    try:
        StartVPN()
        driver.get("https://whatismyipaddress.com/")
    except:
        print("Error")
