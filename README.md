A module to reduce the boilerplate required for quick scripts. Before:

```python
    """
    Usage: test.py [--verbose] [-h] <arg1>
    
    -h, --help  show this
    --verbose   enable verbose logging
    """
    import docopt
    import logging
    import sys

    def main():
        args = docopt.docopt(__doc__)
        
        if args['--verbose']:
            logging.basicConfig(level = logging.INFO)
        else:
            logging.basicConfig(level = logging.WARN)

        do_stuff_with_args(args)
    
    if __name__ == '__main__':
        sys.exit(main())
```

After:

```python
    """
    Usage: test.py [--verbose] [-h] <arg1>
    
    -h, --help  show this
    --verbose   enable verbose logging
    """
    import boilerplate

    def main(args):
        do_stuff_with_args(args)
```

This module will automatically import the following modules:
* os
* re
* sys
* functools
* itertools
* logging

