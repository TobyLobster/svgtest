# Fun with Bezier Curves (BBC Micro)

Given a simple SVG (one that just contains cubic splines and lines: everything else e.g. transforms, arcs, fills, colours, path thickness etc is ignored) we use a python script to translate and scale the data to fit on a BBC Micro screen and create a binary file of the data. Then we use a short BBC BASIC program to load and render it. The result is shown by default in MODE 0 but it is independent of screen mode.

* *disk.ssd* is the disc image
* *bezier.bas.txt* is the BASIC program
* *extract.py* is the Python. You'll need 'svgpathtools' as a prerequisite.
* *go* is the Mac/Unix shell script that puts it all together. You'll need beebasm to execute this.
