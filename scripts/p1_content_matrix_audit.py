from pathlib import Path
from html.parser import HTMLParser
import json,re

ROOT=Path(__file__).resolve().parents[1]
BASE='https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/'

class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.title=[]; self.in_title=False; self.h1=[]; self.in_h1=False; self.cur=[]; self.hrefs=[]; self.ids=set(); self.metas=[]; self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='title': self.in_title=True; self.cur=[]
        if tag=='h1': self.in_h1=True; self.cur=[]
        if 'id' in a: self.ids.add(a['id'])
        if tag=='a' and a.get('href') is not None: self.hrefs.append(a.get('href'))
        if tag=='meta': self.metas.append(a)
        if tag=='link': self.links.append(a)
    def handle_data(self,data):
        if self.in_title or self.in_h1: self.cur.append(data)
    def handle_endtag(self,tag):
        if tag=='title' and self.in_title:
            self.title.append(' '.join(''.join(self.cur).split())); self.in_title=False; self.cur=[]
        if tag=='h1' and self.in_h1:
            self.h1.append(' '.join(''.join(self.cur).split())); self.in_h1=False; self.cur=[]

files=sorted(ROOT.glob('*.html'))
site={}
for path in files:
    text=path.read_text(encoding='utf-8',errors='replace')
    p=P(); p.feed(text)
    desc=''; robots=''; canonical=''
    for m in p.metas:
        if m.get('name','').lower()=='description': desc=m.get('content','')
        if m.get('name','').lower()=='robots': robots=m.get('content','')
    for l in p.links:
        rel=l.get('rel','')
        if isinstance(rel,list): rel=' '.join(rel)
        if 'canonical' in str(rel).lower(): canonical=l.get('href','')
    site[path.name]={'text':text,'title':p.title,'h1':p.h1,'hrefs':p.hrefs,'ids':p.ids,'desc':desc,'robots':robots,'canonical':canonical}

html_names=set(site)
def normalize(href,source):
    if not href or href.startswith(('#','mailto:','tel:','javascript:')): return None
    if href.startswith(BASE): href=href[len(BASE):]
    elif href.startswith('http://') or href.startswith('https://'): return None
    href=href.split('?',1)[0]
    if '#' in href: target,frag=href.split('#',1)
    else: target,frag=href,''
    if target in ('','./','.'):
        target='index.html'
    elif target.startswith('./'): target=target[2:]
    return target,frag

inbound={n:[] for n in html_names}; broken=[]; index_links=[]
for src,d in site.items():
    for href in d['hrefs']:
        norm=normalize(href,src)
        if not norm: continue
        target,frag=norm
        if target in html_names:
            inbound[target].append((src,href))
            if frag and frag not in site[target]['ids']:
                broken.append((src,href,'missing-fragment'))
        elif target.endswith('.html'):
            broken.append((src,href,'missing-file'))
        if target=='index.html' and href not in ('./','./#top','#top'):
            index_links.append((src,href))

terms=['before launch','demo form','future email-capture','illustrative performance','replace with verified','connect this form','production crm','example.com']
placeholders=[]
for n,d in site.items():
    low=d['text'].lower()
    for t in terms:
        if t in low: placeholders.append((n,t,low.count(t)))

print('===== P1 CONTENT + INTERNAL LINK MATRIX AUDIT =====')
print('HTML_FILES',len(files))
for n in sorted(site):
    d=site[n]
    print(f'PAGE|{n}|TITLE={d["title"]}|H1={d["h1"]}|CANON={d["canonical"]}|ROBOTS={d["robots"]}|INBOUND={len(inbound[n])}|OUTBOUND={len(d["hrefs"])}')
print('\n===== LOW-INBOUND INDEXABLE PAGES =====')
for n in sorted(site):
    if 'noindex' not in site[n]['robots'].lower() and n!='google83fa3a3dc6e43838.html':
        uniq=sorted(set(s for s,_ in inbound[n]))
        if len(uniq)<=2: print(f'LOW|{n}|UNIQUE_INBOUND={len(uniq)}|FROM={uniq}')
print('\n===== KEY HUB INBOUND =====')
for n in ['services.html','industries.html','resources.html','social-media-marketing-for-limo-companies.html','booking-systems.html','seo-for-limo-companies.html','google-ads-for-limo-companies.html','limo-website-design.html','geo-ai-search-optimization.html']:
    if n in site:
        uniq=sorted(set(s for s,_ in inbound[n]))
        print(f'HUB|{n}|UNIQUE_INBOUND={len(uniq)}|FROM={uniq}')
print('\n===== INDEX.HTML INTERNAL LINKS =====')
for x in index_links: print('INDEXLINK|'+repr(x))
print('\n===== BROKEN INTERNAL LINKS/FRAGMENTS =====')
for x in broken: print('BROKEN|'+repr(x))
print('BROKEN_COUNT',len(broken))
print('\n===== PLACEHOLDER / PRE-LAUNCH SIGNALS =====')
for x in placeholders: print('PLACEHOLDER|'+repr(x))
print('\n===== HOMEPAGE KEY RELATIONSHIPS =====')
for target in ['services.html','industries.html','resources.html','social-media-marketing-for-limo-companies.html','booking-systems.html','seo-for-limo-companies.html','google-ads-for-limo-companies.html','limo-website-design.html','geo-ai-search-optimization.html']:
    links=[]
    for h in site.get('index.html',{}).get('hrefs',[]):
        norm=normalize(h,'index.html')
        if norm and norm[0]==target: links.append(h)
    print(f'HOME|{target}|LINKS={links}')
print('\n===== JSON-LD =====')
for n,d in site.items():
    blocks=re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>\s*(.*?)\s*</script>',d['text'],flags=re.S|re.I)
    for i,b in enumerate(blocks,1):
        try: json.loads(b)
        except Exception as e: print(f'JSONLD_ERROR|{n}|BLOCK={i}|{e}')
print('AUDIT_DONE')
