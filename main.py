#Spider-man test bot for reddit @tigerater

#!/usr/bin/python
import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')

def checkcondition(c):
    text = c.body
    if "spiderman" in text or "Spiderman" in text:
        return True
    else:
        return False
    
#subreddit = reddit.get_subreddit('spiderbot')
#comments = subreddit.get_comments(limit=100)
comments = reddit.subreddit('marvelstudios').comments(limit=500)

if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []
else:
    with open("comments_replied_to.txt", "r") as f:
       comments_replied_to = f.read()
       comments_replied_to = comments_replied_to.split("\n")
       comments_replied_to = list(filter(None, comments_replied_to))
       
for c in comments:
    if c.id not in comments_replied_to:
        if checkcondition(c):
            c.reply("Mr. Stark come on, it's Spider-man, this must have been the millionth time by now :/ \n\n I'm a bot created by u/tigerater to correct the lack of hyphens found in Spider-man! I'll only be up in for a few days but please pm my owner if you have any questions!")
            comments_replied_to.append(c.id)
    with open("comments_replied_to.txt", "w") as f:
        for comment_id in comments_replied_to:
            f.write(comment_id + "\n")

