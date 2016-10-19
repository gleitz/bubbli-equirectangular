# Convert http://bubb.li spheres to equirectanglar images

import os
import re
import sys


def convert(bubbli_id):
    directions = ['py', 'ny', 'px', 'nx', 'pz', 'nz']
    filenames = []

    for direction in directions:
        filename = bubbli_id + '_' + direction + '.jpg'
        filenames.append(filename)
        os.system('wget https://d39cwcjmzdw2iw.cloudfront.net/' + bubbli_id + '/stitched_' + direction + '.jpg -O ' + filename)

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

    png_filenames = [f.replace('jpg', 'png') for f in filenames]

    command = 'cube2sphere --format=png --blender-path=/Applications/blender.app/Contents/MacOS/blender ' + ' '.join(png_filenames)
    os.system(command)
    os.system('trash {}_*.png'.format(bubbli_id))
    os.system('convert out0001.png -flop {}.png'.format(bubbli_id))
    os.system('trash out0001.png')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage: python convert.py bubbli_url1 [bubbli_url2 bubbli_url3...]'
    for bubbli_url in sys.argv[1:]:
        bubbli_id = re.match(r'http://on.bubb.li/(\w+)\/?', bubbli_url).group(1)
        convert(bubbli_id)
