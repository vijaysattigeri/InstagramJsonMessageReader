import os
import json
import codecs
import sys
import textwrap
import unicodedata
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
file_handle = codecs.open("messages.json", "r", "utf-8")
str_data = file_handle.read()
file_handle.close()
my_jobj = json.loads(str_data)
f = codecs.open('out.html', 'w+', "utf-8")
f.write("Your messages are as follows <br>");
f.write("__________________________________________________<br><br>")
# Latest message will be first! So displaying in the reverse order.
for i in range (len(my_jobj[0]["conversation"]) - 1, -1, -1) :
    sender_name = my_jobj[0]["conversation"][i]["sender"]
    if sender_name == None :
    	sender_name = "N/A"
    try:
	text = my_jobj[0]["conversation"][i]["text"]
    	rslt = textwrap.fill(sender_name + ": " + text.translate(non_bmp_map), 50)
    except:
	try:
	   media = my_jobj[0]["conversation"][i]["media"]
       	   rslt  = sender_name + ": <img src='"+media+"'>"
	except:
	   rslt  = sender_name + ": ~Attached media unavailable~"
    f.write(rslt)
    f.write("<br><br>")
f.write("<br><br>__________________________________________________<br>")
f.write("\tScript completed execution!<br><br>");
f.close()
