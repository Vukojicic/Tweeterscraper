#!/usr/bin/python
import tweepy
import cgi
from textblob import TextBlob



print "Content-type:text/html\r\n\r\n"
print '<!DOCTYPE html>'
print '<html lang="en">'
print '<head>'
print '<meta charset="UTF-8">'
print '<title>Tviter Pretrazivac</title>'

print '<style>'
print 'body {background-color: #F7730E;text-align: center;margin: auto;}'
print '</style>'

print '</head>'
print '<body>'



print '<form method="post" action="hello.py">'
print '<div class = "prva">'
print '<input type="text" name="name" style="border:3px solid #F7730E;"/>'
print '<input type="submit" value="Submit" />'
print '</div>'

form = cgi.FieldStorage()



consumer_key = '#####your_consumer_key#####'
consumer_secret = '#####your_consumer_secret######'

access_token = '#####your_access_token#####'
access_token_secret = '#####yout_access_token_secret#####'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



if form.getvalue("name"):
	name = form.getvalue("name")
	public_tweets = api.search(str(name),count=1000)
	print '<h1>Ovo su rezultati pretrage : ' + name + '</h1><br />'
	print '<textarea name="myTextBox" cols="50" rows="50" style="border:3px solid #F7730E;">'
	k=0
	for tweet in public_tweets:
		print str(tweet.text.encode('UTF-8')) + "\n \n"
		analysis = TextBlob(tweet.text)
		anal1=str(analysis.sentiment)
		print anal1
		p=analysis.sentiment.polarity
		print p
		print '--------------------------------------------------'
		k=k+p
	
	print 'Konacni rezultat polariteta je :'
	print k 
	print '</textarea>'



print '</form>'


print '</body>'
print '</html>'


	




