<?php

namespace ccxt;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

use Exception; // a common import
use \ccxt\ExchangeError;
use \ccxt\ArgumentsRequired;
use \ccxt\OrderNotFound;

class tidebit extends Exchange {

    public function describe() {
        return $this->deep_extend(parent::describe (), array(
            'id' => 'tidebit',
            'name' => 'TideBit',
            'countries' => array( 'HK' ),
            'rateLimit' => 1000,
            'version' => 'v2',
            'has' => array(
                'CORS' => null,
                'spot' => true,
                'margin' => false,
                'swap' => false,
                'future' => false,
                'option' => false,
                'addMargin' => false,
                'cancelOrder' => true,
                'createOrder' => true,
                'createReduceOnlyOrder' => false,
                'fetchBalance' => true,
                'fetchBorrowRate' => false,
                'fetchBorrowRateHistories' => false,
                'fetchBorrowRateHistory' => false,
                'fetchBorrowRates' => false,
                'fetchBorrowRatesPerSymbol' => false,
                'fetchDepositAddress' => true,
                'fetchFundingHistory' => false,
                'fetchFundingRate' => false,
                'fetchFundingRateHistory' => false,
                'fetchFundingRates' => false,
                'fetchIndexOHLCV' => false,
                'fetchLeverage' => false,
                'fetchLeverageTiers' => false,
                'fetchMarginMode' => false,
                'fetchMarkets' => true,
                'fetchMarkOHLCV' => false,
                'fetchOHLCV' => true,
                'fetchOpenInterestHistory' => false,
                'fetchOrderBook' => true,
                'fetchPosition' => false,
                'fetchPositionMode' => false,
                'fetchPositions' => false,
                'fetchPositionsRisk' => false,
                'fetchPremiumIndexOHLCV' => false,
                'fetchTicker' => true,
                'fetchTickers' => true,
                'fetchTrades' => true,
                'fetchTradingFee' => false,
                'fetchTradingFees' => false,
                'reduceMargin' => false,
                'setLeverage' => false,
                'setMarginMode' => false,
                'setPositionMode' => false,
                'withdraw' => true,
            ),
            'timeframes' => array(
                '1m' => '1',
                '5m' => '5',
                '15m' => '15',
                '30m' => '30',
                '1h' => '60',
                '2h' => '120',
                '4h' => '240',
                '12h' => '720',
                '1d' => '1440',
                '3d' => '4320',
                '1w' => '10080',
            ),
            'urls' => array(
                'logo' => 'https://user-images.githubusercontent.com/51840849/87460811-1e690280-c616-11ea-8652-69f187305add.jpg',
                'api' => array(
                    'rest' => 'https://www.tidebit.com',
                ),
                'www' => 'https://www.tidebit.com',
                'doc' => array(
                    'https://www.tidebit.com/documents/api/guide',
                    'https://www.tidebit.com/swagger/#/default',
                ),
                'referral' => 'http://bit.ly/2IX0LrM',
            ),
            'api' => array(
                'public' => array(
                    'get' => array(
                        'markets',
                        'tickers',
                        'tickers/{market}',
                        'timestamp',
                        'trades',
                        'trades/{market}',
                        'order_book',
                        'order',
                        'k_with_pending_trades',
                        'k',
                        'depth',
                    ),
                    'post' => array(),
                ),
                'private' => array(
                    'get' => array(
                        'addresses/{address}',
                        'deposits/history',
                        'deposits/get_deposit',
                        'deposits/deposit_address',
                        'historys/orders',
                        'historys/vouchers',
                        'historys/accounts',
                        'historys/snapshots',
                        'linkage/get_status',
                        'members/me',
                        'order',
                        'orders',
                        'partners/orders/{id}/trades',
                        'referral_commissions/get_undeposited',
                        'referral_commissions/get_graph_data',
                        'trades/my',
                        'withdraws/bind_account_list',
                        'withdraws/get_withdraw_account',
                        'withdraws/fetch_bind_info',
                    ),
                    'post' => array(
                        'deposits/deposit_cash',
                        'favorite_markets/update',
                        'order/delete',
                        'orders',
                        'orders/multi',
                        'orders/clear',
                        'referral_commissions/deposit',
                        'withdraws/apply',
                        'withdraws/bind_bank',
                        'withdraws/bind_address',
                    ),
                ),
            ),
            'fees' => array(
                'trading' => array(
                    'tierBased' => false,
                    'percentage' => true,
                    'maker' => $this->parse_number('0.003'),
                    'taker' => $this->parse_number('0.003'),
                ),
                'funding' => array(
                    'tierBased' => false,
                    'percentage' => true,
                    'withdraw' => array(), // There is only 1% fee on withdrawals to your bank account.
                ),
            ),
            'precisionMode' => TICK_SIZE,
            'exceptions' => array(
                '2002' => '\\ccxt\\InsufficientFunds',
                '2003' => '\\ccxt\\OrderNotFound',
            ),
        ));
    }

