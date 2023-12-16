# pageforge
Python Script for help your pagination.

## Usage

    import pageforge

    result = pageforge.count({'page':6,'limit':10,'records':1432})
    print(result)

Output

    {
      'page': {
        'current': 6,
        'all': 144
      },
      'record': {
        'all': 1432,
        'min': 51,
        'max': 60
      },
      'limit': 10,
      'offset': 50
    }
