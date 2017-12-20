
class Parser(object):
    """
    Base class for malware config parsers

    DC3-MWCP modules should be named ${name}_malwareconfigparser.py where ${name} the name used
    to invoke the parser.

    Currently, a new parser object is created by the framework for each run().

    Parameters:
        description: brief description
        author: Initials of author
        reporter: reference to current reporter object

    Attributes:
        description: short description
        author: initials of author
        reporter: reference to reporter (malwareconfigreporter) object that executed this parser.
                  Set when parser is created.
    """

    def __init__(self,
                 description='na',
                 author='na',
                 reporter=None
                 ):
        self.description = description
        self.author = author
        self.reporter = reporter

    def run(self):
        """
        Parser execution method.

        All parsers should implement this function which will be called by DC3-MWCP Framework.

        All externally visible operations should be performed through the reporter object.

        """
        pass
