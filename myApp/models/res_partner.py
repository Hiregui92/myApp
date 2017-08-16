# coding: utf-8

import datetime
from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    card_ids = fields.One2many(
        'card.line', 'partner_id', string="Attribute Lines")

    card_num = fields.Float(
        compute='_compute_card',
        help="Printing total cost by unit for each product")

    @api.depends('card_ids')
    def _compute_card(self):
        """ Compute the produce price based on the printing price and
        the extra charges value.
        """
        for partner in self:
            partner.card_num = len(partner.card_ids)


class CardLine(models.Model):
    _name = 'card.line'

    partner_id = fields.Many2one('res.partner', required=True)
    card_type_id = fields.Many2one('card.type', required=True)
    description = fields.Text(
        string="Comments",
        help="Additional comments of card to be displayed on"
        " line description")
    available_balance = fields.Float(
        compute='_compute_card_balance',
        help="Balance available on the total credit card - locked")
    total_balance = fields.Float(
        help="Balance available on the total credit card - locked")
    balance_blocked = fields.Float(
        help="Balance available on the total credit card - locked")
    payment_date = fields.Date(default=datetime.datetime.now())
    name = fields.Char(
        required=True,
        string="Card Number",
        help="Card number without - and unique for cards")
    expiration_date = fields.Date(
        required=True,
        default=datetime.datetime.now())

    @api.depends('total_balance', 'balance_blocked')
    def _compute_card_balance(self):
        """ Compute the produce price based on the printing price and
        the extra charges value.
        """
        for card in self:
            card.available_balance = (
                card.total_balance - card.balance_blocked)


class CardType(models.Model):
    _name = 'card.type'

    name = fields.Char(required=True)