    public function fetch_deposit_address($code, $params = array ()) {
        /**
         * fetch the deposit $address for a $currency associated with this account
         * @param {string} $code unified $currency $code
         * @param {array} $params extra parameters specific to the tidebit api endpoint
         * @return {array} an {@link https://docs.ccxt.com/en/latest/manual.html#$address-structure $address structure}
         */
        $this->load_markets();
        $currency = $this->currency($code);
        $request = array(
            'currency' => $currency['id'],
        );
        $response = $this->privateGetDepositAddress (array_merge($request, $params));
        if (is_array($response) && array_key_exists('success', $response)) {
            if ($response['success']) {
                $address = $this->safe_string($response, 'address');
                $tag = $this->safe_string($response, 'addressTag');
                return array(
                    'currency' => $code,
                    'address' => $this->check_address($address),
                    'tag' => $tag,
                    'info' => $response,
                );
            }
        }
    }

    public function fetch_markets($params = array ()) {
        /**
         * retrieves data on all markets for tidebit
         * @param {array} $params extra parameters specific to the exchange api endpoint
         * @return {[array]} an array of objects representing $market data
         */
        $response = $this->publicGetMarkets ($params);
        //
        //    [
        //        array(
        //            "id" => "btchkd",
        //            "name" => "BTC/HKD",
        //            "bid_fixed" => "2",
        //            "ask_fixed" => "4",
        //            "price_group_fixed" => null
        //        ),
        //        array(
        //            "id" => "btcusdt",
        //            "name" => "BTC/USDT",
        //            "bid_fixed" => "2",
        //            "ask_fixed" => "3",
        //            "price_group_fixed" => null
        //        ),
        // }
        //
        $result = array();
        for ($i = 0; $i < count($response); $i++) {
            $market = $response[$i];
            $id = $this->safe_string($market, 'id');
            $symbol = $this->safe_string($market, 'name');
            list($baseId, $quoteId) = explode('/', $symbol);
            $result[] = array(
                'id' => $id,
                'symbol' => $symbol,
                'base' => $this->safe_currency_code($baseId),
                'quote' => $this->safe_currency_code($quoteId),
                'settle' => null,
                'baseId' => $baseId,
                'quoteId' => $quoteId,
                'settleId' => null,
                'type' => 'spot',
                'spot' => true,
                'margin' => false,
                'swap' => false,
                'future' => false,
                'option' => false,
                'active' => null,
                'contract' => false,
                'linear' => null,
                'inverse' => null,
                'contractSize' => null,
                'expiry' => null,
                'expiryDatetime' => null,
                'strike' => null,
                'optionType' => null,
                'precision' => array(
                    'amount' => $this->parse_number($this->parse_precision($this->safe_string($market, 'ask_fixed'))),
                    'price' => $this->parse_number($this->parse_precision($this->safe_string($market, 'bid_fixed'))),
                ),
                'limits' => array_merge(array(
                    'leverage' => array(
                        'min' => null,
                        'max' => null,
                    ),
                ), $this->limits),
                'info' => $market,
            );
        }
        return $result;
    }

    public function parse_balance($response) {
        $balances = $this->safe_value($response, 'accounts', array());
        $result = array( 'info' => $balances );
        for ($i = 0; $i < count($balances); $i++) {
            $balance = $balances[$i];
            $currencyId = $this->safe_string($balance, 'currency');
            $code = $this->safe_currency_code($currencyId);
            $account = $this->account();
            $account['free'] = $this->safe_string($balance, 'balance');
            $account['used'] = $this->safe_string($balance, 'locked');
            $result[$code] = $account;
        }
        return $this->safe_balance($result);
    }

