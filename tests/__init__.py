# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
try:
    from trytond.modules.product_price_list_party_rebate.tests.test_product_price_list_party_rebate import suite
except ImportError:
    from test_product_price_list_party_rebate import suite

__all__ = ['suite']
