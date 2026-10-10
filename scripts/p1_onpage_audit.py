from pathlib import Path
import re, json, html, xml.etree.ElementTree as ET

ROOT = 'https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/'

def one(pat, text, flags=re.I|re.S):
    m = re.search(pat, text, flags)
    return html.unescape(re.sub(r'<[^>]+>', ' ', m.group(1)).strip()) if m else ''

def clean(s):
    return re.sub(r'\s+', ' ', html.unescape(s or '')).strip()

def schema_types(text):
    out=[]
    for raw in re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', text, re.I|re.S):
        try:
            data=json.loads(raw)
        except Exception:
            continue
        nodes=[]
        if isinstance(data,dict):
            nodes=data.get('@graph',[]) if isinstance(data.get('@graph'),list) else [data]
        for n in nodes:
            if isinstance(n,dict) and n.get('@type'):
                t=n['@type']
                if isinstance(t,list): out.extend(map(str,t))
                else: out.append(str(t))
    return ','.join(dict.fromkeys(out))

sitemap=ET.parse('sitemap.xml').getroot()
ns={'sm':'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls=[n.text.strip() for n in sitemap.findall('.//sm:loc',ns) if n.text]
print('P1_ONPAGE_AUDIT_START')
print('URL\tTITLE_LEN\tTITLE\tMETA_LEN\tMETA\tH1_COUNT\tH1\tH2_COUNT\tROBOTS\tCANONICAL\tSCHEMA_TYPES\tINTERNAL_LINKS\tWORD_COUNT')
for url in urls:
    rel=url[len(ROOT):] if url.startswith(ROOT) else url
    fn='index.html' if rel in ('','/') else rel
    p=Path(fn)
    if not p.exists():
        print(f'{url}\tMISSING_FILE')
        continue
    text=p.read_text(encoding='utf-8',errors='ignore')
    title=clean(one(r'<title[^>]*>(.*?)</title>',text))
    meta=clean(one(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\'][^>]*>',text) or one(r'<meta[^>]+content=["\'](.*?)["\'][^>]+name=["\']description["\'][^>]*>',text))
    robots=clean(one(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'](.*?)["\'][^>]*>',text) or one(r'<meta[^>]+content=["\'](.*?)["\'][^>]+name=["\']robots["\'][^>]*>',text))
    canonical=clean(one(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\'](.*?)["\'][^>]*>',text) or one(r'<link[^>]+href=["\'](.*?)["\'][^>]+rel=["\']canonical["\'][^>]*>',text))
    h1s=re.findall(r'<h1\b[^>]*>(.*?)</h1>',text,re.I|re.S)
    h1=clean(re.sub(r'<[^>]+>',' ',h1s[0])) if h1s else ''
    h2s=re.findall(r'<h2\b[^>]*>(.*?)</h2>',text,re.I|re.S)
    hrefs=re.findall(r'<a\b[^>]+href=["\']([^"\']+)["\']',text,re.I)
    internal=sum(1 for x in hrefs if not re.match(r'^(?:https?:)?//|^mailto:|^tel:',x,re.I))
    visible=re.sub(r'<script\b.*?</script>|<style\b.*?</style>',' ',text,flags=re.I|re.S)
    visible=re.sub(r'<[^>]+>',' ',visible)
    words=len(re.findall(r"\b[\w'-]+\b",html.unescape(visible)))
    row=[url,str(len(title)),title,str(len(meta)),meta,str(len(h1s)),h1,str(len(h2s)),robots,canonical,schema_types(text),str(internal),str(words)]
    print('\t'.join(x.replace('\t',' ') for x in row))
print('P1_ONPAGE_AUDIT_END')
