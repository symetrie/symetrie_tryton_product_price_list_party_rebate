# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from . import product
from . import party

__all__ = ['register']


def register():
    Pool.register(
        product.PriceList,
        party.Party,
        module='product_price_list_party_rebate', type_='model')
