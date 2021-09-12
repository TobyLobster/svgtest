# Fun with Bezier Curves (BBC Micro)

Given a simple SVG (one that just contains cubic splines and lines - no transforms, arcs, fills etc) we use a python script to transform (translate and scale) the data, create a binary file of the data, and have a BBC BASIC program to load and render it.

* *disk.ssd* is the disc image
* *bezier.bas.txt* is the BASIC program
* *extract.py* is the Python. You'll need 'svgpathtools' as a prerequisite.
* *go* is the Mac/Unix shell script that puts it all together. You'll need beebasm to execute this.