    public function fetch_balance($params = array ()) {
        /**
         * query for balance and get the amount of funds available for trading or funds locked in orders
         * @param {array} $params extra parameters specific to the tidebit api endpoint
         * @return {array} a ~@link https://docs.ccxt.com/en/latest/manual.html?#balance-structure balance structure~
         */
        $this->load_markets();
        $response = $this->privateGetMembersMe ($params);
        return $this->parse_balance($response);
    }

    public function fetch_order_book($symbol, $limit = null, $params = array ()) {
        /**
         * fetches information on open orders with bid (buy) and ask (sell) prices, volumes and other data
         * @param {string} $symbol unified $symbol of the $market to fetch the order book for
         * @param {int|float|null} $limit the maximum amount of order book entries to return
         * @param {array} $params extra parameters specific to the tidebit api endpoint
         * @return {array} A dictionary of {@link https://docs.ccxt.com/en/latest/manual.html#order-book-structure order book structures} indexed by $market symbols
         */
        $this->load_markets();
        $market = $this->market($symbol);
        $request = array(
            'market' => $market['id'],
        );
        if ($limit !== null) {
            $request['limit'] = $limit; // default = 300
        }
        $request['market'] = $market['id'];
        $response = $this->publicGetDepth (array_merge($request, $params));
        $timestamp = $this->safe_timestamp($response, 'timestamp');
        return $this->parse_order_book($response, $symbol, $timestamp);
    }

    public function parse_ticker($ticker, $market = null) {
        //
        //     {
        //         "at":1398410899,
        //         "ticker" => {
        //             "buy" => "3000.0",
        //             "sell":"3100.0",
        //             "low":"3000.0",
        //             "high":"3000.0",
        //             "last":"3000.0",
        //             "vol":"0.11"
        //         }
        //     }
        //
        $timestamp = $this->safe_timestamp($ticker, 'at');
        $ticker = $this->safe_value($ticker, 'ticker', array());
        $market = $this->safe_market(null, $market);
        $last = $this->safe_string($ticker, 'last');
        return $this->safe_ticker(array(
            'symbol' => $market['symbol'],
            'timestamp' => $timestamp,
            'datetime' => $this->iso8601($timestamp),
            'high' => $this->safe_string($ticker, 'high'),
            'low' => $this->safe_string($ticker, 'low'),
            'bid' => $this->safe_string($ticker, 'buy'),
            'ask' => $this->safe_string($ticker, 'sell'),
            'bidVolume' => null,
            'askVolume' => null,
            'vwap' => null,
            'open' => null,
            'close' => $last,
            'last' => $last,
            'change' => null,
            'percentage' => null,
            'previousClose' => null,
            'average' => null,
            'baseVolume' => $this->safe_string($ticker, 'vol'),
            'quoteVolume' => null,
            'info' => $ticker,
        ), $market);
    }

    public function fetch_tickers($symbols = null, $params = array ()) {
        /**
         * fetches price $tickers for multiple markets, statistical calculations with the information calculated over the past 24 hours each $market
         * @param {[string]|null} $symbols unified $symbols of the markets to fetch the $ticker for, all $market $tickers are returned if not assigned
         * @param {array} $params extra parameters specific to the tidebit api endpoint
         * @return {array} an array of {@link https://docs.ccxt.com/en/latest/manual.html#$ticker-structure $ticker structures}
         */
        $this->load_markets();
        $tickers = $this->publicGetTickers ($params);
        $ids = is_array($tickers) ? array_keys($tickers) : array();
        $result = array();
        for ($i = 0; $i < count($ids); $i++) {
            $id = $ids[$i];
            $market = $this->safe_market($id);
            $symbol = $market['symbol'];
            $ticker = $tickers[$id];
            $result[$symbol] = $this->parse_ticker($ticker, $market);
        }
        return $this->filter_by_array($result, 'symbol', $symbols);
    }

