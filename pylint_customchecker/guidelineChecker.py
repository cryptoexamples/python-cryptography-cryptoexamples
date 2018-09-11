from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class GuidelineChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'guidelines'
    ONE_DEMONSTRATE = 'one-demonstrate'
    EXAMPLE_PREFIX = 'example-prefix'
    MISSING_LOGGER = 'missing-logger'

    priority = -1
    msgs = {
        'C5000': ('Only one "demonstrate_" method allowed',
                  ONE_DEMONSTRATE,
                  'Refer to guidelines'),
        'C5001': ('Files have to start with "example_"',
                  EXAMPLE_PREFIX,
                  'Refer to guidelines'),
        'C5002': (
            'A logger has to be specified. Should be named "logger" and be available as global variable',
            MISSING_LOGGER,
            'Refer to guidelines')
    }

    options = ()

    def __init__(self, linter=None):
        super(GuidelineChecker, self).__init__(linter)
        self.demonstrate = 0

    def visit_functiondef(self, node):
        # CHECK if only one demonstrate_method exists
        if node.name.startswith('demonstrate_'):
            self.demonstrate += 1
        if self.demonstrate > 1:
            self.add_message(self.ONE_DEMONSTRATE, node=node)

    def visit_module(self, node):
        # reset demonstrate count for each file
        self.demonstrate = 0
        # check filename begins with example_
        if not (node.name.startswith('example_') or node.name.startswith(
                'cryptoexamples.example_')):
            self.add_message(self.EXAMPLE_PREFIX, node=node)
        # check for logger
        if 'logger' not in node.globals:
            self.add_message(self.MISSING_LOGGER, node=node)


def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(GuidelineChecker(linter))
