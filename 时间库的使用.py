import pendulum;
dt=pendulum.datetime(2023,9,22)
print(dt);
#使用本地时间
local=pendulum.local(2023,9,22)
print("本地时间",local)
print("本地时区",local.timezone.name)
#创建日期时间
utc=pendulum.now('UTC')
print(utc)
#UTC转化其他时区时间
europe=utc.in_timezone('Europe/Paris')
print('巴黎当前时间',europe)