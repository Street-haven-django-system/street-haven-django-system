import json
with open('fixtures.json', 'rb') as f:
    content = f.read()
content = content.decode('latin-1')
data = json.loads(content)
with open('fixtures_clean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
print('Done')