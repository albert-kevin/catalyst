from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import datetime
from time import sleep
# import time
import secret
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pandas as pd
import requests

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument('headless')
chrome_options.add_argument('no-sandbox')
driver = webdriver.Chrome("/home/ubuntu/notebooks/azuremachinelearning/code/notebooks/chromedriver", options=chrome_options)

#open the webpage
driver.get("https://cardano.ideascale.com/a/community/login")

# maximize the window
driver.maximize_window()

# remove cookies window blocking login proces
# driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/div/div[2]/button[2]').click()
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/button/span').click()
sleep(2)
#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='emailAddress']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
#enter username and password
username.clear()
username.send_keys(secret.my_username)
password.clear()
password.send_keys(secret.my_password)
#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
sleep(3)

# # parsing the visible webpage
# pageSource = driver.page_source
# lxml_soup = BeautifulSoup(pageSource, 'lxml')
# # archive page source
# filename = "campaign_overview_"
# with open("data/bronze/catalyst/" + filename + datetime.datetime.now().strftime("%d%b%Y") + '.txt', 'w') as file:
#     file.write(pageSource)

# # campaigns overview data
# campaigns = lxml_soup.find_all('section', class_='cl-campaigns')[0]
# campaign_id = [x['href'].split('/')[-1] for x in campaigns.find_all('a')]
# campaign_title = [x.text for x in campaigns.find_all('span', class_='cl-campaign-title')]
# campaign_url = ["https://cardano.ideascale.com" + x['href'] for x in campaigns.find_all('a')]
# campaign_context = [x.p.text for x in campaigns.find_all('article')]

# # creating a dataframe
# campaign_df = pd.DataFrame({
#     'campaign_id': campaign_id,
#     'campaign_title': campaign_title,
#     'campaign_url': campaign_url,
#     'campaign_context': campaign_context})
# # cleaning description column
# campaign_df['campaign_context'] = campaign_df['campaign_context'].str.replace('\n','')
# # save dataset to csv
# campaign_df.to_csv('data/bronze/catalyst/cardano_ideascale_campaign_dataset.csv', index=0)

# data = pd.DataFrame()
# counter = 1
# for campaignId in campaign_df['campaign_id']:
#     url = "https://cardano.ideascale.com/a/ideas/recent/campaign-filter/byids/campaigns/"+campaignId+"/stage/unspecified"
#     driver.get(url)
#     # we need to scroll down to load all projects
#     # increase the range to sroll (+20 projects each scroll down)
#     print('scrolling down... wait {} seconds.'.format(3*25))
#     for _ in range(0, 25):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         sleep(3)
#     # parsing the visible webpage
#     pageSource = driver.page_source
#     lxml_soup = BeautifulSoup(pageSource, 'lxml')
#     idea_header = lxml_soup.find_all('header', class_ = 'idea-header')
#     print('You are scraping {} projects from campaign ID {}.'.format(len(idea_header), campaignId))
#     # let's create lists
#     campaign_id = [campaignId for x in range(len(idea_header))]
#     project_title = [x.h2.find_all('a', class_='classic-link')[0].text.strip() for x in idea_header]
#     project_url = ['https://cardano.ideascale.com' + x.h2.find_all('a', class_='classic-link')[0]['href'] for x in idea_header]
#     project_context = [x.h2.find_all('a', class_='classic-link')[0]['title'] for x in idea_header]
#     project_id = [x.split('/')[-1] for x in project_url]
#     # creating a dataframe
#     project_df = pd.DataFrame({
#         'campaign_id': campaign_id,
#         'project_id': project_id,
#         'project_title': project_title,
#         'project_url': project_url,
#         'project_context': project_context})
#     # save dataset to csv
#     project_df.to_csv('data/bronze/catalyst/cardano_ideascale_'+campaignId+'_projects_dataset.csv', index=0)
#     data = data.append(project_df, ignore_index=True, verify_integrity=False, sort=False)
#     print(project_df.info())
#     print('running challenge #{}'.format(counter))
#     counter += 1

# # store all challenges combined
# data.to_csv('data/bronze/catalyst/cardano_ideascale_projects_dataset.csv', index=0)

# ### NEW CHAPTER ###
# challenges = pd.read_csv('data/bronze/catalyst/cardano_ideascale_campaign_dataset.csv')
# projects = pd.read_csv('data/bronze/catalyst/cardano_ideascale_projects_dataset.csv')
# df = projects.merge(challenges, how='left', on='campaign_id')
# counter = 1
# # setting up list of scalar values
# project_url = []
# project_solution = []
# kudos = []
# submitted = []
# owner_name = []
# owner_url = []
# contributor_name = []
# contributor_url = []
# requested_funds = []
# requested_currency = []
# details = []
# remarks = []
# project_definitions = []
# total_comments = []
# total_followers = []


# for url in projects['project_url'][:]:
#     # load the webpage of the project
#     driver.get(url)
#     # load the page bottom scroll
#     for _ in range(0, 1):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         sleep(2)
#     # parsing the visible webpage
#     pageSource = driver.page_source
#     lxml_soup = BeautifulSoup(pageSource, 'lxml')

#     # save the known url for later merge
#     project_url.append(url)

#     # get project solution description
#     node = lxml_soup.find('div', {'data-element-id':"CF_3857"})
#     if node is not None:
#         project_solution.append(node.text.strip())
#     else:
#         project_solution.append('')
    
#     # get the first kudos amount
#     node = lxml_soup.find('a', class_='kudos-link')
#     if node is not None:
#         kudos.append(node.text.strip())
#     else:
#         kudos.append('')

