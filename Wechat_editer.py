import re
import requests
import time

def get_short_url(url_list):
    """
        :param url_list: url list and length <= 200
        :return: results list
        """
    headers = {
        'Pragma': 'no-cache',
        'Origin': 'http://tool.chinaz.com',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Cache-Control': 'no-cache',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Referer': 'http://tool.chinaz.com/tools/sinadwz.aspx',
    }

    data = {
        'url': "^".join(url_list) + "^"
    }
    flag1 = 0
    flag2 = 0
    while ((flag1 != 1) & (flag2 != 3)):
        try:
            response = requests.post('http://tool.chinaz.com/AjaxSeo.aspx?t=sinadwz', headers=headers, data=data)
            res_list = response.json()
            flag1 = 1
        except (requests.exceptions.ConnectionError, requests.exceptions.SSLError, KeyError, UnicodeDecodeError, IndexError):
            flag2 = flag2 + 1
            print(url_list + "connect failed!")
            if (flag2 == 3):
                print("网不好？还是网线没连？")
                exit(0)
                # time.sleep(2)
                # flag2 = 0
                # flag1 = 0

    return res_list

r_f_org = open('.\original_info_detail\original.txt','r',encoding='utf-8')
w_f_short = open('.\original_info_detail\\shorturl_original.txt','w',encoding='utf-8')
for d_org in r_f_org.readlines():
    if(re.search('http',d_org)):
        if(re.search('t.cn/',d_org)):
            w_f_short.write(d_org)
        else:
            lis = [str(d_org).strip()]
            print(lis)
            shorturl = get_short_url(lis)
            w_f_short.write(str(shorturl[0]['url_short'])+'\n')
    else:
        w_f_short.write(d_org)

r_f_org.close()
w_f_short.close()


w_f_today = open('.\original_info_detail\\today.txt', 'w', encoding='utf-8')

# 写头
r_f_head = open('.\original_info_detail\\head.html', 'r', encoding='utf-8')
for d_head in r_f_head.readlines():
    w_f_today.write(d_head)
