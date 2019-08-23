
# coding: utf-8

# In[1]:


import pymysql


# In[2]:


def db_connect():
    db = pymysql.connect(
        host='fininsightdevdb.mysql.database.azure.com', 
        user='election@fininsightdevdb',
        port=3306,
        password='election',
        db='election',
        charset='utf8'
    )
    
    return db


# In[3]:


def db_close(db):
    db.close()

