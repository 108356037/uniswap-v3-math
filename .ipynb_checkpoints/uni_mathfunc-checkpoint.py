import math

# def liquidity(x, y):
#     return math.sqrt(x * y)


# def sqrtp(x, y):
#     return math.sqrt(x / y)


def price_to_tick(price_no_sqrt):
    """price_to_tick takes in the price as y/x without square rooted"""
    return math.floor(math.log(price_no_sqrt, 1.0001))


def price_no_sqrtp_to_uniswapX96(price_no_sqrt):
    """
    price_no_sqrtp_to_uniswapX96 takes in the price as y/x without square rooted

    Uniswap uses Q64.96 number to store price
    """
    return int(math.sqrt(price_no_sqrt) * (2**96))

def price_with_sqrtp_to_uniswapX96(price_with_sqrt):
    """price_with_sqrtp_to_uniswapX96 takes in the price as sqrt(y/x)

    Uniswap uses Q64.96 number to store price
    """
    return int(price_with_sqrt * (2**96))

def liquidity_x_X(amount, sqrt_a, sqrt_b):
    """takes in prices in the format of sqrt(y/x)"""
    b = max(sqrt_a, sqrt_b)
    c = min(sqrt_a, sqrt_b)
    return int(amount * b * c / (b - c))



# def liquidity_y(amount, sqrt_a, sqrt_b):
#     """takes in prices in the format of sqrt(y/x)"""
#     c = max(sqrt_a, sqrt_b)
#     a = min(sqrt_a, sqrt_b)
#     return int(amount / (c - a))



# def amount_x_to_pool(liquidity, sqrt_a, sqrt_b):
#     """takes in prices in the format of sqrt(y/x)"""
#     b = max(sqrt_a, sqrt_b)
#     c = min(sqrt_a, sqrt_b)
#     return int(liquidity * (b - c) / (b * c))



# def amount_y_to_pool(amount, sqrt_a, sqrt_b):
#     """takes in prices in the format of sqrt(y/x)"""
#     c = max(sqrt_a, sqrt_b)
#     a = min(sqrt_a, sqrt_b)
#     return int(amount * (c - a))

def liquidity_x(amount, x, y):
    '''takes in prices in the format of y/x'''
    b = max(math.sqrt(x), math.sqrt(y))
    c = min(math.sqrt(x), math.sqrt(y))
    return int(amount * b * c / (b - c))



def liquidity_y(amount, x, y):
    """takes in prices in the format of y/x"""
    c = max(math.sqrt(x), math.sqrt(y))
    a = min(math.sqrt(x), math.sqrt(y))
    return int(amount / (c - a))



def amount_x_to_pool(liquidity, x, y):
    """takes in prices in the format of y/x"""
    b = max(math.sqrt(x), math.sqrt(y))
    c = min(math.sqrt(x), math.sqrt(y))
    return int(liquidity * (b - c) / (b * c))



def amount_y_to_pool(amount, x, y):
    """takes in prices in the format of y/x"""
    c = max((math.sqrt(x), math.sqrt(y)))
    a = min((math.sqrt(x), math.sqrt(y)))
    return int(amount * (c - a))