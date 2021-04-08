import os

def read_file(filename): #讀取檔案
    products = []
    with open (filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
    return(products)

def user_input(products): #讓使用者輸入
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        price = int(price)
        products.append([name, price])
    print(products)
    return products

def print_product(products):#印出所有購買紀錄
    for p in products:
        print(p[0], '的價格是', p[1])
def write_file(filename, products): #寫入檔案
    filename = 'products.csv'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
    if os.path.isfile('products.csv'): # 檢查檔案在不在
        print('Yeah!找到檔案了')
        products = read_file('products.csv')
        
    else:
        print('找不到檔案...')
    products = user_input(products)
    print_product(products)
    write_file('products.csv', products)

main()



