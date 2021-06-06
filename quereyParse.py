from urllib.parse import urlparse, parse_qs

# Google検索 桜
prs = urlparse('https://www.google.com/search?q=%E6%A1%9C&oq=%E6%A1%9C&aqs=chrome..69i57j0i131i433j0j0i433j0j0i433l3j0i131i433j0i433.1280j0j7&sourceid=chrome&ie=UTF-8')

print( "URLをParse" )
print( prs )

print("")

query_str = prs.query

print( "QueryをParse" )
print( query_str )

print("")


query_str2 = parse_qs(prs.query)

print( "QueryをParse" )
print( query_str2 )
