'''

    Execute a right merge using pd.merge() with revenue and sales to yield a new DataFrame revenue_and_sales.
        Use how='right' and on=['city', 'state'].
    Print the new DataFrame revenue_and_sales. This has been done for you.
    Execute a left merge with sales and managers to yield a new DataFrame sales_and_managers.
        Use how='left', left_on=['city', 'state'], and right_on=['branch', 'state'].
    Print the new DataFrame sales_and_managers. This has been done for you, so hit 'Submit Answer' to see the result!

'''
# Merge revenue and sales: revenue_and_sales
revenue_and_sales = pd.merge(revenue, sales, how='right', on=['city', 'state'])

# Print revenue_and_sales
print(revenue_and_sales)

# Merge sales and managers: sales_and_managers
sales_and_managers = pd.merge(sales, managers, how='left', left_on=['city', 'state'],right_on=['branch', 'state'])

# Print sales_and_managers
print(sales_and_managers)
