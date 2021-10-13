
GDBIGtools: A command line tools for GDBIG varaints browser
===========================================================

[![PyPI Version](https://img.shields.io/pypi/v/GDBIGtools.svg)](https://pypi.org/project/GDBIGtools/)
[![License](https://img.shields.io/pypi/l/GDBIGtools.svg)](https://github.com/BIGCS-Lab/GDBIGtools/blob/master/LICENSE)

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

Please enable your API access from Profile in [GDBIG browser](http://gdbig.bigcs.com.cn/api.html) before using **GDBIGtools**.

Help
------------
type `GDBIGtools -h/--help` for detail.
```
Usage: GDBIGtools [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  annotate   Annotate input VCF file with BIGCS allele Frequency.
  login      Login GDBIG.
  logout     Logout GDBIG.
  print-api  Display API information for GDBIG.
  query      Query variants from GDBIG database.
  version    GDBIGtools version: 1.1.0
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

```bash
##fileformat=VCFv4.2
##FILTER=<ID=PASS,Description="All filters passed">
##FORMAT=<ID=DS,Number=1,Type=Float,Description="estimated ALT dose [P(RA) + P(AA)]">
##FORMAT=<ID=GP,Number=G,Type=Float,Description="Estimated Genotype Probability">
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
##bcftools_concatVersion=1.9+htslib-1.9
##reference=file:/GRCh38/GCA_000001405.15_GRCh38_no_alt_analysis_set.fa
##INFO=<ID=GDBIG_AF,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0">
##INFO=<ID=GDBIG_AF_SouthChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in SouthChina region">
##INFO=<ID=GDBIG_AF_CentralChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in CentralChina region">
##INFO=<ID=GDBIG_AF_EastChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in EastChina region">
##INFO=<ID=GDBIG_AF_SouthwestChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in SouthwestChina region">
##INFO=<ID=GDBIG_AF_NortheastChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in NortheastChina region">
##INFO=<ID=GDBIG_AF_NorthwestChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in NorthwestChina region">
##INFO=<ID=GDBIG_AF_NorthChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from GDBIG_GRCh38_v1.0 in NorthChina region">
#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO
chr22   10515882        rs1490973086    G       A       .       PASS    GDBIG_AF=0.105296;GDBIG_AF_SouthChina=0.106336;GDBIG_AF_CentralChina=0.116307;GDBIG_AF_EastChina=0.113487;GDBIG_AF_SouthwestChina=0.078571;GDBIG_AF_NortheastChina=0.098837;GDBIG_AF_NorthwestChina=0.061644;GDBIG_AF_NorthChina=0.057377;AR2=0.63;DR2=0.68
chr22   10516264        .       TAC     T       .       PASS    GDBIG_AF=0.000123;GDBIG_AF_SouthChina=0;GDBIG_AF_CentralChina=0;GDBIG_AF_EastChina=0.001645;GDBIG_AF_SouthwestChina=0;GDBIG_AF_NortheastChina=0;GDBIG_AF_NorthwestChina=0;GDBIG_AF_NorthChina=0;AR2=0.78;DR2=0.78
chr22   10516615        rs1228174166    TTTG    T       .       PASS    GDBIG_AF=0.000123;GDBIG_AF_SouthChina=0.000169;GDBIG_AF_CentralChina=0;GDBIG_AF_EastChina=0;GDBIG_AF_SouthwestChina=0;GDBIG_AF_NortheastChina=0;GDBIG_AF_NorthwestChina=0;GDBIG_AF_NorthChina=0;AR2=0.221;DR2=0.222
chr22   10518420        rs1177693979    CA      C       .       PASS    GDBIG_AF=0.000246;GDBIG_AF_SouthChina=0.000337;GDBIG_AF_CentralChina=0;GDBIG_AF_EastChina=0;GDBIG_AF_SouthwestChina=0;GDBIG_AF_NortheastChina=0;GDBIG_AF_NorthwestChina=0;GDBIG_AF_NorthChina=0;AR2=0.547;DR2=0.607
chr22   10519243        rs1186022611    A       AG      .       PASS    GDBIG_AF=0.000123;GDBIG_AF_SouthChina=0.000169;GDBIG_AF_CentralChina=0;GDBIG_AF_EastChina=0;GDBIG_AF_SouthwestChina=0;GDBIG_AF_NortheastChina=0;GDBIG_AF_NorthwestChina=0;GDBIG_AF_NorthChina=0;AR2=0.673;DR2=0.707
chr22   10519428        rs1361775216    C       T       .       PASS    GDBIG_AF=0.062931;GDBIG_AF_SouthChina=0.062521;GDBIG_AF_CentralChina=0.082734;GDBIG_AF_EastChina=0.057566;GDBIG_AF_SouthwestChina=0.05;GDBIG_AF_NortheastChina=0.052326;GDBIG_AF_NorthwestChina=0.068493;GDBIG_AF_NorthChina=0.02459;AR2=0.799;DR2=0.828
```

Citation
------------
-
