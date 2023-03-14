import { Exchange } from './base/Exchange.js';
export default class cryptocom extends Exchange {
    describe(): any;
    fetchMarkets(params?: {}): Promise<any>;
    fetchSpotMarkets(params?: {}): Promise<any[]>;
    fetchDerivativesMarkets(params?: {}): Promise<any[]>;
    fetchTickers(symbols?: any, params?: {}): Promise<any>;
    fetchTicker(symbol: any, params?: {}): Promise<import("./base/types.js").Ticker>;
    fetchOrders(symbol?: any, since?: any, limit?: any, params?: {}): Promise<import("./base/types.js").Order[]>;
    fetchTrades(symbol: any, since?: any, limit?: any, params?: {}): Promise<import("./base/types.js").Trade[]>;
    fetchOHLCV(symbol: any, timeframe?: string, since?: any, limit?: any, params?: {}): Promise<import("./base/types.js").OHLCV[]>;
    fetchOrderBook(symbol: any, limit?: any, params?: {}): Promise<import("./base/types.js").OrderBook>;
    parseSwapBalance(response: any): import("./base/types.js").Balances;
    parseSpotBalance(response: any): import("./base/types.js").Balances;
    fetchBalance(params?: {}): Promise<any>;
    fetchOrder(id: any, symbol?: any, params?: {}): Promise<any>;
    createOrder(symbol: any, type: any, side: any, amount: any, price?: any, params?: {}): Promise<any>;
    cancelAllOrders(symbol?: any, params?: {}): Promise<any>;
    cancelOrder(id: any, symbol?: any, params?: {}): Promise<any>;
    fetchOpenOrders(symbol?: any, since?: any, limit?: any, params?: {}): Promise<import("./base/types.js").Order[]>;
    fetchMyTrades(symbol?: any, since?: any, limit?: any, params?: {}): Promise<import("./base/types.js").Trade[]>;
    parseAddress(addressString: any): any[];
    withdraw(code: any, amount: any, address: any, tag?: any, params?: {}): Promise<{
        info: any;
        id: string;
        txid: string;
        timestamp: number;
        datetime: string;
        network: any;
        address: any;
        addressTo: any;
        addressFrom: any;
        tag: any;
        tagTo: any;
        tagFrom: any;
        type: any;
        amount: number;
        currency: any;
        status: any;
        updated: number;
        internal: any;
        fee: any;
    }>;
    fetchDepositAddressesByNetwork(code: any, params?: {}): Promise<{}>;
    fetchDepositAddress(code: any, params?: {}): Promise<any>;
    safeNetwork(networkId: any): string;
    fetchDeposits(code?: any, since?: any, limit?: any, params?: {}): Promise<object[]>;
    fetchWithdrawals(code?: any, since?: any, limit?: any, params?: {}): Promise<object[]>;
    transfer(code: any, amount: any, fromAccount: any, toAccount: any, params?: {}): Promise<{
        info: any;
        id: string;
        timestamp: any;
        datetime: string;
        currency: any;
        amount: any;
        fromAccount: any;
        toAccount: any;
        status: any;
    }>;
    fetchTransfers(code?: any, since?: any, limit?: any, params?: {}): Promise<object[]>;
    parseTransferStatus(status: any): string;
    parseTransfer(transfer: any, currency?: any): {
        info: any;
        id: string;
        timestamp: any;
        datetime: string;
        currency: any;
        amount: any;
        fromAccount: any;
        toAccount: any;
        status: any;
    };
    parseTicker(ticker: any, market?: any): import("./base/types.js").Ticker;
    parseTrade(trade: any, market?: any): import("./base/types.js").Trade;
    parseOHLCV(ohlcv: any, market?: any): number[];
    parseOrderStatus(status: any): string;
    parseTimeInForce(timeInForce: any): string;
    parseOrder(order: any, market?: any): any;
    parseDepositStatus(status: any): string;
    parseWithdrawalStatus(status: any): string;
    parseTransaction(transaction: any, currency?: any): {
        info: any;
        id: string;
        txid: string;
        timestamp: number;
        datetime: string;
        network: any;
        address: any;
        addressTo: any;
        addressFrom: any;
        tag: any;
        tagTo: any;
        tagFrom: any;
        type: any;
        amount: number;
        currency: any;
        status: any;
        updated: number;
        internal: any;
        fee: any;
    };
    repayMargin(code: any, amount: any, symbol?: any, params?: {}): Promise<any>;
    borrowMargin(code: any, amount: any, symbol?: any, params?: {}): Promise<any>;
    parseMarginLoan(info: any, currency?: any): {
        id: number;
        currency: any;
        amount: any;
        symbol: any;
        timestamp: any;
        datetime: any;
        info: any;
    };
    fetchBorrowInterest(code?: any, symbol?: any, since?: any, limit?: any, params?: {}): Promise<object[]>;
    parseBorrowInterest(info: any, market?: any): {
        symbol: any;
        marginMode: any;
        currency: any;
        interest: number;
        interestRate: number;
        amountBorrowed: any;
        timestamp: number;
        datetime: string;
        info: any;
    };
    fetchBorrowRates(params?: {}): Promise<any[]>;
    parseBorrowRates(info: any, codeKey: any): any[];
    customHandleMarginModeAndParams(methodName: any, params?: {}): any[];
    nonce(): number;
    sign(path: any, api?: string, method?: string, params?: {}, headers?: any, body?: any): {
        url: string;
        method: string;
        body: any;
        headers: any;
    };
    handleErrors(code: any, reason: any, url: any, method: any, headers: any, body: any, response: any, requestHeaders: any, requestBody: any): void;
}
