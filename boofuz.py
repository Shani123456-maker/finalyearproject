from boofuzz import *

session = Session(target=Target(connection=SocketConnection('172.16.16.145',9999, proto='tcp')))

s_initialize("trun")
s_static("TRUN")
s_delim(" ")
s_string("AAAA")

session.connect(s_get("trun"))
session.fuzz()
