'''

    Import case, cast, and Float from sqlalchemy.
    Build an expression female_pop2000to calculate female population in 2000. To achieve this:
        Use case() inside func.sum().
        The first argument of case() is a list containing a tuple of
            i) A boolean checking that census.columns.sex is equal to 'F'.
            ii) The column census.columns.pop2000.
        The second argument is the else_ condition, which should be set to 0.
    Calculate the total population in 2000 and use cast() to convert it to Float.
    Build a query to calculate the percentage of females in 2000. To do this, divide female_pop2000 by total_pop2000 and multiply by 100.
    Execute the query and print percent_female.

'''
# import case, cast and Float from sqlalchemy
from sqlalchemy import case, cast, Float

# Build an expression to calculate female population in 2000
female_pop2000 = func.sum(
    case([
        (census.columns.sex == 'F', census.columns.pop2000)
    ], else_=0))

# Cast an expression to calculate total population in 2000 to Float
total_pop2000 = cast(func.sum(census.columns.pop2000), Float)

# Build a query to calculate the percentage of females in 2000: stmt
stmt = select([female_pop2000 / total_pop2000* 100])

# Execute the query and store the scalar result: percent_female
percent_female = connection.execute(stmt).scalar()

# Print the percentage
print(percent_female)
