# Litematica to Exylo's Redstone Atlas Converter
# developped by Loé BERTRAND <louisgjbertrand@icloud.com>
# MIT license

from typing import Iterable
from litemapy import Schematic, Region, BlockState
import json

class l2eUtility:
    schem:Schematic
    reg:Region
    baseJson = {
        "id": "untitled_schematic",
        "name": "Untitled Schematic",
        "description": "",
        "minecraftEdition": "Java Edition",
        "minecraftVersion": "current",
        "category": "undefined",
        "difficulty": "",
        "tags": [],
        "layers": { "minY": 0, "maxY": 0 },
        "blocks": [],
        "controls": []
    }

    def loadSchem(this, path):
        this.schem = Schematic.load(path)
        this.reg = list(this.schem.regions.values())[0]

    def prepareBlockstate(this, state: Iterable[tuple[str, str]]):
        output = {}
        for el in state:
            output[el[0]] = el[1]
        return output

    def convert(this):
        output = this.baseJson

        for blockPos in this.reg.block_positions():

            x = blockPos[0]
            y = blockPos[1]
            z = blockPos[2]

            if(output["layers"]["minY"] > y):
                output["layers"]["minY"] = y

            if(output["layers"]["maxY"] < y):
                output["layers"]["maxY"] = y

            block = this.reg[x, y, z]
            state = this.prepareBlockstate(block.properties())

            output["blocks"].append(
            {
                "id": block.id,
                "pos": [blockPos[0], blockPos[1], blockPos[2]],
                "state": state,
                "label": "Undefined"
            })
        return output

# TEST SCRIPT
if __name__ == '__main__':

    util: l2eUtility = l2eUtility()

    # load schem
    util.loadSchem("test.litematic")
    # convert schem
    output = util.convert()

    # output to file
    with open("tests/output.json", "w") as f:
        f.write(json.dumps(output))