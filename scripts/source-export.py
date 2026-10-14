from pathlib import Path
from io import BytesIO
import json,zipfile,hashlib
root=Path(__file__).resolve().parents[1]
def source_zip():
 files=[]
 for directory in ['web','worker','db','drizzle','scripts','docs']:
  for p in (root/directory).rglob('*'):
   if p.is_file() and '__pycache__' not in p.parts and p.name!='finish-reference.png':files.append(p)
 files += [root/p for p in ['package.json','drizzle.config.ts','.gitignore','README.md'] if (root/p).exists()]
 buffer=BytesIO()
 with zipfile.ZipFile(buffer,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
  digests={}
  for p in sorted(files):
   name=p.relative_to(root).as_posix();data=p.read_bytes();digests[name]=hashlib.sha256(data).hexdigest();archive.writestr(name,data)
  archive.writestr('.openai/hosting.json',json.dumps({'d1':'DB','r2':'BUCKET'},indent=2))
  archive.writestr('ORIGEN.json',json.dumps({'source_project_id':'appgprj_6accf416fee08191ab83bd2557b2bebf','url':'https://cache-interiores-control-interno.espacio-de-t-0477.chatgpt.site','purpose':'Código de origen; usar el ID del proyecto de destino al publicar','live_database_included':False,'browser_local_data_included':False},ensure_ascii=False,indent=2))
  archive.writestr('SHA256.json',json.dumps(digests,indent=2))
 return buffer.getvalue()
if __name__=='__main__':
 destination=root/'dist'/'cache-interiores-codigo.zip';destination.parent.mkdir(exist_ok=True);data=source_zip();destination.write_bytes(data);print('ZIP preparado:',len(data),'bytes')
