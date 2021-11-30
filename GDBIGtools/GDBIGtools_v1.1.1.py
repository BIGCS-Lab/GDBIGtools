"""
A command line tools for GDBIG variants browser

Author: Chengrui Wang
Date: 2021-11-30

"""
import os
import sys
import csv
import json
import requests
import hashlib
import math
import click
import yaml
import stat
import time
import gzip
from datetime import datetime

USER_HOME = os.path.expanduser("~")
GDBIG_DIR = '.gdbig'
GDBIG_TOKENSTORE = 'authaccess.yaml'

GDBIG_DATASET_VERSION = 'GDBIG_GRCh38_v1.0'
GDBIG_API_VERSION = '1.1.1'

VCF_HEADER = [
    '##fileformat=VCFv4.2',
    '##FILTER=<ID=PASS,Description="All filters passed">',
    '##INFO=<ID=GDBIG_AF,Number=A,Type=Float,Description="Alternate Allele Frequencies from {}">'.format(GDBIG_DATASET_VERSION),
    '##INFO=<ID=GDBIG_AF_SouthChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from {} in SouthChina region">'.format(GDBIG_DATASET_VERSION),
    '##INFO=<ID=GDBIG_AF_CentralChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from {} in CentralChina region">'.format(GDBIG_DATASET_VERSION),
    '##INFO=<ID=GDBIG_AF_EastChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from {} in EastChina region">'.format(GDBIG_DATASET_VERSION),
    '##INFO=<ID=GDBIG_AF_SouthwestChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from {} in SouthwestChina region">'.format(GDBIG_DATASET_VERSION),
    '##INFO=<ID=GDBIG_AF_NortheastChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from {} in NortheastChina region">'.format(GDBIG_DATASET_VERSION),
    '##INFO=<ID=GDBIG_AF_NorthwestChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from {} in NorthwestChina region">'.format(GDBIG_DATASET_VERSION),
    '##INFO=<ID=GDBIG_AF_NorthChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from {} in NorthChina region">'.format(GDBIG_DATASET_VERSION),
    '##INFO=<ID=AF_CMDB,Number=A,Type=Float,Description="Alternate Allele Frequencies in CMDB database">',
    '##INFO=<ID=AF_ChinaMAP,Number=A,Type=Float,Description="Alternate Allele Frequencies in ChinaMAP database">',
    '##INFO=<ID=AF_NyuWa,Number=A,Type=Float,Description="Alternate Allele Frequencies in NyuWa(NCVD) database">',
    '##INFO=<ID=AF_WBBC,Number=A,Type=Float,Description="Alternate Allele Frequencies in WBBC database">',
    '##INFO=<ID=AF_WBBC_North,Number=A,Type=Float,Description="Alternate Allele Frequencies in North region of WBBC database">',
    '##INFO=<ID=AF_WBBC_Central,Number=A,Type=Float,Description="Alternate Allele Frequencies in Central region of WBBC database">',
    '##INFO=<ID=AF_WBBC_South,Number=A,Type=Float,Description="Alternate Allele Frequencies in South region of WBBC database">',
    '##INFO=<ID=AF_WBBC_Lingnan,Number=A,Type=Float,Description="Alternate Allele Frequencies in Lingnan region of WBBC database">',
    '##INFO=<ID=AF_gnomAD,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD database">',
    '##INFO=<ID=AF_gnomAD_afr,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_afr database">',
    '##INFO=<ID=AF_gnomAD_ami,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_ami database">',
    '##INFO=<ID=AF_gnomAD_asj,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_asj database">',
    '##INFO=<ID=AF_gnomAD_eas,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_eas database">',
    '##INFO=<ID=AF_gnomAD_fin,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_fin database">',
    '##INFO=<ID=AF_gnomAD_amr,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_amr database">',
    '##INFO=<ID=AF_gnomAD_nfe,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_nfe database">',
    '##INFO=<ID=AF_gnomAD_sas,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_sas database">',
    '##INFO=<ID=AF_gnomAD_oth,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD_oth database">',
    '##INFO=<ID=AF_1KGP,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes database">',
    '##INFO=<ID=AF_1KGP_AFR,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes AFR database">',
    '##INFO=<ID=AF_1KGP_AMR,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes AMR database">',
    '##INFO=<ID=AF_1KGP_EAS,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes EAS database">',
    '##INFO=<ID=AF_1KGP_EUR,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes EUR database">',
    '##INFO=<ID=AF_1KGP_SAS,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes SAS database">',
    '##reference=file:/human_reference/GRCh38/GCA_000001405.15_GRCh38_no_alt_analysis_set.fa',
    '#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO'
]

