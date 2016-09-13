'''
18-Aug-2015
mstirling

for 1 folder, iterate through all files and write records into 1 file

Timing:
Should take <10 seconds

'''

#import libraries
import os, time

#timing
t1 = time.time()

#reuse same code for both var and algo riskwatch session
session = ['var','algo'][0]

if session == 'var':

    #in folder + out folder
    parent_folder = 'C:/Users/bwu/Desktop/Shared/RW/VAR Session/market.16.08.04/'
    in_folder = parent_folder + 'calibration/deals'
    out_folder = parent_folder + 'all/'
    out_file = 'deals.csv'
    out_audit_file = 'deals_audit.csv'
    
    list_filenames_to_skip = (['__bns__derivProdData__riskWatch__ACG13__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__CFHYPO__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQASIACORP__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYASIA__HKD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYASIA__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYD1D__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYD1D__HKD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYD1D__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYD1U__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYD1U__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYDC__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYDS__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYETF__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYFIO__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYFIO__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYFWD__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYFWD__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYIAB__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYILN__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYILN__EUR__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYILN__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYIO__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYLATAM__JPY__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYLATAM__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYSBI__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYSPI__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYSPI__EUR__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYSPI__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYSPS__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYSP__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYSP__EUR__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITYSSO__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITY__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__EQUITY__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__FLMSTRBIF__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__GPFLATAM__ALL__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__GPFLATAM__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__GTTRSRSUPSU__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__NYFIOPTHEDGE__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__PORTMGMT__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__PSLOANHEDGE__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__RETAILDH__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__RETAILDH__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__RETAIL__CAD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__RETAIL__EUR__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__RETAIL__USD__Sybase_K2.csv',
                               '__bns__derivProdData__riskWatch__STRPLACEHDR__USD__Sybase_K2.csv',
                               '__bns__var_rw__data__riskwatch__epsilon__Sybase.csv',
                               '__bns__var_rw__data__riskwatch__epsilon__Sybase_Asia.csv',])




elif session == 'algo':
    
    #in folder + out folder
    parent_folder = 'C:/Users/bwu/Desktop/Shared/RW/Algo Session/dynamic.20160721/'
    in_folder = parent_folder + 'input/UDS'
    out_folder = parent_folder + 'all/'
    out_file = 'deals.csv'
    out_audit_file = 'deals_audit.csv'
    
    list_filenames_to_skip = (['exclude/cpty_excludes.cfg'
                            'exclude/cpty_excludes_imm.cfg'
                            'exclude/credit_rating_exclude.cfg'
                            'exclude/trade_exclusion.csv'])

#make sure we have the folder
try:
    os.stat(out_folder[:-1])
except:
    os.mkdir(out_folder[:-1])

#output files
f_out = open(out_folder + out_file,'w')
f_audit_out = open(out_folder + out_audit_file,'w')

for (dirpath, dirnames, filenames) in os.walk(in_folder):
    this_dirpath = dirpath.replace('\\','/')
    this_dir = dirpath[len(in_folder):].replace('\\','/')
    
    for filename in [f for f in filenames if f not in list_filenames_to_skip]:
        #only grab files with the inclusion date
        #if included_date in filename:
        #CTR_filelist.extend(filename)
        #f.write(str(this_dir) + '/' + str(filename) + '\n') # python will convert \n to os.linesep
        this_dirfile = this_dir + '/' + filename 
        this_dirfilepath = this_dirpath + '/' + filename
        line_cnt_infile = 1
        print this_dirfile
        
        f_in = open(this_dirfilepath,'r')
        for line in f_in:
            f_out.write(line.strip() + '\n')
            f_audit_out.write(this_dirfile + ',' + str(line_cnt_infile) + '\n')
            line_cnt_infile += 1
        f_in.close()

#close file          
f_out.close()

#done message
print 'done files from ' + str(in_folder) 
print 'wrote to ' + str(out_folder) + str(out_file)

t2 = time.time()
print 'total run = ' + str(t2-t1) + ' sec'

