#! /usr/bin/env python3
import codecs
import sys
import json
import cgi

# 標準出力をutf-8で出力
sys.stdout = codecs.getwriter('utf_8')(sys.stdout.detach())

# chat.txtのJSON読み込み
try:
    with open('chat.txt', 'r') as file:
        chat = json.load(file)
except ValueError:
    chat = []

# フォーム情報を取得
form = cgi.FieldStorage()
image = form.getfirst('image')
text = form.getfirst('text')
print(form)

if image and text:
    # chat.append(dict(image = image, text = text))
    chat.append({'image': image, 'text': text})
    # JSONファイルに保存
    with open('chat.txt', 'w') as file:
        json.dump(chat, file, indent=4)

# HTMLの表示
print('''
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>Python Web Programing</title>
</head>
<body>
    <h2>Pythonチャット</h2>
    <form action="chat.py" method="post">
        <select name="image">
            <option value="python_icon">Python</option>
            <option value="html_icon">HTML</option>
        </select>
        <input type="text" name="text">
        <input type="submit" value="発信">
    </form>
    <hr>
''')

for line in chat:
    print('<p><img src="/{0}.png" alt="image" width="100">{1}</p>'.format(line['image'], line['text']))

print('''
</body>
</html>
''')