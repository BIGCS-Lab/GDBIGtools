#/bin/bash

time GDBIGtools query -s 21:9662064
time GDBIGtools query -s 22:10577666-10581518
time GDBIGtools query -l positions.list
time GDBIGtools annotate -i GDBIG.test.vcf
