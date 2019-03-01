import unittest

from pyext.underline_syntax.underline_syntax import __


class UnderlineSyntax(unittest.TestCase):

    def testAdd(self):
        lambdaSyntax = lambda x: x + 5
        underlineSyntax = __ + 5
        self.assertEqual(lambdaSyntax(2), underlineSyntax(2))

    def testTrueDiv(self):
        lambdaSyntax = lambda x: x / 5
        underlineSyntax = __ / 5
        self.assertEqual(lambdaSyntax(2), underlineSyntax(2))

    def testDiv(self):
        lambdaSyntax = lambda x: x // 5
        underlineSyntax = __ // 5
        self.assertEqual(lambdaSyntax(2), underlineSyntax(2))

    def testAttributeAccess(self):
        class A:
            @property
            def inner(self):
                return "inner"
        lambdaSyntax = lambda x: x.inner
        underlineSyntax = __.inner.done()
        self.assertEqual(lambdaSyntax(A()), underlineSyntax(A()))

    def testCallMethod(self):
        class A:
            def inner(self):
                return "inner"
        lambdaSyntax = lambda x: x.inner()
        underlineSyntax = __.inner()
        self.assertEqual(lambdaSyntax(A()), underlineSyntax(A()))