from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.support.ui import WebDriverWait

def setup_driver():

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:8080")
    driver = webdriver.Chrome(options=chrome_options)
    
    return driver


    

def load_morejobs(driver):
    wait = WebDriverWait(driver, 10)
    job_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".job-card-container--clickable")))
    for job_element in job_elements:
      job_element.click()
    for i in range(7):
        body_elem = driver.find_element(By.TAG_NAME, "body")
        body_elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        print("scroll down")
        time.sleep(3)
        #generate again all the job elements on the page after scrolling down
    job_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".job-card-container--clickable")))
    job_elements = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
    print("there are",len(job_elements))


def check_applying(driver,job_element):
 job_element.click()
     
 time.sleep(2)
    
 for i in range(3):
        print("here")
        time.sleep(3)
        try:
            applied_buuton = driver.find_element(By.CLASS_NAME, "artdeco-inline-feedback").text
            if "Applied" or "No longer accepting applications" in  applied_buuton :
                print("the job is already applied for it or it is no longer accepting applications")
        
            break 
          
        except:
            print("there is no applied jobs")   

def apply_to_job(driver,job_element):

 try :   

    for i in range(8):
        try :
            easyapply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
            easyapply_button.click()
            
            time.sleep(3)
            print("There is easyapply button")
            break
        except:
            print("The page is not loaded yet")
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        next_button.click()
        time.sleep(1)
        
    except:
        print("the job you have already applied for it")        
    try:
        
       # choose_button = driver.find_element(By.CLASS_NAME, "jobs-resume-picker__resume-btn-container")
        #choose_button.click()
        #time.sleep(0.5)
        review_button=driver.find_element(By.XPATH, '//button[normalize-space()="Review"]').click()
        time.sleep(3)
       
        Submit_button=driver.find_element(By.XPATH,'//button[normalize-space()="Submit application"]').click()
        time.sleep(2)
    except:
        time.sleep(2)
        
        close_button=driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss').click()
        time.sleep(2)
        
        discard_button=driver.find_element(By.XPATH, '//button[normalize-space()="Discard"]').click()
    
 except:
     print("move forward")
def main():
    driver = setup_driver()
    driver.get(r'https://www.linkedin.com/jobs/search/?currentJobId=13775086&f_AL=true&geoId=103644278&keywords=Dotnet%20Developer&location=United%20States&refresh=true')
    time.sleep(3)
    list_jobs = driver.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")
   
    
    load_morejobs(driver)
    wait = WebDriverWait(driver, 10)
    job_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".job-card-container--clickable")))
    print("last",len(job_elements))
    for job_element in job_elements:
        
        time.sleep(2)
         
        check_applying(driver,job_element)
        apply_to_job(driver,job_element)
        #driver.quit()
    
if __name__ == "__main__":
    main() 
