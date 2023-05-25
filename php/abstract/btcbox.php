<?php

namespace ccxt\abstract;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code


abstract class btcbox extends \ccxt\Exchange {
    public function public_get_depth($params = array()) {
        return $this->request('depth', 'public', 'GET', $params, null, null, array());
    }
    public function public_get_orders($params = array()) {
        return $this->request('orders', 'public', 'GET', $params, null, null, array());
    }
    public function public_get_ticker($params = array()) {
        return $this->request('ticker', 'public', 'GET', $params, null, null, array());
    }
    public function private_post_balance($params = array()) {
        return $this->request('balance', 'private', 'POST', $params, null, null, array());
    }
    public function private_post_trade_add($params = array()) {
        return $this->request('trade_add', 'private', 'POST', $params, null, null, array());
    }
    public function private_post_trade_cancel($params = array()) {
        return $this->request('trade_cancel', 'private', 'POST', $params, null, null, array());
    }
    public function private_post_trade_list($params = array()) {
        return $this->request('trade_list', 'private', 'POST', $params, null, null, array());
    }
    public function private_post_trade_view($params = array()) {
        return $this->request('trade_view', 'private', 'POST', $params, null, null, array());
    }
    public function private_post_wallet($params = array()) {
        return $this->request('wallet', 'private', 'POST', $params, null, null, array());
    }
    public function publicGetDepth($params = array()) {
        return $this->request('depth', 'public', 'GET', $params, null, null, array());
    }
    public function publicGetOrders($params = array()) {
        return $this->request('orders', 'public', 'GET', $params, null, null, array());
    }
    public function publicGetTicker($params = array()) {
        return $this->request('ticker', 'public', 'GET', $params, null, null, array());
    }
    public function privatePostBalance($params = array()) {
        return $this->request('balance', 'private', 'POST', $params, null, null, array());
    }
    public function privatePostTradeAdd($params = array()) {
        return $this->request('trade_add', 'private', 'POST', $params, null, null, array());
    }
    public function privatePostTradeCancel($params = array()) {
        return $this->request('trade_cancel', 'private', 'POST', $params, null, null, array());
    }
    public function privatePostTradeList($params = array()) {
        return $this->request('trade_list', 'private', 'POST', $params, null, null, array());
    }
    public function privatePostTradeView($params = array()) {
        return $this->request('trade_view', 'private', 'POST', $params, null, null, array());
    }
    public function privatePostWallet($params = array()) {
        return $this->request('wallet', 'private', 'POST', $params, null, null, array());
    }
}
