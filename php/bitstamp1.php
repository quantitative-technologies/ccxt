<?php

namespace ccxt;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

use Exception; // a common import
use \ccxt\ExchangeError;
use \ccxt\BadSymbol;

class bitstamp1 extends Exchange {

    public function describe() {
        return $this->deep_extend(parent::describe (), array(
            'id' => 'bitstamp1',
            'name' => 'Bitstamp',
            'countries' => array( 'GB' ),
            'rateLimit' => 1000,
            'version' => 'v1',
            'has' => array(
                'CORS' => true,
                'spot' => true,
                'margin' => false,
                'swap' => false,
                'future' => false,
                'option' => false,
                'addMargin' => false,
                'cancelOrder' => true,
                'createOrder' => true,
                'createReduceOnlyOrder' => false,
                'createStopLimitOrder' => false,
                'createStopMarketOrder' => false,
                'createStopOrder' => false,
                'fetchBalance' => true,
                'fetchBorrowRate' => false,
                'fetchBorrowRateHistories' => false,
                'fetchBorrowRateHistory' => false,
                'fetchBorrowRates' => false,
                'fetchBorrowRatesPerSymbol' => false,
                'fetchFundingHistory' => false,
                'fetchFundingRate' => false,
                'fetchFundingRateHistory' => false,
                'fetchFundingRates' => false,
                'fetchIndexOHLCV' => false,
                'fetchLeverage' => false,
                'fetchMarginMode' => false,
                'fetchMarkOHLCV' => false,
                'fetchMyTrades' => true,
                'fetchOpenInterestHistory' => false,
                'fetchOrder' => null,
                'fetchOrderBook' => true,
                'fetchPosition' => false,
                'fetchPositionMode' => false,
                'fetchPositions' => false,
                'fetchPositionsRisk' => false,
                'fetchPremiumIndexOHLCV' => false,
                'fetchTicker' => true,
                'fetchTrades' => true,
                'reduceMargin' => false,
                'setLeverage' => false,
                'setMarginMode' => false,
                'setPositionMode' => false,
            ),
            'urls' => array(
                'logo' => 'https://user-images.githubusercontent.com/1294454/27786377-8c8ab57e-5fe9-11e7-8ea4-2b05b6bcceec.jpg',
                'api' => array(
                    'rest' => 'https://www.bitstamp.net/api',
                ),
                'www' => 'https://www.bitstamp.net',
                'doc' => 'https://www.bitstamp.net/api',
            ),
            'requiredCredentials' => array(
                'apiKey' => true,
                'secret' => true,
                'uid' => true,
            ),
            'api' => array(
                'public' => array(
                    'get' => array(
                        'ticker',
                        'ticker_hour',
                        'order_book',
                        'transactions',
                        'eur_usd',
                    ),
                ),
                'private' => array(
                    'post' => array(
                        'balance',
                        'user_transactions',
                        'open_orders',
                        'order_status',
                        'cancel_order',
                        'cancel_all_orders',
                        'buy',
                        'sell',
                        'bitcoin_deposit_address',
                        'unconfirmed_btc',
                        'ripple_withdrawal',
                        'ripple_address',
                        'withdrawal_requests',
                        'bitcoin_withdrawal',
                    ),
                ),
            ),
            'precisionMode' => TICK_SIZE,
            'markets' => array(
                'BTC/USD' => array( 'id' => 'btcusd', 'symbol' => 'BTC/USD', 'base' => 'BTC', 'quote' => 'USD', 'baseId' => 'btc', 'quoteId' => 'usd', 'maker' => 0.005, 'taker' => 0.005, 'type' => 'spot', 'spot' => true ),
                'BTC/EUR' => array( 'id' => 'btceur', 'symbol' => 'BTC/EUR', 'base' => 'BTC', 'quote' => 'EUR', 'baseId' => 'btc', 'quoteId' => 'eur', 'maker' => 0.005, 'taker' => 0.005, 'type' => 'spot', 'spot' => true ),
                'EUR/USD' => array( 'id' => 'eurusd', 'symbol' => 'EUR/USD', 'base' => 'EUR', 'quote' => 'USD', 'baseId' => 'eur', 'quoteId' => 'usd', 'maker' => 0.005, 'taker' => 0.005, 'type' => 'spot', 'spot' => true ),
                'XRP/USD' => array( 'id' => 'xrpusd', 'symbol' => 'XRP/USD', 'base' => 'XRP', 'quote' => 'USD', 'baseId' => 'xrp', 'quoteId' => 'usd', 'maker' => 0.005, 'taker' => 0.005, 'type' => 'spot', 'spot' => true ),
                'XRP/EUR' => array( 'id' => 'xrpeur', 'symbol' => 'XRP/EUR', 'base' => 'XRP', 'quote' => 'EUR', 'baseId' => 'xrp', 'quoteId' => 'eur', 'maker' => 0.005, 'taker' => 0.005, 'type' => 'spot', 'spot' => true ),
                'XRP/BTC' => array( 'id' => 'xrpbtc', 'symbol' => 'XRP/BTC', 'base' => 'XRP', 'quote' => 'BTC', 'baseId' => 'xrp', 'quoteId' => 'btc', 'maker' => 0.005, 'taker' => 0.005, 'type' => 'spot', 'spot' => true ),
                'LTC/USD' => array( 'id' => 'ltcusd', 'symbol' => 'LTC/USD', 'base' => 'LTC', 'quote' => 'USD', 'baseId' => 'ltc', 'quoteId' => 'usd', 'maker' => 0.005, 'taker' => 0.005, 'type' => 'spot', 'spot' => true ),
                'LTC/EUR' => array( 'id' => 'ltceur', 'symbol' => 'LTC/EUR', 'base' => 'LTC', 'quote' => 'EUR', 'baseId' => 'ltc', 'quoteId' => 'eur', 'maker' => 0.005, 'taker' => 0.005, 'type' => 'spot', 'spot' => true ),
                'LTC/BTC' => array( 'id' => 'ltcbtc', 'symbol' => 'LTC/BTC', 'base' => 'LTC', 'quote' => 'BTC', 'baseId' => 'ltc', 'quoteId' => 'btc', 'maker' => 0.005, 'taker' => 0.005, 'type' => 'spot', 'spot' => true ),
                'ETH/USD' => array( 'id' => 'ethusd', 'symbol' => 'ETH/USD', 'base' => 'ETH', 'quote' => 'USD', 'baseId' => 'eth', 'quoteId' => 'usd', 'maker' => 0.005, 'taker' => 0.005, 'type' => 'spot', 'spot' => true ),
                'ETH/EUR' => array( 'id' => 'etheur', 'symbol' => 'ETH/EUR', 'base' => 'ETH', 'quote' => 'EUR', 'baseId' => 'eth', 'quoteId' => 'eur', 'maker' => 0.005, 'taker' => 0.005, 'type' => 'spot', 'spot' => true ),
                'ETH/BTC' => array( 'id' => 'ethbtc', 'symbol' => 'ETH/BTC', 'base' => 'ETH', 'quote' => 'BTC', 'baseId' => 'eth', 'quoteId' => 'btc', 'maker' => 0.005, 'taker' => 0.005, 'type' => 'spot', 'spot' => true ),
            ),
        ));
    }

