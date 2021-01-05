
# An example of dictionary of tuples as keys
corona_data = {
    ('2021-01-01',  'United States'): 20128693,
    ('2021-01-02',  'United States'): 20426184,
    ('2021-01-03',  'United States'): 20636663
    }

corona_data['United States']

corona_data['2021-01-01']

corona_data[('2021-01-02', 'United States')]

corona_data[('United States', '2021-01-02')]

# An example of a dicionary of tuples as keys and lists as values
corona_data1 = {
    ('2021-01-01',  'United States'): [20128693, 347788],
    ('2021-01-02',  'United States'): [20426184, 350186],
    ('2021-01-03',  'United States'): [20636663, 351580]
    }

corona_data1[('2021-01-02',  'United States')]
corona_data1[('2021-01-03',  'United States')]