def authaccess_exists():
    return os.path.isfile(os.path.join(USER_HOME, GDBIG_DIR, GDBIG_TOKENSTORE))

def create_authentication(api_key, api_secret, url):
    p = os.path.join(USER_HOME, GDBIG_DIR)
    if not os.path.isdir(p):
        os.mkdir(p, stat.S_IRWXU)  ## 0700

    p = os.path.join(p, GDBIG_TOKENSTORE)
    with open(p, 'w') as tokenstore:
        token_obj = {
            "url": url,
            "api_key": api_key,
            "api_secret": api_secret,
            "version": GDBIG_DATASET_VERSION
        }
        yaml.dump(token_obj, tokenstore)

    os.chmod(p, stat.S_IRUSR + stat.S_IWUSR)  # 0600
def read_authentication():
    file_auth = os.path.join(USER_HOME, GDBIG_DIR, GDBIG_TOKENSTORE)
    with open(file_auth, 'r') as I:
        tokenstore = yaml.load(I, Loader=yaml.FullLoader)
        status_code, result = getVariant(tokenstore.get('api_key', None), tokenstore.get('api_secret', None), tokenstore.get('url', 'http://gdbig.bigcs.com.cn'))
        if status_code != 200:
            sys.stderr.write('[Error] Invalid or outdated access token. \nYou may need to run login.\n')
            return
        return tokenstore

def getVariantID(api_key, api_secret, url, search_key="rs1801133"):
    h1 = hashlib.md5()
    h1.update((api_key+search_key+api_secret).encode(encoding="utf-8"))
    req_hash = h1.hexdigest()
    req_hash = req_hash[:28]+str(math.ceil(time.time()))[-4:]
    r = requests.get(url+"/openapi/search",{'api_key':api_key, 'key':search_key, 'api_hash':req_hash})
    res = json.loads(r.text)
    IDlist = []
    try:
        for l in res['Data']['SNPs']:
            newid = "%s:%s-%s-%s"%(l['Chrom'],l['Position'],l['Ref'],l['Alt'])
            IDlist.append(newid)
    except:
        pass
    return(r.status_code, res, IDlist)

def getVariant(api_key, api_secret, url, search_key="rs1801133"):
    h1 = hashlib.md5()
    h1.update((api_key+search_key+api_secret).encode(encoding="utf-8"))
    req_hash = h1.hexdigest()
    req_hash = req_hash[:28]+str(math.ceil(time.time()))[-4:]
    r = requests.get(url+"/openapi/search",{'api_key':api_key, 'key':search_key, 'api_hash':req_hash})

    res = json.loads(r.text)
    if r.status_code!=200:
        return(r.status_code, res)
    else:
        if res['code']!="":
            return(r.status_code, res)
        else:
            if res['Data']==None:
                sys.stderr.write('[Error] Your search identifier: [%s]. Query region is too large (at most 100kb) or position format is error (e.g. chr:[integer] or chr:[smaller integer]-[larger integer]).'%search_key)
                sys.exit()
            else:
                return(r.status_code, res)
def json2vcf(res, stdout = True):
    result = []
    for vv in res:
        v = vv['Data']['SNPs'][0]
        w = vv['Data']['otherDB']
        vcf_line = ['chr' + v['Chrom'], v['Position'], v['RS'], v['Ref'], v['Alt'], '.', 'PASS']

        vcf_line1 = 'GDBIG_AF={};GDBIG_AF_SouthChina={};GDBIG_AF_CentralChina={};GDBIG_AF_EastChina={};GDBIG_AF_SouthwestChina={};GDBIG_AF_NortheastChina={};GDBIG_AF_NorthwestChina={};GDBIG_AF_NorthChina={}'.format(v['AF'],v['AF_SouthChina'],v['AF_CentralChina'],v['AF_EastChina'],v['AF_SouthwestChina'],v['AF_NortheastChina'],v['AF_NorthwestChina'],v['AF_NorthChina'])

        CMDB = w['CMDB']['AF'] if w['CMDB'] else 'Na'
        ChinaMap = w['ChinaMap']['AF'] if w['ChinaMap'] else 'Na'
        NyuWa = w['NyuWa']['AF'] if w['NyuWa'] else 'Na'
        vcf_line2 = 'AF_CMDB={};AF_ChinaMAP={};AF_NyuWa={}'.format(CMDB,ChinaMap,NyuWa)
        
        WBBC = w['WBBC'] if w['WBBC'] else {'AF':'Na','South_AF':'Na','Central_AF':'Na','South_AF':'Na','Lingnan_AF':'Na'}
        vcf_line3 = 'AF_WBBC={};AF_WBBC_North={};AF_WBBC_Central={};AF_WBBC_South={};AF_WBBC_Lingnan={}'.format(WBBC['AF'],WBBC['South_AF'],WBBC['Central_AF'],WBBC['South_AF'],WBBC['Lingnan_AF'])

        gnomAD = w['gnomAD'] if w['gnomAD'] else {'AF_Total':'Na','AF_afr':'Na','AF_ami':'Na','AF_asj':'Na','AF_eas':'Na','AF_fin':'Na','AF_amr':'Na','AF_nfe':'Na','AF_sas':'Na','AF_oth':'Na'}
        vcf_line4 = 'AF_gnomAD={};AF_gnomAD_afr={};AF_gnomAD_ami={};AF_gnomAD_asj={};AF_gnomAD_eas={};AF_gnomAD_fin={};AF_gnomAD_amr={};AF_gnomAD_nfe={};AF_gnomAD_sas={};AF_gnomAD_oth={}'.format(gnomAD['AF_Total'],gnomAD['AF_afr'],gnomAD['AF_ami'],gnomAD['AF_asj'],gnomAD['AF_eas'],gnomAD['AF_fin'],gnomAD['AF_amr'],gnomAD['AF_nfe'],gnomAD['AF_sas'],gnomAD['AF_oth'])

        OneK_Genomes = w['OneK_Genomes'] if w['OneK_Genomes'] else {'AF':'Na','AFR_AF':'Na','AMR_AF':'Na','EAS_AF':'Na','EUR_AF':'Na','SAS_AF':'Na'}
        vcf_line5 = 'AF_1KGP={};AF_1KGP_AFR={};AF_1KGP_AMR={};AF_1KGP_EAS={};AF_1KGP_EUR={};AF_1KGP_SAS={}'.format(OneK_Genomes['AF'],OneK_Genomes['AFR_AF'],OneK_Genomes['AMR_AF'],OneK_Genomes['EAS_AF'],OneK_Genomes['EUR_AF'],OneK_Genomes['SAS_AF'])
        if stdout:
            vcf_line.append("%s;%s;%s;%s;%s"%(vcf_line1,vcf_line2,vcf_line3,vcf_line4,vcf_line5))
            sys.stdout.write('%s\n' % '\t'.join(map(str, vcf_line)))
        result.extend(vcf_line)
    return(result)

def query_one(api_info, search_identifier, stdout = True):
    res_status, res, IDlist = getVariantID(api_info['api_key'], api_info['api_secret'], api_info['url'], search_key = search_identifier)
    if  res['code'] == 'geneID':
        res_status, res, IDlist = getVariantID(api_info['api_key'], api_info['api_secret'], api_info['url'], search_key = res['Data']['major_transcript'])
    reslist = []
    for newid in IDlist:
        res_status, res = getVariant(api_info['api_key'], api_info['api_secret'], api_info['url'], search_key = newid)
        reslist.append(res)
    return(json2vcf(reslist, stdout))
def query_file(api_info, list_file):
    with gzip.open(list_file) if list_file.endswith('.gz') else open(list_file,'r') as P:
        for line in P:
            if line.startswith("#"):
                continue
            col = line.strip().split()

            if len(col) == 0:
                continue
            elif len(col) == 1:
                key_word = col[0]
            elif len(col) == 2:
                key_word = col[0]+':'+col[1]
            elif len(col) == 3:
                key_word = col[0]+':'+col[1]+'-'+col[2]
            else:
                sys.stderr.write("[Error] Unexpected format hit [%s] in %s.\n" % (line.strip(), list_file))
            query_one(api_info, key_word)

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def GDBIGtools():
    pass  
@click.command(context_settings=CONTEXT_SETTINGS, help='Login GDBIG.')
@click.option('-k','--api_key', type=click.STRING, required=True, help='api key, please using single quotes! e.g. -k \'your_api_key\'')
@click.option('-s','--api_secret', type=click.STRING, required=True, help='api secret key, please using single quotes! e.g. -s \'your_api_secret\'')
@click.option('-u','--url', default='http://gdbig.bigcs.com.cn', help='The web url of GDBIG. [http://gdbig.bigcs.com.cn].')
def login(api_key, api_secret, url):
    status_code, result = getVariant(api_key, api_secret, url)
    if status_code != 200:
        sys.stderr.write('[Error] while obtaining your GDBIG API authentication server. You may do not have the API access or the API is wrong.\n[Error] Please confirm your API information [http://gdbig.bigcs.com.cn/api.html]')
        return
    else:
        create_authentication(api_key, api_secret, url)
        sys.stdout.write("Done.\nYou are signed in now.\n")

@click.command(context_settings=CONTEXT_SETTINGS, help='Logout GDBIG.')
def logout():
    if not authaccess_exists():
        sys.stderr.write("[Error] Don't find any your API information, no need to logout.\n")
        return

    file_path = os.path.join(USER_HOME, GDBIG_DIR, GDBIG_TOKENSTORE)
    os.remove(file_path)
    sys.stdout.write("Done.\nLogout successful.\n")
    return

@click.command(context_settings=CONTEXT_SETTINGS, help='GDBIGtools version: %s'%GDBIG_API_VERSION)
def version():
    sys.stdout.write("\nGDBIGtools version: %s \n\n"%GDBIG_API_VERSION)
    return

@click.command(context_settings=CONTEXT_SETTINGS, help="Display API information for GDBIG.")
def print_api():
    if not authaccess_exists():
        sys.stderr.write("[Error] Don't find any your API information, please login first.\n")
        return

    api_info = read_authentication()
    if api_info!=None:
        sys.stdout.write("API status: Enabled\n")
        sys.stdout.write("API Key: %s\n"%api_info['api_key'])
        sys.stdout.write("Secret Key: %s\n"%api_info['api_secret'])
        sys.stdout.write("url: %s\n"%api_info['url'])
        sys.stdout.write("version: %s\n"%api_info['version'])
    else:
        sys.stderr.write("[Error] API status: Invalid\n")

