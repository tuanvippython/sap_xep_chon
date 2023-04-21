# Sử dụng hàm split để nhập dãy số
list = input("Nhập dãy số nguyên, cách nhau bằng dấu cách: ").split()
a = [int(num) for num in list]
print("Dãy số vừa nhập là: ",a)

print("----Dãy số sau khi sắp xếp tăng dần----")

# Sử dụng vòng lặp for với biến i để duyệt qua từng phần tử trong danh sách (chạy từ phần tử đầu tiên đến phần tử cuối cùng)
for i in range(len(a)):
    # Sử dụng vòng lặp for với biến j để duyệt qua các phần tử còn lại trong danh sách (phần tử tiếp theo của i)
    for j in range(i+1,len(a)):
        # Ta sẽ so sánh phần tử đầu tiên của list với các phần tử còn lại của list
        # Nếu phần tử đầu tiên lớn hơn phần tử phía bên phải của nó thì sẽ thực hiện đổi chỗ cho nhau
        # Vòng lặp sẽ kết thúc khi list được sắp xếp các phần tử theo chiều tăng dần
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print(a)

print("----Dãy số sau khi sắp xếp giảm dần----")

# Sử dụng vòng lặp for với biến i để duyệt qua từng phần tử trong danh sách (chạy từ phần tử đầu tiên đến phần tử cuối cùng)
for i in range(len(a)):
    # Sử dụng vòng lặp for với biến j để duyệt qua các phần tử còn lại trong danh sách (phần tử tiếp theo của i)
    for j in range(i+1,len(a)):
        # Ta sẽ so sánh phần tử đầu tiên của list với các phần tử còn lại của list
        # Nếu phần tử đầu tiên nhỏ hơn phần tử phía bên phải của nó thì sẽ thực hiện đổi chỗ cho nhau
        # Vòng lặp sẽ kết thúc khi list được sắp xếp các phần tử theo chiều giảm dần
        if a[i] < a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print(a)