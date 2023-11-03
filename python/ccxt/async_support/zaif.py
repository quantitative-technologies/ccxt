# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.async_support.base.exchange import Exchange
from ccxt.abstract.zaif import ImplicitAPI
import hashlib
from ccxt.base.types import Order, OrderSide, OrderType
from typing import Optional
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import BadRequest
from ccxt.base.decimal_to_precision import TICK_SIZE
from ccxt.base.precise import Precise


class zaif(Exchange, ImplicitAPI):

    def describe(self):
        return self.deep_extend(super(zaif, self).describe(), {
            'id': 'zaif',
            'name': 'Zaif',
            'countries': ['JP'],
            # 10 requests per second = 1000ms / 10 = 100ms between requests(public market endpoints)
            'rateLimit': 100,
            'version': '1',
            'has': {
                'CORS': None,
                'spot': True,
                'margin': None,  # has but unimplemented
                'swap': False,
                'future': False,
                'option': False,
                'cancelOrder': True,
                'createMarketOrder': False,
                'createOrder': True,
                'fetchBalance': True,
                'fetchClosedOrders': True,
                'fetchFundingHistory': False,
                'fetchFundingRate': False,
                'fetchFundingRateHistory': False,
                'fetchFundingRates': False,
                'fetchIndexOHLCV': False,
                'fetchMarkets': True,
                'fetchMarkOHLCV': False,
                'fetchOpenInterestHistory': False,
                'fetchOpenOrders': True,
                'fetchOrderBook': True,
                'fetchPremiumIndexOHLCV': False,
                'fetchTicker': True,
                'fetchTrades': True,
                'fetchTradingFee': False,
                'fetchTradingFees': False,
                'withdraw': True,
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/27766927-39ca2ada-5eeb-11e7-972f-1b4199518ca6.jpg',
                'api': {
                    'rest': 'https://api.zaif.jp',
                },
                'www': 'https://zaif.jp',
                'doc': [
                    'https://techbureau-api-document.readthedocs.io/ja/latest/index.html',
                    'https://corp.zaif.jp/api-docs',
                    'https://corp.zaif.jp/api-docs/api_links',
                    'https://www.npmjs.com/package/zaif.jp',
                    'https://github.com/you21979/node-zaif',
                ],
                'fees': 'https://zaif.jp/fee?lang=en',
            },
            'fees': {
                'trading': {
                    'percentage': True,
                    'taker': self.parse_number('0.001'),
                    'maker': self.parse_number('0'),
                },
            },
            'api': {
                'public': {
                    'get': {
                        'depth/{pair}': 1,
                        'currencies/{pair}': 1,
                        'currencies/all': 1,
                        'currency_pairs/{pair}': 1,
                        'currency_pairs/all': 1,
                        'last_price/{pair}': 1,
                        'ticker/{pair}': 1,
                        'trades/{pair}': 1,
                    },
                },
                'private': {
                    'post': {
                        'active_orders': 5,  # 10 in 5 seconds = 2 per second => cost = 10 / 2 = 5
                        'cancel_order': 5,
                        'deposit_history': 5,
                        'get_id_info': 5,
                        'get_info': 10,  # 10 in 10 seconds = 1 per second => cost = 10 / 1 = 10
                        'get_info2': 5,  # 20 in 10 seconds = 2 per second => cost = 10 / 2 = 5
                        'get_personal_info': 5,
                        'trade': 5,
                        'trade_history': 50,  # 12 in 60 seconds = 0.2 per second => cost = 10 / 0.2 = 50
                        'withdraw': 5,
                        'withdraw_history': 5,
                    },
                },
                'ecapi': {
                    'post': {
                        'createInvoice': 1,  # unverified
                        'getInvoice': 1,
                        'getInvoiceIdsByOrderNumber': 1,
                        'cancelInvoice': 1,
                    },
                },
                'tlapi': {
                    'post': {
                        'get_positions': 66,  # 10 in 60 seconds = 0.166 per second => cost = 10 / 0.166 = 66
                        'position_history': 66,  # 10 in 60 seconds
                        'active_positions': 5,  # 20 in 10 seconds
                        'create_position': 33,  # 3 in 10 seconds = 0.3 per second => cost = 10 / 0.3 = 33
                        'change_position': 33,  # 3 in 10 seconds
                        'cancel_position': 33,  # 3 in 10 seconds
                    },
                },
                'fapi': {
                    'get': {
                        'groups/{group_id}': 1,  # testing
                        'last_price/{group_id}/{pair}': 1,
                        'ticker/{group_id}/{pair}': 1,
                        'trades/{group_id}/{pair}': 1,
                        'depth/{group_id}/{pair}': 1,
                    },
                },
            },
            'options': {
                # zaif schedule defines several market-specific fees
                'fees': {
                    'BTC/JPY': {'maker': self.parse_number('0'), 'taker': self.parse_number('0.001')},
                    'BCH/JPY': {'maker': self.parse_number('0'), 'taker': self.parse_number('0.003')},
                    'BCH/BTC': {'maker': self.parse_number('0'), 'taker': self.parse_number('0.003')},
                    'PEPECASH/JPY': {'maker': self.parse_number('0'), 'taker': self.parse_number('0.0001')},
                    'PEPECASH/BT': {'maker': self.parse_number('0'), 'taker': self.parse_number('0.0001')},
                },
            },
            'precisionMode': TICK_SIZE,
            'exceptions': {
                'exact': {
                    'unsupported currency_pair': BadRequest,  # {"error": "unsupported currency_pair"}
                },
                'broad': {
                },
            },
        })

    async def fetch_markets(self, params={}):
        """
        :see: https://zaif-api-document.readthedocs.io/ja/latest/PublicAPI.html#id12
        retrieves data on all markets for zaif
        :param dict [params]: extra parameters specific to the exchange api endpoint
        :returns dict[]: an array of objects representing market data
        """
        markets = await self.publicGetCurrencyPairsAll(params)
        #
        #     [
        #         {
        #             "aux_unit_point": 0,
        #             "item_japanese": "\u30d3\u30c3\u30c8\u30b3\u30a4\u30f3",
        #             "aux_unit_step": 5.0,
        #             "description": "\u30d3\u30c3\u30c8\u30b3\u30a4\u30f3\u30fb\u65e5\u672c\u5186\u306e\u53d6\u5f15\u3092\u884c\u3046\u3053\u3068\u304c\u3067\u304d\u307e\u3059",
        #             "item_unit_min": 0.001,
        #             "event_number": 0,
        #             "currency_pair": "btc_jpy",
        #             "is_token": False,
        #             "aux_unit_min": 5.0,
        #             "aux_japanese": "\u65e5\u672c\u5186",
        #             "id": 1,
        #             "item_unit_step": 0.0001,
        #             "name": "BTC/JPY",
        #             "seq": 0,
        #             "title": "BTC/JPY"
        #         }
        #     ]
        #
        result = []
        for i in range(0, len(markets)):
            market = markets[i]
            id = self.safe_string(market, 'currency_pair')
            name = self.safe_string(market, 'name')
            baseId, quoteId = name.split('/')
            base = self.safe_currency_code(baseId)
            quote = self.safe_currency_code(quoteId)
            symbol = base + '/' + quote
            fees = self.safe_value(self.options['fees'], symbol, self.fees['trading'])
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'settle': None,
                'baseId': baseId,
                'quoteId': quoteId,
                'settleId': None,
                'type': 'spot',
                'spot': True,
                'margin': None,
                'swap': False,
                'future': False,
                'option': False,
                'active': None,  # can trade or not
                'contract': False,
                'linear': None,
                'inverse': None,
                'taker': fees['taker'],
                'maker': fees['maker'],
                'contractSize': None,
                'expiry': None,
                'expiryDatetime': None,
                'strike': None,
                'optionType': None,
                'precision': {
                    'amount': self.safe_number(market, 'item_unit_step'),
                    'price': self.parse_number(self.parse_precision(self.safe_string(market, 'aux_unit_point'))),
                },
                'limits': {
                    'leverage': {
                        'min': None,
                        'max': None,
                    },
                    'amount': {
                        'min': self.safe_number(market, 'item_unit_min'),
                        'max': None,
                    },
                    'price': {
                        'min': self.safe_number(market, 'aux_unit_min'),
                        'max': None,
                    },
                    'cost': {
                        'min': None,
                        'max': None,
                    },
                },
                'created': None,
                'info': market,
            })
        return result

    def parse_balance(self, response):
        balances = self.safe_value(response, 'return', {})
        deposit = self.safe_value(balances, 'deposit')
        result = {
            'info': response,
            'timestamp': None,
            'datetime': None,
        }
        funds = self.safe_value(balances, 'funds', {})
        currencyIds = list(funds.keys())
        for i in range(0, len(currencyIds)):
            currencyId = currencyIds[i]
            code = self.safe_currency_code(currencyId)
            balance = self.safe_string(funds, currencyId)
            account = self.account()
            account['free'] = balance
            account['total'] = balance
            if deposit is not None:
                if currencyId in deposit:
                    account['total'] = self.safe_string(deposit, currencyId)
            result[code] = account
        return self.safe_balance(result)

    async def fetch_balance(self, params={}):
        """
        :see: https://zaif-api-document.readthedocs.io/ja/latest/TradingAPI.html#id10
        query for balance and get the amount of funds available for trading or funds locked in orders
        :param dict [params]: extra parameters specific to the zaif api endpoint
        :returns dict: a `balance structure <https://github.com/ccxt/ccxt/wiki/Manual#balance-structure>`
        """
        await self.load_markets()
        response = await self.privatePostGetInfo(params)
        return self.parse_balance(response)

    async def fetch_order_book(self, symbol: str, limit: Optional[int] = None, params={}):
        """
        :see: https://zaif-api-document.readthedocs.io/ja/latest/PublicAPI.html#id34
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dict [params]: extra parameters specific to the zaif api endpoint
        :returns dict: A dictionary of `order book structures <https://github.com/ccxt/ccxt/wiki/Manual#order-book-structure>` indexed by market symbols
        """
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'pair': market['id'],
        }
        response = await self.publicGetDepthPair(self.extend(request, params))
        return self.parse_order_book(response, market['symbol'])

    def parse_ticker(self, ticker, market=None):
        #
        # {
        #     "last": 9e-08,
        #     "high": 1e-07,
        #     "low": 9e-08,
        #     "vwap": 0.0,
        #     "volume": 135250.0,
        #     "bid": 9e-08,
        #     "ask": 1e-07
        # }
        #
        symbol = self.safe_symbol(None, market)
        timestamp = self.milliseconds()
        vwap = self.safe_string(ticker, 'vwap')
        baseVolume = self.safe_string(ticker, 'volume')
        quoteVolume = Precise.string_mul(baseVolume, vwap)
        last = self.safe_string(ticker, 'last')
        return self.safe_ticker({
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_string(ticker, 'high'),
            'low': self.safe_string(ticker, 'low'),
            'bid': self.safe_string(ticker, 'bid'),
            'bidVolume': None,
            'ask': self.safe_string(ticker, 'ask'),
            'askVolume': None,
            'vwap': vwap,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': baseVolume,
            'quoteVolume': quoteVolume,
            'info': ticker,
        }, market)

    async def fetch_ticker(self, symbol: str, params={}):
        """
        :see: https://zaif-api-document.readthedocs.io/ja/latest/PublicAPI.html#id22
        fetches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market
        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the zaif api endpoint
        :returns dict: a `ticker structure <https://github.com/ccxt/ccxt/wiki/Manual#ticker-structure>`
        """
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'pair': market['id'],
        }
        ticker = await self.publicGetTickerPair(self.extend(request, params))
        #
        # {
        #     "last": 9e-08,
        #     "high": 1e-07,
        #     "low": 9e-08,
        #     "vwap": 0.0,
        #     "volume": 135250.0,
        #     "bid": 9e-08,
        #     "ask": 1e-07
        # }
        #
        return self.parse_ticker(ticker, market)

    def parse_trade(self, trade, market=None):
        #
        # fetchTrades(public)
        #
        #      {
        #          "date": 1648559414,
        #          "price": 5880375.0,
        #          "amount": 0.017,
        #          "tid": 176126557,
        #          "currency_pair": "btc_jpy",
        #          "trade_type": "ask"
        #      }
        #
        side = self.safe_string(trade, 'trade_type')
        side = 'buy' if (side == 'bid') else 'sell'
        timestamp = self.safe_timestamp(trade, 'date')
        id = self.safe_string_2(trade, 'id', 'tid')
        priceString = self.safe_string(trade, 'price')
        amountString = self.safe_string(trade, 'amount')
        marketId = self.safe_string(trade, 'currency_pair')
        symbol = self.safe_symbol(marketId, market, '_')
        return self.safe_trade({
            'id': id,
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'type': None,
            'side': side,
            'order': None,
            'takerOrMaker': None,
            'price': priceString,
            'amount': amountString,
            'cost': None,
            'fee': None,
        }, market)

    async def fetch_trades(self, symbol: str, since: Optional[int] = None, limit: Optional[int] = None, params={}):
        """
        :see: https://zaif-api-document.readthedocs.io/ja/latest/PublicAPI.html#id28
        get the list of most recent trades for a particular symbol
        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of trades to fetch
        :param dict [params]: extra parameters specific to the zaif api endpoint
        :returns Trade[]: a list of `trade structures <https://github.com/ccxt/ccxt/wiki/Manual#public-trades>`
        """
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'pair': market['id'],
        }
        response = await self.publicGetTradesPair(self.extend(request, params))
        #
        #      [
        #          {
        #              "date": 1648559414,
        #              "price": 5880375.0,
        #              "amount": 0.017,
        #              "tid": 176126557,
        #              "currency_pair": "btc_jpy",
        #              "trade_type": "ask"
        #          }, ...
        #      ]
        #
        numTrades = len(response)
        if numTrades == 1:
            firstTrade = response[0]
            if not firstTrade:
                response = []
        return self.parse_trades(response, market, since, limit)

    async def create_order(self, symbol: str, type: OrderType, side: OrderSide, amount, price=None, params={}):
        """
        :see: https://zaif-api-document.readthedocs.io/ja/latest/MarginTradingAPI.html#id23
        create a trade order
        :param str symbol: unified symbol of the market to create an order in
        :param str type: must be 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float [price]: the price at which the order is to be fullfilled, in units of the quote currency, ignored in market orders
        :param dict [params]: extra parameters specific to the zaif api endpoint
        :returns dict: an `order structure <https://github.com/ccxt/ccxt/wiki/Manual#order-structure>`
        """
        await self.load_markets()
        if type != 'limit':
            raise ExchangeError(self.id + ' createOrder() allows limit orders only')
        market = self.market(symbol)
        request = {
            'currency_pair': market['id'],
            'action': 'bid' if (side == 'buy') else 'ask',
            'amount': amount,
            'price': price,
        }
        response = await self.privatePostTrade(self.extend(request, params))
        return self.safe_order({
            'info': response,
            'id': str(response['return']['order_id']),
        }, market)

    async def cancel_order(self, id: str, symbol: Optional[str] = None, params={}):
        """
        :see: https://zaif-api-document.readthedocs.io/ja/latest/TradingAPI.html#id37
        cancels an open order
        :param str id: order id
        :param str symbol: not used by zaif cancelOrder()
        :param dict [params]: extra parameters specific to the zaif api endpoint
        :returns dict: An `order structure <https://github.com/ccxt/ccxt/wiki/Manual#order-structure>`
        """
        request = {
            'order_id': id,
        }
        return await self.privatePostCancelOrder(self.extend(request, params))

    def parse_order(self, order, market=None) -> Order:
        #
        #     {
        #         "currency_pair": "btc_jpy",
        #         "action": "ask",
        #         "amount": 0.03,
        #         "price": 56000,
        #         "timestamp": 1402021125,
        #         "comment" : "demo"
        #     }
        #
        side = self.safe_string(order, 'action')
        side = 'buy' if (side == 'bid') else 'sell'
        timestamp = self.safe_timestamp(order, 'timestamp')
        marketId = self.safe_string(order, 'currency_pair')
        symbol = self.safe_symbol(marketId, market, '_')
        price = self.safe_string(order, 'price')
        amount = self.safe_string(order, 'amount')
        id = self.safe_string(order, 'id')
        return self.safe_order({
            'id': id,
            'clientOrderId': None,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': None,
            'status': 'open',
            'symbol': symbol,
            'type': 'limit',
            'timeInForce': None,
            'postOnly': None,
            'side': side,
            'price': price,
            'stopPrice': None,
            'triggerPrice': None,
            'cost': None,
            'amount': amount,
            'filled': None,
            'remaining': None,
            'trades': None,
            'fee': None,
            'info': order,
            'average': None,
        }, market)

    async def fetch_open_orders(self, symbol: Optional[str] = None, since: Optional[int] = None, limit: Optional[int] = None, params={}):
        """
        :see: https://zaif-api-document.readthedocs.io/ja/latest/MarginTradingAPI.html#id28
        fetch all unfilled currently open orders
        :param str symbol: unified market symbol
        :param int [since]: the earliest time in ms to fetch open orders for
        :param int [limit]: the maximum number of  open orders structures to retrieve
        :param dict [params]: extra parameters specific to the zaif api endpoint
        :returns Order[]: a list of `order structures <https://github.com/ccxt/ccxt/wiki/Manual#order-structure>`
        """
        await self.load_markets()
        market = None
        request = {
            # 'is_token': False,
            # 'is_token_both': False,
        }
        if symbol is not None:
            market = self.market(symbol)
            request['currency_pair'] = market['id']
        response = await self.privatePostActiveOrders(self.extend(request, params))
        return self.parse_orders(response['return'], market, since, limit)

    async def fetch_closed_orders(self, symbol: Optional[str] = None, since: Optional[int] = None, limit: Optional[int] = None, params={}):
        """
        :see: https://zaif-api-document.readthedocs.io/ja/latest/TradingAPI.html#id24
        fetches information on multiple closed orders made by the user
        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of  orde structures to retrieve
        :param dict [params]: extra parameters specific to the zaif api endpoint
        :returns Order[]: a list of `order structures <https://github.com/ccxt/ccxt/wiki/Manual#order-structure>`
        """
        await self.load_markets()
        market = None
        request = {
            # 'from': 0,
            # 'count': 1000,
            # 'from_id': 0,
            # 'end_id': 1000,
            # 'order': 'DESC',
            # 'since': 1503821051,
            # 'end': 1503821051,
            # 'is_token': False,
        }
        if symbol is not None:
            market = self.market(symbol)
            request['currency_pair'] = market['id']
        response = await self.privatePostTradeHistory(self.extend(request, params))
        return self.parse_orders(response['return'], market, since, limit)

    async def withdraw(self, code: str, amount, address, tag=None, params={}):
        """
        :see: https://zaif-api-document.readthedocs.io/ja/latest/TradingAPI.html#id41
        make a withdrawal
        :param str code: unified currency code
        :param float amount: the amount to withdraw
        :param str address: the address to withdraw to
        :param str tag:
        :param dict [params]: extra parameters specific to the zaif api endpoint
        :returns dict: a `transaction structure <https://github.com/ccxt/ccxt/wiki/Manual#transaction-structure>`
        """
        tag, params = self.handle_withdraw_tag_and_params(tag, params)
        self.check_address(address)
        await self.load_markets()
        currency = self.currency(code)
        if code == 'JPY':
            raise ExchangeError(self.id + ' withdraw() does not allow ' + code + ' withdrawals')
        request = {
            'currency': currency['id'],
            'amount': amount,
            'address': address,
            # 'message': 'Hi!',  # XEM and others
            # 'opt_fee': 0.003,  # BTC and MONA only
        }
        if tag is not None:
            request['message'] = tag
        result = await self.privatePostWithdraw(self.extend(request, params))
        #
        #     {
        #         "success": 1,
        #         "return": {
        #             "id": 23634,
        #             "fee": 0.001,
        #             "txid":,
        #             "funds": {
        #                 "jpy": 15320,
        #                 "btc": 1.392,
        #                 "xem": 100.2,
        #                 "mona": 2600
        #             }
        #         }
        #     }
        #
        returnData = self.safe_value(result, 'return')
        return self.parse_transaction(returnData, currency)

    def parse_transaction(self, transaction, currency=None):
        #
        #     {
        #         "id": 23634,
        #         "fee": 0.001,
        #         "txid":,
        #         "funds": {
        #             "jpy": 15320,
        #             "btc": 1.392,
        #             "xem": 100.2,
        #             "mona": 2600
        #         }
        #     }
        #
        currency = self.safe_currency(None, currency)
        fee = None
        feeCost = self.safe_value(transaction, 'fee')
        if feeCost is not None:
            fee = {
                'cost': feeCost,
                'currency': currency['code'],
            }
        return {
            'id': self.safe_string(transaction, 'id'),
            'txid': self.safe_string(transaction, 'txid'),
            'timestamp': None,
            'datetime': None,
            'network': None,
            'addressFrom': None,
            'address': None,
            'addressTo': None,
            'amount': None,
            'type': None,
            'currency': currency['code'],
            'status': None,
            'updated': None,
            'tagFrom': None,
            'tag': None,
            'tagTo': None,
            'comment': None,
            'fee': fee,
            'info': transaction,
        }

    def custom_nonce(self):
        num = (self.milliseconds() / str(1000))
        nonce = float(num)
        return format(nonce, '.8f')

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api']['rest'] + '/'
        if api == 'public':
            url += 'api/' + self.version + '/' + self.implode_params(path, params)
        elif api == 'fapi':
            url += 'fapi/' + self.version + '/' + self.implode_params(path, params)
        else:
            self.check_required_credentials()
            if api == 'ecapi':
                url += 'ecapi'
            elif api == 'tlapi':
                url += 'tlapi'
            else:
                url += 'tapi'
            nonce = self.custom_nonce()
            body = self.urlencode(self.extend({
                'method': path,
                'nonce': nonce,
            }, params))
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Key': self.apiKey,
                'Sign': self.hmac(self.encode(body), self.encode(self.secret), hashlib.sha512),
            }
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, httpCode, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if response is None:
            return None
        #
        #     {"error": "unsupported currency_pair"}
        #
        feedback = self.id + ' ' + body
        error = self.safe_string(response, 'error')
        if error is not None:
            self.throw_exactly_matched_exception(self.exceptions['exact'], error, feedback)
            self.throw_broadly_matched_exception(self.exceptions['broad'], error, feedback)
            raise ExchangeError(feedback)  # unknown message
        success = self.safe_value(response, 'success', True)
        if not success:
            raise ExchangeError(feedback)
        return None
