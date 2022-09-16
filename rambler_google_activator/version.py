class Version(object):
    """0.1.2"""

    def __setattr__(self, *args):
        raise TypeError("can't modify immutable instance")
    __delattr__ = __setattr__

    def __init__(self, num):
        super(Version, self).__setattr__('number', num)
