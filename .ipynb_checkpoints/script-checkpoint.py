import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import time
import pandas as pd

def get_indeed_data(job_title, location):
    # 1. Initialize Driver
    #options = uc.ChromeOptions()
    # options.add_argument('--headless') # Run without window once debugged
    driver = uc.Chrome(options=uc.ChromeOptions())
    
    # 2. Build URL
    url = f"https://www.indeed.com/jobs?q={job_title.replace(' ', '+')}&l={location}"
    driver.get(url)
    
    time.sleep(7) # Allow time for JS to load
    
    # 3. Parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    job_list = []
    
    # Identify job cards (Check Indeed's current CSS classes as they change)
    cards = soup.find_all('div', class_='job_seen_beacon')
    
    for card in cards:
        title = card.find('h2').text.strip() if card.find('h2') else "N/A"
        company = card.find('span', {'data-testid': 'company-name'}).text.strip() if card.find('span', {'data-testid': 'company-name'}) else "N/A"
        
        job_list.append({
            'Title': title,
            'Company': company,
        })
    
    driver.quit()
    return pd.DataFrame(job_list)

# Usage
df = get_indeed_data("Data Scientist", "Canada")
print(df.head())