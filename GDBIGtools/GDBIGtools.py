"""
A command line tools for GDBIG variants browser

Author: Chengrui Wang
Date: 2021-12-01

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
GDBIG_API_VERSION = '1.1.6'

VCF_HEADER = [
    '##fileformat=VCFv4.2',
    '##FILTER=<ID=PASS,Description="All filters passed">',
    '##INFO=<ID=AF_GDBIG,Number=A,Type=Float,Description="Alternate Allele Frequencies in {}">'.format(GDBIG_DATASET_VERSION),
    '##INFO=<ID=AF_GDBIG_SouthChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from SouthChina region in {}">'.format(GDBIG_DATASET_VERSION),
    '##INFO=<ID=AF_GDBIG_CentralChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from CentralChina region in {}">'.format(GDBIG_DATASET_VERSION),
    '##INFO=<ID=AF_GDBIG_EastChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from EastChina region in {}">'.format(GDBIG_DATASET_VERSION),
    '##INFO=<ID=AF_GDBIG_SouthwestChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from SouthwestChina region in {}">'.format(GDBIG_DATASET_VERSION),
    '##INFO=<ID=AF_GDBIG_NortheastChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from NortheastChina region in {}">'.format(GDBIG_DATASET_VERSION),
    '##INFO=<ID=AF_GDBIG_NorthwestChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from NorthwestChina region in {}">'.format(GDBIG_DATASET_VERSION),
    '##INFO=<ID=AF_GDBIG_NorthChina,Number=A,Type=Float,Description="Alternate Allele Frequencies from NorthChina region in {}">'.format(GDBIG_DATASET_VERSION),
    '##INFO=<ID=AF_CMDB,Number=A,Type=Float,Description="Alternate Allele Frequencies in CMDB database">',
    '##INFO=<ID=AF_ChinaMAP,Number=A,Type=Float,Description="Alternate Allele Frequencies in ChinaMAP database">',
    '##INFO=<ID=AF_NyuWa,Number=A,Type=Float,Description="Alternate Allele Frequencies in NyuWa(NCVD) database">',
    '##INFO=<ID=AF_WBBC,Number=A,Type=Float,Description="Alternate Allele Frequencies in WBBC database">',
    '##INFO=<ID=AF_WBBC_North,Number=A,Type=Float,Description="Alternate Allele Frequencies from North region in WBBC database">',
    '##INFO=<ID=AF_WBBC_Central,Number=A,Type=Float,Description="Alternate Allele Frequencies from Central region in WBBC database">',
    '##INFO=<ID=AF_WBBC_South,Number=A,Type=Float,Description="Alternate Allele Frequencies from South region in WBBC database">',
    '##INFO=<ID=AF_WBBC_Lingnan,Number=A,Type=Float,Description="Alternate Allele Frequencies from Lingnan region in WBBC database">',
    '##INFO=<ID=AF_gnomAD,Number=A,Type=Float,Description="Alternate Allele Frequencies in gnomAD database">',
    '##INFO=<ID=AF_gnomAD_afr,Number=A,Type=Float,Description="Alternate Allele Frequencies from African-American/African population in gnomAD database">',
    '##INFO=<ID=AF_gnomAD_ami,Number=A,Type=Float,Description="Alternate Allele Frequencies from Amish population in gnomAD database">',
    '##INFO=<ID=AF_gnomAD_asj,Number=A,Type=Float,Description="Alternate Allele Frequencies from Ashkenazi Jewish population in gnomAD database">',
    '##INFO=<ID=AF_gnomAD_eas,Number=A,Type=Float,Description="Alternate Allele Frequencies from East Asian population in gnomAD database">',
    '##INFO=<ID=AF_gnomAD_fin,Number=A,Type=Float,Description="Alternate Allele Frequencies from Finnish population in gnomAD database">',
    '##INFO=<ID=AF_gnomAD_amr,Number=A,Type=Float,Description="Alternate Allele Frequencies from Latino population in gnomAD database">',
    '##INFO=<ID=AF_gnomAD_nfe,Number=A,Type=Float,Description="Alternate Allele Frequencies from Non-Finnish European population in gnomAD database">',
    '##INFO=<ID=AF_gnomAD_sas,Number=A,Type=Float,Description="Alternate Allele Frequencies from South Asian population in gnomAD database">',
    '##INFO=<ID=AF_gnomAD_oth,Number=A,Type=Float,Description="Alternate Allele Frequencies from Other population in gnomAD database">',
    '##INFO=<ID=AF_1KGP,Number=A,Type=Float,Description="Alternate Allele Frequencies in 1000 Genomes database">',
    '##INFO=<ID=AF_1KGP_AFR,Number=A,Type=Float,Description="Alternate Allele Frequencies from African population in 1000 Genomes database">',
    '##INFO=<ID=AF_1KGP_AMR,Number=A,Type=Float,Description="Alternate Allele Frequencies from Admixed American population in 1000 Genomes database">',
    '##INFO=<ID=AF_1KGP_EAS,Number=A,Type=Float,Description="Alternate Allele Frequencies from East Asian population in 1000 Genomes database">',
    '##INFO=<ID=AF_1KGP_EUR,Number=A,Type=Float,Description="Alternate Allele Frequencies from European population in 1000 Genomes database">',
    '##INFO=<ID=AF_1KGP_SAS,Number=A,Type=Float,Description="Alternate Allele Frequencies from South Asian population in 1000 Genomes database">',
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
    
    if res['code']=='geneID':
        return(r.status_code, res, IDlist)
    elif r.status_code!=200:
        return(r.status_code, res, IDlist)
    else:
        if res['Data']:
            for l in res['Data']['SNPs']:
                newid = "%s:%s-%s-%s"%(l['Chrom'],l['Position'],l['Ref'],l['Alt'])
                IDlist.append(newid)
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
                sys.stderr.write('[Error] Your search identifier: [%s]. Query region is too large (at most 100kb) or position format is error (e.g. chr:[integer] or chr:[smaller integer]-[larger integer]).\n'%search_key)
                sys.exit()
            else:
                return(r.status_code, res)
def json2vcf(res, stdout = True):
    result = []
    for vv in res:
        v = vv['Data']['SNPs'][0]
        w = vv['Data']['otherDB']
        vcf_line = ['chr' + v['Chrom'], v['Position'], v['RS'], v['Ref'], v['Alt'], '.', 'PASS']

        vcf_line1 = 'AF_GDBIG={};AF_GDBIG_SouthChina={};AF_GDBIG_CentralChina={};AF_GDBIG_EastChina={};AF_GDBIG_SouthwestChina={};AF_GDBIG_NortheastChina={};AF_GDBIG_NorthwestChina={};AF_GDBIG_NorthChina={}'.format(v['AF'],v['AF_SouthChina'],v['AF_CentralChina'],v['AF_EastChina'],v['AF_SouthwestChina'],v['AF_NortheastChina'],v['AF_NorthwestChina'],v['AF_NorthChina'])

        CMDB = w['CMDB']['AF'] if w['CMDB'] else 'NA'
        ChinaMap = w['ChinaMap']['AF'] if w['ChinaMap'] else 'NA'
        NyuWa = w['NyuWa']['AF'] if w['NyuWa'] else 'NA'
        vcf_line2 = 'AF_CMDB={};AF_ChinaMAP={};AF_NyuWa={}'.format(CMDB,ChinaMap,NyuWa)
        
        WBBC = w['WBBC'] if w['WBBC'] else {'AF':'NA','South_AF':'NA','Central_AF':'NA','South_AF':'NA','Lingnan_AF':'NA'}
        vcf_line3 = 'AF_WBBC={};AF_WBBC_North={};AF_WBBC_Central={};AF_WBBC_South={};AF_WBBC_Lingnan={}'.format(WBBC['AF'],WBBC['South_AF'],WBBC['Central_AF'],WBBC['South_AF'],WBBC['Lingnan_AF'])

        gnomAD = w['gnomAD'] if w['gnomAD'] else {'AF_Total':'NA','AF_afr':'NA','AF_ami':'NA','AF_asj':'NA','AF_eas':'NA','AF_fin':'NA','AF_amr':'NA','AF_nfe':'NA','AF_sas':'NA','AF_oth':'NA'}
        vcf_line4 = 'AF_gnomAD={};AF_gnomAD_afr={};AF_gnomAD_ami={};AF_gnomAD_asj={};AF_gnomAD_eas={};AF_gnomAD_fin={};AF_gnomAD_amr={};AF_gnomAD_nfe={};AF_gnomAD_sas={};AF_gnomAD_oth={}'.format(gnomAD['AF_Total'],gnomAD['AF_afr'],gnomAD['AF_ami'],gnomAD['AF_asj'],gnomAD['AF_eas'],gnomAD['AF_fin'],gnomAD['AF_amr'],gnomAD['AF_nfe'],gnomAD['AF_sas'],gnomAD['AF_oth'])

        OneK_Genomes = w['OneK_Genomes'] if w['OneK_Genomes'] else {'AF':'NA','AFR_AF':'NA','AMR_AF':'NA','EAS_AF':'NA','EUR_AF':'NA','SAS_AF':'NA'}
        vcf_line5 = 'AF_1KGP={};AF_1KGP_AFR={};AF_1KGP_AMR={};AF_1KGP_EAS={};AF_1KGP_EUR={};AF_1KGP_SAS={}'.format(OneK_Genomes['AF'],OneK_Genomes['AFR_AF'],OneK_Genomes['AMR_AF'],OneK_Genomes['EAS_AF'],OneK_Genomes['EUR_AF'],OneK_Genomes['SAS_AF'])
        vcf_line.append("%s;%s;%s;%s;%s"%(vcf_line1,vcf_line2,vcf_line3,vcf_line4,vcf_line5))
        if stdout:
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
    AFlist = json2vcf(reslist, stdout)
    return(AFlist)
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
        sys.stderr.write('[Error] API access or the API is wrong !!!\n[Error] Please confirm your API information [http://gdbig.bigcs.com.cn/api.html]\n')
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
                    sys.stdout.write('\n'.join(VCF_HEADER[2:34])+'\n')
                    sys.stdout.write('{}\n'.format(in_line.rstrip()))
                continue
            in_fields = in_line.rstrip().split()
            chromosome = in_fields[0]
            position = int(in_fields[1])
            ref = in_fields[3].upper()
            alt = in_fields[4].upper()

            GDBIG_variant_list = query_one(api_info, chromosome+':'+str(position)+'-'+ref+'-'+alt, stdout = False)
            if len(GDBIG_variant_list)==0:
                # not variants found in GDBIG
                sys.stdout.write('{}\n'.format(in_line.strip()))
            else:
                GDBIG_variant = GDBIG_variant_list
                if GDBIG_variant[4].upper() in alt.split(',') and GDBIG_variant[3].upper() == ref:
                    new_info, info_set = [], set()
                    if in_fields[7] == ".":
                        list_info = GDBIG_variant[7]
                    else:
                        list_info = in_fields[7] +';'+ GDBIG_variant[7]
                    if len(in_fields) > 8:
                        sys.stdout.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(chromosome, position, in_fields[2], ref, alt, in_fields[5], in_fields[6], list_info, '\t'.join(in_fields[8:])))
                    else:
                        sys.stdout.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(chromosome, position, in_fields[2], ref, alt, in_fields[5], in_fields[6], list_info))
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
