from timeit import timeit

setup_list = 'collection = list(range(10_000))'
setup_set = 'collection = set(range(10_000))'
statement = '300 in collection'

result_list = timeit(setup=setup_list, stmt=statement)
result_set = timeit(setup=setup_set, stmt=statement)

print(f'item check in list took {result_list}ms')
print(f'item check in set took {result_set}ms')
