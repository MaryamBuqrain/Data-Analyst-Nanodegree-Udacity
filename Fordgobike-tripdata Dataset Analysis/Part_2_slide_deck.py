#!/usr/bin/env python
# coding: utf-8

# # Part II - (Analysis for Ford GoBike Service)
# ## by (Maryam Abdullah)

# 
# 
# ## Investigation Overview
# 
# 
# In this project, We aim to demonstrate the value and importance of data visualization techniques in the data analysis process. First, we use Python's NumPy, and pandas libraries to explore data then we use Matplotlib and Seaborn to visualize data. This project will take you to understand the user behavior toward the biking system, which will help you in your investment decision in the future regarding the biking sharing system. 
# 
# ## Dataset Overview
#  The data inculde information regarding approximately 183412 trip made in a bike-sharing system covering the San Francisco Bay area. Which they described with 16 features include duration, customer type, and gender, as well as additional variables such as member's year of birth, start and end station name, start and end station longitude, and latitude. 

# In[1]:


# import all packages and set plots to be embedded inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from datetime import date

get_ipython().run_line_magic('matplotlib', 'inline')

# suppress warnings from final output
import warnings
warnings.simplefilter("ignore")


# In[2]:


# load in the dataset into a pandas dataframe
df = pd.read_csv("fordgobike-tripdata.csv")


# In[3]:


# Cleaning data type
df.user_type = df.user_type.astype('category')
df.member_gender = df.member_gender.astype('category')
# Extracting age 
current_year = date.today().year
age = current_year - df.member_birth_year
df['age']= age
# Convert start time from object to datetime to help extract the hours of the start and end trip 
df['start_hour']=pd.to_datetime(df['start_time']).dt.hour
df['end_hour']=pd.to_datetime(df['end_time']).dt.hour
df['day_of_week']=pd.to_datetime(df['start_time']).dt.day_name()
# calacualate the durations hour and min 
df['duration_hrs'] = df['duration_sec'] // 3600
df['duration_minu'] = df['duration_sec'] // 60
# Creating order for days
week_order=["Monday", "Tuesday", "Wednesday", "Thursday","Friday","Saturday","Sunday"]


# > Note that the above cells have been set as "Skip"-type slides. That means
# that when the notebook is rendered as http slides, those cells won't show up.

# ## (User type)
# 
#  Since knowing the type of user in each business help to observe  and understand its behavior, in this data for Gobike service the majority of user is a subscriber

# In[4]:


def bar_catg(xvalue,order,titel,xlebel):
    plt.figure(figsize=[8, 5])
    sb.countplot(data = df, x = xvalue,order = order)
    plt.title(titel)
    plt.xlabel(xlebel) 
    plt.show();


# In[5]:


bar_catg("user_type",df.user_type.value_counts().index, 'Count of users in each triep','Users')


# ## (User Age)
# 
# The majority of users are subscribers and young, between the ages of 22-25 and 25-45. Consequently, it is a positive sign since they will be able to stay with this type of business and enjoy riding bikes if they are young.

# In[6]:


sb.boxplot(data= df, x = "user_type", y='age')
plt.xlabel('Users')
plt.ylabel('Age')
plt.title("How user distributed depending on their age")
plt.show();


# ## (Duration usage over a week day)
# 
# As we see previously most of the users are young so they spend more minutes on each trip. But because they are mostly subscribed they spend less time over the week, on the other hand, they almost spend more than 20 minutes at weekend. Overall, If your main target is customers or subscribed you should provide more bikes at the stations during the weekend. 

# In[7]:


plt.title(' Duration Usage in minutes')
sb.barplot(data=df, x='duration_minu', y='day_of_week', hue='user_type',order=week_order);


# ## ( Peak time for riding bikes )
# 
# Most of the customers and subscribers use bikes at the same time so this means there are high demands at 17 PM or 8 AM . For that you should plan to provide more at these hours.Also,customers may have more flexible time and use almost more after 12 PM

# In[8]:


x = sb.countplot(x=df.start_hour, hue=df.user_type,data=df, palette=['orange',"blue"])
x.set_title("User type usage over day's hours ")
plt.xlabel('Hour')
plt.ylabel('Count')
plt.legend(labels = ['Customer', 'Subscriber'])
plt.show();


# >**Generate Slideshow**: Once you're ready to generate your slideshow, use the `jupyter nbconvert` command to generate the HTML slide show. . From the terminal or command line, use the following expression.

# > This should open a tab in your web browser where you can scroll through your presentation. Sub-slides can be accessed by pressing 'down' when viewing its parent slide. Make sure you remove all of the quote-formatted guide notes like this one before you finish your presentation! At last, you can stop the Kernel. 

# In[ ]:


get_ipython().system('jupyter nbconvert Part_2_slide_deck.ipynb --to slides --post serve --no-input --no-prompt')


# In[ ]:





# In[ ]:




