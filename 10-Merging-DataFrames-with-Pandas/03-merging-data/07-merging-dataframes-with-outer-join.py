'''

    Merge sales_and_managers with revenue_and_sales. Store the result as merge_default.
    Print merge_default. This has been done for you.
    Merge sales_and_managers with revenue_and_sales using how='outer'. Store the result as merge_outer.
    Print merge_outer. This has been done for you.
    Merge sales_and_managers with revenue_and_sales only on ['city','state'] using an outer join. Store the result as merge_outer_on and hit 'Submit Answer' to see what the merged DataFrames look like!

'''
# Perform the first merge: merge_default
merge_default = pd.merge(sales_and_managers, revenue_and_sales)

# Print merge_default
print(merge_default)

# Perform the second merge: merge_outer
merge_outer = pd.merge(sales_and_managers, revenue_and_sales, how='outer')

# Print merge_outer
print(merge_outer)

# Perform the third merge: merge_outer_on
merge_outer_on = pd.merge(sales_and_managers, revenue_and_sales, how='outer', on=['city', 'state'])

# Print merge_outer_on
print(merge_outer_on)
