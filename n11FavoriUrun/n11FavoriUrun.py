from selenium.webdriver.common.action_chains import ActionChains
from n11UserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class n11():

      def __init__(self, username, password):
        self.browser = webdriver.Firefox()
        self.username = username
        self.password = password

      def mainPage(self):
        self.browser.get("https://www.n11.com")
        self.browser.maximize_window()
        time.sleep(2)

        self.browser.save_screenshot("mainPage.png")
        baslik = self.browser.title
        if baslik == "n11 - Hayat Sana Gelir":
          print ("Ana Sayfa - Pass")
        else:
          print("Ana Sayfa - Fail")

      def login(self):

        self.browser.find_element(By.CLASS_NAME, 'btnSignIn').click()
        time.sleep(2)
        self.browser.save_screenshot("login.png")
        self.browser.find_element(By.ID, 'email').send_keys(username)
        self.browser.find_element(By.ID, 'password').send_keys(password)
        time.sleep(2)

        self.browser.find_element(By.ID, 'loginButton').click()
        time.sleep(2)
        assert "n11 - Hayat Sana Gelir" in self.browser.title

      def search(self):

        searchInput = self.browser.find_element(By.ID, 'searchData')
        searchInput.send_keys("Iphone")
        self.browser.save_screenshot("search.png")
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)
        a1 = self.browser.find_element(By.CLASS_NAME, 'resultText').text
        print(a1)

      def secondPage(self):

        self.browser.find_element(By.LINK_TEXT, "2").click()
        self.browser.save_screenshot("secondPage.png")
        sPage = "pg=2"
        if sPage in self.browser.current_url:
          print("2. Sayfa - Pass")
        else:
          print("2. Sayfa - Fail")

      def thirdProduct(self):

        time.sleep(2)
        self.browser.find_element(By.XPATH, "//span[@data-productid='521972016']").click()
        self.browser.save_screenshot("thirdProduct.png")

      def favoriteProduct(self):
        e1 = self.browser.find_element(By.CLASS_NAME, "user")
        actions = ActionChains(self.browser)
        actions.move_to_element(e1)
        actions.perform()
        time.sleep(2)
        self.browser.find_element(By.LINK_TEXT, "Favorilerim / Listelerim").click()
        time.sleep(2)
        assert "Favorilerim / Listelerim" in self.browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[5]/div[1]/div[2]/div[2]/div[1]/div[1]/h2[1]").text
        self.browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[5]/div[1]/div[2]/div[2]/ul[1]/li[1]/div[1]/ul[1]/li[1]/a[1]/img[1]").click()
        self.browser.save_screenshot("favoriteProduct.png")
        time.sleep(2)

      def deleteFavoriteProduct(self):

        ActionChains(self.browser).send_keys(Keys.PAGE_UP).perform()
        time.sleep(2)
        self.browser.find_element(By.CLASS_NAME, "deleteProFromFavorites").click()
        time.sleep(3)
        mesaj = self.browser.find_element(By.CLASS_NAME, "message").text
        if mesaj == "Ürününüz listeden silindi.":
          print("Favori Ürün Silme - Pass")
        else:
          print("Favori Ürün Silme - Fail")
        self.browser.save_screenshot("deleteFavoriteProduct.png")
        self.browser.find_element(By.CLASS_NAME, "btn.btnBlack.confirm").click()
        time.sleep(3)

      def logOut(self):

        e1 = self.browser.find_element(By.CLASS_NAME, "user")
        actions = ActionChains(self.browser)
        actions.move_to_element(e1)
        actions.perform()
        time.sleep(2)
        self.browser.save_screenshot("logOut.png")
        self.browser.find_element(By.CLASS_NAME, "logoutBtn").click()

        self.browser.close()


n11 = n11(username, password)
n11.mainPage()
n11.login()
n11.search()
n11.secondPage()
n11.thirdProduct()
n11.favoriteProduct()
n11.deleteFavoriteProduct()
n11.logOut()








