# Python_URL_Parse
### URLをPythonでParseする場合のサンプルコード
#### urlParse.py
#### URL(ex: http://www.cwi.nl:80/%7Eguido/Python.html)をパースするPythonコード
  
  
#### 実行結果は以下の通り
```
$ py urlParse.py
ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html', params='', query='', fragment='')
```

### URLとクエリをParseする場合のサンプルコード
#### quereyParse.py
#### URL(https://www.google.com/search?q=%E6%A1%9C&oq=%E6%A1%9C&aqs=chrome..69i57j0i131i433j0j0i433j0j0i433l3j0i131i433j0i433.1280j0j7&sourceid=chrome&ie=UTF-8)をパースするPythonコード
#### URLはGoogleで「桜」を検索した検索結果のURLとなる
  
  
#### 実行結果は以下の通り
```
$ py quereyParse.py
URLをParse
ParseResult(scheme='https', netloc='www.google.com', path='/search', params='', query='q=%E6%A1%9C&oq=%E6%A1%9C&aqs=chrome..69i57j0i131i433j0j0i433j0j0i433l3j0i131i433j0i433.1280j0j7&sourceid=chrome&ie=UTF-8', fragment='')

QueryをParse
q=%E6%A1%9C&oq=%E6%A1%9C&aqs=chrome..69i57j0i131i433j0j0i433j0j0i433l3j0i131i433j0i433.1280j0j7&sourceid=chrome&ie=UTF-8

QueryをParse
{'q': ['桜'], 'oq': ['桜'], 'aqs': ['chrome..69i57j0i131i433j0j0i433j0j0i433l3j0i131i433j0i433.1280j0j7'], 'sourceid': ['chrome'], 'ie': ['UTF-8']}
```
