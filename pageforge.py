import math

def count(input):
    page    = input['page'      ]
    limit   = input['limit'     ]
    records = input['records'   ]

    offset  = (page*limit)-limit
    pages   = math.ceil(records/limit)

    record_min = offset+1

    if page == pages:
        record_max = records
    else:
        record_max = offset+limit

    output = {
        'page':{
            'current':page,
            'all':pages
        },
        'record':{
            'all'   : records,
            'min'   : record_min,
            'max'   : record_max,
        },
        'limit':limit,
        'offset':offset
    }

    return output
