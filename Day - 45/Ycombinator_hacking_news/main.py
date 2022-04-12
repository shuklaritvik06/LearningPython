from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text,'html.parser')
all_a_tags= soup.find_all(name='a',class_='titlelink')
all_span_tags = soup.find_all(name='span',class_='score')
titles_list = []
temp_scores_list = []
final_scores_list =[]
maximum_score = 0
for i in all_a_tags:
    text = i.get_text()
    titles_list.append(text)
for i in all_span_tags:
    score = i.get_text()
    temp_scores_list.append(score)
for j in temp_scores_list:
    j = int(j.strip(' points'))
    final_scores_list.append(j)
maximum_score = max(final_scores_list)
index = final_scores_list.index(maximum_score)
title = titles_list[index]
url = all_a_tags[index]['href']
print(f"Title:{title}\nUrl:{url}\nScore:{maximum_score}")