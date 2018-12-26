# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from decimal import Decimal

from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['Party']


class Party:
    __metaclass__ = PoolMeta
    __name__ = 'party.party'

    rebate = fields.Numeric('Rebate', digits=(16, 2),
        domain=[
            ('rebate', '>=', 0),
            ('rebate', '<=', 100),
            ],
        help='Rebate negotiated: percentage expressed '
        'by a number between 0 and 100')

    @classmethod
    def default_rebate(cls):
        return Decimal(0)
