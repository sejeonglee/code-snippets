import importlib
import json

with open("/Users/user/Downloads/packages_0531.csv", "r") as f:
    lines = f.readlines()[1:]

open_std = set()
open_ext = set()

for line in lines:
    lib_name = line.split(",")[0]
    try:
        importlib.import_module(lib_name)
        open_std.add(lib_name)
    except ModuleNotFoundError as e:
        open_ext.add(lib_name)

open_installed = open_std.union(open_ext)

with open("package_list.txt", "r") as f:
    lines = f.readlines()[2:]

gpt_installed = set()
gpt_std = set()
unknown = set()
for line in lines:
    lib_name = line.split()[0]
    gpt_installed.add(lib_name)
    try:
        importlib.import_module(lib_name)
        gpt_std.add(lib_name)
    except ModuleNotFoundError as e:
        pass
    except Exception:
        unknown.add(lib_name)

print(unknown)

gpt_only = gpt_installed.difference(open_installed)
open_only = open_installed.difference(gpt_installed)
common = open_installed.intersection(gpt_installed)

std_set = open_std.union(gpt_std)

with open("result_diff.json", "w") as wf:
    json.dump({
        "gpt_only": list(gpt_only),
        "open_only": list(open_only),
        "common": list(common),
    }, wf)
with open("result_diff_wo_std.json", "w") as wf:
    json.dump({
        "gpt_only": list(gpt_only.difference(std_set)),
        "open_only": list(open_only.difference(std_set)),
        "common": list(common.difference(std_set)),
    }, wf)

