#!/usr/bin/env python
import os
from git import Repo
from wordcloud import WordCloud

working_dir = os.getcwd()
repo = Repo(working_dir)
assert not repo.bare

messages = ''
# authors = ''
for l in repo.iter_commits():

  # name = l.actor.name.replace(' ', '')
  # authors += str(name) +' '

  messages += l.message
  print l.message



wordcloud = WordCloud().generate(messages)
wordcloud.to_file('/tmp/git-messages.png')


# wordcloud = WordCloud().generate(authors)
# wordcloud.to_file('/tmp/git-authors.png')

