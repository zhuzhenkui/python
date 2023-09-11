import requests
a='https://v16m-default.akamaized.net/36b3f6312100eebad54cb532539104eb/64dfcd23/video/tos/alisg/tos-alisg-v-0051c001-sg/oU7mmegIDZnApQm8uFBJek4LYUnBNDjsI7tjbQ/?a=0&ch=0&cr=0&dr=0&er=0&lr=default&cd=0%7C0%7C0%7C0&br=1226&bt=613&cs=0&ds=6&ft=dl9~j-Inz7TRcusfiyq8Z&mime_type=video_mp4&qs=13&rc=amt2djk6ZnBobDMzODYzNEBpamt2djk6ZnBobDMzODYzNEBtZGcxcjRfMmdgLS1kMC1zYSNtZGcxcjRfMmdgLS1kMC1zcw%3D%3D&l=20230818133342182D1C7FFFCF4B457930&btag=e00068000'
# a='https://v3-web.douyinvod.com/d93e2f3587a7fbcf7c0073b9ac53b09c/64df8ac1/video/tos/cn/tos-cn-ve-15c001-alinc2/okIIQHTY9x9jwEAuIj1fsoefAcmHQaQoefjsE4/?a=6383&ch=224&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1167&bt=1167&cs=2&ds=3&ft=bvTKJbQQqUxRfu-VagkM5S_psHrBJBOsfbgQg3-Xg8kLd-I&mime_type=video_mp4&qs=15&rc=PGQ4aGVnNmQ2NGg8Z2U1NkBpanl5dzU6ZjlzazMzNGkzM0A1Y2JeMy80NmIxYC82NTE1YSNjMDVxcjRnL2xgLS1kLS9zcw%3D%3D&btag=e00028000&dy_q=1692367931&l=20230818221210CC269BCDC5A18E2505C4'
b=requests.get(a).content
open("154.mp4","wb").write(b)
