# Convert http://bubb.li spheres to equirectanglar images

import os

bubbli_id = '361964aqy29yeowtwjovxeg'
directions = ['py', 'ny', 'px', 'nx', 'pz', 'nz']
filenames = []
should_mogrify = False

for direction in directions:
    filename = bubbli_id + '_' + direction + '.jpg'
    png_filename = bubbli_id + '_' + direction + '.png'
    filenames.append(filename)
    if os.path.isfile(png_filename):
        continue
    should_mogrify = True
    os.system('wget https://d39cwcjmzdw2iw.cloudfront.net/' + bubbli_id + '/stitched_' + direction + '.jpg -O ' + filename)

if should_mogrify:
    os.system('mogrify -format png *.jpg')
    os.system('trash *.jpg')
    filename = bubbli_id + '_' + 'py.png'
    os.system('convert ' + filename + ' -rotate 180 ' + filename)
    filename = bubbli_id + '_' + 'nx.png'
    os.system('convert ' + filename + ' -rotate 270 ' + filename)
    filename = bubbli_id + '_' + 'px.png'
    os.system('convert ' + filename + ' -rotate 90 ' + filename)
    filename = bubbli_id + '_' + 'nz.png'
    os.system('convert ' + filename + ' -rotate 180 ' + filename)

filenames = [filename.replace('jpg', 'png') for filename in filenames]

command = 'cube2sphere --format=png --blender-path=/Applications/blender.app/Contents/MacOS/blender ' + ' '.join(filenames)
os.system(command)
