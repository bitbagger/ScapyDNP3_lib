try:
    from crcmod.crcmod import *
    import crcmod.predefined
except ModuleNotFoundError:
    # Make this backward compatible
    from crcmod import *
    import predefined
__doc__ = crcmod.__doc__
