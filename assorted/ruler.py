#!/usr/bin/env python
# coding: utf-8

"""
The english ruler problem. The English ruler pattern is a fractal.
Self-recursive at different levels of magnification.

Major tick length: e.g. 4
Example:

---- 0
-
--
-
---
-
--
-
---- 1

Or:

---- 0
--
---
--
---
--
---
--
---- 1

Or: 

---- 0
-
--
-
---
-
--
-
---
-
--
-
---
-
--
-
---
-
--
---- 1

Parameters: Major ticks and minor ticks.
"""

from __future__ import division

#
# Own approach
#
def ruler(length=4, left=0, right=1):
    print('%0.2f .... \t%s' % (left, '-' * length))
    value = (right - left) / 2
    draw(length=length, value=value, level=1, shift=left)
    print('%0.2f .... \t%s' % (right, '-' * length))

def draw(length=4, value=0.5, level=1, shift=0):
    """ Wrong numbers at diff = value / ((level + 1) * level) """
    if length > 0:
        diff = value / ((level + 1) * level)
        left, right = value - diff, value + diff
        draw(length=length - 1, value=left, level=level + 1, shift=shift)
        print('%0.2f .... \t%s' % (value + shift, '-' * length))
        draw(length=length - 1, value=right, level=level + 1, shift=shift)

#
# From the book
#
def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    print('%s %s' % (line, tick_label))

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))


if __name__ == '__main__':
    # ruler(5, left=0, right=7)
    draw_ruler(18, 8)
