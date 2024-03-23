def classify_gpa_4scale(gpa):
    if gpa < 0 or gpa > 4:
        return "GPA không hợp lệ"
    elif gpa >= 3.6:
        return "Xuất sắc"
    elif gpa >= 3.2:
        return "Giỏi"
    elif gpa >= 2.5:
        return "Khá"
    else:
        return "Trung bình"

# Kiểm thử
test_cases_4scale = [
    (3.6, "Xuất sắc"),
    (3.2, "Giỏi"),
    (2.5, "Khá"),
    (2.0, "Trung bình"),
    (-1.0, "GPA không hợp lệ")
]
for gpa, expected in test_cases_4scale:
    result = classify_gpa_4scale(gpa)
    assert result == expected, f"Test failed for GPA {gpa}. Expected {expected}, got {result}"
print("Tất cả ca kiểm thử đều thành công!")
