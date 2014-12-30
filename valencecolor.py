# -*- coding: utf-8 -*-
import sys
import array
import codecs
import re
from optparse import OptionParser
import bayes

#translation
try:
  from ekorpus.lib.base import *
except ImportError:
  def _(s):
    return s

silent = None
hybrid = 1

htmlStart = """
<html><head>
<style>
</style>
</head>
<body>
"""

htmlEnd = """
</body>
</html>
"""
paraOpen = '<div class="'
paraClose = '</div>'
words = ''

def load():
  global words
  if words:
    return words
  words = {}
  with codecs.open('sqnad.csv', 'r', encoding='utf-8') as f:
    for row in f:
      parts=row.split(',',3)
      if len(parts)<2:
        continue
      words[parts[0]] = parts[1]
      
  words['ei'] = ''
  words['ega'] = ''

  return words

def mark(text, words):

  space = re.compile('([\'".,!?\\s\\(\\)]+)')
  stop = re.compile("[,.!?]")
  para = re.compile("\\n")

  textWords = space.split(text)
  positive = negative = extreme = count = 0
  total = [0,0,0,0]
  paraStart=0
  r = []
  stats = []
  bayesStats = []
  wordStyle = { '1':'word positiveW', '-1':'word negativeW', '-8':'word extremeW'}
  statStyle = { 'positiivne':'positiveB', 'negatiivne':'negativeB', 'neutraalne':'neutralB' }
  statWords = []

  def doBayes():
    feats = dict([(item, True) for item in statWords if not space.match(item)])
    c = bayes.classify(feats)
    bayesStats.append(c)
    return statStyle[c]

  def closePara():

    if len(r) != paraStart:
      
      s = '<a name="%d"></a>%s' % (len(stats), paraOpen)
      if extreme > 0:
        s = s+'para extremeP'
      elif positive>negative:
        s = s+'para positiveP'
      elif negative>positive:
        s = s+'para negativeP'
      elif positive>0:
        s = s+'para mixedP'
      else:
        s = s+'para neutralP'

      if hybrid:
          stat_class = doBayes()
          s = s + " " + stat_class
          del statWords[:]

      s = s + '">'

      r.insert(paraStart,s)
      r.append(word)
      r.append(paraClose)
      total[0] = total[0] + count
      total[1] = total[1] + positive 
      total[2] = total[2] + negative 
      total[3] = total[3] + extreme 
      stats.append((count,positive,negative,extreme))
    return len(r)

  try:
    i = iter(textWords)
    while 1:
      word = next(i)
      if not word:
        continue
      if para.search(word):
        paraStart=closePara()
        positive = negative = extreme = count = 0
        continue

      if not space.search(word):
        count = count + 1
        if hybrid:
            statWords.append(word)

      w = word.lower()
      if w in words:
        flag = words[w]

        if not flag: #negator
          separator = next(i,'.')
          word = word + separator
          if stop.search(separator): # neg eos
            r.append(word)
            continue
          
          word2 = next(i,'')
          if not word2: # neg eof
            r.append(word)
            continue

          word = word + word2
          w = word2.lower()
          if w in words:
            flag = words[w]
            if flag == "1":
              flag = "-1"
            elif flag == "-1":
              flag = "1"
            elif flag == "-8":
              flag = "-8"
            else:
              flag = '' # neg neg  
          else:
            flag = "-1"   
             
        if flag == "1":
          positive = positive + 1
        elif flag == "-1":
          negative = negative + 1
        elif flag == "-8":
          extreme = extreme + 1

        if flag:
          r.append('<span class="%s">' % (wordStyle[flag]))
        r.append(word)
        if flag:
          r.append("</span>")
      else:
        r.append(word)
      word=''
  except StopIteration:
    pass
  closePara()
  rtn = '<div class="text">' + ''.join(r) + '</div>'

  # rtn:   html
  # total: word counts (count, positive, negative, extreme) for whole text 
  # stats: list of word counts for each paragraph
  return (rtn, total, stats, bayesStats)
 