    public function fetch_order_book($symbol, $limit = null, $params = array ()) {
        /**
         * fetches information on open orders with bid (buy) and ask (sell) prices, volumes and other data
         * @param {string} $symbol unified $symbol of the market to fetch the order book for
         * @param {int|float|null} $limit the maximum amount of order book entries to return
         * @param {array} $params extra parameters specific to the bitstamp1 api endpoint
         * @return {array} A dictionary of {@link https://docs.ccxt.com/en/latest/manual.html#order-book-structure order book structures} indexed by market symbols
         */
        if ($symbol !== 'BTC/USD') {
            throw new ExchangeError($this->id . ' ' . $this->version . " fetchOrderBook doesn't support " . $symbol . ', use it for BTC/USD only');
        }
        $this->load_markets();
        $orderbook = $this->publicGetOrderBook ($params);
        $timestamp = $this->safe_timestamp($orderbook, 'timestamp');
        return $this->parse_order_book($orderbook, $symbol, $timestamp);
    }

    public function parse_ticker($ticker, $market = null) {
        //
        // {
        //     "volume" => "2836.47827985",
        //     "last" => "36544.93",
        //     "timestamp" => "1643372072",
        //     "bid" => "36535.79",
        //     "vwap":"36594.20",
        //     "high" => "37534.15",
        //     "low" => "35511.32",
        //     "ask" => "36548.47",
        //     "open" => 37179.62
        // }
        //
        $symbol = $this->safe_symbol(null, $market);
        $timestamp = $this->safe_timestamp($ticker, 'timestamp');
        $vwap = $this->safe_string($ticker, 'vwap');
        $baseVolume = $this->safe_string($ticker, 'volume');
        $quoteVolume = Precise::string_mul($baseVolume, $vwap);
        $last = $this->safe_string($ticker, 'last');
        return $this->safe_ticker(array(
            'symbol' => $symbol,
            'timestamp' => $timestamp,
            'datetime' => $this->iso8601($timestamp),
            'high' => $this->safe_string($ticker, 'high'),
            'low' => $this->safe_string($ticker, 'low'),
            'bid' => $this->safe_string($ticker, 'bid'),
            'bidVolume' => null,
            'ask' => $this->safe_string($ticker, 'ask'),
            'askVolume' => null,
            'vwap' => $vwap,
            'open' => $this->safe_string($ticker, 'open'),
            'close' => $last,
            'last' => $last,
            'previousClose' => null,
            'change' => null,
            'percentage' => null,
            'average' => null,
            'baseVolume' => $baseVolume,
            'quoteVolume' => $quoteVolume,
            'info' => $ticker,
        ), $market);
    }

