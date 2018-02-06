# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class ProductPriceListPartyRebateTestCase(ModuleTestCase):
    'Test Product Price List Party Rebate module'
    module = 'product_price_list_party_rebate'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            ProductPriceListPartyRebateTestCase))
    return suite
