from pathlib import Path
import re

FORM_FILES = [Path('index.html'), Path('contact.html')]
THANK_YOU = Path('thank-you.html')

success_pattern = re.compile(
    r"(window\.dataLayer\.push\(\{\s*event:'website_form_submission',\s*source_page:form\.dataset\.sourcePage\|\|document\.title\s*\}\);\s*)"
    r"(status\.textContent='Submitted successfully\. Redirecting\.\.\.';\s*window\.location\.href=thankYou;)"
)

session_block = """try{\n        sessionStorage.setItem('tlma_lead_submitted','1');\n        sessionStorage.setItem('tlma_lead_source_page',form.dataset.sourcePage||document.title);\n      }catch(_e){}\n\n      """

for path in FORM_FILES:
    text = path.read_text(encoding='utf-8')
    if "sessionStorage.setItem('tlma_lead_submitted','1')" in text:
        continue
    new_text, count = success_pattern.subn(r"\1" + session_block + r"\2", text, count=1)
    if count != 1:
        raise SystemExit(f'Expected one successful form handler in {path}, found {count}')
    path.write_text(new_text, encoding='utf-8')

thank_you = THANK_YOU.read_text(encoding='utf-8')
if 'id="tlma-generate-lead-event"' not in thank_you:
    conversion_script = r'''<script id="tlma-generate-lead-event">
(function(){
  window.dataLayer=window.dataLayer||[];
  var confirmed=false;
  var leadSource='website';

  try{
    confirmed=sessionStorage.getItem('tlma_lead_submitted')==='1';
    leadSource=sessionStorage.getItem('tlma_lead_source_page')||'website';
    if(confirmed){
      sessionStorage.removeItem('tlma_lead_submitted');
      sessionStorage.removeItem('tlma_lead_source_page');
    }
  }catch(_e){}

  if(!confirmed) return;

  window.dataLayer.push({
    event:'generate_lead',
    lead_source:leadSource,
    form_type:'consultation',
    conversion_page:'thank-you'
  });
})();
</script>
'''
    if '</body>' not in thank_you:
        raise SystemExit('thank-you.html missing </body>')
    thank_you = thank_you.replace('</body>', conversion_script + '</body>', 1)
    THANK_YOU.write_text(thank_you, encoding='utf-8')

# Validation
for path in FORM_FILES:
    text = path.read_text(encoding='utf-8')
    assert text.count("sessionStorage.setItem('tlma_lead_submitted','1')") == 1, path
    assert text.count("sessionStorage.setItem('tlma_lead_source_page'") == 1, path
    assert "event:'website_form_submission'" in text, path

thank_you = THANK_YOU.read_text(encoding='utf-8')
assert thank_you.count('id="tlma-generate-lead-event"') == 1
assert "event:'generate_lead'" in thank_you
assert "confirmed=sessionStorage.getItem('tlma_lead_submitted')==='1'" in thank_you
assert '<meta content="noindex,follow" name="robots"/>' in thank_you

print('Measurement foundation patch validated successfully.')
