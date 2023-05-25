<?php
namespace ccxt;
use \ccxt\Precise;

// ----------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -----------------------------------------------------------------------------
include_once __DIR__ . '/../base/test_order_book.php';

function test_fetch_order_book($exchange, $skipped_properties, $symbol) {
    $method = 'fetchOrderBook';
    $orderbook = $exchange->fetch_order_book($symbol);
    test_order_book($exchange, $skipped_properties, $method, $orderbook, $symbol);
}
