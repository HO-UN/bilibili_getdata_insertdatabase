#coding:utf-8
from py2neo import Graph,NodeMatcher,Relationship,Node

graph = Graph('bolt://103.135.251.124:1911',auth=('neo4j','Hechenghan1234'))
node_matcher = NodeMatcher(graph)
neoupdata = "match(p:PersonWeb){name:"+ name +"})-[rel:ConnectWeb]->(:personWeb) set "