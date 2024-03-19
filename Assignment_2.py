class Stock:
    def __init__(self, code):
        self.code = code
        self.prices = []

    def add_price(self, open_price, close_price):
        self.prices.append((open_price, close_price))

    def average_price_difference(self):
        if not self.prices:
            return 0
        total_difference = sum(close - open for open, close in self.prices)
        return total_difference / len(self.prices)

    def max_min_prices(self):
        if not self.prices:
            return None, None
        max_price = max(close for open, close in self.prices)
        min_price = min(close for open, close in self.prices)
        return max_price, min_price

def read_file(filename):
    stocks = {}
    with open(filename, 'r') as file:
        num_stocks = int(file.readline().strip())
        for _ in range(num_stocks):
            code, open_price, close_price = file.readline().strip().split()
            open_price = float(open_price)
            close_price = float(close_price)
            if code not in stocks:
                stocks[code] = Stock(code)
            stocks[code].add_price(open_price, close_price)
    return stocks

def print_sorted_stocks(stocks):
    sorted_codes = sorted(stocks.keys())
    for code in sorted_codes:
        stock = stocks[code]
        avg_diff = stock.average_price_difference()
        print(f"{code}: {avg_diff:.3f}")

def search_stock(stocks, code):
    if code in stocks:
        max_price, min_price = stocks[code].max_min_prices()
        if max_price is not None and min_price is not None:
            print(f"Max price: {max_price:.3f}, Min price: {min_price:.3f}")
        else:
            print("Không có dữ liệu giá cho mã chứng khoán này.")
    else:
        print("Không tìm thấy mã chứng khoán.")

def find_trending_stocks(stocks):
    trending_stocks = []
    for code, stock in stocks.items():
        if len(stock.prices) >= 2:
            if stock.prices[0][1] > stock.prices[0][0] and stock.prices[1][1] > stock.prices[1][0]:
                trending_stocks.append(code)
    print("Các mã cổ phiếu có xu hướng tăng đồng thời trong ngày 1 và ngày 2:")
    print(trending_stocks)

def find_longest_increasing_stocks(stocks):
    max_increase = max(len(stock.prices) for stock in stocks.values())
    longest_stocks = [code for code, stock in stocks.items() if len(stock.prices) == max_increase]
    print(f"Mã có số ngày tăng lớn nhất ({max_increase} ngày):")
    print(longest_stocks)

if __name__ == "__main__":
    filename = "data.txt"
    stocks = read_file(filename)
    while True:
        print("\n===== MENU =====")
        print("1. In thông tin các mã chứng khoán")
        print("2. Tìm kiếm theo mã chứng khoán")
        print("3. Tìm mã chứng khoán có xu hướng tăng")
        print("4. Tìm mã có số ngày tăng lớn nhất")
        print("5. Thoát chương trình")
        choice = input("Chọn chức năng (1-5): ")
        
        if choice == "1":
            print_sorted_stocks(stocks)
        elif choice == "2":
            code = input("Nhập mã chứng khoán: ")
            search_stock(stocks, code)
        elif choice == "3":
            find_trending_stocks(stocks)
        elif choice == "4":
            find_longest_increasing_stocks(stocks)
        elif choice == "5":
            print("Tác giả: [Họ và tên sinh viên] - [MSSV]")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
