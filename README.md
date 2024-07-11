# cocube

## Table of Contents

- [Installation](#installation)
- [Usage](#Usage)
- [License](#license)

## Installation

```console
pip install cocube
```

## Usage

Save [this project(same as Snap!)](https://microblocksfun.cn/run/microblocks.html#project=https://wwj718.github.io/post/img/CoCube-server-dynatalk-v1.ubp) to your MicroBlocks device.

```py
# pip install -U cocube
from cocube import CoCube

client = CoCube()
found_devices = client.discover(timeout=5)
print("found devices:", found_devices)
client.connect("MicroBlocks QCQ", timeout=3)

client.request("displayCharacter", ["f"])

while True:
    position_x = client.position_x
    print(position_x)
```

ref: [Snap! 中的 CoCube 库](https://wwj718.github.io/post/%E7%BC%96%E7%A8%8B/snap-cocube/)

### Connect multiple devices

```py
from cocube import CoCube

client = CoCube()
found_devices = client.discover(timeout=5)
print("found devices:", found_devices)
# connect all discovered devices
devices = [CoCube(i) for i in found_devices]

for index, device in enumerate(devices):
    device.display_character(index)
```

## License

`cocube` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.