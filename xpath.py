from lxml import html, etree
import argparse
import sys

try: #python3
  import urllib.request as pyurllib
except: #python2
  import urllib2 as pyurllib

def parse_arguments(argv):
  parser = argparse.ArgumentParser(description='XPath tester')
  parser.add_argument('--url')
  parser.add_argument('--html')
  parser.add_argument('--xpath')
  return parser.parse_args(argv)

def main(argv):
  args = parse_arguments(argv)

  if args.xpath == None:
    print('What XPath that you need to try?')
    return
  print('XPath: ' + args.xpath)

  html_data = args.html

  if html_data == None:
    if (args.url != None):
      print('Start URL fetch')
      url = args.url
      if url[:4] != 'http':
        url = 'http://' + url
      html_data = pyurllib.urlopen(url).read()
    else:
      print('Please insert --html or --url')
      return
  
  tree = html.fromstring(html_data)
  results = tree.xpath(args.xpath)

  for result in results:
    try:
      print(etree.tostring(result, pretty_print=True))
    except:
      print(result)
    print('--- --- --- --- --- ---')
    
if __name__ == "__main__":
  main(sys.argv[1:])

