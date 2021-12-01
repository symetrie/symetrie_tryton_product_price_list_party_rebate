# The COPYRIGHT file at the top level of #this repository contains the full
# copyright notices and license terms.

from trytond.pool import PoolMeta

__all__ = ['PriceList']


class PriceList:
    __name__ = 'product.price_list'

    def get_context_formula(self, party, product, unit_price, quantity, uom):
        '''
        Override get_context_formula to add rebate to evaluation context
        '''
        context = super(PriceList, self).get_context_formula(party,
            product, unit_price, quantity, uom)
        context['names']['rebate'] = party.rebate if party else 0
        return context
