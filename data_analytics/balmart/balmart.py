import pandas as pd
from matplotlib import pyplot as plt

data = pd.ExcelFile('data/Balmart Store.xlsx', encoding='latin-1')
orders_header = [
    'row_id', 'order_priority', 'discount', 'unit_price', 'shipping_cost',
    'customer_id', 'customer_name', 'ship_mode',
    'customer_segment', 'product_category', 'product_subcategory',
    'product_container', 'product_name', 'product_base_margin', 'country', 'region',
    'state', 'city', 'postal_code', 'order_date', 'ship_date',
    'profit', 'quantity_ordered_new', 'sales', 'order_id'
]

orders = data.parse(0, header=None, names=orders_header)
returns = data.parse(1)
managers = data.parse(2)

# print('orders'.center(60, '='))
# print(orders.head())
# print(orders.dtypes)
#
# print('returns'.center(60, '='))
# print(returns.head())
# print(returns.dtypes)
#
# print('managers'.center(60, '='))
# print(managers.head())
# print(managers.dtypes)

# Sales Over Time
prof = orders.groupby(['order_date', 'product_category']).sum()['profit'].unstack().plot(kind='line')
sales = orders.groupby(['order_date', 'product_category']).sum()['sales'].unstack().plot(kind='line')
prof.set_ylim(-7500, 7500)
plt.show()

a = orders['product_category'].drop_duplicates()
b = orders['product_subcategory'].drop_duplicates()

print(a)
print(b)

# Profit and Profit Margin per Subcategory

# prof = orders.groupby(['product_category', 'product_subcategory']).sum()['profit'].unstack().plot(kind='bar')
# plt.show()
#
# orders['profit_margin'] = orders['profit'] / orders['sales']
#
# prof_marg = orders.groupby(['product_category', 'product_subcategory']).sum()['profit_margin'].unstack().plot(kind='bar')
# plt.show()
