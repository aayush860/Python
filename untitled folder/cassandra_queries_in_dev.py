#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 17:36:15 2018

@author: aayushbhargava
"""

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
auth_provider = PlainTextAuthProvider(username='cassandra_name', password='My password is my password none of your passwrod')
cluster = Cluster(["10.13.1.33"],9046,auth_provider = auth_provider)
session = cluster.connect()
count=1
x=list()
upins=["'uhjiuhei'","'kjneckjnece'","'keckjne'"]
#update table.keyspace set minor_dependent_flag=True, dob='1996-02-01' WHERE upin='cmcmclmi';

for xxx in upcc:
        x=session.execute("bla bla query")
        
        
for upn in upins:
        x=session.execute("Bla Bla query")
        #print("DELETED for upin:"+upn)
   

cluster.shutdown()

