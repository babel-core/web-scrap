import os, json, sys
from os import path
from datetime import datetime
from subprocess import call
from TrelloClipCollector import TrelloClipCollector
from MarkdownBuilder import MarkDownBuilder

def getDate():
    now = datetime.now()
    return '{0}{1}{2}'.format(now.year, now.month, now.day)

conf_filepath = path.splitext(__file__)[0] + '.conf'
text_conf = open(conf_filepath, 'r', encoding='utf-8').read()
conf = json.loads(text_conf)

clipType = conf["ClipType"]
clipUrl = conf["ClipUrl"]
searchUrl = conf["SearchUrl"]
interval = conf["Interval"]

print('============================================================================')
print("ClipType:", clipType)
print("ClipUrl:", clipUrl)
print("SearchUrl:", searchUrl)
print("Interval:", interval)
print('============================================================================')

if clipType == "Trello":
    clips = TrelloClipCollector().collect(clipUrl)
else:
    print("Unsupported Clip Type")
    sys.exit()

md_filepath = MarkDownBuilder(searchUrl, clips, interval=interval).build()
jn_filepath = path.splitext(md_filepath)[0] + '.ipynb'

print('Convert File :\n\t ' + '{0} to {1}'.format(md_filepath, jn_filepath))
call(['notedown', md_filepath, '--output', jn_filepath])
os.remove(md_filepath)
jn_filename = path.basename(jn_filepath)

now = datetime.now()
yyyymm = "{0}-{1}".format(now.year, now.month)
targetdir = path.join(path.dirname(jn_filepath), yyyymm)
targetPath = path.join(targetdir, jn_filename)

if os.direxists(targetdir) == False :
    os.mkdir(targetdir)
os.rename(jn_filepath, targetPath)