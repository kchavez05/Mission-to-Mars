#!/usr/bin/env python
# coding: utf-8

# In[131]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[132]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[134]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[135]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[136]:


slide_elem.find('div', class_='content_title')


# In[137]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[138]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[139]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[140]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[141]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[142]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[143]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[144]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[145]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[146]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[156]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)
html = browser.html
hemisphere_soup = soup(html, 'html.parser')


# In[157]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# In[158]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
    
results = hemisphere_soup.find_all("div",class_='item')

#Loop through results
for result in results:
        img_dict = {}
        titles = result.find('h3').text
        img_rel_url = result.find('a')['href']
        img_full_url = f"{url}{img_rel_url}"  
        
        # Navigate to image site
        browser.visit(img_full_url)
        html = browser.html
        img_soup= soup(html, 'html.parser')
        
        # Pull image url
        downloads = img_soup.find('div', class_='downloads')
        image_rel_url = downloads.find('a')['href']
        image_full_url = f"{url}{image_rel_url}"
        
        
        print(titles)
        print(image_full_url)
        
        img_dict['title']= titles
        img_dict['image_url']= image_full_url
        hemisphere_image_urls.append(img_dict)


# In[159]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[160]:


# 5. Quit the browser
browser.quit()


# In[ ]:




