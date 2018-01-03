# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.

from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['Party']


class Party:
    __metaclass__ = PoolMeta
    __name__ = 'party.party'

    rebate = fields.Numeric('Rebate', digits=(16, 2),
        help='Rebate negociated: percentage exprimed by a number between 0 and 100')

    @classmethod
    def __setup__(cls):
        super(Party, cls).__setup__()
        cls._constraints += [('check_rebate', 'invalid_rebate'),]
        cls._error_messages.update({
            'invalid_rebate': 'Invalid rebate!',
                })

    def check_rebate(self, ids):
        return all(0 <= party.rebate <= 100 for party in self.browse(ids))
