import sys
import docopt
import inspect
import imp

def add_import(module, import_name):
    imported_module = __import__(import_name)
    setattr(module, import_name, imported_module)

current_frame = inspect.currentframe()
caller = inspect.getouterframes(current_frame)[2]
module = inspect.getmodule(caller[0])

if module.__name__ == '__main__':
    caller_module = imp.load_source('__caller__', module.__file__)

    add_import(caller_module, 'os')
    add_import(caller_module, 're')
    add_import(caller_module, 'sys')
    add_import(caller_module, 'functools')
    add_import(caller_module, 'itertools')
    add_import(caller_module, 'logging')

    main_func = caller_module.main
    args = docopt.docopt(caller_module.__doc__)

    if '--verbose' in args:
        import logging
        if args['--verbose']:
            logging.basicConfig(level = logging.INFO)
        else:
            logging.basicConfig(level = logging.WARN)

    sys.exit(main_func(args))

