#/bin/bash

time python ../GDBIGtools.py query -s 21:9662064
time python ../GDBIGtools.py query -s 22:10577666-10581518
time python ../GDBIGtools.py query -l positions.list
time python ../GDBIGtools.py annotate -i GDBIG.test.vcf