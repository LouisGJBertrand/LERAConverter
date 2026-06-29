
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
# output to file
with open("tests/output.json", "a") as f:
    f.write(json.dumps(output))