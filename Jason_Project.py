import tkinter

def calculate():
    try:
        a = int(a_entry.get())
        b = int(b_entry.get())
    except ValueError:
        result_label.config(text="請輸入有效整數")
        return
    
    x = a - b
    y = 2 * b - a
    
    
    if x > 0 and y > 0 and x < 13 and y < 13:
        result_label.config(text=f"需要2隻 {x} 星超量怪獸，1隻 {y} 星融合怪獸")
    else:
        a_min = max(b + 1, 2 * b - 12)
        a_max = min(b + 12, 2 * b - 1)
        
        if a_min <= a_max:
            advice = ""
            if a < a_min:
                delta = a_min - a
                advice = f"場上還需要增加{delta}張卡，"
            elif a > a_max:
                delta = a - a_max
                advice = f"場上還需要减少{delta}張卡"
            result_text = f"無法發動。{advice} 有效卡的數量範圍是{a_min}到{a_max}。"
        else:
            result_text = "無法發動且無法調整a滿足條件。"
        result_label.config(text=result_text)

# 主窗口
window = tkinter.Tk()
window.title("連栗炮計算器")

# 輸入
tkinter.Label(window, text="場上和手牌卡數量:").grid(row=0, column=0, padx=5, pady=5)
a_entry = tkinter.Entry(window)
a_entry.grid(row=0, column=1, padx=5, pady=5)

tkinter.Label(window, text="目標怪獸星級:").grid(row=1, column=0, padx=5, pady=5)
b_entry = tkinter.Entry(window)
b_entry.grid(row=1, column=1, padx=5, pady=5)

# 按鈕
tkinter.Button(window, text="計算", command=calculate).grid(row=2, columnspan=2, padx=5, pady=5)

# 結果
result_label = tkinter.Label(window, text="", fg="blue")
result_label.grid(row=3, columnspan=2, padx=5, pady=5)

window.mainloop()