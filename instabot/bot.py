from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class Bot():
    
    username = ""
    password = ""
    browser = None
    
    def __init__(self,myUser,pwd,driverPath):
        
        self.username = myUser
        self.password = pwd
        
        self.browser = webdriver.Chrome(f"{driverPath}")
        
        
    def surf_instagram(self):
        self.browser.get("https://www.instagram.com")
        
    
    def close_browser(self):
        self.browser.quit()
        
    
    def login(self):
        unameTextfield = self.browser.find_element_by_name("username")
        unameTextfield.send_keys(self.username)
        
        time.sleep(1)
        
        pwdTextfield = self.browser.find_element_by_name("password")
        pwdTextfield.send_keys(self.password + Keys.RETURN)
        
    
    def reach_homepage(self):    
        pswd_notnow_path = '/html/body/div/section/main/div/div/div/div/button'
        notfc_notnow_path = '/html/body/div[4]/div/div/div/div[3]/button[2]'
        
        time.sleep(5)
        try:
            pswd_notnow = self.browser.find_element_by_xpath(pswd_notnow_path)
        
        except Exception as e:
            time.sleep(1)
            pswd_notnow = self.browser.find_element_by_xpath(pswd_notnow_path)

        pswd_notnow.click()

        time.sleep(3)
        
        try:
            notfc_notnow = self.browser.find_element_by_xpath(notfc_notnow_path)
        
        except Exception as e:
            time.sleep(3)
            notfc_notnow = self.browser.find_element_by_xpath(notfc_notnow_path)
            
        notfc_notnow.click()

        time.sleep(1)
        
    
    def search_hashtag(self,hashtag):
        search_bar_path = '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input'
        search_bar = self.browser.find_element_by_xpath(search_bar_path)
        search_bar.send_keys(f'#{hashtag}')
        
        time.sleep(2)
        
        search_bar.send_keys(Keys.RETURN)
        search_bar.send_keys(Keys.RETURN)
        search_bar.send_keys(Keys.RETURN)
        

    def click_topPost(self):
        top = "_9AhH0"
        try:
            time.sleep(1)
            top_post = self.browser.find_element_by_class_name(top)
        
        except Exception as e:
            time.sleep(2)
            top_post = self.browser.find_element_by_class_name(top)

        try:
            top_post.click()

        except Exception as e:
            time.sleep(1)
            top_post.click()

        finally:
            pass
        
    
    def hit_next(self):
            time.sleep(1)
            body_path = '/html/body'
            body_elem = self.browser.find_element_by_xpath(body_path)
            body_elem.send_keys(Keys.RIGHT)
        
    
    def like_photo(self):
        like_button_path = "/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button"
        try:
            try:
                like_button = self.browser.find_element_by_xpath(like_button_path)

            except Exception as e:
                time.sleep(1)
                like_button = self.browser.find_element_by_xpath(like_button_path)

            like_button.click()
            
            self.hit_next()
        
        except Exception as e:
            try:
                time.sleep(3)
                
                like_button = self.browser.find_element_by_xpath(like_button_path)
                like_button.click()
                
                self.hit_next()
                
            except Exception as e:
                self.hit_next()
                

    def do_comment(self,comments):
        textarea = '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea'
        btn = '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]'
        
        try:
            time.sleep(1)
            comment_field = self.browser.find_element_by_xpath(textarea)
            comment_field.send_keys(f'{random.choice(comments)}')

            post_btn = self.browser.find_element_by_xpath(btn)
            post_btn.click()

            self.hit_next()
        
        except Exception as e:
    
            time.sleep(3)
    
            try:
                comment_field = self.browser.find_element_by_xpath(textarea)
                comment_field.send_keys(f'{random.choice(comments)}')

                post_btn = self.browser.find_element_by_xpath(btn)
                post_btn.click()

                self.hit_next()
                
            except Exception as e:
                print("Error occured!!")
                self.hit_next()
