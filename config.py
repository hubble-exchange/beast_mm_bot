ETH = {
    "name": "ETH-Perp",
    "marginShare": 0.33,
    "leverage": 5,
    "refreshTolerance": 0.03,
    "orderExpiry": 2,
    "defensiveSkew": 0.01,
    "priceFeed": "binance-futures",
    "orderLevels": {
        "1": {
            "spread": 0.01,
            "qty": 0.12,
            "refreshTolerance": 0
        },
        "2": {
            "spread": 0.03,
            "qty": 0.23,
            "refreshTolerance": 0
        },
        "3": {
            "spread": 0.05,
            "qty": 0.45,
            "refreshTolerance": 0
        }
    }
}

AVAX = {
    "name": "AVAX-Perp",
    "marginShare": 1,
    "leverage": 2,
    "refreshTolerance": 0.03,
    "orderExpiry": 2,
    "defensiveSkew": 0.01,
    "priceFeed": "binance-futures",
    "orderLevels": {
        "1": {
            "spread": 0.01,
            "qty": 16,
            "refreshTolerance": 0
        },
        "2": {
            "spread": 0.02,
            "qty": 42,
            "refreshTolerance": 0
        },
        "3": {
            "spread": 0.03,
            "qty": 69,
            "refreshTolerance": 0
        }
    }
}

SOL = {
    "name": "SOL-Perp",
    "marginShare": 0.33,
    "leverage": 5,
    "refreshTolerance": 0.03,
    "orderExpiry": 2,
    "defensiveSkew": 0.01,
    "priceFeed": "binance-futures",
    "orderLevels": {
        "1": {
            "spread": 0.01,
            "qty": 3.1,
            "refreshTolerance": 0
        },
        "2": {
            "spread": 0.02,
            "qty": 4.2,
            "refreshTolerance": 0
        },
        "3": {
            "spread": 0.03,
            "qty": 5.3,
            "refreshTolerance": 0
        }
    }
}