    public function fetch_ticker($symbol, $params = array ()) {
        /**
         * fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific $market
         * @param {string} $symbol unified $symbol of the $market to fetch the ticker for
         * @param {array} $params extra parameters specific to the tidebit api endpoint
         * @return {array} a {@link https://docs.ccxt.com/en/latest/manual.html#ticker-structure ticker structure}
         */
        $this->load_markets();
        $market = $this->market($symbol);
        $request = array(
            'market' => $market['id'],
        );
        $response = $this->publicGetTickersMarket (array_merge($request, $params));
        //
        //     {
        //         "at":1398410899,
        //         "ticker" => {
        //             "buy" => "3000.0",
        //             "sell":"3100.0",
        //             "low":"3000.0",
        //             "high":"3000.0",
        //             "last":"3000.0",
        //             "vol":"0.11"
        //         }
        //     }
        //
        return $this->parse_ticker($response, $market);
    }

    public function parse_trade($trade, $market = null) {
        $timestamp = $this->parse8601($this->safe_string($trade, 'created_at'));
        $id = $this->safe_string($trade, 'id');
        $price = $this->safe_string($trade, 'price');
        $amount = $this->safe_string($trade, 'volume');
        $market = $this->safe_market(null, $market);
        return $this->safe_trade(array(
            'id' => $id,
            'info' => $trade,
            'timestamp' => $timestamp,
            'datetime' => $this->iso8601($timestamp),
            'symbol' => $market['symbol'],
            'type' => null,
            'side' => null,
            'order' => null,
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
         * @param {array} $params extra parameters specific to the tidebit api endpoint
         * @return {[array]} a list of ~@link https://docs.ccxt.com/en/latest/manual.html?#public-trades trade structures~
         */
        $this->load_markets();
        $market = $this->market($symbol);
        $request = array(
            'market' => $market['id'],
        );
        $response = $this->publicGetTrades (array_merge($request, $params));
        return $this->parse_trades($response, $market, $since, $limit);
    }

    public function parse_ohlcv($ohlcv, $market = null) {
        //
        //     array(
        //         1498530360,
        //         2700.0,
        //         2700.0,
        //         2700.0,
        //         2700.0,
        //         0.01
        //     )
        //
        return array(
            $this->safe_timestamp($ohlcv, 0),
            $this->safe_number($ohlcv, 1),
            $this->safe_number($ohlcv, 2),
            $this->safe_number($ohlcv, 3),
            $this->safe_number($ohlcv, 4),
            $this->safe_number($ohlcv, 5),
        );
    }

    public function fetch_ohlcv($symbol, $timeframe = '1m', $since = null, $limit = null, $params = array ()) {
        /**
         * fetches historical candlestick data containing the open, high, low, and close price, and the volume of a $market
         * @param {string} $symbol unified $symbol of the $market to fetch OHLCV data for
         * @param {string} $timeframe the length of time each candle represents
         * @param {int|float|null} $since timestamp in ms of the earliest candle to fetch
         * @param {int|float|null} $limit the maximum amount of candles to fetch
         * @param {array} $params extra parameters specific to the tidebit api endpoint
         * @return {[[int|float]]} A list of candles ordered as timestamp, open, high, low, close, volume
         */
        $this->load_markets();
        $market = $this->market($symbol);
        if ($limit === null) {
            $limit = 30; // default is 30
        }
        $request = array(
            'market' => $market['id'],
            'period' => $this->timeframes[$timeframe],
            'limit' => $limit,
        );
        if ($since !== null) {
            $request['timestamp'] = intval($since / 1000);
        } else {
            $request['timestamp'] = 1800000;
        }
        $response = $this->publicGetK (array_merge($request, $params));
        //
        //     [
        //         [1498530360,2700.0,2700.0,2700.0,2700.0,0.01],
        //         [1498530420,2700.0,2700.0,2700.0,2700.0,0],
        //         [1498530480,2700.0,2700.0,2700.0,2700.0,0],
        //     ]
        //
        if ($response === 'null') {
            return array();
        }
        return $this->parse_ohlcvs($response, $market, $timeframe, $since, $limit);
    }

    public function parse_order_status($status) {
        $statuses = array(
            'done' => 'closed',
            'wait' => 'open',
            'cancel' => 'canceled',
        );
        return $this->safe_string($statuses, $status, $status);
    }

    public function parse_order($order, $market = null) {
        //
        //     {
        //         "id" => 7,                              // 唯一的 Order ID
        //         "side" => "sell",                       // Buy/Sell 代表买单/卖单
        //         "price" => "3100.0",                    // 出价
        //         "avg_price" => "3101.2",                // 平均成交价
        //         "state" => "wait",                      // 订单的当前状态 [wait,done,cancel]
        //                                               //   wait   表明订单正在市场上挂单
        //                                               //          是一个active $order
        //                                               //          此时订单可能部分成交或者尚未成交
        //                                               //   done   代表订单已经完全成交
        //                                               //   cancel 代表订单已经被撤销
        //         "market" => "btccny",                   // 订单参与的交易市场
        //         "created_at" => "2014-04-18T02:02:33Z", // 下单时间 ISO8601格式
        //         "volume" => "100.0",                    // 购买/卖出数量
        //         "remaining_volume" => "89.8",           // 还未成交的数量 remaining_volume 总是小于等于 volume
        //                                               //   在订单完全成交时变成 0
        //         "executed_volume" => "10.2",            // 已成交的数量
        //                                               //   volume = remaining_volume . executed_volume
        //         "trades_count" => 1,                    // 订单的成交数 整数值
        //                                               //   未成交的订单为 0 有一笔成交的订单为 1
        //                                               //   通过该字段可以判断订单是否处于部分成交状态
        //         "trades" => array(                           // 订单的详细成交记录 参见Trade
        //                                               //   注意 => 只有某些返回详细订单数据的 API 才会包含 Trade 数据
        //             {
        //                 "id" => 2,
        //                 "price" => "3100.0",
        //                 "volume" => "10.2",
        //                 "market" => "btccny",
        //                 "created_at" => "2014-04-18T02:04:49Z",
        //                 "side" => "sell"
        //             }
        //         )
        //     }
        //
        $marketId = $this->safe_string($order, 'market');
        $symbol = $this->safe_symbol($marketId, $market);
        $timestamp = $this->parse8601($this->safe_string($order, 'created_at'));
        $status = $this->parse_order_status($this->safe_string($order, 'state'));
        $id = $this->safe_string($order, 'id');
        $type = $this->safe_string($order, 'ord_type');
        $side = $this->safe_string($order, 'side');
        $price = $this->safe_string($order, 'price');
        $amount = $this->safe_string($order, 'volume');
        $filled = $this->safe_string($order, 'executed_volume');
        $remaining = $this->safe_string($order, 'remaining_volume');
        $average = $this->safe_string($order, 'avg_price');
        return $this->safe_order(array(
            'id' => $id,
            'clientOrderId' => null,
            'timestamp' => $timestamp,
            'datetime' => $this->iso8601($timestamp),
            'lastTradeTimestamp' => null,
            'status' => $status,
            'symbol' => $symbol,
            'type' => $type,
            'timeInForce' => null,
            'postOnly' => null,
            'side' => $side,
            'price' => $price,
            'stopPrice' => null,
            'amount' => $amount,
            'filled' => $filled,
            'remaining' => $remaining,
            'cost' => null,
            'trades' => null,
            'fee' => null,
            'info' => $order,
            'average' => $average,
        ), $market);
    }

    public function create_order($symbol, $type, $side, $amount, $price = null, $params = array ()) {
        /**
         * create a trade order
         * @param {string} $symbol unified $symbol of the $market to create an order in
         * @param {string} $type 'market' or 'limit'
         * @param {string} $side 'buy' or 'sell'
         * @param {int|float} $amount how much of currency you want to trade in units of base currency
         * @param {int|float|null} $price the $price at which the order is to be fullfilled, in units of the quote currency, ignored in $market orders
         * @param {array} $params extra parameters specific to the tidebit api endpoint
         * @return {array} an {@link https://docs.ccxt.com/en/latest/manual.html#order-structure order structure}
         */
        $this->load_markets();
        $market = $this->market($symbol);
        $request = array(
            'market' => $market['id'],
            'side' => $side,
            'volume' => (string) $amount,
            'ord_type' => $type,
        );
        if ($type === 'limit') {
            $request['price'] = (string) $price;
        }
        $response = $this->privatePostOrders (array_merge($request, $params));
        return $this->parse_order($response);
    }

    public function cancel_order($id, $symbol = null, $params = array ()) {
        /**
         * cancels an open $order
         * @param {string} $id $order $id
         * @param {string|null} $symbol not used by tidebit cancelOrder ()
         * @param {array} $params extra parameters specific to the tidebit api endpoint
         * @return {array} An {@link https://docs.ccxt.com/en/latest/manual.html#$order-structure $order structure}
         */
        $this->load_markets();
        $request = array(
            'id' => $id,
        );
        $result = $this->privatePostOrderDelete (array_merge($request, $params));
        $order = $this->parse_order($result);
        $status = $this->safe_string($order, 'status');
        if ($status === 'closed' || $status === 'canceled') {
            throw new OrderNotFound($this->id . ' ' . $this->json($order));
        }
        return $order;
    }

    public function withdraw($code, $amount, $address, $tag = null, $params = array ()) {
        /**
         * make a withdrawal
         * @param {string} $code unified $currency $code
         * @param {int|float} $amount the $amount to withdraw
         * @param {string} $address the $address to withdraw to
         * @param {string|null} $tag
         * @param {array} $params extra parameters specific to the tidebit api endpoint
         * @return {array} a {@link https://docs.ccxt.com/en/latest/manual.html#transaction-structure transaction structure}
         */
        list($tag, $params) = $this->handle_withdraw_tag_and_params($tag, $params);
        $this->check_address($address);
        $this->load_markets();
        $currency = $this->currency($code);
        $id = $this->safe_string($params, 'id');
        if ($id === null) {
            throw new ArgumentsRequired($this->id . ' withdraw() requires an extra `$id` param (withdraw account $id according to withdraws/bind_account_list endpoint');
        }
        $request = array(
            'id' => $id,
            'currency_type' => 'coin', // or 'cash'
            'currency' => $currency['id'],
            'body' => $amount,
            // 'address' => $address, // they don't allow withdrawing to direct addresses?
        );
        if ($tag !== null) {
            $request['memo'] = $tag;
        }
        $result = $this->privatePostWithdrawsApply (array_merge($request, $params));
        return $this->parse_transaction($result, $currency);
    }

    public function parse_transaction($transaction, $currency = null) {
        $currency = $this->safe_currency(null, $currency);
        return array(
            'id' => null,
            'txid' => null,
            'timestamp' => null,
            'datetime' => null,
            'network' => null,
            'addressFrom' => null,
            'address' => null,
            'addressTo' => null,
            'amount' => null,
            'type' => null,
            'currency' => $currency['code'],
            'status' => null,
            'updated' => null,
            'tagFrom' => null,
            'tag' => null,
            'tagTo' => null,
            'comment' => null,
            'fee' => null,
            'info' => $transaction,
        );
    }

    public function nonce() {
        return $this->milliseconds();
    }

    public function encode_params($params) {
        return $this->urlencode($this->keysort($params));
    }

    public function sign($path, $api = 'public', $method = 'GET', $params = array (), $headers = null, $body = null) {
        $request = '/' . 'api/' . $this->version . '/' . $this->implode_params($path, $params) . '.json';
        $query = $this->omit($params, $this->extract_params($path));
        $url = $this->urls['api']['rest'] . $request;
        if ($api === 'public') {
            if ($query) {
                $url .= '?' . $this->urlencode($query);
            }
        } else {
            $this->check_required_credentials();
            $nonce = (string) $this->nonce();
            $sortedByKey = $this->keysort(array_merge(array(
                'access_key' => $this->apiKey,
                'tonce' => $nonce,
            ), $params));
            $query = $this->urlencode($sortedByKey);
            $payload = $method . '|' . $request . '|' . $query;
            $signature = $this->hmac($this->encode($payload), $this->encode($this->secret));
            $suffix = $query . '&$signature=' . $signature;
            if ($method === 'GET') {
                $url .= '?' . $suffix;
            } else {
                $body = $suffix;
                $headers = array( 'Content-Type' => 'application/x-www-form-urlencoded' );
            }
        }
        return array( 'url' => $url, 'method' => $method, 'body' => $body, 'headers' => $headers );
    }

    public function handle_errors($code, $reason, $url, $method, $headers, $body, $response, $requestHeaders, $requestBody) {
        if (($code === 400) || ($response === null)) {
            $feedback = $this->id . ' ' . $body;
            if ($response === null) {
                throw new ExchangeError($feedback);
            }
            $error = $this->safe_value($response, 'error', array());
            $errorCode = $this->safe_string($error, 'code');
            $this->throw_exactly_matched_exception($this->exceptions, $errorCode, $feedback);
            // fallback to default $error handler
        }
    }
}
