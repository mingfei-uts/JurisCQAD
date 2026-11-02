"""Split only by group_id. Ratios are deliberately required; no split is created on import."""
import argparse,json,hashlib,random,collections,gzip
from pathlib import Path

def main():
 p=argparse.ArgumentParser(description='按group_id划分数据，避免已识别的同题/近似题跨集合。')
 p.add_argument('--ratios',nargs=3,type=float,required=True,metavar=('TRAIN','VALIDATION','TEST'))
 p.add_argument('--seed',type=int,default=42)
 p.add_argument('--out',type=Path,required=True)
 a=p.parse_args()
 if any(x<0 for x in a.ratios) or abs(sum(a.ratios)-1)>1e-8:p.error('三个比例必须非负且合计为1')
 root=Path(__file__).resolve().parent
 data_path=root/'JurisCQAD_cleaned.jsonl'
 data=data_path.read_bytes() if data_path.exists() else gzip.decompress((root/'JurisCQAD_cleaned.jsonl.gz').read_bytes())
 records=[json.loads(x) for x in data.decode('utf-8').splitlines()]
 mapping=[json.loads(x) for x in (root/'split_groups.jsonl').open()]
 summary=json.loads((root/'summary.json').read_text())
 assert hashlib.sha256(data).hexdigest()==summary['clean_sha256'],'Dataset changed; regenerate grouping first'
 assert len(records)==len(mapping)
 groups=collections.defaultdict(list)
 for i,m in enumerate(mapping):
  assert m['clean_line']==i+1
  groups[m['group_id']].append(i)
 items=list(groups.items());random.Random(a.seed).shuffle(items)
 items.sort(key=lambda x:len(x[1]),reverse=True)
 names=['train','validation','test'];targets=[len(records)*r for r in a.ratios];counts=[0,0,0];allocation={}
 for gid,indices in items:
  bucket=max((i for i,r in enumerate(a.ratios) if r>0),key=lambda i:targets[i]-counts[i])
  allocation[gid]=names[bucket];counts[bucket]+=len(indices)
 a.out.mkdir(parents=True,exist_ok=True)
 paths=[a.out/(x+'.jsonl') for x in names]+[a.out/'assignments.jsonl',a.out/'split_summary.json']
 if any(x.exists() for x in paths):p.error('目标文件已存在，请选择新目录以免覆盖')
 handles={name:(a.out/(name+'.jsonl')).open('w') for name in names}
 with (a.out/'assignments.jsonl').open('w') as f:
  for record,m in zip(records,mapping):
   subset=allocation[m['group_id']]
   handles[subset].write(json.dumps(record,ensure_ascii=False)+'\n')
   f.write(json.dumps(dict(m,split=subset),ensure_ascii=False)+'\n')
 for f in handles.values():f.close()
 info={'seed':a.seed,'requested_ratios':dict(zip(names,a.ratios)),'record_counts':dict(zip(names,counts)),'groups':len(groups),'group_overlap':0,'note':'仅对已识别group_id保证不跨集合；不能排除未识别的语义近似题。'}
 (a.out/'split_summary.json').write_text(json.dumps(info,ensure_ascii=False,indent=2))
 print(json.dumps(info,ensure_ascii=False))

if __name__=='__main__':main()
