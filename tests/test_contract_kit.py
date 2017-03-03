# This file is part of the contract_kit module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import doctest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import (doctest_setup, doctest_teardown,
    doctest_checker)


class ContractKitTestCase(ModuleTestCase):
    'Test Contract Kit module'
    module = 'contract_kit'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ContractKitTestCase))
    suite.addTests(doctest.DocFileSuite('scenario_contract_kit.rst',
            setUp=doctest_setup, tearDown=doctest_teardown, encoding='utf-8',
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE,
            checker=doctest_checker))
    return suite
