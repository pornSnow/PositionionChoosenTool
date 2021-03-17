# -*- coding: utf-8 -*-
import requests
import json
import time
import random
import ast

ak = "aFaqYWrHdIt4lF4x2aDmyA85OH6YCANj" #百度地图API访问AK

#按条件检索给定范围内所有地点
def searchPositions(ak, region, keyWord):
    page_size = 20
    resNum=20
    i=0
    resList=[]
    while (resNum==page_size):
        print('正在进行第' + str(i+1) + '轮检索...')
        url = "http://api.map.baidu.com/place/v2/search?ak=" + str(ak) + "&output=json&query=" + \
            str(keyWord) + "&region=" + str(region) + "&page_size=" + str(page_size) + "&page_num=" + str(i)
        response = requests.get(url.encode(encoding='utf-8'))               # 对网页进行请求
        jsondata = json.loads(response.text)          			# 对下载的内容进行loads一下
        resNum=0 
        for j in jsondata['results']:
            resList.append({'name':j.get('name'), 'address':j.get('address')})
            resNum=resNum+1
        i=i+1
        time.sleep(2)  #防止达到百度地图并发检索数上限
    #输出结果
    print('检索完毕，共检索到到以下' + str(len(resList)) + '条信息')
    for i in resList:
        print(i['name'].ljust(30)+'   '+i['address'])
    return resList

if __name__ == "__main__":
    print('+++++++++++++++++++++++++++++++++++++++++++')
    print('+           任务地点随机生成工具            +')
    print('+                ver 1.0                  +')
    print('+                                         +')
    print('+                     powered by 江雪     +')
    print('+++++++++++++++++++++++++++++++++++++++++++')
    print('正在读取本地数据...')
    posList=[]
    for line in open("positions.txt"):
        posList.append(ast.literal_eval(line))
    inp=99
    #用户菜单
    while(inp!='0'):
        print('=======用户菜单=======')
        print('1.查看任务地点列表')
        print('2.根据给定条件搜索任务地点')
        print('3.将现在的地点列表保存到本机')
        print('4.随机选择任务地点')
        print('0.退出')
        choosenList=['0', '1', '2', '3', '4']
        inp=99
        while (inp not in choosenList):
            inp=input('请输入你的选择:')
        if (inp=='1'):   #查看任务地点列表
            print('当前任务地点列表：')
            for value in posList:
                print(value['name'].ljust(30)+'   '+value['address'])
        elif (inp=='2'):   #根据给定条件搜索任务地点
            region = input('请输入检索范围（如：北京市）:')
            keyWord = input('请输入检索关键字:')
            posList=searchPositions(ak, region, keyWord)
        elif (inp=='3'):   #将现在的地点列表保存到本机
            print('正在保存数据...')
            f = open("positions.txt", "w")
            for value in posList:
                f.write(str(value))
                f.write('\n') 
            f.close()
            print('数据保存完毕！')
        elif (inp=='4'):   #随机选择任务地点
            if (len(posList)==0):
                print("目前的任务地点列表为空")
            else:
                index=random.randint(0,len(posList)-1)
                print('已为你选出一个随机的任务地点')
                print('名称：' + posList[index]['name'])
                print('名称：' + posList[index]['address'])
        print('')
            
        
        
        
