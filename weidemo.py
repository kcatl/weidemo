#!/usr/bin/python2

import weibo
import urllib2, urllib, socket, cookielib, os
from weibo import APIClient
from conf.info import * 

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=APP_CALLBACK)
url = client.get_authorize_url()
#try to open the authentication url

def make_access_token():   
    content = urllib2.urlopen(url, timeout=socket.setdefaulttimeout(2))
    if content:
        #something to post
        '''Tips: What data you should post to Sina?
        1.There are only two parameters in Sina's Official API doc page, including
        client_id, redirect_uri(NOT redirect_url!!! See the differneces between url and uri...it must be an ERROR!)
        2.Some information about the login user, including userId and passwd
        3.You can get this parameter from Web browser hack, 'action' is the only one we need.
        4.The last one is headers, you should make sure 'Referer' in your headers
        '''
        headers = {  #'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:24.0) Gecko/20140827 Firefox/24.0',
                   'Referer': url}
        parameters = urllib.urlencode({'client_id': APP_KEY,
                      'redirect_uri': APP_CALLBACK,
                      'userId': USER_ID,
                      'passwd': USER_PASSWD,
                      'action': 'login',
                      })
        login_url = 'https://api.weibo.com/oauth2/authorize'
        #make a post request
        request = urllib2.Request(login_url, parameters, headers)
        #enable cookie
        cookie = cookielib.CookieJar()
        handler = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)
        try:
            r = opener.open(request)
            code = r.geturl().split('=')[1]
        except urllib2.HTTPError, e:
            code = e.geturl().split('=')[1]
        except:
            pass
        #get access token. Here we use Python SDK. More Info here---> https://github.com/michaelliao/sinaweibopy/wiki/OAuth2-HOWTO
        r = client.request_access_token(code)
        access_token = r.access_token
        expires_in = r.expires_in
        save_access_token(access_token, expires_in)
        check_access_token()
#save token and expires_in
filename = 'tokenfile.txt'
filepath = os.path.dirname(__file__) + os.path.sep + 'conf'
fileabspath = os.path.join(filepath, filename)

def save_access_token(access_token, expires_in):
    file = open(fileabspath, 'w')
    file.write(access_token + ' ' + str(expires_in))
    file.close
def check_access_token():
    file = open(fileabspath, 'r')
    token = file.read().split()
    file.close()
    if len(token) == 2:
        access_token, expires_in = token
        #print access_token, expires_in 
    else:
        make_access_token()
    try:
        client.set_access_token(access_token, expires_in)
    except:
        make_access_token()
        
if __name__ == '__main__':
    check_access_token()
    #now , we can get user's data
    print len(client.statuses.user_timeline.get(screen_name="Kcatl").statuses)     