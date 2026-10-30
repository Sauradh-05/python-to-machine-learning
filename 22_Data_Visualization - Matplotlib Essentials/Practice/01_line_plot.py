import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

sales = [120, 150, 135, 200, 220, 250]

plt.plot(
    months,
    sales,
    marker ='o',
    color ='blue',
    linestyle ='-',
    linewidth = 2,
    
)

plt.title('Monthly Sales Trend')
plt.xlabel('Months')
plt.ylabel('Sales')

plt.grid(True)
plt.show()
