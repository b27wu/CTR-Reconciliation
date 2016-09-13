'''
Created on Feb 23, 2016

@author: mstirling
'''
import pandas as pd
from Map_Rules import apply_map_rule

#control variables
bWriteReport = 1

#in VAR files
in_folder = 'C:/Users/bwu/Desktop/Shared/RW/VAR Session/market.16.08.04/'
in_file_TRS = 'all/ByProduct/out_20160809_deals_BNS_Total_Return_Equity_Swap.csv' 

#in CTR files
map_folder = 'C:/Users/bwu/Desktop/Shared/RW/CTR Files/20160804_DEV/'
map_file = 'map/map_K2_TRS.csv'

#out folder
out_folder = in_folder + 'recon/'
out_file_FX_Deals = 'K2_TRS.csv'

#open in_files
df_TRS = pd.read_csv(in_folder+in_file_TRS)
#print len(df_TRS.index)

#filter 
file_list_in_scope = ['/__bns__derivProdData__riskWatch__ACG13__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__CFHYPO__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__CMGSTRNBIF__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__COVEREDBOND__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__CREDIT__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EMERGINGTRS__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQASIACORP__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITY__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITY__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYASIA__HKD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYASIA__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYD1D__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYD1D__HKD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYD1D__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYD1U__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYD1U__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYDC__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYDS__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYETF__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYFIO__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYFIO__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYFWD__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYFWD__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYIAB__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYILN__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYILN__EUR__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYILN__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYIO__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYLATAM__JPY__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYLATAM__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYSBI__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYSP__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYSP__EUR__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYSPI__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYSPI__EUR__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYSPI__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYSPS__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__EQUITYSSO__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__FLMSTRBIF__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__GPFLATAM__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__GTCBLP__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__GTTRSRSUPSU__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__HEDGEFUND__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__LDNTRS__GBP__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__LOANTRS__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__LOANTRS__EUR__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__LOANTRS__GBP__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__LOANTRS__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__NYFIOPTHEDGE__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__PORTMGMT__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__PORTMGMTCUST__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__PORTMGMTCUST__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__PSLOANHEDGE__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__RETAIL__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__RETAIL__EUR__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__RETAIL__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__RETAILDH__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__RETAILDH__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__SCOTIABANC__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__SCTLFINANCE__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__SERIES1__CAD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__SILHF__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__STRPLACEHDR__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__SWAPS_BOOK__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__SWAPSHEDGE__USD__Sybase_K2.csv',
                      '/__bns__derivProdData__riskWatch__THAIPAIR__USD__Sybase_K2.csv']
df_merge = df_TRS[(df_TRS.Filename.isin(file_list_in_scope))]
df_merge.reset_index(inplace=True,drop=True)
#print len(df_TRS.index)

ID_list = [':TA9624', ':TA9625', ':TB1793', ':TB2195', ':TB2199', ':TB2540', ':TB2895', ':TB2896', ':TB2986', ':TB2987', ':TB3000', ':TB3144', 
':TB3147', ':TB3207', ':TB3220', ':TB3241', ':TB3256', ':TB3297', ':TB3313', ':TB3315', ':TB3322', ':TB3323', ':TB3327', ':TB3338', ':TB3345', ':TB3346', 
':TB3347', ':TB3350', ':TB3351', ':TB3355', ':TB3356', ':TB3371', ':TB3372', ':TB3383', ':TB3396'] 

df_merge = df_merge[df_merge['ID'].isin(ID_list) == False]

#reorder columns
df_merge.sort_index(axis=1,inplace=True)

#open mapping rules
df_map = pd.read_csv(map_folder+map_file)

#apply transformation for alias
#copy alias values to real column and drop alias column
for i in df_map[~df_map['RW Alias'].isnull()].index:
    #assume only 1 alias per column for now
    this_col = str(df_map.at[i,'Column Name'])
    this_alias = str(df_map.at[i,'RW Alias'])
    
    #copy alias values to 'this_col'
    for j in df_merge[~df_merge[this_alias].isnull()].index:
        df_merge.at[j,this_col] = df_merge.at[j,this_alias] 
    
    #drop alias column
    df_merge.drop([this_alias],axis=1,inplace=True)

#now apply 'within-cell' mapping rules
for i in df_map['Column Name'].index:
    this_col = str(df_map.at[i,'Column Name'])
    this_map_rule = str(df_map.at[i,'RW Map Rule'])
    
    #apply the mapping rule if rule 'not nan/blank'
    if not this_map_rule == 'nan':
        for j in df_merge.index:
            df_merge.at[j, this_col] = apply_map_rule(df_merge.at[j, this_col], this_map_rule) 

#sort by Name
df_merge.sort('Name', inplace = True)

#write out_files
df_merge.to_csv(out_folder + out_file_FX_Deals,index=False)

print 'done.'
print 'from ' + in_folder
print 'to ' + out_folder