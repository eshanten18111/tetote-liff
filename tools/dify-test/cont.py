import json, sys, dify
KEEP = ("パラメータ抽出", "コード（支援", "IF/ELSE 10", "IF/ELSE 6", "IF/ELSE 4", "HTTP", "入口フォーム")
DROP = ("__usage","__reason","__is_success","headers")
def clean(o): return {k:v for k,v in o.items() if k not in DROP} if isinstance(o,dict) else o
user, conv = sys.argv[1], sys.argv[2]
turns = json.load(open(sys.argv[3]))
for q in turns:
    r = dify.turn(user, q, conv)
    conv = r["conversation_id"]
    print(f"\n--- USER: {q[:100]}")
    print(f"BOT: {r['answer'][:1500]}")
    for n in r["nodes"]:
        if any(k in (n["title"] or "") for k in KEEP):
            print(f"   [{n['title']}] {json.dumps(clean(n['outputs']),ensure_ascii=False)[:500]}")
    if r["error"]: print("   !!ERR", json.dumps(r["error"],ensure_ascii=False)[:300])
print("\nCONV:", conv)
