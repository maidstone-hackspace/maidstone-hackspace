from uuid import uuid4
import os
import hashlib    
import requests


def save_remote_image(url, path='', domain='', skip_exists=True):
    filename = '%s.%s' % (hashlib.md5(url.encode()).hexdigest(), url[-3:])
    filepath = os.path.abspath('./static/images/blogs/%s' %(filename))
    urlpath = 'static/images/blogs/' + filename

    if not url:
        return None

    if url[-3:] not in ('jpg', 'png'):
        return None
    print(domain + urlpath)
    if skip_exists is True and os.path.exists(filepath):
        return domain + urlpath

    r = requests.get(url, stream=True)
    if r.status_code != 200:
        return None

    with open(filepath, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
    return domain + urlpath
