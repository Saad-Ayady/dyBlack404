#!/usr/bin/python3

import sys
sys.path.append('lib/')
try :
    import runfile
    runfile.main()
except ImportError as err:
    print(err)