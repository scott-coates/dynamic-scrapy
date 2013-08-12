import htmlentitydefs
import re


def unescape(text):
  def fixup(m):
    text = m.group(0)
    if text[:2] == '&#':
      # character reference
      try:
        if text[:3] == '&#x':
          return unichr(int(text[3:-1], 16))
        else:
          return unichr(int(text[2:-1]))
      except ValueError:
        pass
    else:
      # named entity
      try:
        text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
      except KeyError:
        pass
    return text # leave as is

  return re.sub(r'&#?\w+;', fixup, text)


def despacify(text):
  def fixup(m):
    text = m.group(0)
    return ' ' + ''.join(text.split()) + ' '

  return re.sub(r'((?:\s\S){3,})\s', fixup, text)

# this only works on really naive js obfuscations; tacks decoded emails on the end.
def decodeJs(text):
  def fixup(m):
    return ''.join(unichr(int(point)) for point in m.group(1).split(','))

  return re.sub(r'fromCharCode\((.+)\)', fixup, text)
