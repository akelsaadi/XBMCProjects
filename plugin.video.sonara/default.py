# -*- coding: utf8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
from httplib import HTTP
from urlparse import urlparse
import StringIO
import httplib
import time


__settings__ = xbmcaddon.Addon(id='plugin.video.sonara')
__icon__ = __settings__.getAddonInfo('icon')
__fanart__ = __settings__.getAddonInfo('fanart')
__language__ = __settings__.getLocalizedString
_thisPlugin = int(sys.argv[1])
_pluginName = (sys.argv[0])



def patch_http_response_read(func):
    def inner(*args):
        try:
            return func(*args)
        except httplib.IncompleteRead, e:
            return e.partial

    return inner
httplib.HTTPResponse.read = patch_http_response_read(httplib.HTTPResponse.read)


def CATEGORIES():
	#xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%('WARNING','This addon is completely FREE DO NOT buy any products from http://tvtoyz.com/', 16000, 'http://upload.wikimedia.org/wikipedia/he/e/ed/Sonara_logo_.gif'))
	addDir('2016 مسلسلات رمضان ','http://www.sonara.net/vncat/92/%D9%85%D8%B3%D9%84%D8%B3%D9%84%D8%A7%D8%AA-%D8%B1%D9%85%D8%B6%D8%A7%D9%86-2016',1,'http://profile.ak.fbcdn.net/hprofile-ak-ash4/s160x160/416801_327989490581599_1718150811_a.jpg')
	addDir('مسلسلات رمضان ','http://www.sonara.net/vncat/90/',1,'http://profile.ak.fbcdn.net/hprofile-ak-ash4/s160x160/416801_327989490581599_1718150811_a.jpg')
	addDir('مسلسلات رمضان 2014','http://www.sonara.net/vncat/86/%D9%85%D8%B3%D9%84%D8%B3%D9%84%D8%A7%D8%AA_%D8%B1%D9%85%D8%B6%D8%A7%D9%86_2014',1,'http://profile.ak.fbcdn.net/hprofile-ak-ash4/s160x160/416801_327989490581599_1718150811_a.jpg')
	addDir('مسلسلات رمضان 2013','http://www.sonara.net/videon-85.html',1,'http://profile.ak.fbcdn.net/hprofile-ak-ash4/s160x160/416801_327989490581599_1718150811_a.jpg')
	addDir('مسلسلات عربية','http://www.sonara.net/vncat/49/%D9%85%D8%B3%D9%84%D8%B3%D9%84%D8%A7%D8%AA_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9',1,'http://profile.ak.fbcdn.net/hprofile-ak-ash4/s160x160/416801_327989490581599_1718150811_a.jpg')
	addDir('كرتون ','http://www.sonara.net/vncat/53/%D9%83%D8%B1%D8%AA%D9%88%D9%86',1,'http://profile.ak.fbcdn.net/hprofile-ak-ash4/s160x160/416801_327989490581599_1718150811_a.jpg')
	addDir('افلام عربية','http://www.sonara.net/vcat/603/%D8%A7%D9%81%D9%84%D8%A7%D9%85_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9',4,'http://profile.ak.fbcdn.net/hprofile-ak-ash4/s160x160/416801_327989490581599_1718150811_a.jpg')
	addDir('افلام اسود و ابيض','http://www.sonara.net/vcat/722/%D8%A7%D9%81%D9%84%D8%A7%D9%85_%D8%A7%D8%A8%D9%8A%D8%B6_%D9%88%D8%A7%D8%B3%D9%88%D8%AF',4,'http://profile.ak.fbcdn.net/hprofile-ak-ash4/s160x160/416801_327989490581599_1718150811_a.jpg')
	#addDir('افلام وثائقية','http://www.sonara.net/video_cat-970.html',4,'http://profile.ak.fbcdn.net/hprofile-ak-ash4/s160x160/416801_327989490581599_1718150811_a.jpg')
	addDir('برامج','http://www.sonara.net/vncat/52/%D8%A8%D8%B1%D8%A7%D9%85%D8%AC',1,'http://profile.ak.fbcdn.net/hprofile-ak-ash4/s160x160/416801_327989490581599_1718150811_a.jpg')
	#addDir('خاص بالصنارة','http://www.sonara.net/videon-54.html',1,'http://profile.ak.fbcdn.net/hprofile-ak-ash4/s160x160/416801_327989490581599_1718150811_a.jpg')
	addDir('مسلسلات تركية','http://www.sonara.net/vncat/50/%D9%85%D8%B3%D9%84%D8%B3%D9%84%D8%A7%D8%AA_%D8%AA%D8%B1%D9%83%D9%8A%D8%A9',1,'http://profile.ak.fbcdn.net/hprofile-ak-ash4/s160x160/416801_327989490581599_1718150811_a.jpg')
	addDir('افلام تركية','http://www.sonara.net/vcat/860/%D8%A7%D9%81%D9%84%D8%A7%D9%85_%D8%AA%D8%B1%D9%83%D9%8A%D8%A9',4,'http://profile.ak.fbcdn.net/hprofile-ak-ash4/s160x160/416801_327989490581599_1718150811_a.jpg')
	#addDir('افلام هندية','http://www.sonara.net/video_cat-604.html',4,'http://profile.ak.fbcdn.net/hprofile-ak-ash4/s160x160/416801_327989490581599_1718150811_a.jpg')
	
	
		