r_f_head.close()
##################
#身体
n=1
line=1
r_f_short_org = open('.\original_info_detail\shorturl_original.txt','r',encoding='utf-8')
for d_org in r_f_short_org.readlines():
   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
   if (re.search("安全-资讯",d_org)):   # 如果是安全资讯
       r_f_title = open('.\original_info_detail\\title.html','r',encoding='utf-8')
       for d_title in r_f_title.readlines():
           if (d_title.replace('title_name', "安全资讯")):
               new_one = d_title.replace('title_name', d_org)
               w_f_today.write(new_one)
           else:
               w_f_today.write(d_title)
       r_f_title.close()
   else:
       #####################################################################
       if (re.search("国际-动态",d_org)):  # 如果是国际动态
           r_f_title = open('.\original_info_detail\\title.html', 'r', encoding='utf-8')
           for d_title in r_f_title.readlines():
               if (d_title.replace('title_name', "国际动态")):
                   new_one = d_title.replace('title_name', d_org)
                   w_f_today.write(new_one)
               else:
                   w_f_today.write(d_title)
           r_f_title.close()
       else:
           #####################################################################
           if (re.search("安全-事件",d_org)):  # 如果是
               r_f_title = open('.\original_info_detail\\title.html', 'r', encoding='utf-8')
               for d_title in r_f_title.readlines():
                   if (d_title.replace('title_name', "安全事件")):
                       new_one = d_title.replace('title_name', d_org)
                       w_f_today.write(new_one)
                   else:
                       w_f_today.write(d_title)
               r_f_title.close()
           else:
               #####################################################################
               if (re.search("最新-漏洞",d_org)):  # 如果是
                   r_f_title = open('.\original_info_detail\\title.html', 'r', encoding='utf-8')
                   for d_title in r_f_title.readlines():
                       if (d_title.replace('title_name', "最新漏洞")):
                           new_one = d_title.replace('title_name', d_org)
                           w_f_today.write(new_one)
                       else:
                           w_f_today.write(d_title)
                   r_f_title.close()
               else:
                   #####################################################################
                   if (re.search("工具-脚本",d_org)):  # 如果是
                       r_f_title = open('.\original_info_detail\\title.html', 'r', encoding='utf-8')
                       for d_title in r_f_title.readlines():
                           if (d_title.replace('title_name', "工具脚本")):
                               new_one = d_title.replace('title_name', d_org)
                               w_f_today.write(new_one)
                           else:
                               w_f_today.write(d_title)
                       r_f_title.close()
                   else:
                       #####################################################################
                       if (re.search("安全-研究",d_org)):  # 如果是
                           r_f_title = open('.\original_info_detail\\title.html', 'r', encoding='utf-8')
                           for d_title in r_f_title.readlines():
                               if (d_title.replace('title_name', "安全研究")):
                                   new_one = d_title.replace('title_name', d_org)
                                   w_f_today.write(new_one)
                               else:
                                   w_f_today.write(d_title)
                           r_f_title.close()
                       else:
                           #####################################################################
                           if(d_org=="\n"):     # 如果空行
                               n = n+1
                               print(n)
                           else:                # 如果不是标题
                               #####################################################################
                               if(line%3 == 1):
                                   r_f_detail1 = open('.\original_info_detail\\detail1.html', 'r', encoding='utf-8')
                                   for d_detail1 in r_f_detail1.readlines():
                                       if (d_detail1.replace('detail_title', d_org)):
                                           new_one = d_detail1.replace('detail_title', d_org)
                                           w_f_today.write(new_one)
                                       else:
                                           w_f_today.write(d_detail1)
                                   r_f_detail1.close()
                                   line = line + 1
                               else:
                                   #####################################################################
                                   if (line % 3 == 2):
                                       r_f_detail2 = open('.\original_info_detail\\detail2.html', 'r', encoding='utf-8')
                                       for d_detail2 in r_f_detail2.readlines():
                                           if (d_detail2.replace('detail_info', d_org)):
                                               new_one = d_detail2.replace('detail_info', d_org)
                                               w_f_today.write(new_one)
                                           else:
                                               w_f_today.write(d_detail2)
                                       r_f_detail2.close()
                                       line = line + 1
                                   else:
                                       #####################################################################
                                       if (line % 3 == 0):
                                           r_f_detail3 = open('.\original_info_detail\\detail3.html', 'r',encoding='utf-8')
                                           for d_detail3 in r_f_detail3.readlines():
                                               if (d_detail3.replace('detail_url', d_org)):
                                                   new_one = d_detail3.replace('detail_url', d_org)
                                                   w_f_today.write(new_one)
                                               else:
                                                   w_f_today.write(d_detail3)
                                           r_f_detail3.close()
                                           ###################################################将评价删了，并到这里了
                                           r_f_detail4 = open('.\original_info_detail\\detail4.html', 'r',encoding='utf-8')
                                           for d_detail4 in r_f_detail4.readlines():
                                               if (d_detail4.replace('review_editer', '')):# 就是这个''里面
                                                   new_one = d_detail4.replace('review_editer', '')
                                                   w_f_today.write(new_one)
                                               else:
                                                   w_f_today.write(d_detail4)
                                           r_f_detail4.close()
                                           ###################################################
                                           line = line + 1
                                       # else:
                                       #     #####################################################################
                                       #     if (line % 4 == 0):
                                       #         r_f_detail4 = open('.\original_info_detail\\detail4.html', 'r',encoding='utf-8')
                                       #         for d_detail4 in r_f_detail4.readlines():
                                       #             if (d_detail4.replace('review_editer', d_org)):
                                       #                 new_one = d_detail4.replace('review_editer', d_org)
                                       #                 w_f_today.write(new_one)
                                       #             else:
                                       #                 w_f_today.write(d_detail4)
                                       #         r_f_detail4.close()
                                       #         line = line + 1
#################
# 写尾
r_f_tail = open('.\original_info_detail\\tail.html', 'r', encoding='utf-8')
for d_head in r_f_tail.readlines():
    w_f_today.write(d_head)
r_f_tail.close()
###############
r_f_short_org.close()
w_f_today.close()






