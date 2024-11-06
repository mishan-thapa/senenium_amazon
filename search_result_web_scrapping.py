from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# import time

print("Script Started")
driver = webdriver.Chrome()
query = "laptop"
file_no = 0
for i in range(1, 2):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=1RL7T1C4KFBE9&qid=1730863091&sprefix=lapt%2Caps%2C354&ref=sr_pg_2")
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"search_result_web_scrapping_data_folder/{query}-{file_no}.html", "w") as f:
            f.write(d)
            file_no += 1
    # time.sleep(2)
driver.close()
print("Script Completed")