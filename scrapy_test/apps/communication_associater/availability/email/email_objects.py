from collections import namedtuple

SearchSpecificEmailMessageRequest = namedtuple('SearchSpecificEmailMessageRequest', 'from_name subject body')

SearchSpecificEmailMessageInstance = namedtuple('SearchSpecificEmailMessageInstance',
                                                'from_address from_name subject body to_address')
