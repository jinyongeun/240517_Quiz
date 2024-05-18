def number(resident_registration_number, multipliers):
    total = 0
    for a in range(12):
        total += int(resident_registration_number[a]) * multipliers[a]
    b = total % 11
    check = 11 - b

    return check

resident_registration = input("주민등록번호를 입력하세요: ")

resident_registration_number = resident_registration.replace('-','')

multipliers = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

check = number(resident_registration_number, multipliers)

if check == int(resident_registration_number[12]):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")