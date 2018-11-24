import pandas as pd 
import numpy as np 
import requests
import json
from sklearn.metrics import jaccard_similarity_score
from scipy.stats import pearsonr

myun = 'Sun-ZhenXing' # YOUR_USERNAME
mypw = '75809a8ff3e18a8adcccf34944ca177b7db00936' # YOUR_USER_TOKEN
my_starred_repos = []
def get_starred_by_me():
    resp_list = []
    last_resp = ''
    first_url_to_get = 'https://api.github.com/user/starred'
    first_url_resp = requests.get(first_url_to_get, auth=(myun,mypw))
    last_resp = first_url_resp
    resp_list.append(json.loads(first_url_resp.text))
    
    while last_resp.links.get('next'):
        next_url_to_get = last_resp.links['next']['url']
        next_url_resp = requests.get(next_url_to_get, auth=(myun,mypw))
        last_resp = next_url_resp
        resp_list.append(json.loads(next_url_resp.text))
        
    for i in resp_list:
        for j in i:
            msr = j['html_url']
            my_starred_repos.append(msr)
get_starred_by_me()
print("我已经标记了",len(my_starred_repos),"个库。\n他们分别是：")
print(my_starred_repos)
my_starred_users = []
for ln in my_starred_repos:
    right_split = ln.split('.com/')[1]
    starred_usr = right_split.split('/')[0]
    my_starred_users.append(starred_usr)
print("我已经标记的库的所有者：")
print(my_starred_users)
print("我标记的所有者个数：")
print(len(my_starred_users))
# 看起来有些重复
# 删除重复的部分
print(len(set(my_starred_users)))
# 看看这些作者们标记了哪些库
starred_repos = {k:[] for k in set(my_starred_users)}
def get_starred_by_user(user_name):
    starred_resp_list = []
    last_resp = ''
    first_url_to_get = 'https://api.github.com/users/'+ user_name +'/starred'
    first_url_resp = requests.get(first_url_to_get, auth=(myun,mypw))
    last_resp = first_url_resp
    starred_resp_list.append(json.loads(first_url_resp.text))
    
    while last_resp.links.get('next'):
        next_url_to_get = last_resp.links['next']['url']
        next_url_resp = requests.get(next_url_to_get, auth=(myun,mypw))
        last_resp = next_url_resp
        starred_resp_list.append(json.loads(next_url_resp.text))
        
    for i in starred_resp_list:
        for j in i:
            sr = j['html_url']
            starred_repos.get(user_name).append(sr)

for usr in list(set(my_starred_users)):
    print(usr)
    try:
        get_starred_by_user(usr)
    except:
        print('failed for user', usr)
# 打印所有作者
print("一共找到了",len(starred_repos),"个用户")
# 回馈找出这些作者们标记了多少库
repo_vocab = [item for sl in list(starred_repos.values()) for item in sl]
repo_set = list(set(repo_vocab))
print("找到了",len(repo_set),"个库")
all_usr_vector = []
for k,v in starred_repos.items():
    usr_vector = []
    for url in repo_set:
        if url in v:
            usr_vector.extend([1])
        else:
            usr_vector.extend([0])
    all_usr_vector.append(usr_vector)
print(len(all_usr_vector))
df = pd.DataFrame(all_usr_vector, columns=repo_set, index=starred_repos.keys())
print(len(df.columns))
print(df)
my_repo_comp = []
for i in df.columns:
    if i in my_starred_repos:
        my_repo_comp.append(1)
    else:
        my_repo_comp.append(0)
mrc = pd.Series(my_repo_comp).to_frame(myun).T
print(mrc)
mrc.columns = df.columns
fdf = pd.concat([df, mrc])
print(fdf)
l2 = my_starred_repos
l1 = fdf.iloc[-1,:][fdf.iloc[-1,:]==1].index.values
a = set(l1)
b = set(l2)
b.difference(a)
sim_score = {}
for i in range(len(fdf)):
    ss = pearsonr(fdf.iloc[-1,:], fdf.iloc[i,:])
    sim_score.update({i: ss[0]})
sf = pd.Series(sim_score).to_frame('similarity')
print(sf)
print(sf.sort_values('similarity', ascending=False))
print(fdf.index[5])
print(fdf.iloc[5,:][fdf.iloc[5,:]==1])
all_recs = fdf.iloc[[1,5,7,9],:][fdf.iloc[[1,5,7,9],:]==1].fillna(0).T
print(all_recs[(all_recs==1).all(axis=1)])
str_recs_tmp = all_recs[all_recs[myun]==0].copy()
str_recs = str_recs_tmp.iloc[:,:-1].copy()
print(str_recs)
print(str_recs[(str_recs==1).all(axis=1)])
print(str_recs[str_recs.sum(axis=1)>1])












