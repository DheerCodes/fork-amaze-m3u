import requests
import os
import xml.etree.ElementTree as ET
regioncodes=['all','au','ca','es','fr','gb','mx','nz','us']
for region in regioncodes:
    playlist = [f'#EXTM3U x-tvg-url="https://i.mjh.nz/Plex/{region}.xml.gz"']
    url = f'https://raw.githubusercontent.com/matthuisman/i.mjh.nz/refs/heads/master/Plex/{region}.xml'
    resp = requests.get(url)
    root = ET.fromstring(resp.text)
    for type_tag in root.findall('channel'):
        chnlid = type_tag.get('id')
        name = type_tag.find('display-name').text
        ico = type_tag.find('icon').get('src')
        playlist.append(f'#EXTINF:-1 tvg-id="{chnlid}" tvg-name="{name}" tvg-logo="{ico}",{name}')
        playlist.append(f'https://jmp2.uk/plex-{chnlid}.m3u8')
    with open(f'./Plex/{region}.m3u', 'w') as f:
        for line in playlist:
            f.write(f"{line}\n")
    f.close()
