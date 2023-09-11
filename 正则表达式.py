import re
a='<li class="chapter-item" data-rid="1"><a class="chaptername"href="//www.qidian.com/chapter/1036843680/750089779/" alt="">001 大哥，你可别怪我！</a> </li>"'
b=re.findall('<li class="chapter-item" data-rid="(.*?)"><a class="chaptername"href="(.*?)".*?">(.*?)</a> </li>"',a)
print(b)