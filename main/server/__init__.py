import sys

# this is the BioStar release number
VERSION = '1.2.17'

try:
    import docutils
except ImportError, exc:
    print '(!) unable to import the docutils module'
    print '(!) some functionality may be disabled'
    #sys.exit(-1)