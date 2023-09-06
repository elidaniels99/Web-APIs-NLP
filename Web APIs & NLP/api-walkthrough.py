#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import requests
import time


# ### Authorizing
# 
# In order to make requests to Reddit's API, we're going to have to authenticate ourselves via OAuth2. Unfortunately we're going to need to do several things before we get to the point of receiving our authorization token though.
# 
# 1. Create a [Reddit](https://www.reddit.com) account.
#     - Be sure to remember both your username and password
# 2. Once you're signed in [create an application](https://www.reddit.com/prefs/apps) to generate the credentials needed to request an authorization token.
#     - Scroll all the way down and click `create another app...`
#     - Select `script`
#     - Enter a name for your application and enter `http://localhost:8080` as your redirect uri
#     - Click `create_app`
# 3. Fill out the information below

# In[3]:


client_id = 'OWpV-MSPnpZUzW4bGAjvJg'
client_secret =  'ADKiyrd3kqLqxxxr6jT9M8WrWk72uQ'
user_agent =  'MSDC'
username =  'NameUnkn0wno'
password =  'peanutbutter11'


# Now we're on our way to retrieving our access token; we'll use the basic authentication framework to get there.

# In[4]:


auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

data = {
    'grant_type': 'password',
    'username': username,
    'password': password
}


# In[5]:


#create an informative header for your application
headers = {'User-Agent': 'namehere/0.0.1'}

res = requests.post(
    'https://www.reddit.com/api/v1/access_token',
    auth=auth,
    data=data,
    headers=headers)

print(res)


# In[6]:


res.json()


# Hopefully upon running the above, you received a successful response code and can save your token. These should last for about two hours by default.

# In[7]:


#retrieve access token
token = res.json()['access_token']


# Now let's add your access token to the headers and verify that you can successfully submit a call to the api.

# In[8]:


headers['Authorization'] = f'bearer {token}'

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers).status_code == 200


# If all went correctly, we can finally create a simple request.

# In[9]:


base_url = 'https://oauth.reddit.com/r/'
subreddit = 'marvelstudios'

res = requests.get(base_url+subreddit, headers=headers)


# In[10]:


res.json()['data']['children']


# Explore the response object. Where is our submission data? How many posts were retrieved by default?

# In[11]:


#check out response object


# In[12]:


posts = res.json()['data']


# In[13]:


len(posts)


# In[14]:


# Function to fetch posts and return post data in a list
def fetch_posts(url, headers, params):
    res = requests.get(url, headers=headers, params=params)
    if res.status_code == 200:
        return res.json()


# In[30]:


post = res.json()['data']['children'][0]
[i for i in post['data'].keys()]


# Let's now make use of the fact that we can pass a parameters dictionary to increase the size of our request then create a dataframe of our submissions.

# In[15]:


#modify request
params = {
    'limit': 100
}

res = requests.get(base_url+subreddit,
                   headers=headers,
                  params=params)


# In[35]:


all_post_data = []
post_count = 1000
subreddits = ["marvelstudios", "DCcomics"]
#While loop in a for loop 
def get_submissions(subreddits):
    all_post_data = []
    post_count = 1000
    after = None

    for subreddit in subreddits:
        while len(all_post_data) < post_count:
            data = fetch_posts(base_url + subreddit, headers=headers, params=params)
            if data is None:
                print(f"Error: Failed to fetch data for subreddit '{subreddit}'. Skipping.")
                break

            posts = data.get('data', {}).get('children', [])
            posts_count = len(posts)
            print("Number of posts retrieved in the current response:", posts_count)

            if not posts:
                print(f"No posts found for subreddit '{subreddit}'. Skipping.")
                break

            for post in posts:
                combined_text = post['data']['title'] + " " + post['data']['selftext']
                all_post_data.append({
                    'Title_and_Selftext': combined_text,
                    'Author': post['data']['author'],
                    'Score': post['data']['score'],
                    'URL': post['data']['url'],
                    'Created': post['data']['created_utc']
                })

            after = posts[-1]['data']['name']
            params = {'limit': 100, 'after': after}

            if posts_count < 100:
                break


# In[36]:


#check status code
res.status_code


# In[37]:


#create a dataframe of your submissions
df = pd.DataFrame(all_post_data)


# **Exercise**: write a loop to retrieve the 1000 most recent submissions. What parameters of the submissions endpoint will be most helpful for you here? [To the docs!](https://www.reddit.com/dev/api/)

# In[40]:


df.nunique()


# In[39]:


df.head()


# In[ ]:





# In[ ]:




