import requests
import re
import json
from pprint import pprint
import os
import subprocess

filename = 'video\\'
if not os.path.exists(filename):
    os.mkdir(filename)

for page in range(1, 8):
    link = f'https://api.bilibili.com/x/space/wbi/arc/search?mid=313580179&pn={page}&keyword=&order=pubdate&order_avoided=true&jsonp=jsonp'
    headers = {
        'referer': 'https://space.bilibili.com/313580179/video',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'
    }

    json_lists = requests.get(url=link, headers=headers).json()
    #pprint(json_lists)
    json_lists_ = json_lists['data']['list']['vlist']
    for json_list in json_lists_:
        # pprint(json_list)
        rid = json_list['bvid']
        # print(rid)
        url = f'https://www.bilibili.com/video/{rid}/?spm_id_from=333.999.0.0&vd_source=a3664d3b767e4253cd991d79b2d98cd6'
        response = requests.get(url=url, headers=headers)
        title = re.findall('<title data-vue-meta="true">(.*?)_哔哩哔哩_bilibili</title>', response.text)[0]
        # print(title)
        json_str = re.findall('window.__playinfo__=(.*?)</script>', response.text)[0]
        #print(json_str)
        json_data = json.loads(json_str)
        audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
        video_url = json_data['data']['dash']['video'][0]['baseUrl']
        audio_content = requests.get(url=audio_url, headers=headers).content
        video_content = requests.get(url=video_url, headers=headers).content
        with open(filename + title + '.mp3', mode='wb') as f:
            f.write(audio_content)
        with open(filename + title + '.mp4', mode='wb') as f:
            f.write(video_content)
            print('*******正在保存*******', title)

        COMMAND = f'ffmpeg -i video\\{title}.mp3 -i video\\{title}.mp4 -c:v copy -c:a aac -strict experimental video\\{title}output.mp4'
        subprocess.run(COMMAND, shell=True)
        os.remove(f'video\\{title}.mp3')
        os.remove(f'video\\{title}.mp4')
