
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
  version    GDBIGtools version: 1.1.2
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
##INFO=<ID=AF_CMDB,Number=A,Type=Float,Description="Alternate Allele Frequencies in CMDB database">
##INFO=<ID=AF_ChinaMAP,Number=A,Type=Float,Description="Alternate Allele Frequencies in ChinaMAP database">
##INFO=<ID=AF_NyuWa,Number=A,Type=Float,Description="Alternate Allele Frequencies in NyuWa(NCVD) database">
##INFO=<ID=AF_WBBC,Number=A,Type=Float,Description="Alternate Allele Frequencies in WBBC database">
##INFO=<ID=AF_WBBC_North,Number=A,Type=Float,Description="Alternate Allele Frequencies in North region of WBBC database">
##INFO=<ID=AF_WBBC_Central,Number=A,Type=Float,Description="Alternate Allele Frequencies in Central region of WBBC database">
##INFO=<ID=AF_WBBC_South,Number=A,Type=Float,Description="Alternate Allele Frequencies in South region of WBBC database">
##INFO=<ID=AF_WBBC_Lingnan,Number=A,Type=Float,Description="Alternate Allele Frequencies in Lingnan region of WBBC database">
##INFO=<ID=AF_gnomAD,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD database">
##INFO=<ID=AF_gnomAD_afr,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_afr database">
##INFO=<ID=AF_gnomAD_ami,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_ami database">
##INFO=<ID=AF_gnomAD_asj,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_asj database">
##INFO=<ID=AF_gnomAD_eas,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_eas database">
##INFO=<ID=AF_gnomAD_fin,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_fin database">
##INFO=<ID=AF_gnomAD_amr,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_amr database">
##INFO=<ID=AF_gnomAD_nfe,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_nfe database">
##INFO=<ID=AF_gnomAD_sas,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_sas database">
##INFO=<ID=AF_gnomAD_oth,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_oth database">
##INFO=<ID=AF_1KGP,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes database">
##INFO=<ID=AF_1KGP_AFR,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes AFR database">
##INFO=<ID=AF_1KGP_AMR,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes AMR database">
##INFO=<ID=AF_1KGP_EAS,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes EAS database">
##INFO=<ID=AF_1KGP_EUR,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes EUR database">
##INFO=<ID=AF_1KGP_SAS,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes SAS database">
##reference=file:/human_reference/GRCh38/GCA_000001405.15_GRCh38_no_alt_analysis_set.fa
#CHROM  POS ID  REF ALT QUAL  FILTER  INFO
chr7  24926827  rs123 C A . PASS  GDBIG_AF=0.898399;GDBIG_AF_SouthChina=0.899225;GDBIG_AF_CentralChina=0.894484;GDBIG_AF_EastChina=0.919408;GDBIG_AF_SouthwestChina=0.914286;GDBIG_AF_NortheastChina=0.883721;GDBIG_AF_NorthwestChina=0.835616;GDBIG_AF_NorthChina=0.852459;AF_CMDB=0.872917;AF_ChinaMAP=0.901964;AF_NyuWa=0.896132;AF_WBBC=0.904878592;AF_WBBC_North=0.90578635;AF_WBBC_Central=0.94;AF_WBBC_South=0.90578635;AF_WBBC_Lingnan=0.96031746;AF_gnomAD=0.579731;AF_gnomAD_afr=0.702737;AF_gnomAD_ami=0.57461;AF_gnomAD_asj=0.550572;AF_gnomAD_eas=0.910955;AF_gnomAD_fin=0.513438;AF_gnomAD_amr=0.586364;AF_gnomAD_nfe=0.489122;AF_gnomAD_sas=0.710994;AF_gnomAD_oth=0.55948;AF_1KGP=0.707867;AF_1KGP_AFR=0.7269;AF_1KGP_AMR=0.6383;AF_1KGP_EAS=0.9038;AF_1KGP_EUR=0.5119;AF_1KGP_SAS=0.7311
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
##INFO=<ID=AF_CMDB,Number=A,Type=Float,Description="Alternate Allele Frequencies in CMDB database">
##INFO=<ID=AF_ChinaMAP,Number=A,Type=Float,Description="Alternate Allele Frequencies in ChinaMAP database">
##INFO=<ID=AF_NyuWa,Number=A,Type=Float,Description="Alternate Allele Frequencies in NyuWa(NCVD) database">
##INFO=<ID=AF_WBBC,Number=A,Type=Float,Description="Alternate Allele Frequencies in WBBC database">
##INFO=<ID=AF_WBBC_North,Number=A,Type=Float,Description="Alternate Allele Frequencies in North region of WBBC database">
##INFO=<ID=AF_WBBC_Central,Number=A,Type=Float,Description="Alternate Allele Frequencies in Central region of WBBC database">
##INFO=<ID=AF_WBBC_South,Number=A,Type=Float,Description="Alternate Allele Frequencies in South region of WBBC database">
##INFO=<ID=AF_WBBC_Lingnan,Number=A,Type=Float,Description="Alternate Allele Frequencies in Lingnan region of WBBC database">
##INFO=<ID=AF_gnomAD,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD database">
##INFO=<ID=AF_gnomAD_afr,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_afr database">
##INFO=<ID=AF_gnomAD_ami,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_ami database">
##INFO=<ID=AF_gnomAD_asj,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_asj database">
##INFO=<ID=AF_gnomAD_eas,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_eas database">
##INFO=<ID=AF_gnomAD_fin,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_fin database">
##INFO=<ID=AF_gnomAD_amr,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_amr database">
##INFO=<ID=AF_gnomAD_nfe,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_nfe database">
##INFO=<ID=AF_gnomAD_sas,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_sas database">
##INFO=<ID=AF_gnomAD_oth,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_oth database">
##INFO=<ID=AF_1KGP,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes database">
##INFO=<ID=AF_1KGP_AFR,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes AFR database">
##INFO=<ID=AF_1KGP_AMR,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes AMR database">
##INFO=<ID=AF_1KGP_EAS,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes EAS database">
##INFO=<ID=AF_1KGP_EUR,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes EUR database">
##INFO=<ID=AF_1KGP_SAS,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes SAS database">
##reference=file:/human_reference/GRCh38/GCA_000001405.15_GRCh38_no_alt_analysis_set.fa
#CHROM  POS ID  REF ALT QUAL  FILTER  INFO
chr17 7668445 . T C . PASS  GDBIG_AF=0.000123;GDBIG_AF_SouthChina=0;GDBIG_AF_CentralChina=0.001199;GDBIG_AF_EastChina=0;GDBIG_AF_SouthwestChina=0;GDBIG_AF_NortheastChina=0;GDBIG_AF_NorthwestChina=0;GDBIG_AF_NorthChina=0;AF_CMDB=Na;AF_ChinaMAP=4.7e-05;AF_NyuWa=Na;AF_WBBC=Na;AF_WBBC_North=Na;AF_WBBC_Central=Na;AF_WBBC_South=Na;AF_WBBC_Lingnan=Na;AF_gnomAD=Na;AF_gnomAD_afr=Na;AF_gnomAD_ami=Na;AF_gnomAD_asj=Na;AF_gnomAD_eas=Na;AF_gnomAD_fin=Na;AF_gnomAD_amr=Na;AF_gnomAD_nfe=Na;AF_gnomAD_sas=Na;AF_gnomAD_oth=Na;AF_1KGP=Na;AF_1KGP_AFR=Na;AF_1KGP_AMR=Na;AF_1KGP_EAS=Na;AF_1KGP_EUR=Na;AF_1KGP_SAS=Na
chr17 7668556 rs891497989 G A . PASS  GDBIG_AF=0.000493;GDBIG_AF_SouthChina=0.000506;GDBIG_AF_CentralChina=0;GDBIG_AF_EastChina=0;GDBIG_AF_SouthwestChina=0.003571;GDBIG_AF_NortheastChina=0;GDBIG_AF_NorthwestChina=0;GDBIG_AF_NorthChina=0;AF_CMDB=Na;AF_ChinaMAP=4.7e-05;AF_NyuWa=Na;AF_WBBC=Na;AF_WBBC_North=Na;AF_WBBC_Central=Na;AF_WBBC_South=Na;AF_WBBC_Lingnan=Na;AF_gnomAD=7.67706e-05;AF_gnomAD_afr=0.000118923;AF_gnomAD_ami=0;AF_gnomAD_asj=0;AF_gnomAD_eas=0.00159744;AF_gnomAD_fin=0;AF_gnomAD_amr=0;AF_gnomAD_nfe=1.5488e-05;AF_gnomAD_sas=0;AF_gnomAD_oth=0;AF_1KGP=Na;AF_1KGP_AFR=Na;AF_1KGP_AMR=Na;AF_1KGP_EAS=Na;AF_1KGP_EUR=Na;AF_1KGP_SAS=Na
chr17 7668587 . T G . PASS  GDBIG_AF=0.000123;GDBIG_AF_SouthChina=0;GDBIG_AF_CentralChina=0;GDBIG_AF_EastChina=0.001645;GDBIG_AF_SouthwestChina=0;GDBIG_AF_NortheastChina=0;GDBIG_AF_NorthwestChina=0;GDBIG_AF_NorthChina=0;AF_CMDB=Na;AF_ChinaMAP=Na;AF_NyuWa=Na;AF_WBBC=0.000111383;AF_WBBC_North=0.00012364;AF_WBBC_Central=0;AF_WBBC_South=0.00012364;AF_WBBC_Lingnan=0;AF_gnomAD=Na;AF_gnomAD_afr=Na;AF_gnomAD_ami=Na;AF_gnomAD_asj=Na;AF_gnomAD_eas=Na;AF_gnomAD_fin=Na;AF_gnomAD_amr=Na;AF_gnomAD_nfe=Na;AF_gnomAD_sas=Na;AF_gnomAD_oth=Na;AF_1KGP=Na;AF_1KGP_AFR=Na;AF_1KGP_AMR=Na;AF_1KGP_EAS=Na;AF_1KGP_EUR=Na;AF_1KGP_SAS=Na
chr17 7668649 rs1393899747  G A . PASS  GDBIG_AF=0.000369;GDBIG_AF_SouthChina=0.000506;GDBIG_AF_CentralChina=0;GDBIG_AF_EastChina=0;GDBIG_AF_SouthwestChina=0;GDBIG_AF_NortheastChina=0;GDBIG_AF_NorthwestChina=0;GDBIG_AF_NorthChina=0;AF_CMDB=Na;AF_ChinaMAP=0.000519;AF_NyuWa=0.000667;AF_WBBC=0.0006683;AF_WBBC_North=0.0006182;AF_WBBC_Central=0;AF_WBBC_South=0.0006182;AF_WBBC_Lingnan=0;AF_gnomAD=3.49557e-05;AF_gnomAD_afr=0;AF_gnomAD_ami=0;AF_gnomAD_asj=0;AF_gnomAD_eas=0.00159847;AF_gnomAD_fin=0;AF_gnomAD_amr=0;AF_gnomAD_nfe=0;AF_gnomAD_sas=0;AF_gnomAD_oth=0;AF_1KGP=Na;AF_1KGP_AFR=Na;AF_1KGP_AMR=Na;AF_1KGP_EAS=Na;AF_1KGP_EUR=Na;AF_1KGP_SAS=Na
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
-   `AF_CMDB`: Alternate Allele Frequencies in CMDB database;
-   `AF_ChinaMAP`: Alternate Allele Frequencies in ChinaMAP database;
-   `AF_NyuWa`: Alternate Allele Frequencies in NyuWa(NCVD) database;
-   `AF_WBBC`: Alternate Allele Frequencies in WBBC database;
-   `AF_WBBC_North`: Alternate Allele Frequencies in North region of WBBC database;
-   `AF_WBBC_Central`: Alternate Allele Frequencies in Central region of WBBC database;
-   `AF_WBBC_South`: Alternate Allele Frequencies in South region of WBBC database;
-   `AF_WBBC_Lingnan`: Alternate Allele Frequencies in Lingnan region of WBBC database;
-   `AF_gnomAD`: Alternate Allele Frequencies in gnomAD database;
-   `AF_gnomAD_afr`: Alternate Allele Frequencies in gnomAD_afr database;
-   `AF_gnomAD_ami`: Alternate Allele Frequencies in gnomAD_ami database;
-   `AF_gnomAD_asj`: Alternate Allele Frequencies in gnomAD_asj database;
-   `AF_gnomAD_eas`: Alternate Allele Frequencies in gnomAD_eas database;
-   `AF_gnomAD_fin`: Alternate Allele Frequencies in gnomAD_fin database;
-   `AF_gnomAD_amr`: Alternate Allele Frequencies in gnomAD_amr database;
-   `AF_gnomAD_nfe`: Alternate Allele Frequencies in gnomAD_nfe database;
-   `AF_gnomAD_sas`: Alternate Allele Frequencies in gnomAD_sas database;
-   `AF_gnomAD_oth`: Alternate Allele Frequencies in gnomAD_oth database;
-   `AF_1KGP`: Alternate Allele Frequencies in 1000 Genomes database;
-   `AF_1KGP_AFR`: Alternate Allele Frequencies in 1000 Genomes AFR database;
-   `AF_1KGP_AMR`: Alternate Allele Frequencies in 1000 Genomes AMR database;
-   `AF_1KGP_EAS`: Alternate Allele Frequencies in 1000 Genomes EAS database;
-   `AF_1KGP_EUR`: Alternate Allele Frequencies in 1000 Genomes EUR database;
-   `AF_1KGP_SAS`: Alternate Allele Frequencies in 1000 Genomes SAS database;

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
##INFO=<ID=AF_CMDB,Number=A,Type=Float,Description="Alternate Allele Frequencies in CMDB database">
##INFO=<ID=AF_ChinaMAP,Number=A,Type=Float,Description="Alternate Allele Frequencies in ChinaMAP database">
##INFO=<ID=AF_NyuWa,Number=A,Type=Float,Description="Alternate Allele Frequencies in NyuWa(NCVD) database">
##INFO=<ID=AF_WBBC,Number=A,Type=Float,Description="Alternate Allele Frequencies in WBBC database">
##INFO=<ID=AF_WBBC_North,Number=A,Type=Float,Description="Alternate Allele Frequencies in North region of WBBC database">
##INFO=<ID=AF_WBBC_Central,Number=A,Type=Float,Description="Alternate Allele Frequencies in Central region of WBBC database">
##INFO=<ID=AF_WBBC_South,Number=A,Type=Float,Description="Alternate Allele Frequencies in South region of WBBC database">
##INFO=<ID=AF_WBBC_Lingnan,Number=A,Type=Float,Description="Alternate Allele Frequencies in Lingnan region of WBBC database">
##INFO=<ID=AF_gnomAD,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD database">
##INFO=<ID=AF_gnomAD_afr,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_afr database">
##INFO=<ID=AF_gnomAD_ami,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_ami database">
##INFO=<ID=AF_gnomAD_asj,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_asj database">
##INFO=<ID=AF_gnomAD_eas,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_eas database">
##INFO=<ID=AF_gnomAD_fin,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_fin database">
##INFO=<ID=AF_gnomAD_amr,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_amr database">
##INFO=<ID=AF_gnomAD_nfe,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_nfe database">
##INFO=<ID=AF_gnomAD_sas,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_sas database">
##INFO=<ID=AF_gnomAD_oth,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_oth database">
##INFO=<ID=AF_1KGP,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes database">
##INFO=<ID=AF_1KGP_AFR,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes AFR database">
##INFO=<ID=AF_1KGP_AMR,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes AMR database">
##INFO=<ID=AF_1KGP_EAS,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes EAS database">
##INFO=<ID=AF_1KGP_EUR,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes EUR database">
##INFO=<ID=AF_1KGP_SAS,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes SAS database">
#CHROM  POS ID  REF ALT QUAL  FILTER  INFO
chr22 10515882  rs1490973086  G A . PASS  GDBIG_AF=0.105296;GDBIG_AF_SouthChina=0.106336;GDBIG_AF_CentralChina=0.116307;GDBIG_AF_EastChina=0.113487;GDBIG_AF_SouthwestChina=0.078571;GDBIG_AF_NortheastChina=0.098837;GDBIG_AF_NorthwestChina=0.061644;GDBIG_AF_NorthChina=0.057377;AF_CMDB=Na;AF_ChinaMAP=Na;AF_NyuWa=Na;AF_WBBC=Na;AF_WBBC_North=Na;AF_WBBC_Central=Na;AF_WBBC_South=Na;AF_WBBC_Lingnan=Na;AF_gnomAD=0.0918221;AF_gnomAD_afr=0.0347594;AF_gnomAD_ami=0.123162;AF_gnomAD_asj=0.196657;AF_gnomAD_eas=0.261649;AF_gnomAD_fin=0.171307;AF_gnomAD_amr=0.0983247;AF_gnomAD_nfe=0.10664;AF_gnomAD_sas=0.20235;AF_gnomAD_oth=0.11147;AF_1KGP=Na;AF_1KGP_AFR=Na;AF_1KGP_AMR=Na;AF_1KGP_EAS=Na;AF_1KGP_EUR=Na;AF_1KGP_SAS=Na;AR2=0.63;DR2=0.68
chr22 10516264  . TAC T . PASS  GDBIG_AF=0.000123;GDBIG_AF_SouthChina=0;GDBIG_AF_CentralChina=0;GDBIG_AF_EastChina=0.001645;GDBIG_AF_SouthwestChina=0;GDBIG_AF_NortheastChina=0;GDBIG_AF_NorthwestChina=0;GDBIG_AF_NorthChina=0;AF_CMDB=Na;AF_ChinaMAP=Na;AF_NyuWa=Na;AF_WBBC=Na;AF_WBBC_North=Na;AF_WBBC_Central=Na;AF_WBBC_South=Na;AF_WBBC_Lingnan=Na;AF_gnomAD=Na;AF_gnomAD_afr=Na;AF_gnomAD_ami=Na;AF_gnomAD_asj=Na;AF_gnomAD_eas=Na;AF_gnomAD_fin=Na;AF_gnomAD_amr=Na;AF_gnomAD_nfe=Na;AF_gnomAD_sas=Na;AF_gnomAD_oth=Na;AF_1KGP=Na;AF_1KGP_AFR=Na;AF_1KGP_AMR=Na;AF_1KGP_EAS=Na;AF_1KGP_EUR=Na;AF_1KGP_SAS=Na;AR2=0.78;DR2=0.78
chr22 10516615  rs1228174166  TTTG  T . PASS  AR2=0.221;DR2=0.222
chr22 10518420  rs1177693979  CA  C . PASS  GDBIG_AF=0.000246;GDBIG_AF_SouthChina=0.000337;GDBIG_AF_CentralChina=0;GDBIG_AF_EastChina=0;GDBIG_AF_SouthwestChina=0;GDBIG_AF_NortheastChina=0;GDBIG_AF_NorthwestChina=0;GDBIG_AF_NorthChina=0;AF_CMDB=Na;AF_ChinaMAP=0.00069;AF_NyuWa=Na;AF_WBBC=Na;AF_WBBC_North=Na;AF_WBBC_Central=Na;AF_WBBC_South=Na;AF_WBBC_Lingnan=Na;AF_gnomAD=Na;AF_gnomAD_afr=Na;AF_gnomAD_ami=Na;AF_gnomAD_asj=Na;AF_gnomAD_eas=Na;AF_gnomAD_fin=Na;AF_gnomAD_amr=Na;AF_gnomAD_nfe=Na;AF_gnomAD_sas=Na;AF_gnomAD_oth=Na;AF_1KGP=Na;AF_1KGP_AFR=Na;
```

Citation
------------
-
