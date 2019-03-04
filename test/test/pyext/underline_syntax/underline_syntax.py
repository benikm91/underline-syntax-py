import unittest

from pyext.underline_syntax.underline_syntax import __


class UnderlineSyntax(unittest.TestCase):

    def testAdd(self):
        lambda_syntax = lambda x: x + 5
        underline_syntax = __ + 5
        self.assertEqual(lambda_syntax(2), underline_syntax(2))

    def testTrueDiv(self):
        lambda_syntax = lambda x: x / 5
        underline_syntax = __ / 5
        self.assertEqual(lambda_syntax(2), underline_syntax(2))

    def testDiv(self):
        lambda_syntax = lambda x: x // 5
        underline_syntax = __ // 5
        self.assertEqual(lambda_syntax(2), underline_syntax(2))

    def testAttributeAccess(self):
        class A:
            @property
            def inner(self):
                return "inner"
        lambda_syntax = lambda x: x.inner
        underline_syntax = __.inner.done()
        self.assertEqual(lambda_syntax(A()), underline_syntax(A()))

    def testMethodCall(self):
        class A:
            def inner(self):
                return "inner"
        lambda_syntax = lambda x: x.inner()
        underline_syntax = __.inner()
        self.assertEqual(lambda_syntax(A()), underline_syntax(A()))

    def testMethodCalls(self):
        class A:

            def recursive(self):
                return self

            def inner(self):
                return "inner"

        lambda_syntax = lambda x: x.recursive().recursive().inner()
        underline_syntax = __.recursive().recursive().inner()
        self.assertEqual(lambda_syntax(A()), underline_syntax(A()))

    def testToString(self):
        lambda_syntax = lambda x: str(x)
        underline_syntax = __.__toString__()
        self.assertEqual(lambda_syntax(2), underline_syntax(2))

    def testIndex(self):
        lambda_syntax = lambda x: x['key']
        underline_syntax = __['key']
        self.assertEqual(lambda_syntax({'key': 'value'}), underline_syntax({'key': 'value'}))

    def testEq(self):
        lambda_syntax = lambda x: x == 5
        underline_syntax = __ == 5
        self.assertEqual(lambda_syntax(5), underline_syntax(5))
        self.assertEqual(lambda_syntax(6), underline_syntax(6))