@click.command(context_settings=CONTEXT_SETTINGS, help="Query variants from GDBIG database.")
@click.option('-s','--search-identifier', help='Input single identifier, e.g. rs ID, chr:pos, chr:pos_start-pos_end, ensembl transcript ID')
@click.option('-l','--list-file', help='File contain a list of search identifier. One for each line.')
#@click.option('-o','--output', help='Output VCF filename, [default for stdout]')
def query(search_identifier, list_file):
    if not authaccess_exists():
        sys.stderr.write("[Error] Don't find any your API information, please login first.\n")
        return
    
    api_info = read_authentication()
    if api_info==None:
        sys.stderr.write("[Error] API status: Invalid\n")
        return

    if search_identifier!=None and list_file==None:
        sys.stdout.write('%s\n' % '\n'.join(VCF_HEADER))
        query_one(api_info, search_identifier)

    elif search_identifier==None and list_file!=None:
        sys.stdout.write('%s\n' % '\n'.join(VCF_HEADER))
        query_file(api_info, list_file)
    elif search_identifier!=None and list_file!=None:
        sys.stdout.write('%s\n' % '\n'.join(VCF_HEADER))
        query_one(api_info, search_identifier)
        query_file(api_info, list_file)
    else:
        sys.stderr.write("[Error] Choose either -s or -l option! type \"GDBIGtools -h/--help\" for detail.\n")
        return

@click.command(context_settings=CONTEXT_SETTINGS, help="Annotate input VCF file with BIGCS allele Frequency. Multi-allelic variant records in input VCF must be split into multiple bi-allelic variant records.")
@click.option('-i','--input-vcf', required=True, help='Input VCF file, allowed .vcf or .vcf.gz')
def annotate(input_vcf):
    if not authaccess_exists():
        sys.stderr.write("[Error] Don't find any your API information, please login first.\n")
        return
    
    api_info = read_authentication()
    if api_info==None:
        sys.stderr.write("[Error] API status: Invalid\n")
        return
    with gzip.open(input_vcf) if input_vcf.endswith('.gz') else open(input_vcf,'r') as I:
        for in_line in I:
            #in_line = in_line.decode("UTF-8")
            if in_line.startswith('#'):
                if in_line.startswith('##'):
                    sys.stdout.write('{}\n'.format(in_line.rstrip()))
                elif in_line.startswith('#CHROM'):
                    sys.stdout.write('\n'.join(VCF_HEADER[2:10])+'\n')
                    sys.stdout.write('{}\n'.format(in_line.rstrip()))
                continue
            in_fields = in_line.rstrip().split()
            chromosome = in_fields[0]
            position = int(in_fields[1])
            ref = in_fields[3].upper()
            alt = in_fields[4].upper()

            GDBIG_variant_list = query_one(api_info, chromosome+':'+str(position), stdout = False)
            if len(GDBIG_variant_list)==0:
                # not variants found in GDBIG
                sys.stdout.write('{}\n'.format(in_line.strip()))
            else:
                GDBIG_variant = GDBIG_variant_list[0]
                if GDBIG_variant[4].upper() in alt.split(',') and GDBIG_variant[3].upper() == ref:
                    new_info, info_set = [], set()
                    if in_fields[7] == ".":
                        list_info = GDBIG_variant[7].split(';')
                    else:
                        list_info = GDBIG_variant[7].split(';') + in_fields[7].split(';')
                    for f in list_info:
                        n = f.split('=')[0]
                        if n not in info_set:
                            new_info.append(f)
                            info_set.add(n)
                    info = ';'.join(new_info)
                    if len(in_fields) > 8:
                        sys.stdout.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(chromosome, position, in_fields[2], ref, alt, in_fields[5], in_fields[6], info, '\t'.join(in_fields[8:])))
                    else:
                        sys.stdout.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(chromosome, position, in_fields[2], ref, alt, in_fields[5], in_fields[6], info))
                else:
                    sys.stdout.write('{}\n'.format(in_line.strip()))

GDBIGtools.add_command(login)
GDBIGtools.add_command(logout)
GDBIGtools.add_command(print_api)
GDBIGtools.add_command(query)
GDBIGtools.add_command(annotate)
GDBIGtools.add_command(version)

if __name__ == '__main__':
    GDBIGtools()
