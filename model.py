import json
from datetime import datetime


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries=[]
next_id=0    #add a global variable next_id--hw14 part2

def init():
    global entries
    global next_id
    try:
        f=open(GUESTBOOK_ENTRIES_FILE)
        entries=json.loads(f.read())
        for e in entries:
            if 'id' not in e:
                e['id']=str(next_id)
                next_id=next_id+1
        next_id=len(entries)
        f.close()
    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE
    global next_id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    entry = {"author": name, "text": text, "timestamp": time_string, "id":str(next_id)}
    entries.insert(0, entry) ## add to front of list
    next_id+=1
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

#implement delete_entry()--hw14 part4
def delete_entry(id):
    global entries, GUESTBOOK_ENTRIES_FILE
    for ee in entries:
        if ee["id"]==str(id):
            entries.remove(ee)
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")
