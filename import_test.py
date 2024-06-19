import importlib
import json

with open("/Users/user/Downloads/packages_0531.csv", "r") as f:
    lines = f.readlines()[1:]

std_libs = []
ext_libs = []

for line in lines:
    lib_name = line.split(",")[0]
    try:
        importlib.import_module(lib_name)
        std_libs.append(lib_name)
    except ModuleNotFoundError as e:
        ext_libs.append(lib_name)

with open("result.json","w") as wf:
    json.dump({
        "standard": std_libs,
        "external": ext_libs
    }, wf)