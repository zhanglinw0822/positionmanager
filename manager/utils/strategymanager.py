import os
import sys
import xml.etree.ElementTree as ET


strategys = []

def init():
    if (strategys.__len__()==0):
        xmlFilePath = os.path.abspath("D:\strategy\config.xml")
        try:
            tree = ET.parse(xmlFilePath)
            # 获得根节点
            root = tree.getroot()
        except Exception as e:  # 捕获除与程序退出sys.exit()相关之外的所有异常
            print("parse test.xml fail!")
            print(e)
            sys.exit()

        # 根据标签名查找root下的所有标签
        strategyList = root.findall("strategy")  # 在当前指定目录下遍历

        for strategy in strategyList:
            path = None
            key = None
            secret = None
            name = None
            for child in strategy:
                # print(child.tag, child.text)
                if child.tag == 'path':
                    path = child.text
                if child.tag == 'key':
                    key = child.text
                if child.tag == 'secret':
                    secret = child.text
                if child.tag == 'name':
                    name = child.text
            strategys.append({'path': path, 'key': key, 'secret': secret, 'name': name})
