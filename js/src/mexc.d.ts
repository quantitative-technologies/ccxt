import Exchange from './abstract/mexc.js';
import { IndexType, Int, OrderSide, Balances, OrderType, OHLCV, FundingRateHistory, Position, OrderBook, OrderRequest, FundingHistory, Order, Trade, Transaction, Ticker } from './base/types.js';
/**
 * @class mexc
 * @extends Exchange
 */
export default class mexc extends Exchange {
    describe(): any;
    fetchStatus(params?: {}): Promise<{
        status: any;
        updated: any;
        url: any;
        eta: any;
        info: any;
    }>;
    fetchTime(params?: {}): Promise<number>;
    fetchCurrencies(params?: {}): Promise<{}>;
    safeNetwork(networkId: any): string;
    fetchMarkets(params?: {}): Promise<any>;
    fetchSpotMarkets(params?: {}): Promise<any[]>;
    fetchSwapMarkets(params?: {}): Promise<any[]>;
    fetchOrderBook(symbol: string, limit?: Int, params?: {}): Promise<OrderBook>;
    parseBidAsk(bidask: any, priceKey?: IndexType, amountKey?: IndexType, countKey?: IndexType): number[];
    fetchTrades(symbol: string, since?: Int, limit?: Int, params?: {}): Promise<Trade[]>;
    parseTrade(trade: any, market?: any): Trade;
    syntheticTradeId(market?: any, timestamp?: any, side?: any, amount?: any, price?: any, orderType?: any, takerOrMaker?: any): string;
    fetchOHLCV(symbol: string, timeframe?: string, since?: Int, limit?: Int, params?: {}): Promise<OHLCV[]>;
    parseOHLCV(ohlcv: any, market?: any): OHLCV;
    fetchTickers(symbols?: string[], params?: {}): Promise<import("./base/types.js").Dictionary<Ticker>>;
    fetchTicker(symbol: string, params?: {}): Promise<Ticker>;
    parseTicker(ticker: any, market?: any): Ticker;
    fetchBidsAsks(symbols?: string[], params?: {}): Promise<import("./base/types.js").Dictionary<Ticker>>;
    createOrder(symbol: string, type: OrderType, side: OrderSide, amount: any, price?: any, params?: {}): Promise<Order>;
    createSpotOrderRequest(market: any, type: any, side: any, amount: any, price?: any, marginMode?: any, params?: {}): any;
    createSpotOrder(market: any, type: any, side: any, amount: any, price?: any, marginMode?: any, params?: {}): Promise<Order>;
    createSwapOrder(market: any, type: any, side: any, amount: any, price?: any, marginMode?: any, params?: {}): Promise<Order>;
    createOrders(orders: OrderRequest[], params?: {}): Promise<Order[]>;
    fetchOrder(id: string, symbol?: string, params?: {}): Promise<Order>;
    fetchOrders(symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<Order[]>;
    fetchOrdersByIds(ids: any, symbol?: string, params?: {}): Promise<Order[]>;
    fetchOpenOrders(symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<Order[]>;
    fetchClosedOrders(symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<Order[]>;
    fetchCanceledOrders(symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<Order[]>;
    fetchOrdersByState(state: any, symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<Order[]>;
    cancelOrder(id: string, symbol?: string, params?: {}): Promise<Order>;
    cancelOrders(ids: any, symbol?: string, params?: {}): Promise<Order[]>;
    cancelAllOrders(symbol?: string, params?: {}): Promise<Order[]>;
    parseOrder(order: any, market?: any): Order;
    parseOrderSide(status: any): string;
    parseOrderType(status: any): string;
    parseOrderStatus(status: any): string;
    parseOrderTimeInForce(status: any): string;
    fetchAccountHelper(type: any, params: any): Promise<any>;
    fetchAccounts(params?: {}): Promise<any[]>;
    fetchTradingFees(params?: {}): Promise<{}>;
    customParseBalance(response: any, marketType: any): Balances;
    parseBalanceHelper(entry: any): import("./base/types.js").Balance;
    fetchBalance(params?: {}): Promise<Balances>;
    fetchMyTrades(symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<Trade[]>;
    fetchOrderTrades(id: string, symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<Trade[]>;
    modifyMarginHelper(symbol: string, amount: any, addOrReduce: any, params?: {}): Promise<any>;
    reduceMargin(symbol: string, amount: any, params?: {}): Promise<any>;
    addMargin(symbol: string, amount: any, params?: {}): Promise<any>;
    setLeverage(leverage: any, symbol?: string, params?: {}): Promise<any>;
    fetchFundingHistory(symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<FundingHistory[]>;
    parseFundingRate(contract: any, market?: any): {
        info: any;
        symbol: any;
        markPrice: any;
        indexPrice: any;
        interestRate: any;
        estimatedSettlePrice: any;
        timestamp: number;
        datetime: string;
        fundingRate: number;
        fundingTimestamp: number;
        fundingDatetime: string;
        nextFundingRate: any;
        nextFundingTimestamp: any;
        nextFundingDatetime: any;
        previousFundingRate: any;
        previousFundingTimestamp: any;
        previousFundingDatetime: any;
    };
    fetchFundingRate(symbol: string, params?: {}): Promise<{
        info: any;
        symbol: any;
        markPrice: any;
        indexPrice: any;
        interestRate: any;
        estimatedSettlePrice: any;
        timestamp: number;
        datetime: string;
        fundingRate: number;
        fundingTimestamp: number;
        fundingDatetime: string;
        nextFundingRate: any;
        nextFundingTimestamp: any;
        nextFundingDatetime: any;
        previousFundingRate: any;
        previousFundingTimestamp: any;
        previousFundingDatetime: any;
    }>;
    fetchFundingRateHistory(symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<FundingRateHistory[]>;
    fetchLeverageTiers(symbols?: string[], params?: {}): Promise<{}>;
    parseMarketLeverageTiers(info: any, market?: any): any[];
    parseDepositAddress(depositAddress: any, currency?: any): {
        currency: any;
        address: string;
        tag: any;
        network: string;
        info: any;
    };
    fetchDepositAddressesByNetwork(code: string, params?: {}): Promise<any[]>;
    createDepositAddress(code: string, params?: {}): Promise<{
        info: any;
        currency: string;
        network: string;
        address: string;
        tag: string;
    }>;
    fetchDepositAddress(code: string, params?: {}): Promise<any>;
    fetchDeposits(code?: string, since?: Int, limit?: Int, params?: {}): Promise<Transaction[]>;
    fetchWithdrawals(code?: string, since?: Int, limit?: Int, params?: {}): Promise<Transaction[]>;
    parseTransaction(transaction: any, currency?: any): Transaction;
    parseTransactionStatusByType(status: any, type?: any): string;
    fetchPosition(symbol: string, params?: {}): Promise<Position>;
    fetchPositions(symbols?: string[], params?: {}): Promise<Position[]>;
    parsePosition(position: any, market?: any): Position;
    fetchTransfer(id: string, since?: Int, limit?: Int, params?: {}): Promise<{
        info: any;
        id: string;
        timestamp: number;
        datetime: string;
        currency: any;
        amount: number;
        fromAccount: string;
        toAccount: string;
        status: string;
    }>;
    fetchTransfers(code?: string, since?: Int, limit?: Int, params?: {}): Promise<any>;
    transfer(code: string, amount: any, fromAccount: any, toAccount: any, params?: {}): Promise<any>;
    parseTransfer(transfer: any, currency?: any): {
        info: any;
        id: string;
        timestamp: number;
        datetime: string;
        currency: any;
        amount: number;
        fromAccount: string;
        toAccount: string;
        status: string;
    };
    parseAccountId(status: any): string;
    parseTransferStatus(status: any): string;
    withdraw(code: string, amount: any, address: any, tag?: any, params?: {}): Promise<Transaction>;
    setPositionMode(hedged: any, symbol?: string, params?: {}): Promise<any>;
    fetchPositionMode(symbol?: string, params?: {}): Promise<{
        info: any;
        hedged: boolean;
    }>;
    borrowMargin(code: string, amount: any, symbol?: string, params?: {}): Promise<any>;
    repayMargin(code: string, amount: any, symbol?: string, params?: {}): Promise<any>;
    fetchTransactionFees(codes?: any, params?: {}): Promise<{
        withdraw: {};
        deposit: {};
        info: any;
    }>;
    parseTransactionFees(response: any, codes?: any): {
        withdraw: {};
        deposit: {};
        info: any;
    };
    parseTransactionFee(transaction: any, currency?: any): {};
    fetchDepositWithdrawFees(codes?: string[], params?: {}): Promise<any>;
    parseDepositWithdrawFee(fee: any, currency?: any): any;
    parseMarginLoan(info: any, currency?: any): {
        id: string;
        currency: any;
        amount: any;
        symbol: any;
        timestamp: any;
        datetime: any;
        info: any;
    };
    handleMarginModeAndParams(methodName: any, params?: {}, defaultValue?: any): any[];
    sign(path: any, api?: string, method?: string, params?: {}, headers?: any, body?: any): {
        url: any;
        method: string;
        body: any;
        headers: any;
    };
    handleErrors(code: any, reason: any, url: any, method: any, headers: any, body: any, response: any, requestHeaders: any, requestBody: any): any;
}
