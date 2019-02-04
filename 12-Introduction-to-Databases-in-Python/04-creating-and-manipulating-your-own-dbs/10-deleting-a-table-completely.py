'''

    Drop the state_fact table by applying the method .drop() to it and passing it the argument engine (in fact, engine will be the sole argument for every function/method in this exercise!)
    Check to see if state_fact exists via print. Use the .exists() method with engine as the argument.
    Drop all the tables via the metadata using the .drop_all() method.
    Use a print statement to check if the census table exists.

'''
# Drop the state_fact table
state_fact.drop(engine)

# Check to see if state_fact exists
print(state_fact.exists(engine))

# Drop all tables
metadata.drop_all(engine)

# Check to see if census exists
print(census.exists(engine))
