def get_books_to_buy(N, M1, my_books, M2, shop_books):
    books_to_buy = sorted(set(shop_books) - set(my_books))
    return " ".join(map(str, books_to_buy)) if books_to_buy else "None"


N = int(input())
M1 = int(input())
my_books = list(map(int, input().split()))
M2 = int(input())
shop_books = list(map(int, input().split()))

result = get_books_to_buy(N, M1, my_books, M2, shop_books)
print(result)
