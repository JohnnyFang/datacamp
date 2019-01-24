'''
The DataFrames revenue and managers are displayed in the IPython Shell. Here, they are indexed by 'branch_id'.

Choose the function call below that will join the DataFrames on their indexes and return 5 rows with index labels [10, 20, 30, 31, 47]. Explore each of them in the IPython Shell to get a better understanding of their functionality.
'''
revenue.join(managers, lsuffix='_rev', rsuffix='_mng', how='outer')
