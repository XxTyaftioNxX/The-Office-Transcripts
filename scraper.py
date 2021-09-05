from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://transcripts.foreverdreaming.org/viewtopic.php?f=574&t=25447').text

soup = BeautifulSoup(html_text, 'lxml')
all_lines = soup.find_all('div', class_ = 'postbody')

for line in all_lines:
    dialogues = line.find_all('p')


with open('scripts/Season 7/7x22.txt', 'w') as f:
    for dialogue in dialogues:
        f.write(f"{dialogue.text} \n")


#soup = BeautifulSoup(html_text, 'lxml')
#
#all_lines = soup.find_all('div', class_ = 'page-content')
# 
#for line in all_lines:
#    print(line.text)
#    with open('scripts/B99.txt', 'w') as f:
#        f.write(line.text)
#        
#    print('writing')

'''
with open('Pilot_Transcript Brooklyn Nine-Nine Wiki Fandom.html', 'rt', encoding='utf8') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    all_lines = soup.find_all('div', class_ = "page-content")
    for line in all_lines:
        print(line.text)
'''