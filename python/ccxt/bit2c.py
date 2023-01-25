# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.base.exchange import Exchange
import hashlib
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import PermissionDenied
from ccxt.base.errors import ArgumentsRequired
from ccxt.base.errors import OrderNotFound
from ccxt.base.errors import NotSupported
from ccxt.base.errors import InvalidNonce
from ccxt.base.decimal_to_precision import TICK_SIZE
from ccxt.base.precise import Precise


class bit2c(Exchange):

    def describe(self):
        return self.deep_extend(super(bit2c, self).describe(), {
            'id': 'bit2c',
            'name': 'Bit2C',
            'countries': ['IL'],  # Israel
            'rateLimit': 3000,
            'has': {
                'CORS': None,
                'spot': True,
                'margin': False,
                'swap': False,
                'future': False,
                'option': False,
                'addMargin': False,
                'cancelOrder': True,
                'createOrder': True,
                'createReduceOnlyOrder': False,
                'fetchBalance': True,
                'fetchBorrowRate': False,
                'fetchBorrowRateHistories': False,
                'fetchBorrowRateHistory': False,
                'fetchBorrowRates': False,
                'fetchBorrowRatesPerSymbol': False,
                'fetchDepositAddress': True,
                'fetchFundingHistory': False,
                'fetchFundingRate': False,
                'fetchFundingRateHistory': False,
                'fetchFundingRates': False,
                'fetchIndexOHLCV': False,
                'fetchLeverage': False,
                'fetchLeverageTiers': False,
                'fetchMarginMode': False,
                'fetchMarkOHLCV': False,
                'fetchMyTrades': True,
                'fetchOpenInterestHistory': False,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchOrderBook': True,
                'fetchPosition': False,
                'fetchPositionMode': False,
                'fetchPositions': False,
                'fetchPositionsRisk': False,
                'fetchPremiumIndexOHLCV': False,
                'fetchTicker': True,
                'fetchTrades': True,
                'fetchTradingFee': False,
                'fetchTradingFees': True,
                'fetchTransfer': False,
                'fetchTransfers': False,
                'reduceMargin': False,
                'setLeverage': False,
                'setMarginMode': False,
                'setPositionMode': False,
                'transfer': False,
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/27766119-3593220e-5ece-11e7-8b3a-5a041f6bcc3f.jpg',
                'api': {
                    'rest': 'https://bit2c.co.il',
                },
                'www': 'https://www.bit2c.co.il',
                'referral': 'https://bit2c.co.il/Aff/63bfed10-e359-420c-ab5a-ad368dab0baf',
                'doc': [
                    'https://www.bit2c.co.il/home/api',
                    'https://github.com/OferE/bit2c',
                ],
            },
            'api': {
                'public': {
                    'get': [
                        'Exchanges/{pair}/Ticker',
                        'Exchanges/{pair}/orderbook',
                        'Exchanges/{pair}/trades',
                        'Exchanges/{pair}/lasttrades',
                    ],
                },
                'private': {
                    'post': [
                        'Merchant/CreateCheckout',
                        'Funds/AddCoinFundsRequest',
                        'Order/AddFund',
                        'Order/AddOrder',
                        'Order/GetById',
                        'Order/AddOrderMarketPriceBuy',
                        'Order/AddOrderMarketPriceSell',
                        'Order/CancelOrder',
                        'Order/AddCoinFundsRequest',
                        'Order/AddStopOrder',
                        'Payment/GetMyId',
                        'Payment/Send',
                        'Payment/Pay',
                    ],
                    'get': [
                        'Account/Balance',
                        'Account/Balance/v2',
                        'Order/MyOrders',
                        'Order/GetById',
                        'Order/AccountHistory',
                        'Order/OrderHistory',
                    ],
                },
            },
            'markets': {
                'BTC/NIS': {'id': 'BtcNis', 'symbol': 'BTC/NIS', 'base': 'BTC', 'quote': 'NIS', 'baseId': 'Btc', 'quoteId': 'Nis', 'type': 'spot', 'spot': True},
                'ETH/NIS': {'id': 'EthNis', 'symbol': 'ETH/NIS', 'base': 'ETH', 'quote': 'NIS', 'baseId': 'Eth', 'quoteId': 'Nis', 'type': 'spot', 'spot': True},
                'LTC/NIS': {'id': 'LtcNis', 'symbol': 'LTC/NIS', 'base': 'LTC', 'quote': 'NIS', 'baseId': 'Ltc', 'quoteId': 'Nis', 'type': 'spot', 'spot': True},
                'USDC/NIS': {'id': 'UsdcNis', 'symbol': 'USDC/NIS', 'base': 'USDC', 'quote': 'NIS', 'baseId': 'Usdc', 'quoteId': 'Nis', 'type': 'spot', 'spot': True},
            },
            'fees': {
                'trading': {
                    'maker': self.parse_number('0.005'),
                    'taker': self.parse_number('0.005'),
                },
            },
            'options': {
                'fetchTradesMethod': 'public_get_exchanges_pair_trades',
            },
            'precisionMode': TICK_SIZE,
            'exceptions': {
                'exact': {
                    'Please provide valid APIkey': AuthenticationError,  # {"error" : "Please provide valid APIkey"}
                    'No order found.': OrderNotFound,  # {"Error" : "No order found."}
                },
                'broad': {
                    # {"error": "Please provide valid nonce in Request Nonce(1598218490) is not bigger than last nonce(1598218490)."}
                    # {"error": "Please provide valid nonce in Request UInt64.TryParse failed for nonce :"}
                    'Please provide valid nonce': InvalidNonce,
                    'please approve new terms of use on site': PermissionDenied,  # {"error" : "please approve new terms of use on site."}
                },
            },
        })

    def parse_balance(self, response):
        result = {
            'info': response,
            'timestamp': None,
            'datetime': None,
        }
        codes = list(self.currencies.keys())
        for i in range(0, len(codes)):
            code = codes[i]
            account = self.account()
            currency = self.currency(code)
            uppercase = currency['id'].upper()
            if uppercase in response:
                account['free'] = self.safe_string(response, 'AVAILABLE_' + uppercase)
                account['total'] = self.safe_string(response, uppercase)
            result[code] = account
        return self.safe_balance(result)

    def fetch_balance(self, params={}):
        """
        query for balance and get the amount of funds available for trading or funds locked in orders
        :param dict params: extra parameters specific to the bit2c api endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/en/latest/manual.html?#balance-structure>`
        """
        self.load_markets()
        response = self.privateGetAccountBalanceV2(params)
        #
        #     {
        #         "AVAILABLE_NIS": 0.0,
        #         "NIS": 0.0,
        #         "LOCKED_NIS": 0.0,
        #         "AVAILABLE_BTC": 0.0,
        #         "BTC": 0.0,
        #         "LOCKED_BTC": 0.0,
        #         "AVAILABLE_ETH": 0.0,
        #         "ETH": 0.0,
        #         "LOCKED_ETH": 0.0,
        #         "AVAILABLE_BCHSV": 0.0,
        #         "BCHSV": 0.0,
        #         "LOCKED_BCHSV": 0.0,
        #         "AVAILABLE_BCHABC": 0.0,
        #         "BCHABC": 0.0,
        #         "LOCKED_BCHABC": 0.0,
        #         "AVAILABLE_LTC": 0.0,
        #         "LTC": 0.0,
        #         "LOCKED_LTC": 0.0,
        #         "AVAILABLE_ETC": 0.0,
        #         "ETC": 0.0,
        #         "LOCKED_ETC": 0.0,
        #         "AVAILABLE_BTG": 0.0,
        #         "BTG": 0.0,
        #         "LOCKED_BTG": 0.0,
        #         "AVAILABLE_GRIN": 0.0,
        #         "GRIN": 0.0,
        #         "LOCKED_GRIN": 0.0,
        #         "Fees": {
        #             "BtcNis": {"FeeMaker": 1.0, "FeeTaker": 1.0},
        #             "EthNis": {"FeeMaker": 1.0, "FeeTaker": 1.0},
        #             "BchabcNis": {"FeeMaker": 1.0, "FeeTaker": 1.0},
        #             "LtcNis": {"FeeMaker": 1.0, "FeeTaker": 1.0},
        #             "EtcNis": {"FeeMaker": 1.0, "FeeTaker": 1.0},
        #             "BtgNis": {"FeeMaker": 1.0, "FeeTaker": 1.0},
        #             "LtcBtc": {"FeeMaker": 1.0, "FeeTaker": 1.0},
        #             "BchsvNis": {"FeeMaker": 1.0, "FeeTaker": 1.0},
        #             "GrinNis": {"FeeMaker": 1.0, "FeeTaker": 1.0}
        #         }
        #     }
        #
        return self.parse_balance(response)

    def fetch_order_book(self, symbol, limit=None, params={}):
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int|None limit: the maximum amount of order book entries to return
        :param dict params: extra parameters specific to the bit2c api endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/en/latest/manual.html#order-book-structure>` indexed by market symbols
        """
        self.load_markets()
        market = self.market(symbol)
        request = {
            'pair': market['id'],
        }
        orderbook = self.publicGetExchangesPairOrderbook(self.extend(request, params))
        return self.parse_order_book(orderbook, market['symbol'])

    def parse_ticker(self, ticker, market=None):
        symbol = self.safe_symbol(None, market)
        timestamp = self.milliseconds()
        averagePrice = self.safe_string(ticker, 'av')
        baseVolume = self.safe_string(ticker, 'a')
        last = self.safe_string(ticker, 'll')
        return self.safe_ticker({
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': None,
            'low': None,
            'bid': self.safe_string(ticker, 'h'),
            'bidVolume': None,
            'ask': self.safe_string(ticker, 'l'),
            'askVolume': None,
            'vwap': None,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': averagePrice,
            'baseVolume': baseVolume,
            'quoteVolume': None,
            'info': ticker,
        }, market)

    def fetch_ticker(self, symbol, params={}):
        """
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market
        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict params: extra parameters specific to the bit2c api endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/en/latest/manual.html#ticker-structure>`
        """
        self.load_markets()
        market = self.market(symbol)
        request = {
            'pair': market['id'],
        }
        response = self.publicGetExchangesPairTicker(self.extend(request, params))
        return self.parse_ticker(response, market)

    def fetch_trades(self, symbol, since=None, limit=None, params={}):
        """
        get the list of most recent trades for a particular symbol
        :param str symbol: unified symbol of the market to fetch trades for
        :param int|None since: timestamp in ms of the earliest trade to fetch
        :param int|None limit: the maximum amount of trades to fetch
        :param dict params: extra parameters specific to the bit2c api endpoint
        :returns [dict]: a list of `trade structures <https://docs.ccxt.com/en/latest/manual.html?#public-trades>`
        """
        self.load_markets()
        market = self.market(symbol)
        method = self.options['fetchTradesMethod']  # public_get_exchanges_pair_trades or public_get_exchanges_pair_lasttrades
        request = {
            'pair': market['id'],
        }
        if since is not None:
            request['date'] = int(since)
        if limit is not None:
            request['limit'] = limit  # max 100000
        response = getattr(self, method)(self.extend(request, params))
        #
        #     [
        #         {"date":1651785980,"price":127975.68,"amount":0.3750321,"isBid":true,"tid":1261018},
        #         {"date":1651785980,"price":127987.70,"amount":0.0389527820303982335802581029,"isBid":true,"tid":1261020},
        #         {"date":1651786701,"price":128084.03,"amount":0.0015614749161156156626239821,"isBid":true,"tid":1261022},
        #     ]
        #
        if isinstance(response, str):
            raise ExchangeError(response)
        return self.parse_trades(response, market, since, limit)

    def fetch_trading_fees(self, params={}):
        """
        fetch the trading fees for multiple markets
        :param dict params: extra parameters specific to the bit2c api endpoint
        :returns dict: a dictionary of `fee structures <https://docs.ccxt.com/en/latest/manual.html#fee-structure>` indexed by market symbols
        """
        self.load_markets()
        response = self.privateGetAccountBalance(params)
        #
        #     {
        #         "AVAILABLE_NIS": 0.0,
        #         "NIS": 0.0,
        #         "LOCKED_NIS": 0.0,
        #         "AVAILABLE_BTC": 0.0,
        #         "BTC": 0.0,
        #         "LOCKED_BTC": 0.0,
        #         ...
        #         "Fees": {
        #             "BtcNis": {"FeeMaker": 1.0, "FeeTaker": 1.0},
        #             "EthNis": {"FeeMaker": 1.0, "FeeTaker": 1.0},
        #             ...
        #         }
        #     }
        #
        fees = self.safe_value(response, 'Fees', {})
        keys = list(fees.keys())
        result = {}
        for i in range(0, len(keys)):
            marketId = keys[i]
            symbol = self.safe_symbol(marketId)
            fee = self.safe_value(fees, marketId)
            makerString = self.safe_string(fee, 'FeeMaker')
            takerString = self.safe_string(fee, 'FeeTaker')
            maker = self.parse_number(Precise.string_div(makerString, '100'))
            taker = self.parse_number(Precise.string_div(takerString, '100'))
            result[symbol] = {
                'info': fee,
                'symbol': symbol,
                'taker': taker,
                'maker': maker,
                'percentage': True,
                'tierBased': False,
            }
        return result

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        """
        create a trade order
        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float|None price: the price at which the order is to be fullfilled, in units of the quote currency, ignored in market orders
        :param dict params: extra parameters specific to the bit2c api endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/en/latest/manual.html#order-structure>`
        """
        self.load_markets()
        method = 'privatePostOrderAddOrder'
        market = self.market(symbol)
        request = {
            'Amount': amount,
            'Pair': market['id'],
        }
        if type == 'market':
            method += 'MarketPrice' + self.capitalize(side)
        else:
            request['Price'] = price
            request['Total'] = amount * price
            request['IsBid'] = (side == 'buy')
        response = getattr(self, method)(self.extend(request, params))
        return self.parse_order(response, market)

    def cancel_order(self, id, symbol=None, params={}):
        """
        cancels an open order
        :param str id: order id
        :param str|None symbol: Not used by bit2c cancelOrder()
        :param dict params: extra parameters specific to the bit2c api endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/en/latest/manual.html#order-structure>`
        """
        request = {
            'id': id,
        }
        return self.privatePostOrderCancelOrder(self.extend(request, params))

    def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        """
        fetch all unfilled currently open orders
        :param str symbol: unified market symbol
        :param int|None since: the earliest time in ms to fetch open orders for
        :param int|None limit: the maximum number of  open orders structures to retrieve
        :param dict params: extra parameters specific to the bit2c api endpoint
        :returns [dict]: a list of `order structures <https://docs.ccxt.com/en/latest/manual.html#order-structure>`
        """
        if symbol is None:
            raise ArgumentsRequired(self.id + ' fetchOpenOrders() requires a symbol argument')
        self.load_markets()
        market = self.market(symbol)
        request = {
            'pair': market['id'],
        }
        response = self.privateGetOrderMyOrders(self.extend(request, params))
        orders = self.safe_value(response, market['id'], {})
        asks = self.safe_value(orders, 'ask', [])
        bids = self.safe_value(orders, 'bid', [])
        return self.parse_orders(self.array_concat(asks, bids), market, since, limit)

    def fetch_order(self, id, symbol=None, params={}):
        """
        fetches information on an order made by the user
        :param str symbol: unified market symbol
        :param dict params: extra parameters specific to the bit2c api endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/en/latest/manual.html#order-structure>`
        """
        self.load_markets()
        market = self.market(symbol)
        request = {
            'id': id,
        }
        response = self.privateGetOrderGetById(self.extend(request, params))
        #
        #         {
        #             "pair": "BtcNis",
        #             "status": "Completed",
        #             "created": 1666689837,
        #             "type": 0,
        #             "order_type": 0,
        #             "amount": 0.00000000,
        #             "price": 50000.00000000,
        #             "stop": 0,
        #             "id": 10951473,
        #             "initialAmount": 2.00000000
        #         }
        #
        return self.parse_order(response, market)

    def parse_order(self, order, market=None):
        #
        #      createOrder
        #      {
        #          "OrderResponse": {"pair": "BtcNis", "HasError": False, "Error": "", "Message": ""},
        #          "NewOrder": {
        #              "created": 1505531577,
        #              "type": 0,
        #              "order_type": 0,
        #              "status_type": 0,
        #              "amount": 0.01,
        #              "price": 10000,
        #              "stop": 0,
        #              "id": 9244416,
        #              "initialAmount": None,
        #          },
        #      }
        #      fetchOrder, fetchOpenOrders
        #      {
        #          "pair": "BtcNis",
        #          "status": "Completed",
        #          "created": 1535555837,
        #          "type": 0,
        #          "order_type": 0,
        #          "amount": 0.00000000,
        #          "price": 120000.00000000,
        #          "stop": 0,
        #          "id": 10555173,
        #          "initialAmount": 2.00000000
        #      }
        #
        orderUnified = None
        isNewOrder = False
        if 'NewOrder' in order:
            orderUnified = order['NewOrder']
            isNewOrder = True
        else:
            orderUnified = order
        id = self.safe_string(order, 'id')
        symbol = self.safe_symbol(None, market)
        timestamp = self.safe_integer_product(order, 'created', 1000)
        # status field vary between responses
        # bit2c status type:
        # 0 = New
        # 1 = Open
        # 5 = Completed
        status = None
        if isNewOrder:
            tempStatus = self.safe_integer(orderUnified, 'status_type')
            if tempStatus == 0 or tempStatus == 1:
                status = 'open'
            elif tempStatus == 5:
                status = 'closed'
        else:
            tempStatus = self.safe_string(order, 'status')
            if tempStatus == 'New' or tempStatus == 'Open':
                status = 'open'
            elif tempStatus == 'Completed':
                status = 'closed'
        # bit2c order type:
        # 0 = LMT,  1 = MKT
        type = self.safe_integer(orderUnified, 'order_type')
        if type == 0:
            type = 'limit'
        elif type == 1:
            type = 'market'
        # bit2c side:
        # 0 = buy, 1 = sell
        side = self.safe_integer(orderUnified, 'type')
        if side == 0:
            side = 'buy'
        elif side == 1:
            side = 'sell'
        price = self.safe_string(order, 'price')
        amount = None
        remaining = None
        if isNewOrder:
            amount = self.safe_string(orderUnified, 'amount')  # NOTE:'initialAmount' is currently not set on new order
            remaining = self.safe_string(orderUnified, 'amount')
        else:
            amount = self.safe_string(order, 'initialAmount')
            remaining = self.safe_string(order, 'amount')
        return self.safe_order({
            'id': id,
            'clientOrderId': None,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': None,
            'status': status,
            'symbol': symbol,
            'type': type,
            'timeInForce': None,
            'postOnly': None,
            'side': side,
            'price': price,
            'stopPrice': None,
            'triggerPrice': None,
            'amount': amount,
            'filled': None,
            'remaining': remaining,
            'cost': None,
            'trades': None,
            'fee': None,
            'info': order,
            'average': None,
        }, market)

    def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
        """
        fetch all trades made by the user
        :param str|None symbol: unified market symbol
        :param int|None since: the earliest time in ms to fetch trades for
        :param int|None limit: the maximum number of trades structures to retrieve
        :param dict params: extra parameters specific to the bit2c api endpoint
        :returns [dict]: a list of `trade structures <https://docs.ccxt.com/en/latest/manual.html#trade-structure>`
        """
        self.load_markets()
        market = None
        request = {}
        if limit is not None:
            request['take'] = limit
        request['take'] = limit
        if since is not None:
            request['toTime'] = self.yyyymmdd(self.milliseconds(), '.')
            request['fromTime'] = self.yyyymmdd(since, '.')
        if symbol is not None:
            market = self.market(symbol)
            request['pair'] = market['id']
        response = self.privateGetOrderOrderHistory(self.extend(request, params))
        #
        #     [
        #         {
        #             "ticks":1574767951,
        #             "created":"26/11/19 13:32",
        #             "action":1,
        #             "price":"1000",
        #             "pair":"EthNis",
        #             "reference":"EthNis|10867390|10867377",
        #             "fee":"0.5",
        #             "feeAmount":"0.08",
        #             "feeCoin":"₪",
        #             "firstAmount":"-0.015",
        #             "firstAmountBalance":"9",
        #             "secondAmount":"14.93",
        #             "secondAmountBalance":"130,233.28",
        #             "firstCoin":"ETH",
        #             "secondCoin":"₪"
        #         },
        #         {
        #             "ticks":1574767951,
        #             "created":"26/11/19 13:32",
        #             "action":0,
        #             "price":"1000",
        #             "pair":"EthNis",
        #             "reference":"EthNis|10867390|10867377",
        #             "fee":"0.5",
        #             "feeAmount":"0.08",
        #             "feeCoin":"₪",
        #             "firstAmount":"0.015",
        #             "firstAmountBalance":"9.015",
        #             "secondAmount":"-15.08",
        #             "secondAmountBalance":"130,218.35",
        #             "firstCoin":"ETH",
        #             "secondCoin":"₪"
        #         }
        #     ]
        #
        return self.parse_trades(response, market, since, limit)

    def parse_trade(self, trade, market=None):
        #
        # public fetchTrades
        #
        #     {
        #         "date":1651785980,
        #         "price":127975.68,
        #         "amount":0.3750321,
        #         "isBid":true,
        #         "tid":1261018
        #     }
        #
        # private fetchMyTrades
        #
        #     {
        #         "ticks":1574767951,
        #         "created":"26/11/19 13:32",
        #         "action":1,
        #         "price":"1000",
        #         "pair":"EthNis",
        #         "reference":"EthNis|10867390|10867377",
        #         "fee":"0.5",
        #         "feeAmount":"0.08",
        #         "feeCoin":"₪",
        #         "firstAmount":"-0.015",
        #         "firstAmountBalance":"9",
        #         "secondAmount":"14.93",
        #         "secondAmountBalance":"130,233.28",
        #         "firstCoin":"ETH",
        #         "secondCoin":"₪"
        #     }
        #
        timestamp = None
        id = None
        price = None
        amount = None
        orderId = None
        fee = None
        side = None
        reference = self.safe_string(trade, 'reference')
        if reference is not None:
            timestamp = self.safe_timestamp(trade, 'ticks')
            price = self.safe_string(trade, 'price')
            amount = self.safe_string(trade, 'firstAmount')
            reference_parts = reference.split('|')  # reference contains 'pair|orderId|tradeId'
            marketId = self.safe_string(trade, 'pair')
            market = self.safe_market(marketId, market)
            market = self.safe_market(reference_parts[0], market)
            orderId = reference_parts[1]
            id = reference_parts[2]
            side = self.safe_integer(trade, 'action')
            if side == 0:
                side = 'buy'
            elif side == 1:
                side = 'sell'
            feeCost = self.safe_string(trade, 'feeAmount')
            if feeCost is not None:
                fee = {
                    'cost': feeCost,
                    'currency': 'NIS',
                }
        else:
            timestamp = self.safe_timestamp(trade, 'date')
            id = self.safe_string(trade, 'tid')
            price = self.safe_string(trade, 'price')
            amount = self.safe_string(trade, 'amount')
            side = self.safe_value(trade, 'isBid')
            if side is not None:
                if side:
                    side = 'buy'
                else:
                    side = 'sell'
        market = self.safe_market(None, market)
        return self.safe_trade({
            'info': trade,
            'id': id,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': market['symbol'],
            'order': orderId,
            'type': None,
            'side': side,
            'takerOrMaker': None,
            'price': price,
            'amount': amount,
            'cost': None,
            'fee': fee,
        }, market)

    def is_fiat(self, code):
        return code == 'NIS'

    def fetch_deposit_address(self, code, params={}):
        """
        fetch the deposit address for a currency associated with self account
        :param str code: unified currency code
        :param dict params: extra parameters specific to the bit2c api endpoint
        :returns dict: an `address structure <https://docs.ccxt.com/en/latest/manual.html#address-structure>`
        """
        self.load_markets()
        currency = self.currency(code)
        if self.is_fiat(code):
            raise NotSupported(self.id + ' fetchDepositAddress() does not support fiat currencies')
        request = {
            'Coin': currency['id'],
        }
        response = self.privatePostFundsAddCoinFundsRequest(self.extend(request, params))
        #
        #     {
        #         'address': '0xf14b94518d74aff2b1a6d3429471bcfcd3881d42',
        #         'hasTx': False
        #     }
        #
        return self.parse_deposit_address(response, currency)

    def parse_deposit_address(self, depositAddress, currency=None):
        #
        #     {
        #         'address': '0xf14b94518d74aff2b1a6d3429471bcfcd3881d42',
        #         'hasTx': False
        #     }
        #
        address = self.safe_string(depositAddress, 'address')
        self.check_address(address)
        code = self.safe_currency_code(None, currency)
        return {
            'currency': code,
            'network': None,
            'address': address,
            'tag': None,
            'info': depositAddress,
        }

    def nonce(self):
        return self.milliseconds()

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api']['rest'] + '/' + self.implode_params(path, params)
        if api == 'public':
            url += '.json'
        else:
            self.check_required_credentials()
            nonce = self.nonce()
            query = self.extend({
                'nonce': nonce,
            }, params)
            auth = self.urlencode(query)
            if method == 'GET':
                if query:
                    url += '?' + auth
            else:
                body = auth
            signature = self.hmac(self.encode(auth), self.encode(self.secret), hashlib.sha512, 'base64')
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'key': self.apiKey,
                'sign': signature,
            }
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, httpCode, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if response is None:
            return  # fallback to default error handler
        #
        #     {"error" : "please approve new terms of use on site."}
        #     {"error": "Please provide valid nonce in Request Nonce(1598218490) is not bigger than last nonce(1598218490)."}
        #     {"Error" : "No order found."}
        #
        error = self.safe_string(response, 'error')
        if error is None:
            error = self.safe_string(response, 'Error')
        if error is not None:
            feedback = self.id + ' ' + body
            self.throw_exactly_matched_exception(self.exceptions['exact'], error, feedback)
            self.throw_broadly_matched_exception(self.exceptions['broad'], error, feedback)
            raise ExchangeError(feedback)  # unknown message