def textValence(all,para):
  """Calculate whole text emotion from paragraphs words counts.
     where para = [neutral, positive, negative, mixed] total number of words in each type of paragraph.
     and "all" is the total number of words in the text.
  """
  count=0 # number of different emotions
  maxVal=pos=0 # max and its position

  for i, val in enumerate(para):
    if val>0:
      count = count+1
    if val>maxVal: 
      maxVal=val
      pos=i

  valence = _('mostly mixed')
  if count==1:
    valence = [_('only neutral'), _('only positive'), _('only negative'), _('only mixed')][pos]
  elif count==2:
    if (float(all)/maxVal)<1.5:
      valence = [_('mostly neutral'), _('mostly positive'), _('mostly negative'), _('mostly mixed')][pos]
  else:
    if (all/maxVal)<=1:
      valence = [_('mostly neutral'), _('mostly positive'), _('mostly negative'), _('mostly mixed')][pos]
  return valence

def chart(total, stats):
  all = total[0]
  if all==0:
    return ''
  r = []
  para = [0,0,0,0]  # neutral, positive, negative, mixed

  r.append('<div class="chart">')
  i = 0
  for s in stats:
    positive = s[1]
    negative = s[2]
    extreme = s[3]
    valence = 'tile neutralT'
    if extreme>0:
      para[2]=para[2]+s[0] #count all words in this paragraph as negative
      valence = 'tile extremeT'
    elif positive>negative:
      para[1]=para[1]+s[0]
      valence = 'tile positiveT'
    elif negative>positive:
      para[2]=para[2]+s[0]
      valence = 'tile negativeT' 
    elif positive>0:
      para[3]=para[3]+s[0]
      valence = 'tile mixedT'
    else:
      para[0]=para[0]+s[0]

    label1=_('positive:')
    label2=_('negative:')
    label3=_('extreme:')
 
    r.append(
      '''
<a href="#%d"><div class="bar %s" style="width:%.2f%%">&nbsp;<span class="info">%s %d<br/>%s %d<br/>%s %d<br/>%s %d</span></div></a>'''
      % (i, valence, (10000*s[0]/all)/100.0, _('words:'), s[0], label1, positive, label2, negative, label3, extreme)
    )
    i = i+1
    
  r.append('</div>')

  valence = textValence(all,para)
  valenceDiv = '<div class="textvalence">%s: %s</div>' % (_('Valence'),valence) 

  return (valence, valenceDiv + ("".join(r)))

  #<div class="bar" style="width:10%;height:90%;top:10%;background-color:blue">&nbsp;</div>

    
def marktext(text, dataonly) :
  """For web"""
  global words
  load()
  t = mark(text, words)
  s =  chart(t[1],t[2])
  if dataonly:
    if dataonly=="2":
      return s[0]
    if dataonly=="3":
      return emotionBayes(t[3],t[1],t[2])
    return s[1] + t[0]
  return t[0] + s[1]

def emotionBayes(emotions, total, stats):
  all = total[0]
  if all==0:
    return ''

  para = [0,0,0,0]  # neutral, positive, negative, mixed
  for i,e in enumerate(emotions):
    n = stats[i][0]
    if e=="positiivne":
      para[1] = para[1]+n
    elif e=="negatiivne":
      para[2] = para[2]+n
    elif e=="neutraalne":
      para[0] = para[0]+n
  return textValence(all,para)

def doit(filename):
  """Standalone"""
  global words
  load()
  fi = codecs.open(filename, 'r', encoding='utf-8')
  text=fi.read()
  fi.close()
  t = mark(text,words)
  s = chart(t[1],t[2])

  if not silent:
    fo = codecs.open(filename+'.html', 'w', encoding='utf-8')
    fo.write(htmlStart)
    fo.write(t[0])
    #fo.write(t[0].replace('\r','<br>'))
    fo.write(htmlEnd)
    fo.close()
  else:
    print "Dict:", s[0]
    print "Bayes:", emotionBayes(t[3],t[1],t[2]), t[3]

def main():

    global silent

    parser = OptionParser(usage='Usage: %prog file')
    parser.add_option('-s', '--silent', action="store_true", dest="silent", help='Silent: no html file')
    opts, args = parser.parse_args()
    if len(args)!=1: # or not opts.segment:
        parser.print_help()
        sys.exit(1)
    if opts.silent:
        silent=opts.silent

    doit(args[0])

if __name__ == '__main__':
    main()

