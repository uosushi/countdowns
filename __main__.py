import json, time
from datetime import datetime

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if type(obj).__name__ == "datetime":
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return obj

red = "\033[31m"
green = "\033[32m"
black = "\033[30m"
bold = "\033[1m"
end = "\033[0m"
PARENT_DIR = "parent_dir"
SAVE_PATH = PARENT_DIR + "save.json"

def is_int(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if type(obj).__name__ == "datetime":
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return obj

def get_data():
    fr = open(SAVE_PATH, "r")
    data = json.load(fr)
    fr.close()
    return (data)

def save(data):
    fw = open(SAVE_PATH,"w")
    json.dump(data, fw, indent=2, separators=(',', ': '), cls=DatetimeEncoder)
    fw.close()

def mv(d, old_key, new_key):
    if old_key in d:
        d[new_key] = d.pop(old_key)

def black_hole(BH, name):
    tense = "left."
    if BH < 0:
        BH *= -1
        tense = "ago."
    if BH >= 1440:
        time_unit = "days"
        BH //= 1440
    elif BH >= 60:
        time_unit = "hours"
        BH //= 60
    else:
        time_unit = "minutes"
    print(f"{bold}\"{name}\" {BH} {time_unit} {tense}{end}")

def progress_bar(limit, now, name):
    i = 0
    while (i <= now / 10 and i <= limit / 10):
        p = int(i / (limit / 10) * 30)
        print(f"\r{green}[{p * '='}{(30 - p) * ' '}] {(i / limit * 10):.1%}{end}", end="")
        i += 1
        time.sleep(0.05)
    print("")
    black_hole(limit - now, name)

def show_timer(name):
    data = get_data()
    timers = data["timers"]
    if (name in timers):
        timer = timers[name]
        progress_bar(timer["limit"], timer["now"], name)

def new_timer(name, limit):
    data = get_data()
    timers = data["timers"]
    if (name in timers):
        print("The specified timer name already exists.")
        return (None)
    timers[name] = {"limit": limit, "now": 0, "timestamp": "0-0-0 0:0:0"}
    data["timers"] = timers
    save(data)

def mv_timer(old_key, new_key):
    data = get_data()
    timers = data["timers"]
    if old_key in timers:
        timers[new_key] = timers.pop(old_key)
    data["timers"] = timers
    print(f"{old_key} -> {new_key}")
    save(data)

def timer_switch(data, name):
    timestamp = data["timers"][name]["timestamp"]
    if timestamp != 0:
        timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        working_time = datetime.now() - timestamp
        data["timers"][name]["now"] += int(working_time.total_seconds() // 60)
        data["timers"][name]["timestamp"] = 0
        save(data)
        show_timer(name)
        return
    data["timers"][name]["timestamp"] = datetime.now()
    print("start a countdown...")
    save(data)
    

while True:
    argv = input(">> ").split()
    if len(argv) == 0:
        print(bold+"Bye!"+end)
        break
    if argv[0] == "show":
        show_timer(argv[1])
        continue
    if argv[0] == "new" and is_int(argv[2]):
        new_timer(argv[1], int(argv[2]) * 60)
        continue
    elif argv[0] == "mv":
        mv(argv[1], argv[2])
        continue
    data = get_data()
    timers = data["timers"]
    if argv[0] in timers:
        timer_switch(data, argv[0])