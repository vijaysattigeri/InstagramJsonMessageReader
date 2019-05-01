import os
import json
import codecs
import sys
import textwrap

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

file_handle = codecs.open("messages.json", "r", "utf-8")

str_data = file_handle.read()
file_handle.close()

my_jobj = json.loads(str_data)

print("\n\n\tYour messages are as follows\n");
print("__________________________________________________\n\n")

# Latest message will be first! So displaying in the reverse order.
for i in range (len(my_jobj[0]["conversation"]) - 1, -1, -1) :
    sender_name = my_jobj[0]["conversation"][i]["sender"]
    text = my_jobj[0]["conversation"][i]["text"]
    if sender_name == None :
        sender_name = "N/A"
    print(textwrap.fill(sender_name + ": " + text.translate(non_bmp_map), 50))
    print("\n")


print("\n\n__________________________________________________\n")
print("\tScript completed execution!\n\n");

