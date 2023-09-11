import requests
import re
# 获取目标地址
# url='https://www.douyin.com/video/7077902717246508318'
url='http://www.100fyy1.com/mov/80293/1.html'
# 伪装浏览器
headers ={
    # cookie 用户信息
    'Cookie': 'douyin.com; ttwid=1%7ChzbVfjqzo1XfUiSsrRpC3GB40d_fbzQD6LrkWqjnpgo%7C1692367907%7C19f09517e4b14b500a2b97b3294652975ca1180e4e4c44ec3a464aa96c8c7b88; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; passport_csrf_token=bde58c5cf2359166be3cd897d5fa00d7; passport_csrf_token_default=bde58c5cf2359166be3cd897d5fa00d7; s_v_web_id=verify_llgo5nl9_Ift9Yysw_0Cap_4Iyl_Angn_cCpCrb7u1vpK; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtY2xpZW50LWNzciI6Ii0tLS0tQkVHSU4gQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tXHJcbk1JSUJEVENCdFFJQkFEQW5NUXN3Q1FZRFZRUUdFd0pEVGpFWU1CWUdBMVVFQXd3UFltUmZkR2xqYTJWMFgyZDFcclxuWVhKa01Ga3dFd1lIS29aSXpqMENBUVlJS29aSXpqMERBUWNEUWdBRW1ldE5TWERYaVJqTllQalhPdUl2SHg2TVxyXG5UV2pIbElmZkdwOExESGIwbVc2MGdYV1p4VGs2dTd4UGtGNE01TldLTWpGWjloVk10SGJOT2w5bUFxb0RQS0FzXHJcbk1Db0dDU3FHU0liM0RRRUpEakVkTUJzd0dRWURWUjBSQkJJd0VJSU9kM2QzTG1SdmRYbHBiaTVqYjIwd0NnWUlcclxuS29aSXpqMEVBd0lEUndBd1JBSWdLeG0xU25LLzRmNXRIUGhqSVVxUUhlRG5aeVR6L0d0V3JjRFFvUnRGVUtZQ1xyXG5JQjdMc1ZaNk9mN1d4RWs5UnF3bm9KWnVmUmFZSklEbUtCb0ZDYzUwWG5IbFxyXG4tLS0tLUVORCBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS1cclxuIn0=; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; ttcid=5311164df0f844228473340938ecd2ab12; strategyABtestKey=%221692538157.714%22; xgplayer_user_id=921227436417; douyin.com; device_web_cpu_core=20; device_web_memory_size=8; webcast_local_quality=null; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1693146349084%2C%22type%22%3Anull%7D; csrf_session_id=6c65228c2392c2ed790cb1a95f5dde6a; home_can_add_dy_2_desktop=%221%22; msToken=v30I5Hexf9jZUms8QUbqzlQaituIEh8AEA1tJ0CdxrqpgAQix4tXBoMhHYHgYdCJEwZrrf9niCS4FpleFtnN6CblTaRIzo4rlNNDXPMs8eO_Y-xnfXPPSy0fSV4=; tt_scid=bnNkcNs7npzpBTyQY2.J-VhZmIWIQqbbJeBolIDCIDnY4zms4OxK91OvRjzbnOAT7053; download_guide=%223%2F20230820%2F0%22; pwa2=%220%7C0%7C3%7C0%22; msToken=aSqWCE0YwGSf2wk4il5rsw_oF22RCbmwUqg_YQGfldVHnDJsSv_a_WpUVB5EiCqj-JvClqhORVTdT5pXVSh1fAYjQghdCbHk-hjyktAXoDziTg2NhxS2NTzVZOY=',
    # user-agent用户代理
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
request=requests.get(url=url,headers=headers)
# 获取数据 <response[200]> 反应成功不一定获取数据
print(request.text)
# 解析数据 提取