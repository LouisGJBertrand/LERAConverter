# Litematica to Exylo's Redstone Atlas Converter

A small tool to convert litematicas into Exylo's Redstone Atlas json format.

# Requirements

```
- typing.Iterable
- litemapy
- json
```

# Usage

```py
# import l2e
from l2e import l2eUtility
import json

# create object
util: l2eUtility = l2eUtility()

# load schem
util.loadSchem("simpleClock.litematic")
# convert schem
output = util.convert()

# output is a standard array, you have to convert to json
# output to file, replace tests/output.json to anything you want
with open("tests/output.json", "a") as f:
    f.write(json.dumps(output))
```

# License

Free to use - MIT Standard License

# Contributors

Loé BERTRAND