#     # get the project submitted creation date
#     node = lxml_soup.find('div', {'data-element-id':'submitted-date'})
#     if node is not None:
#         submitted.append(node.text)
#     else:
#         submitted.append('')

#     # get the project owner
#     node = lxml_soup.find('a', {'class':"author-info"})
#     if node is not None:
#         owner_name.append(node.find('strong').text.strip())
#     else:
#         owner_name.append('')

#     # get the link to owner
#     node = lxml_soup.find('a', {'class':"author-info"})
#     if node is not None:
#         owner_url.append("https://cardano.ideascale.com" + node['href'])
#     else:
#         owner_url.append('')

#     # get the project contributor
#     node = lxml_soup.find('span', {'class':"contributor-name"})
#     if node is not None:
#         contributor_name.append(node.text.strip(",\n"))
#     else:
#         contributor_name.append('')

#     # get the link to contributor
#     node = lxml_soup.find('span', {'class':"contributor-name"})
#     if node is not None:
#         contributor_url.append("https://cardano.ideascale.com" + node.find('a')["href"])
#     else:
#         contributor_url.append('')

#     # amount of funding
#     node = lxml_soup.find('p', {'data-element-id':"CF_4079"})
#     if node is not None:
#         requested_funds.append(node.find('span').text)
#     else:
#         requested_funds.append('')

#     # funding currency type (USD, EUR, ADA)
#     node = lxml_soup.find('p', {'data-element-id':"CF_4079"})
#     if node is not None:
#         requested_currency.append(node.find('strong').text.strip())
#     else:
#         requested_currency.append('Requested funds in USD')

#     # get the main project text
#     node = lxml_soup.find('div', {'data-element-id':"CF_3825"})
#     if node is not None:
#         details.append(node.text)
#     else:
#         details.append('')

#     # get the text from the project if the main project even is not approved
#     node = lxml_soup.find('div', {'data-element-id':"CF_3832"})
#     if node is not None:
#         remarks.append(node.text)
#     else:
#         remarks.append('')

#     # Which of these definitions apply to you?
#     node = lxml_soup.find('p', {'data-element-id':"CF_718"})
#     if node is not None:
#         project_definitions.append(node.find('span').text)
#     else:
#         project_definitions.append('')

#     node = lxml_soup.find_all('span', class_='idea-action-label')
#     if node is not None and len(node) > 0:
#         if len(node) > 4:
#             total_comments.append(node[0].text)
#             total_followers.append(node[1].text)
#         else:
#             total_comments.append('0')
#             total_followers.append(node[0].text)
#     else:
#         total_comments.append('0')
#         total_followers.append('0')

#     # append records into one dataframe
#     # data = data.append(project_df, ignore_index=True, verify_integrity=False, sort=False)

#     # print(project_df.info())
#     print(url)
#     print('countdown projects #{}/{}'.format(counter, len(projects)))
#     counter += 1

# # create a new dataframe
# project_df = pd.DataFrame({
#     'project_url': project_url,
#     'project_solution': project_solution,
#     'kudos': kudos,
#     'submitted': submitted,
#     'owner_name': owner_name,
#     'owner_url': owner_url,
#     'contributor_name': contributor_name,
#     'contributor_url': contributor_url,
#     'requested_funds': requested_funds,
#     'requested_currency': requested_currency,
#     'details': details,
#     'remarks': remarks,
#     'project_definitions': project_definitions,
#     'total_comments': total_comments,
#     'total_followers': total_followers})

# # save dataset to csv
# project_df.to_csv('data/bronze/catalyst/cardano_ideascale_projects_details_dataset.csv', index=0)
# print(project_df.info())


#### ---- get owner details ---- ####
project_df = pd.read_csv('data/bronze/catalyst/cardano_ideascale_projects_details_dataset.csv')
counter = 1
# setting up list of scalar values
owner_url = []
member_since = []
member_definitions = []
member_kudos = []
member_activity_count = []


for owner in project_df["owner_url"]:
    # load the webpage of the project
    driver.get(owner)
    # load the page bottom scroll
    for _ in range(0, 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
    # parsing the visible webpage
    pageSource = driver.page_source
    lxml_soup = BeautifulSoup(pageSource, 'lxml')

    # save the known url for later merge
    owner_url.append(owner)

    # get member since
    node = lxml_soup.find('article', {'class':"profile"})
    if node is not None:
        member_since.append(node.p.text.strip())
    else:
        member_since.append('')
    
    # get member definitions (entrepreneur, teacher, )
    node = lxml_soup.find('span', {'data-element-id':"field-answer"})
    if node is not None:
        member_definitions.append(node.text)
    else:
        member_definitions.append('')

    # get total amount of kudos
    node = lxml_soup.find('div', {'class':"member-stats-points"})
    if node is not None:
        member_kudos.append(node.strong.text.strip())
    else:
        member_kudos.append('')

    # get total amount of activity with other projects
    node = lxml_soup.find('span', {'id':"activity-event-count"})
    if node is not None:
        member_activity_count.append(node.text.strip('[] '))
    else:
        member_activity_count.append('')

    print(owner)
    print('countdown owners #{}/{}'.format(counter, len(project_df["owner_url"])))
    counter += 1

# create a new dataframe
owner_df = pd.DataFrame({
    'owner_url': owner_url,
    'member_since': member_since,
    'member_definitions': member_definitions,
    'member_kudos': member_kudos,
    'member_activity_count': member_activity_count})

# save dataset to csv
owner_df.to_csv('data/bronze/catalyst/cardano_ideascale_projects_owners_dataset.csv', index=0)
print(owner_df.info())