    public function fetch_ticker($symbol, $params = array ()) {
        /**
         * fetches a price $ticker, a statistical calculation with the information calculated over the past 24 hours for a specific $market
         * @param {string} $symbol unified $symbol of the $market to fetch the $ticker for
         * @param {array} $params extra parameters specific to the bitstamp1 api endpoint
         * @return {array} a {@link https://docs.ccxt.com/en/latest/manual.html#$ticker-structure $ticker structure}
         */
        if ($symbol !== 'BTC/USD') {
            throw new ExchangeError($this->id . ' ' . $this->version . " fetchTicker doesn't support " . $symbol . ', use it for BTC/USD only');
        }
        $this->load_markets();
        $market = $this->market($symbol);
        $ticker = $this->publicGetTicker ($params);
        //
        // {
        //     "volume" => "2836.47827985",
        //     "last" => "36544.93",
        //     "timestamp" => "1643372072",
        //     "bid" => "36535.79",
        //     "vwap":"36594.20",
        //     "high" => "37534.15",
        //     "low" => "35511.32",
        //     "ask" => "36548.47",
        //     "open" => 37179.62
        // }
        //
        return $this->parse_ticker($ticker, $market);
    }

    public function parse_trade($trade, $market = null) {
        $timestamp = $this->safe_timestamp_2($trade, 'date', 'datetime');
        $side = ($trade['type'] === 0) ? 'buy' : 'sell';
        $orderId = $this->safe_string($trade, 'order_id');
        $id = $this->safe_string($trade, 'tid');
        $price = $this->safe_string($trade, 'price');
        $amount = $this->safe_string($trade, 'amount');
        $marketId = $this->safe_string($trade, 'currency_pair');
        $market = $this->safe_market($marketId, $market);
        return $this->safe_trade(array(
            'id' => $id,
            'info' => $trade,
            'timestamp' => $timestamp,
            'datetime' => $this->iso8601($timestamp),
            'symbol' => $market['symbol'],
            'order' => $orderId,
            'type' => null,
            'side' => $side,
            'takerOrMaker' => null,
            'price' => $price,
            'amount' => $amount,
            'cost' => null,
            'fee' => null,
        ), $market);
    }

    public function fetch_trades($symbol, $since = null, $limit = null, $params = array ()) {
        /**
         * get the list of most recent trades for a particular $symbol
         * @param {string} $symbol unified $symbol of the $market to fetch trades for
         * @param {int|float|null} $since timestamp in ms of the earliest trade to fetch
         * @param {int|float|null} $limit the maximum amount of trades to fetch
         * @param {array} $params extra parameters specific to the bitstamp1 api endpoint
         * @return {[array]} a list of ~@link https://docs.ccxt.com/en/latest/manual.html?#public-trades trade structures~
         */
        if ($symbol !== 'BTC/USD') {
            throw new BadSymbol($this->id . ' ' . $this->version . " fetchTrades doesn't support " . $symbol . ', use it for BTC/USD only');
        }
        $this->load_markets();
        $market = $this->market($symbol);
        $request = array(
            'time' => 'minute',
        );
        $response = $this->publicGetTransactions (array_merge($request, $params));
        return $this->parse_trades($response, $market, $since, $limit);
    }

    public function parse_balance($response) {
        $result = array( 'info' => $response );
        $codes = is_array($this->currencies) ? array_keys($this->currencies) : array();
        for ($i = 0; $i < count($codes); $i++) {
            $code = $codes[$i];
            $currency = $this->currency($code);
            $currencyId = $currency['id'];
            $account = $this->account();
            $account['free'] = $this->safe_string($response, $currencyId . '_available');
            $account['used'] = $this->safe_string($response, $currencyId . '_reserved');
            $account['total'] = $this->safe_string($response, $currencyId . '_balance');
            $result[$code] = $account;
        }
        return $this->safe_balance($result);
    }

    public function fetch_balance($params = array ()) {
        /**
         * query for balance and get the amount of funds available for trading or funds locked in orders
         * @param {array} $params extra parameters specific to the bitstamp1 api endpoint
         * @return {array} a ~@link https://docs.ccxt.com/en/latest/manual.html?#balance-structure balance structure~
         */
        $response = $this->privatePostBalance ($params);
        return $this->parse_balance($response);
    }

