import js
import random


def generate():
    return random.randint(0, 255)


rom = list(js.window.rom_content)

worlds_offset = 7364
levels_offset = worlds_offset + 8
title = ''

use_gen = js.confirm('Generate - OK, Use own - Cancel')
if use_gen:
    generate_world = js.confirm('Generate worlds - OK, Generate Levels - Cancel')
    if generate_world:
        rom[worlds_offset] = generate()
        rom[worlds_offset + 1] = generate()
        rom[worlds_offset + 2] = generate()
        rom[worlds_offset + 3] = generate()
        rom[worlds_offset + 4] = generate()
        rom[worlds_offset + 5] = generate()
        rom[worlds_offset + 6] = generate()
        rom[worlds_offset + 7] = generate()
        title = ','.join(map(str, rom[worlds_offset:worlds_offset + 8]))
        js.alert(title + '\nRemember it!')
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
        title = ','.join(map(str, rom[levels_offset:levels_offset + 9]))
        js.alert(title + '\nRemember it!')
else:
    generate_world = js.confirm('Use worlds - OK, Use Levels - Cancel')
    inserted = list(map(int, js.prompt('Enter code: ').split(',')))
    print(inserted)
    if generate_world:
        rom[worlds_offset] = inserted[0]
        rom[worlds_offset + 1] = inserted[1]
        rom[worlds_offset + 2] = inserted[2]
        rom[worlds_offset + 3] = inserted[3]
        rom[worlds_offset + 4] = inserted[4]
        rom[worlds_offset + 5] = inserted[5]
        rom[worlds_offset + 6] = inserted[6]
        rom[worlds_offset + 7] = inserted[7]
        title = ','.join(map(str, rom[worlds_offset:worlds_offset + 8]))
    else:
        rom[levels_offset] = inserted[0]
        rom[levels_offset + 1] = inserted[1]
        rom[levels_offset + 2] = inserted[2]
        rom[levels_offset + 3] = inserted[3]
        rom[levels_offset + 4] = inserted[4]
        rom[levels_offset + 5] = inserted[5]
        rom[levels_offset + 6] = inserted[6]
        rom[levels_offset + 7] = inserted[7]
        rom[levels_offset + 8] = inserted[8]
        title = ','.join(map(str, rom[levels_offset:levels_offset + 9]))


converted = ','.join(map(str, rom))
blob = js.Blob.new([converted], {type : 'application/text'})
url = js.window.URL.createObjectURL(blob)
js.window.open('nes-js/index.html?url=' + url + '&title=' + title)
