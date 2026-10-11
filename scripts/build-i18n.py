from pathlib import Path
import json
source=Path('.shared-i18n/js/asf-i18n.js').read_text(encoding='utf-8')
catalog=json.loads(Path('translations-en.json').read_text(encoding='utf-8'))
assert catalog and all(isinstance(k,str) and isinstance(v,str) and k and v for k,v in catalog.items())
needle='  var SKIP = '
assert source.count(needle)==1,'Shared engine changed unexpectedly'
source=source.replace(needle,'  Object.assign(EN, '+json.dumps(catalog,ensure_ascii=False)+');\n'+needle,1)
source=source.replace("version:'1.0.0'","version:'1.0.0-manobras'",1)
source=source.replace('Home navigation and reviewed interface phrases; long-form content and satellites pending.','ASF Manobras learning content, checklist labels, FAQs and all 8 training focuses.')
source+='\n(function(){var original=document.title;function title(){document.title=window.ASF_I18N.getLanguage()===\'en\'?\'ASF Manobras — Surf Maneuvers, Cutback Guide and XP\':original;}window.addEventListener(\'asf:languagechange\',title);if(document.readyState===\'loading\')document.addEventListener(\'DOMContentLoaded\',title,{once:true});else title();})();\n'
html_path=Path('index.html')
html=html_path.read_text(encoding='utf-8')
include='<script defer src="i18n.js?v=1"></script>'
assert html.count('id="guia-cutback-completo"')==1,'Canonical Cutback anchor missing'
assert "localStorage.getItem('asf_manobras')" in html
assert "['Cutback',20]" in html
if include not in html:
    assert html.count('</body>')==1
    html=html.replace('</body>',include+'\n</body>')
Path('i18n.js').write_text(source,encoding='utf-8')
html_path.write_text(html,encoding='utf-8')
print('Built local shared-engine snapshot and',len(catalog),'reviewed catalog entries; game script untouched.')
