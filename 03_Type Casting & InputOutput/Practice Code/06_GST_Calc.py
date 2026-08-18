price = float(input("Enter the Price:"))

gst = price * 18 / 100

total_price = price + gst

print(f"GST: ₹{gst}")
print(f"Total Price is: ₹{total_price}")