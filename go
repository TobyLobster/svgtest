python3 extract.py input.svg data1.bin
python3 extract.py acorn.svg data2.bin
../tools/beebasm -i control.asm -opt 3 -do disk.ssd
