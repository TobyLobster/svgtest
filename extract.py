import inspect
import sys
import struct

inputFile = sys.argv[1]
outputFile = sys.argv[2]

from svgpathtools import svg2paths2, Path, Line, Arc, CubicBezier, QuadraticBezier, wsvg

# Load input SVG
paths, attributes, svg_attributes = svg2paths2(inputFile)

# Get bounding box
minx = sys.float_info.max
maxx = sys.float_info.min
miny = sys.float_info.max
maxy = sys.float_info.min

for p in paths:
    (x1, x2, y1, y2) = p.bbox()
    minx = min(minx, x1)
    miny = min(miny, y1)
    maxx = max(maxx, x2)
    maxy = max(maxy, y2)

#print("box: ", minx, miny, maxx, maxy)

# calculate scale
scaleX = 1280 / (maxx - minx)
scaleY = 1024 / (maxy - miny)
scale = min(scaleX, scaleY)

# Allow for a 16 unit border
borderX = 16
borderY = 16
borderScale = min((1280-2*borderX)/1280, (1024-2*borderY)/1024)
scale = scale * borderScale

newPaths = []
entries = 0

for p in paths:
    newp = p.translated(borderX -minx -1j * miny +1j*borderY).scaled(scale)
    for e in newp:
        if isinstance(e, CubicBezier):
            e.start = (e.start.real) + 1j*(e.start.imag)
            e.control1 = (e.control1.real) + 1j*(e.control1.imag)
            e.control2 = (e.control2.real) + 1j*(e.control2.imag)
            e.end = (e.end.real) + 1j*(e.end.imag)
            entries += 1
            #print("cubic_bezier: ", e.start, e.control1, e.control2, e.end)
        elif isinstance(e, Line):
            e.start = (e.start.real) + 1j*(e.start.imag)
            e.end = (e.end.real) + 1j*(e.end.imag)
            entries += 1
            #print("line:         ", e.start, e.end)
        elif isinstance(e, QuadraticBezier):
            e.start = (e.start.real) + 1j*(e.start.imag)
            e.control = (e.control.real) + 1j*(e.control.imag)
            e.end = (e.end.real) + 1j*(e.end.imag)
            entries += 1
            #print("quad_bezier:  ", e.start, e.control, e.end)
        elif isinstance(e, Arc):
            print("arc not implemented")
        else:
            print(e)
    newPaths.append(newp);

wsvg(newPaths, "", filename='output.svg')

with open(outputFile, 'bw+') as f:
    f.write(struct.pack('<h', entries))
    for p in newPaths:
        for e in p:
            if isinstance(e, CubicBezier):
                f.write(struct.pack('B', 1))
                f.write(struct.pack('<h', int(e.start.real)))
                f.write(struct.pack('<h', 1024-int(e.start.imag)))
                f.write(struct.pack('<h', int(e.control1.real)))
                f.write(struct.pack('<h', 1024-int(e.control1.imag)))
                f.write(struct.pack('<h', int(e.control2.real)))
                f.write(struct.pack('<h', 1024-int(e.control2.imag)))
                f.write(struct.pack('<h', int(e.end.real)))
                f.write(struct.pack('<h', 1024-int(e.end.imag)))
            elif isinstance(e, Line):
                f.write(struct.pack('B', 2))
                f.write(struct.pack('<h', int(e.start.real)))
                f.write(struct.pack('<h', 1024-int(e.start.imag)))
                f.write(struct.pack('<h', int(e.end.real)))
                f.write(struct.pack('<h', 1024-int(e.end.imag)))
            elif isinstance(e, QuadraticBezier):
                f.write(struct.pack('B', 3))
                f.write(struct.pack('<h', int(e.start.real)))
                f.write(struct.pack('<h', 1024-int(e.start.imag)))
                f.write(struct.pack('<h', int(e.control.real)))
                f.write(struct.pack('<h', 1024-int(e.control.imag)))
                f.write(struct.pack('<h', int(e.end.real)))
                f.write(struct.pack('<h', 1024-int(e.end.imag)))
            elif isinstance(e, Arc):
                print("arc not implemented")
            else:
                print(e)
