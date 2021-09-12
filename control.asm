PUTBASIC "bezier.bas.txt","LOAD"

ORG $E00
.start1
INCBIN "data1.bin"
.end1
.start2
INCBIN "data2.bin"
.end2

SAVE "DATA1", start1, end1
SAVE "DATA2", start2, end2

PUTTEXT "boot.txt","!BOOT",0
