from FinMind.data import DataLoader

# 初始化 DataLoader
api = DataLoader()

# 獲取台灣股票清單
stock_list = api.taiwan_stock_info()

# 將要操作的DataFrame列出所有不重複的industry_category項目
industry_categories = stock_list['industry_category'].unique()

# 打印項目
for category in industry_categories:
    print(category)

# 將項目存檔到文件中
with open('industry_categories.txt', 'w') as file:
    for category in industry_categories:
        file.write(f'{category}\n')
