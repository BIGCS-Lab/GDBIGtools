
GDBIGtools: A command line tools for GDBIG varaints browser
===========================================================

[![PyPI Version](https://img.shields.io/pypi/v/GDBIGtools.svg)](https://pypi.org/project/GDBIGtools/)
[![License](https://img.shields.io/pypi/l/GDBIGtools.svg)](https://github.com/aiyacharley/GDBIGtools/blob/master/LICENSE)

Introduction
------------

Born in Guangzhou Cohort Study Genome Research Database is based on thousands of trios families recruited by the BIGCS Project to conduct whole-genome-sequencing, genome variation detection, annotation and analysis.Phase I included 332 parent-child trios’ families, 1392 mother-child sample pairs, 14 father-child sample pairs, and 70 unrelated children, 150 adult females, and 25 adult males, for a total of 4053 individual samples.The GDBIG delivers periodical and useful variation information and scientific insights derived from the analysis of thousands of born in Guangzhou China sequencing data. The results aim to promote genetic research and precision medicine actions in China.The delivering information includes any of detected variants and the corresponding allele frequency, annotation, frequency comparison to the global populations from existing databases, etc.

The [Genome variation Database of BIGCS(GDBIG)](https://gdbig.bigcs.com.cn) is a large-scale Chinese genomics database produced by BIGCS and hosted in the Guangzhou Women and Children\' Medicine Center. The GDBIG delivers peridical and useful variation information and scientific insights derived from the analysis
of thousands of Chinese sequencing data. The results aim to promote genetic research and precision medicine actions in China.

The delivering information includes any of detected variants and the corresponding allele frequency, annotation, frequency comparison to the global populations from existing databases, etc.

**GDBIGtools** is a command line tool for this GDBIG variants browser.

Quick start
------------

GDBIG variant browser allows authorized access its data through an Genomics API and **GDBIGtools** is a convenient command line tools for this purpose.

Installation
------------

Install the released version by `pip` (Only support Python3 since v1.0.1):

```bash
pip install GDBIGtools
```

Setup
------------

Please enable your API access from Profile in [GDBIG browser](https://gdbig.bigcs.com.cn) before using **GDBIGtools**.

Help
------------
type `GDBIGtools -h/--help` for detail.
```
Usage: GDBIGtools.py [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  annotate   Annotate input VCF file with BIGCS allele Frequency.
  login      Login GDBIG.
  logout     Logout GDBIG.
  print-api  Display API information for GDBIG.
  query      Query variants from GDBIG database.
```

Login
------------

Login with `GDBIGtools` by using GDBIG API access key, which could be found from **<API ACCESS\>** if you have apply for it.

[![GDBIG_genomics_api](assets/figures/GDBIG_genomics_api.png)](assets/figures/GDBIG_genomics_api.png)

```bash
GDBIGtools login -k api-key -s api-secret-key
```

If everything goes smoothly, **means you can use GDBIG as one of your varaints database in command line mode**.

Logout
------------

Logout `GDBIGtools` by simply run the command below:

```bash
GDBIGtools logout
```

Query a single variant
------------

Variants could be retrieved from GDBIG by using `query`.

Run `GDBIGtools query -h/--help` to see all available options. There\'re
two different ways to retrive variants.

One is to use `-s` parameters for variants on command, the other way uses `-l` for input-file.

Here are examples for quering varaints on command.

```bash
GDBIGtools query -s rs117518546
GDBIGtools query -s 21:9662064
GDBIGtools query -s 22:10577666-10581518
GDBIGtools query -s ENST00000269305
GDBIGtools query -s MTHFR
```

and you will get something looks like below:

```bash
##fileformat=VCFv4.2
##FILTER=<ID=PASS,Description="All filters passed">
##INFO=<ID=GDBIG_AF,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0">
##INFO=<ID=GDBIG_AF_SouthChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in SouthChina region">
##INFO=<ID=GDBIG_AF_CentralChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in CentralChina region">
##INFO=<ID=GDBIG_AF_EastChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in EastChina region">
##INFO=<ID=GDBIG_AF_SouthwestChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in SouthwestChina region">
##INFO=<ID=GDBIG_AF_NortheastChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in NortheastChina region">
##INFO=<ID=GDBIG_AF_NorthwestChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in NorthwestChina region">
##INFO=<ID=GDBIG_AF_NorthChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in NorthChina region">
##reference=file:/human_reference/GRCh38/GCA_000001405.15_GRCh38_no_alt_analysis_set.fa
#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO
chr22   10577666        rs1491296197    CAT     C       .       PASS    GDBIG_AF=0.000123;GDBIG_AF_SouthChina=0.000169;GDBIG_AF_CentralChina=0;GDBIG_AF_EastChina=0;GDBIG_AF_SouthwestChina=0;GDBIG_AF_NortheastChina=0;GDBIG_AF_NorthwestChina=0;GDBIG_AF_NorthChina=0
```

Quering for input-file.
------------

A list of variants could be retrieved from GDBIG by using the parameters of `-l` when apply by `query`.

```bash
GDBIGtools query -l positions.list > result.vcf
```

Format for [positions.list](tests/positions.list), could be a mixture of
- `rs ID`
- `ensembl transcript ID`
- `gene symbol` and `ensembl gene ID`
- `chrom   position` and `chrom    start   end`, even with or without `chr` in the chromosome ID column

```
#search key words
rs117518546
chr1:11795125
ENST00000269305
MTHFR

#CHROM	POS	[POS_END]
chr22	17662883
22	17669209    17669357
```

`result.vcf` is VCF format and looks like below:

```bash
##fileformat=VCFv4.2
##FILTER=<ID=PASS,Description="All filters passed">
##INFO=<ID=GDBIG_AF,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0">
##INFO=<ID=GDBIG_AF_SouthChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in SouthChina region">
##INFO=<ID=GDBIG_AF_CentralChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in CentralChina region">
##INFO=<ID=GDBIG_AF_EastChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in EastChina region">
##INFO=<ID=GDBIG_AF_SouthwestChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in SouthwestChina region">
##INFO=<ID=GDBIG_AF_NortheastChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in NortheastChina region">
##INFO=<ID=GDBIG_AF_NorthwestChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in NorthwestChina region">
##INFO=<ID=GDBIG_AF_NorthChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in NorthChina region">
##reference=file:/human_reference/GRCh38/GCA_000001405.15_GRCh38_no_alt_analysis_set.fa
#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO
chr22   10577666        rs1491296197    CAT     C       .       PASS    GDBIG_AF=0.000123;GDBIG_AF_SouthChina=0.000169;GDBIG_AF_CentralChina=0;GDBIG_AF_EastChina=0;GDBIG_AF_SouthwestChina=0;GDBIG_AF_NortheastChina=0;GDBIG_AF_NorthwestChina=0;GDBIG_AF_NorthChina=0
chr22   10577851        .       TA      T       .       PASS    GDBIG_AF=0.000123;GDBIG_AF_SouthChina=0.000169;GDBIG_AF_CentralChina=0;GDBIG_AF_EastChina=0;GDBIG_AF_SouthwestChina=0;GDBIG_AF_NortheastChina=0;GDBIG_AF_NorthwestChina=0;GDBIG_AF_NorthChina=0
chr22   10580900        .       ATTC    A       .       PASS    GDBIG_AF=0.000369;GDBIG_AF_SouthChina=0.000506;GDBIG_AF_CentralChina=0;GDBIG_AF_EastChina=0;GDBIG_AF_SouthwestChina=0;GDBIG_AF_NortheastChina=0;GDBIG_AF_NorthwestChina=0;GDBIG_AF_NorthChina=0
chr22   10581005        rs1268262722    C       T       .       PASS    GDBIG_AF=0.000123;GDBIG_AF_SouthChina=0;GDBIG_AF_CentralChina=0;GDBIG_AF_EastChina=0;GDBIG_AF_SouthwestChina=0.003571;GDBIG_AF_NortheastChina=0;GDBIG_AF_NorthwestChina=0;GDBIG_AF_NorthChina=0
chr22   10581404        rs1283129074    G       A       .       PASS    GDBIG_AF=0.059975;GDBIG_AF_SouthChina=0.060162;GDBIG_AF_CentralChina=0.061151;GDBIG_AF_EastChina=0.057566;GDBIG_AF_SouthwestChina=0.028571;GDBIG_AF_NortheastChina=0.081395;GDBIG_AF_NorthwestChina=0.075342;GDBIG_AF_NorthChina=0.07377
chr22   10581518        rs1318646482    T       A       .       PASS    GDBIG_AF=0.000739;GDBIG_AF_SouthChina=0.001011;GDBIG_AF_CentralChina=0;GDBIG_AF_EastChina=0;GDBIG_AF_SouthwestChina=0;GDBIG_AF_NortheastChina=0;GDBIG_AF_NorthwestChina=0;GDBIG_AF_NorthChina=0
```

Actrually you can use `-s` and `-l` simultaneously if you like. And `positions.list` could just contain one single position.

```bash
GDBIGtools query -s 22:46616520 -l positions.list > result.vcf
```

Annotate your VCF files
------------

Annotate your VCF file with GDBIG by using `GDBIGtools annotate` command.

Download a list of example variants in VCF format from [GDBIG.test.vcf](tests/GDBIG.test.vcf). 
To annotate this list of variants with allele frequences from GDBIG, you can just run the following command in Linux or Mac OS.

```bash
GDBIGtools annotate -i GDBIG.test.vcf > output.GDBIG.test.vcf
```

It\'ll take about 2 or 3 minutes to complete 2,000+ variants\' annotation. 
Then you will get 8 new fields with the information of GDBIG in VCF INFO:

-   `GDBIG_AF`: Alternate Allele Frequencies in GDBIG;
-   `GDBIG_AF_SouthChina`: Alternate Allele Frequencies from GDBIG in SouthChina region;
-   `GDBIG_AF_CentralChina`: Alternate Allele Frequencies from GDBIG in CentralChina region;
-   `GDBIG_AF_EastChina`: Alternate Allele Frequencies from GDBIG in EastChina region.
-   `GDBIG_AF_SouthwestChina`: Alternate Allele Frequencies from GDBIG in SouthwestChina region;
-   `GDBIG_AF_NortheastChina`: Alternate Allele Frequencies from GDBIG in NortheastChina region;
-   `GDBIG_AF_NorthwestChina`: Alternate Allele Frequencies from GDBIG in NorthwestChina region;
-   `GDBIG_AF_NorthChina`: Alternate Allele Frequencies from GDBIG in NorthChina region.

```
##fileformat=VCFv4.2
##ALT=<ID=NON_REF,Description="Represents any possible alternative allele at this location">
##FILTER=<ID=LowQual,Description="Low quality">
##INFO=<ID=AC,Number=A,Type=Integer,Description="Allele count in genotypes, for each ALT allele, in the same order as listed">
##INFO=<ID=AF,Number=A,Type=Float,Description="Allele Frequency, for each ALT allele, in the same order as listed">
##INFO=<ID=AN,Number=1,Type=Integer,Description="Total number of alleles in called genotypes">
##INFO=<ID=BaseQRankSum,Number=1,Type=Float,Description="Z-score from Wilcoxon rank sum test of Alt Vs. Ref base qualities">
##reference=file:///home/tools/hg19_reference/ucsc.hg19.fasta
##INFO=<ID=GDBIG_AN,Number=1,Type=Integer,Description="Number of Alleles in Samples with Coverage from GDBIG_hg19_v1.0">
##INFO=<ID=GDBIG_AC,Number=A,Type=Integer,Description="Alternate Allele Counts in Samples with Coverage from GDBIG_hg19_v1.0">
##INFO=<ID=GDBIG_AF,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_hg19_v1.0">
##INFO=<ID=GDBIG_FILTER,Number=A,Type=Float,Description="Filter from GDBIG_hg19_v1.0">
#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO
chr21   9413612 .       C       T       6906.62 .       AC=25;AF=0.313;AN=80;BaseQRankSum=0.425;GDBIG_AC=2459;GDBIG_AF=0.207525;GDBIG_AN=11834;GDBIG_FILTER=PASS
chr21   9413629 .       C       T       8028.88 .       AC=30;AF=0.375;AN=80;BaseQRankSum=-1.200e+00;GDBIG_AC=6906;GDBIG_AF=0.305445;GDBIG_AN=22406;GDBIG_FILTER=PASS
chr21   9413700 .       G       A       7723.82 .       AC=30;AF=0.375;AN=80;BaseQRankSum=-9.000e-02
chr21   9413735 .       C       A       10121.72        .       AC=35;AF=0.438;AN=80;BaseQRankSum=0.977;GDBIG_AC=2385;GDBIG_AF=0.283965;GDBIG_AN=8382;GDBIG_FILTER=PASS
chr21   9413839 .       C       T       8192.08 .       AC=28;AF=0.350;AN=80;BaseQRankSum=-5.200e-02
chr21   9413840 .       C       A       11514.35        .       AC=38;AF=0.475;AN=80;BaseQRankSum=0.253
chr21   9413870 .       T       C       7390.60 .       AC=26;AF=0.325;AN=80;BaseQRankSum=-4.270e-01
chr21   9413880 .       T       A       146.96  .       AC=1;AF=0.013;AN=80;BaseQRankSum=2.12;ClippingRankSum=0.00
chr21   9413909 .       G       A       1131.78 .       AC=10;AF=0.125;AN=80;BaseQRankSum=0.549;GDBIG_AC=209;GDBIG_AF=0.01507;GDBIG_AN=13683;GDBIG_FILTER=PASS
chr21   9413913 .       C       T       8120.65 .       AC=28;AF=0.350;AN=80;BaseQRankSum=-4.390e-01;GDBIG_AC=2870;GDBIG_AF=0.205597;GDBIG_AN=13955;GDBIG_FILTER=PASS
chr21   9413945 .       T       C       43787.68        .       AC=71;AF=0.888;AN=80;BaseQRankSum=0.089
chr21   9413995 .       C       T       9632.44 .       AC=29;AF=0.363;AN=80;BaseQRankSum=0.747
chr21   9413996 .       A       G       41996.48        .       AC=71;AF=0.888;AN=80;BaseQRankSum=-1.242e+00;GDBIG_AC=3308;GDBIG_AF=0.688533;GDBIG_AN=4790;GDBIG_FILTER=PASS
chr21   9414003 .       T       C       4256.54 .       AC=19;AF=0.238;AN=80;BaseQRankSum=-6.030e-01
```

Citation
------------
-