def listContent(url):
	  
    req = urllib2.Request(url)
    req.add_header('Host', 'www.sonara.net')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20100101 Firefox/21.0')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    req.add_header('Accept-Language', 'en-US,en;q=0.5')
    req.add_header('Cookie', 'InterstitialAd=1; __utma=261095506.1294916015.1370631116.1370631116.1370631116.1; __utmb=261095506.1.10.1370631116; __utmc=261095506; __utmz=261095506.1370631116.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)')
   
    
    req.add_header('Connection', 'keep-alive')
    response = urllib2.urlopen(req)
    link=response.read()
    name = ""
    img = ""
    path = ""
    base = "http://sonara.net"
    target= re.findall(r"<div class='mediasection'>(.*?)\s(.*?)<div class='footer'>", link, re.DOTALL)
    for itr in target:
        myPath=str( itr[1]).split("'>")
        for items in myPath:
        
            if "<a href=" in str( items):
                path=str( items).split("<a href='")[1]
                path=base+str( path).strip()
                
            if "<img src='" in str( items):
                img=str( items).split("<img src='")[1]
                img=str(img).strip()
                
            if "<h4>" in str( items):
                name=str( items).split("</h4></a>")[0]
                name=str(name).replace("<h4>","").strip()
                addDir(name,path,2,img)

def listFilmContent(url):
    req = urllib2.Request(url)
    req.add_header('Host', 'www.sonara.net')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20100101 Firefox/21.0')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    req.add_header('Accept-Language', 'en-US,en;q=0.5')
    req.add_header('Cookie', 'InterstitialAd=1; __utma=261095506.1294916015.1370631116.1370631116.1370631116.1; __utmb=261095506.1.10.1370631116; __utmc=261095506; __utmz=261095506.1370631116.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)')
   
    
    req.add_header('Connection', 'keep-alive')
    response = urllib2.urlopen(req)
    link=response.read()
    name = ""
    img = ""
    path = ""
    base = "http://sonara.net"
    target= re.findall(r"<div class='video_listrel'>(.*?)\s(.*?)<div class='footer'>", link, re.DOTALL)
    for itr in target:
        myPath=str( itr[1]).split("'>")
        for items in myPath:
        
            if "<a href=" in str( items):
				path=str( items).split("<a href='")[1]
				path=str( path).strip()
				path=str( path).split("/")
				path =str( path[2]).strip()
                
            if "<img src='" in str( items):
                img=str( items).split("<img src='")[1]
                img=str(img).strip()
                
            if "<h4>" in str( items):
                name=str( items).split("</h4></a>")[0]
                name=str(name).replace("<h4>","").strip()
                addLink(name,path,3,img)
                                 

def listEpos(url):
	req = urllib2.Request(url)
	req.add_header('Host', 'www.sonara.net')
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20100101 Firefox/21.0')
	req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
	req.add_header('Accept-Language', 'en-US,en;q=0.5')
	req.add_header('Cookie', 'InterstitialAd=1; __utma=261095506.1294916015.1370631116.1370631116.1370631116.1; __utmb=261095506.1.10.1370631116; __utmc=261095506; __utmz=261095506.1370631116.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)')
	req.add_header('Connection', 'keep-alive')
	response = urllib2.urlopen(req)
	link=response.read()
	name = ""
	img = ""
	path = ""
	base = "http://sonara.net"
	target= re.findall(r"<div class='long_after_video'></div>(.*?)\s(.*?)<div class='footer'>", link, re.DOTALL)
	for itr in target:
		myPath=str( itr[1]).split("'>")
		for items in myPath:
			
			if "<a href=" in str( items):
				path=str( items).split("<a href='")[1]
				path=str( path).split("/")
				path =str( path[2]).strip()
            
			if "<img src='" in str( items):
				img=str( items).split("<img src='")[1]
				img=str(img).strip()
            
			if "<h4>" in str( items):
				name=str( items).split("</h4></a>")[0]
				name=str(name).replace("<h4>","").strip()
				addLink(name,path,3,img)
    

def getVideoFile(url):
	 
	try:
		url='http://www.sonara.net/video_player_new.php?ID='+str(url)
		req = urllib2.Request(url)
		response = urllib2.urlopen(req,timeout=1)
		link=response.read()
		print url
		print link
		for rows in link.split(";"):
			if "dlk.addVariable" and 'file'in rows:
				myvideo = rows.split(",")[1].split("&image")[0].replace("'","").strip()
				   
			if "dlk.addVariable" and 'streamer'in rows:
				streamer = rows.split(",")[1].replace("'","").replace(")","").strip()
				print streamer

		listItem = xbmcgui.ListItem(path=str(myvideo))
		xbmcplugin.setResolvedUrl(_thisPlugin, True, listItem)
	except:
		pass
				
    
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





def addLink(name,url,mode,iconimage):
    u=_pluginName+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    liz.setProperty("IsPlayable","true");
    ok=xbmcplugin.addDirectoryItem(handle=_thisPlugin,url=u,listitem=liz,isFolder=False)
    return ok
	


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
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
        CATEGORIES()
       
elif mode==1:
        print ""+url
        listContent(url)
	
elif mode==2:
        print ""+url
        listEpos(url)
elif mode==3:
	print ""+url
	getVideoFile(url)
	
elif mode==4:
        print ""+url
        listFilmContent(url)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
