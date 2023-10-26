import os
import sys

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(root)

# ----------------------------------------------------------------------------

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

# ----------------------------------------------------------------------------
# -*- coding: utf-8 -*-


from ccxt.test.base import test_shared_methods  # noqa E402


def test_position(exchange, skipped_properties, method, entry, symbol, now):
    format = {
        'info': {},
        'symbol': 'XYZ/USDT',
        'timestamp': 1504224000000,
        'datetime': '2017-09-01T00:00:00',
        'initialMargin': exchange.parse_number('1.234'),
        'initialMarginPercentage': exchange.parse_number('0.123'),
        'maintenanceMargin': exchange.parse_number('1.234'),
        'maintenanceMarginPercentage': exchange.parse_number('0.123'),
        'entryPrice': exchange.parse_number('1.234'),
        'notional': exchange.parse_number('1.234'),
        'leverage': exchange.parse_number('1.234'),
        'unrealizedPnl': exchange.parse_number('1.234'),
        'contracts': exchange.parse_number('1'),
        'contractSize': exchange.parse_number('1.234'),
        'marginRatio': exchange.parse_number('1.234'),
        'liquidationPrice': exchange.parse_number('1.234'),
        'markPrice': exchange.parse_number('1.234'),
        'collateral': exchange.parse_number('1.234'),
        'marginMode': 'cross',
        'side': 'long',
        'percentage': exchange.parse_number('1.234'),
    }
    emptyot_allowed_for = ['liquidationPrice', 'initialMargin', 'initialMarginPercentage', 'maintenanceMargin', 'maintenanceMarginPercentage', 'marginRatio']
    test_shared_methods.assert_structure(exchange, skipped_properties, method, entry, format, emptyot_allowed_for)
    test_shared_methods.assert_timestamp_and_datetime(exchange, skipped_properties, method, entry, now)
    test_shared_methods.assert_symbol(exchange, skipped_properties, method, entry, 'symbol', symbol)
    test_shared_methods.assert_in_array(exchange, skipped_properties, method, entry, 'side', ['long', 'short'])
    test_shared_methods.assert_in_array(exchange, skipped_properties, method, entry, 'marginMode', ['cross', 'isolated'])
    test_shared_methods.assert_greater(exchange, skipped_properties, method, entry, 'leverage', '0')
    test_shared_methods.assert_less_or_equal(exchange, skipped_properties, method, entry, 'leverage', '200')
    test_shared_methods.assert_greater(exchange, skipped_properties, method, entry, 'initialMargin', '0')
    test_shared_methods.assert_greater(exchange, skipped_properties, method, entry, 'initialMarginPercentage', '0')
    test_shared_methods.assert_greater(exchange, skipped_properties, method, entry, 'maintenanceMargin', '0')
    test_shared_methods.assert_greater(exchange, skipped_properties, method, entry, 'maintenanceMarginPercentage', '0')
    test_shared_methods.assert_greater(exchange, skipped_properties, method, entry, 'entryPrice', '0')
    test_shared_methods.assert_greater(exchange, skipped_properties, method, entry, 'notional', '0')
    test_shared_methods.assert_greater(exchange, skipped_properties, method, entry, 'contracts', '0')
    test_shared_methods.assert_greater(exchange, skipped_properties, method, entry, 'contractSize', '0')
    test_shared_methods.assert_greater(exchange, skipped_properties, method, entry, 'marginRatio', '0')
    test_shared_methods.assert_greater(exchange, skipped_properties, method, entry, 'liquidationPrice', '0')
    test_shared_methods.assert_greater(exchange, skipped_properties, method, entry, 'markPrice', '0')
    test_shared_methods.assert_greater(exchange, skipped_properties, method, entry, 'collateral', '0')
