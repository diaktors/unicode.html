try:
  from mod_python import apache, util
except ImportError:
  pass
import re, sys, os

def index(req, pattern, limit = 256):
  regexps = [re.compile(i, re.IGNORECASE) for i in re.compile('\s+').split(pattern)]
  cnt = 0
  l = []
  def match(line):
    d = line.split(';')
    for i in regexps:
      if not (i.search(d[0]) or i.search(d[1]) or i.search(d[10])):
        return None
    return d
  for line in open(os.path.join(os.path.dirname( __file__ ), 'UnicodeData.txt')):
    d = match(line)
    if not(d): continue
    cnt = cnt + 1
    if cnt > limit: break
    o = {
        'cpt': d[0],
        'cpti': int(d[0], 16),
        #'c': unichr(int(d[0], 16)),
        'cat': d[2],
        'n': d[1],
        }
    l.append(o)
  if req: req.content_type = 'application/json'
  if req: req.headers_out['Access-Control-Allow-Origin'] = '*'
  return str(l).replace("'", '"')

if __name__ == '__main__':
  print(index(None, sys.argv[1]))
