#!/usr/bin/env python
# coding: utf-8

# In[5]:


# import os module
import os


# In[83]:


# import time module
import time


# In[59]:


# profile list code
profile_list_code = "netsh wlan show profiles > profilelist.txt"

os.system(profile_list_code)


# In[60]:


# open profilelist.txt file
with open(r"profilelist.txt", 'r+') as pl:
    # read an store all lines into list
    lines = pl.readlines()
    
    # move file pointer to the beginning of a file
    pl.seek(0)
    
    # truncate the file
    pl.truncate()

    # start writing lines except the first 9 line
    # lines[9:] from line 9 to last line
    pl.writelines(lines[9:])
    
    #close file
    pl.close()

with open(r"profilelist.txt", "r") as pl:
    lines = pl.readlines()
    
    # empty profile list
    profile_list = []
    
    for profile in lines:
        profile_list.append(profile)
    
    # ammended profile list
    new_profile_list = []
    
    for profile in profile_list:
        new_profile = profile.replace('    All User Profile     : ', '')
        new_profile = new_profile.strip()
        
        new_profile_list.append(new_profile)
    
    # close file
    pl.close()    
    
    #print(new_profile_list)

    


# In[85]:


# list scanner
count = 1
for profile in new_profile_list:
    os.system("netsh wlan show profile name={} key=clear".format(profile)+"> profile{}.txt".format(count))
    
    with open(r'profile{}.txt'.format(count), 'r') as scanfile:
        lines = scanfile.readlines()
        for line in lines:
            if "SSID name" in line:
                line_ = line.replace("SSID name              ", "")
                net_name = line_
                
            if "Key Content" in line:
                line = line.replace("Key Content            ", "Network is {} Password".format(net_name))
                print(line)
                
        scanfile.close()
    count = count + 1
    
time.sleep(5)
print("Done!")