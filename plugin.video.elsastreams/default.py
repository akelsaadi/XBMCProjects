import urllib,urllib2,re,xbmcplugin,xbmcgui
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
from httplib import HTTP
from urlparse import urlparse
import StringIO
import urllib2,urllib
import re
import httplib
import time
import xbmcgui
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import cookielib
import datetime


__settings__ = xbmcaddon.Addon(id='plugin.video.elsastreams')
__icon__ = __settings__.getAddonInfo('icon')
__fanart__ = __settings__.getAddonInfo('fanart')
__language__ = __settings__.getLocalizedString
_thisPlugin = int(sys.argv[1])
_pluginName = (sys.argv[0])

def cats():

	addDir('Soccer', 'http://www.livehd7.com/Matches/view/today', 1, 'http://i3.mirror.co.uk/incoming/article9390720.ece/ALTERNATES/s615/PAY-9Y9A6996.jpg')
	addDir('Basketball', 'http://yoursportsinhd.com/', 1, 'http://sportsrants.com/wp-content/uploads/2014/07/030915-sports-nba-mvp-race-so-far-James-Harden-Stephen-Curry-russell-westbrook-lebron-james-720x340-600x283.png')

def get_games(url):
	if 'livehd' in url:
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		link = response.read()
		counter =0
		ls = list()
		result = re.findall(r';;">\s*<a(.*?)</div></a>', link, re.DOTALL)
		for item in result:
			mypath = 'http://www.livehd7.com' + item.split('href="')[1].split('"')[0]
			#ls.append(str(mypath))
			req1 = urllib2.Request(mypath)
			respons2= urllib2.urlopen(req1)
			link1 = respons2.read()
			result2 = re.findall(r'<li class="active"(.*?)/li>', link1, re.DOTALL)
			for item2 in result2:
				myname = item2.split('>')[1].split('<')[0]
				addDir(myname, mypath, 2, '')
	elif 'yoursportsinhd' in url:
		UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
		req4 = urllib2.Request('http://yoursportsinhd.com/')
		req4.add_header('User-Agent', UA)

		response4 = urllib2.urlopen(req4)
		link4 = response4.read()
		result4 = re.findall(r'<div class="listings-grid__item text-center">(.*?)<div class="listings-grid__main pull-left no-border ">', link4, re.DOTALL)
		for item4 in result4:
			mypath = 'http://yoursportsinhd.com' + item4.split('href="')[1].split('"')[0]
			req5 = urllib2.Request(mypath)
			req5.add_header('User-Agent', UA)
			response5 = urllib2.urlopen(req5)
			link5 = response5.read()
			result5 = re.findall(r'<title>(.*?)</title>', link5, re.DOTALL)
			for item5 in result5:
				myname = item5
				addLink(myname, mypath, 3, '')		
		

def get_links(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    link = response.read()
    result3 = re.findall(r'<a target="_blank" (.*?)/a>', link, re.DOTALL)
    for item3 in result3:
        mypath = item3.split('href="')[1].split('"')[0]
        if (mypath == 'http://www.anassafi.com'):
            mypath =""
        myname = item3.split('">')[1].split('<')[0]
        if 'AnasSafi.com' in myname:
            myname = ""
        addLink(myname, mypath, 3, '')

def get_video(url):
	UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
	
	if '.m3u8' in url:
		listItem = xbmcgui.ListItem(path=str(url))
		xbmcplugin.setResolvedUrl(_thisPlugin, True, listItem)
	elif 'yoursportsinhd' in url:
		req5 = urllib2.Request(url)
		req5.add_header('User-Agent', UA)

		response5 = urllib2.urlopen(req5)
		link5 = response5.read()
		result5 = re.findall(r'src: "(.*?)"', link5, re.DOTALL)
		for item6 in result5:
			if 'nasa' not in item6:
				listItem = xbmcgui.ListItem(path=str(item6))
				xbmcplugin.setResolvedUrl(_thisPlugin, True, listItem)
	else:
	
		req4 = urllib2.Request(url)
		response4 = urllib2.urlopen(req4)
		link4 = response4.read()
		result4 = re.findall(r'source: "(.*?)",', link4, re.DOTALL)
		for item4 in result4:
			listItem = xbmcgui.ListItem(path=str(item4))
			xbmcplugin.setResolvedUrl(_thisPlugin, True, listItem)


def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]

        return param


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addLink(name,url,mode,iconimage):
    u=_pluginName+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    liz.setProperty("IsPlayable","true");
    ok=xbmcplugin.addDirectoryItem(handle=_thisPlugin,url=u,listitem=liz,isFolder=False)
    return ok


params=get_params()
url=None
name=None
mode=None



try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        cats()

elif mode==1:
	get_games(url)

elif mode==2:
		
        print ""+url
        get_links(url)
		
		
if mode ==3:
	get_video(url)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
