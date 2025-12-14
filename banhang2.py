
# Số máy 
maybans = {
    "nuoc": {
        "Coca": {"gia": 12000, "sl": 5},
        "Pepsi": {"gia": 11000, "sl": 4},
        "Sting": {"gia": 10000, "sl": 3}
    },
    "keo": {
        "Kẹo dẻo": {"gia": 5000, "sl": 10},
        "Kẹo bạc hà": {"gia": 4000, "sl": 8},
        "Kẹo chanh": {"gia": 3000, "sl": 6}
    }
}

# --- HÀM HIỂN THỊ MENU SẢN PHẨM (mặc định giao diện có thể chỉnh nếu muốn đẹp)
def sanpham(mayban):
    print(f"\n--- MÁY BÁN: {mayban.upper()} ---")
    hanghoa = maybans[mayban]
    for i, ten in enumerate(hanghoa, 1):
        gia = hanghoa[ten]["gia"]
        sl = hanghoa[ten]["sl"]
        print(f"{i}. {ten} - {gia}đ - còn {sl}")

# --- HÀM MUA
def mua(mayban, tien):
    hanghoa = maybans[mayban]
    ten = list(hanghoa.keys())

    while True:
        sanpham(mayban)
        print("0. Thoát máy này")
        chon = input("Chọn sản phẩm: ")

        if chon == "0":
            return tien

        if not chon.isdigit() or not (1 <= int(chon) <= len(ten)):
            print("Sai lựa chọn.")
            continue

        sp = ten[int(chon)-1]
        gia = hanghoa[sp]["gia"]
        sl = hanghoa[sp]["sl"]

        if sl <= 0:
            print("Hết hàng rồi.")
            continue
        if tien < gia:
            print("Không đủ tiền.")
            continue

        tien -= gia
        hanghoa[sp]["sl"] -= 1
        print(f"Mua {sp} thành công! Tiền còn lại: {tien}đ")


# Hàm nạp
def nap_tien(tien):
    them = input("Nhập số tiền muốn nạp: ")
    if not them.isdigit():
        print("Tiền mà nhập chữ là sao!")
        return tien
    them = int(them)
    tien += them
    print(f"Đã nạp {them}đ  | Tổng tiền hiện có: {tien}đ")
    return tien

# --- MAIN
def main():
    
    while True:
        tien = input("Nhập tiền bạn vào: ")
        if not tien.isdigit():
            print("Tiền mà nhập chữ là sao?")
            continue
        tien = int(tien)
        break
    while True:
        print("\n--- CHỌN MÁY BÁN HÀNG ---")
        for i, m in enumerate(maybans, 1):
            print(f"{i}. Máy bán {m}")
        print("p. Nạp thêm tiền ")
        print("0. Thoát chương trình")

        chon = input("Chọn: ")

        if chon == "0":
            break

        if chon.lower() == "p":
            tien = nap_tien(tien)
            continue

        mkeys = list(maybans.keys())
        if not chon.isdigit() or not (1 <= int(chon) <= len(mkeys)):
            print("Sai lựa chọn.")
            continue

        lua_chon = mkeys[int(chon)-1]
        tien = mua(lua_chon, tien)


main()
