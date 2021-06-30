import js
import random


def generate():
    return random.randint(0, 255)


rom = list(js.window.rom_content)

worlds_offset = 7364
levels_offset = worlds_offset + 8

use_random = js.confirm('Generate?')
#if not use_random:
#    js.location.href = 'emulator.html'

generate_world = js.confirm('Generate worlds - OK, Generate Leves - Cancel')

if generate_world:
    rom[worlds_offset] = generate()
    rom[worlds_offset + 1] = generate()
    rom[worlds_offset + 2] = generate()
    rom[worlds_offset + 3] = generate()
    rom[worlds_offset + 4] = generate()
    rom[worlds_offset + 5] = generate()
    rom[worlds_offset + 6] = generate()
    rom[worlds_offset + 7] = generate()
    js.alert(','.join(map(str, rom[worlds_offset:worlds_offset + 7])) + '\nRemember it!')
else:
    rom[levels_offset] = generate()
    rom[levels_offset + 1] = generate()
    rom[levels_offset + 2] = generate()
    rom[levels_offset + 3] = generate()
    rom[levels_offset + 4] = generate()
    rom[levels_offset + 5] = generate()
    rom[levels_offset + 6] = generate()
    rom[levels_offset + 7] = generate()
    rom[levels_offset + 8] = generate()
    js.alert(','.join(map(str, rom[levels_offset:levels_offset + 7])) + '\nRemember it!')


converted = ','.join(map(str, rom))
blob = js.Blob.new([converted], {type : 'application/text'})
url = js.window.URL.createObjectURL(blob)
js.window.open('nes-js/index.html?url=' + url)
