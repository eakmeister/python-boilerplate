"""
Usage: test.py [--verbose] [-h] <arg1>

-h, --help  show this
--verbose   enable verbose logging
"""
import boilerplate

def main(args):
    logging.info('args: %s' % args)
    print args['<arg1>'], args['--verbose']

