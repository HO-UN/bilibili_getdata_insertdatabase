# coding:utf-8
from py2neo import Graph, NodeMatcher, Relationship, Node

from snow_id import SnowId

graph = Graph('bolt://103.135.251.124:1911', auth=('neo4j', 'Hechenghan1234'))
node_matcher = NodeMatcher(graph)
with open('uid1.txt', 'r', encoding='utf-8') as uu: uid = uu.readlines()
with open('name1.txt', 'r', encoding='utf-8') as bname: name = bname.readlines()

for i in range(0, 73):
    spacelink = "https://space.bilibili.com/" + uid[i].replace("\n","")
    # neoupdata = "match(:PersonWeb)-[rel:ConnectWeb]->(p:PersonWeb{personWebName:'" + name[
    #     i].replace("\n","") + "'}) set p.personWebId='" + str(
    #     SnowId(1, 2, 0).get_id())[1:] + \
    #             "',p.personWebShow = 0,p.personWebPlatform ='['0']',p.personWebLink = '" + spacelink.replace("\n","") + \
    #             "',p.personWebKey = '',p.personWebField = '[]',rel.connectWebId = '" + str(SnowId(1, 2, 0).get_id())[
    #                                                                                  1:] + "',rel.connectWebInfo=''," \
    #                                                                                        "rel.connectWebName = '' " \
    #                                                                                        "return p "
    neoupdata = "match(:PersonWeb)-[rel:ConnectWeb]->(p:PersonWeb{personWebName:'" + name[i].replace("\n", "") + "'}) set p.personWebPlatform ='['0']',p.personWebField = '[]',rel.connectWebId = '"+ str(SnowId(1, 2, 0).get_id())[1:] + "' return p "
    graph.run(str(neoupdata).replace("'", "\""))
