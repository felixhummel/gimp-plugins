#!/usr/bin/env python
# encoding: utf-8

from gimpfu import *


def half_the_size(img, drawable):
    new_height = img.height / 2
    new_width = img.width / 2
    pdb.gimp_image_scale(img, new_width, new_height)


register(
        "resize50",  # name
        "Scale image down to 50%",  # blurb
        "Scale image down to 50%",  # help
        "Felix Hummel",  # author
        "Felix Hummel",  # copyright
        "2018",  # date
        "<Image>/Feli_x/_Resize50",  # menupath
        "RGB*, GRAY*",  # imagetypes
        [],  # params
        [],  # results
        half_the_size)  # function

main()