    public function create_order($symbol, $type, $side, $amount, $price = null, $params = array ()) {
        /**
         * create a trade order
         * @param {string} $symbol unified $symbol of the market to create an order in
         * @param {string} $type 'market' or 'limit'
         * @param {string} $side 'buy' or 'sell'
         * @param {int|float} $amount how much of currency you want to trade in units of base currency
         * @param {int|float|null} $price the $price at which the order is to be fullfilled, in units of the quote currency, ignored in market orders
         * @param {array} $params extra parameters specific to the bitstamp1 api endpoint
         * @return {array} an {@link https://docs.ccxt.com/en/latest/manual.html#order-structure order structure}
         */
        if ($type !== 'limit') {
            throw new ExchangeError($this->id . ' ' . $this->version . ' accepts limit orders only');
        }
        if ($symbol !== 'BTC/USD') {
            throw new ExchangeError($this->id . ' v1 supports BTC/USD orders only');
        }
        $this->load_markets();
        $method = 'privatePost' . $this->capitalize($side);
        $request = array(
            'amount' => $amount,
            'price' => $price,
        );
        $response = $this->$method (array_merge($request, $params));
        $id = $this->safe_string($response, 'id');
        return array(
            'info' => $response,
            'id' => $id,
        );
    }

    public function cancel_order($id, $symbol = null, $params = array ()) {
        /**
         * cancels an open order
         * @param {string} $id order $id
         * @param {string|null} $symbol unified $symbol of the market the order was made in
         * @param {array} $params extra parameters specific to the bitstamp1 api endpoint
         * @return {array} An {@link https://docs.ccxt.com/en/latest/manual.html#order-structure order structure}
         */
        return $this->privatePostCancelOrder (array( 'id' => $id ));
    }

    public function parse_order_status($status) {
        $statuses = array(
            'In Queue' => 'open',
            'Open' => 'open',
            'Finished' => 'closed',
            'Canceled' => 'canceled',
        );
        return $this->safe_string($statuses, $status, $status);
    }

    public function fetch_order_status($id, $symbol = null, $params = array ()) {
        $this->load_markets();
        $request = array(
            'id' => $id,
        );
        $response = $this->privatePostOrderStatus (array_merge($request, $params));
        return $this->parse_order_status($response);
    }

    public function fetch_my_trades($symbol = null, $since = null, $limit = null, $params = array ()) {
        /**
         * fetch all trades made by the user
         * @param {string|null} $symbol unified $market $symbol
         * @param {int|float|null} $since the earliest time in ms to fetch trades for
         * @param {int|float|null} $limit the maximum number of trades structures to retrieve
         * @param {array} $params extra parameters specific to the bitstamp1 api endpoint
         * @return {[array]} a list of {@link https://docs.ccxt.com/en/latest/manual.html#trade-structure trade structures}
         */
        $this->load_markets();
        $market = null;
        if ($symbol !== null) {
            $market = $this->market($symbol);
        }
        $pair = $market ? $market['id'] : 'all';
        $request = array(
            'id' => $pair,
        );
        $response = $this->privatePostOpenOrdersId (array_merge($request, $params));
        return $this->parse_trades($response, $market, $since, $limit);
    }

    public function sign($path, $api = 'public', $method = 'GET', $params = array (), $headers = null, $body = null) {
        $url = $this->urls['api']['rest'] . '/' . $this->implode_params($path, $params);
        $query = $this->omit($params, $this->extract_params($path));
        if ($api === 'public') {
            if ($query) {
                $url .= '?' . $this->urlencode($query);
            }
        } else {
            $this->check_required_credentials();
            $nonce = (string) $this->nonce();
            $auth = $nonce . $this->uid . $this->apiKey;
            $signature = $this->encode($this->hmac($this->encode($auth), $this->encode($this->secret)));
            $query = array_merge(array(
                'key' => $this->apiKey,
                'signature' => strtoupper($signature),
                'nonce' => $nonce,
            ), $query);
            $body = $this->urlencode($query);
            $headers = array(
                'Content-Type' => 'application/x-www-form-urlencoded',
            );
        }
        return array( 'url' => $url, 'method' => $method, 'body' => $body, 'headers' => $headers );
    }

    public function handle_errors($httpCode, $reason, $url, $method, $headers, $body, $response, $requestHeaders, $requestBody) {
        if ($response === null) {
            return;
        }
        $status = $this->safe_string($response, 'status');
        if ($status === 'error') {
            throw new ExchangeError($this->id . ' ' . $this->json($response));
        }
    }
}
