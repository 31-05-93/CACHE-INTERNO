from pathlib import Path
import json,shutil,base64,runpy
root=Path(__file__).resolve().parents[1];out=root/'dist'
if (out/'index.html').exists():(out/'index.html').unlink()
def js(v):return json.dumps(v,ensure_ascii=False)
def b64(p):return base64.b64encode((root/p).read_bytes()).decode()
assets={
 '/assets/sales-xlsx-v1.mjs':{'type':'text/javascript;charset=utf-8','data':b64('worker/xlsx-reader.mjs')},
 '/assets/interior-finishes-v3.webp':{'type':'image/webp','data':b64('worker/finish-reference.webp')},
 '/assets/departments-v1.webp':{'type':'image/webp','data':b64('worker/department-scenes.webp')},
 '/assets/cxc-pdf.mjs':{'type':'text/javascript;charset=utf-8','data':b64('worker/pdfjs/pdf.mjs')},
 '/assets/cxc-pdf.worker.mjs':{'type':'text/javascript;charset=utf-8','data':b64('worker/pdfjs/pdf.worker.mjs')}
}
source_export=runpy.run_path(str(root/'scripts/source-export.py'))['source_zip']()
(out).mkdir(exist_ok=True);(out/'cache-interiores-codigo.zip').write_bytes(source_export)
worker='const SOURCE_ZIP_B64='+js(base64.b64encode(source_export).decode())+';\nconst CLIENTS_SEED='+js(json.loads((root/'worker/clients-seed.json').read_text()))+';\nconst CLIENTS_XLSX_B64='+js(b64('worker/clients-source.xlsx'))+';\nconst SALES_SEED='+js(json.loads((root/'worker/sales-seed.json').read_text()))+';\nconst SALES_XLSX_B64='+js(b64('worker/sales-source.xlsx'))+';\nconst ASSETS='+js(assets)+';\nconst CXC_PDF_B64='+js(b64('worker/cxc-source.pdf'))+';\nconst CXC_EXCEL_B64='+js(b64('worker/cxc-comments.xlsx'))+';\nconst SEED='+js(json.loads((root/'worker/seed.json').read_text()))+';\nconst CXC_SEED='+js(json.loads((root/'worker/cxc-seed.json').read_text()))+';\nconst HTML='+js((root/'web/index.html').read_text())+';\n'+(root/'worker/api.js').read_text()+'\n'+(root/'worker/cxc-api.js').read_text()+'\n'+(root/'worker/projection-api.js').read_text()+'\n'+(root/'worker/clients-api.js').read_text()+'''
export default {async fetch(request,env){const url=new URL(request.url);if(url.pathname.startsWith('/api/cxc'))return cxcApi(request,env);if(url.pathname.startsWith('/api/okr'))return api(request,env);const asset=ASSETS[url.pathname];if(asset)return new Response(Uint8Array.from(atob(asset.data),c=>c.charCodeAt(0)),{headers:{'content-type':asset.type,'cache-control':'public,max-age=31536000,immutable','x-content-type-options':'nosniff'}});if(url.pathname==='/'||url.pathname==='/index.html')return new Response(HTML,{headers:{'content-type':'text/html;charset=utf-8','cache-control':'no-cache','x-content-type-options':'nosniff'}});return new Response('No encontrado',{status:404})}};
'''
(out/'server').mkdir(parents=True,exist_ok=True);(out/'server/index.js').write_text(worker)
(out/'.openai').mkdir(exist_ok=True);shutil.copy(root/'.openai/hosting.json',out/'.openai/hosting.json');shutil.copytree(root/'drizzle',out/'drizzle',dirs_exist_ok=True)
print('Worker y migraciones preparados:',len(worker),'caracteres')
