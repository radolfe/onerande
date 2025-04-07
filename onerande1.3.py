import random
import tkinter as tk
from tkinter import messagebox

def 뽑기_모드_애니메이션():
    global updating
    updating = True
    update_game_mode()
    root.after(2000, show_final_game_mode)

def show_info():
    messagebox.showinfo("설명", "내가 어쩌다 원랜디를 시작해서...")

def update_game_mode():
    modes = ["고도전", "랜유전", "강제상위전", "신세계보상치기", "강제전설,히든", "필수상위(1~5)", "아이템전", "녜힁상위전"]
    선택된_모드.set(random.choice(modes))
    if updating:
        root.after(50, update_game_mode)

def 녜힁뽑기():
    consonants = ['도', '라', '고', '로', '보', '니', '로', '쿠', '규', '루', '피', '바', '호', '스', '사', '야', '마', '토',
                  '우', '조', '베', '쵸', '파', '후', '지', '수', '나', '미', '치', '기', '어', '포', '브', '디', '크', '시',
                  '아', '오', '키', '카', '이', '누', '타', '코', '비', '드', '자', '프', '거', '레', '리', '져', '퍼', '래',
                  '제', '트', '버', '슈', '에', '류', '르', '다', '노', '부', '커'
                  ]
    return random.choice(consonants)

def show_final_game_mode():
    global updating
    updating = False
    root.after(100, update_enabled_functions)

def update_enabled_functions():
    if updating:
        return

    mode = 선택된_모드.get()
    var_숫자뽑기.set(False)
    var_전설히든뽑기.set(False)
    var_필수상위.set(False)
    var_녜힁뽑기.set(False)
    var_팀나누기.set(False)

    if mode == "고도전":
        var_숫자뽑기.set(True)
    elif mode == "필수상위(1~5)":
        var_숫자뽑기.set(True)
    elif mode == "강제전설,히든":
        var_전설히든뽑기.set(True)
    elif mode == "강제상위전":
        var_필수상위.set(True)
    elif mode == "녜힁상위전":
        var_녜힁뽑기.set(True)
    elif mode == "신세계보상치기":
        var_팀나누기.set(True)
    elif mode == "랜유전":
        var_팀나누기.set(True)
    elif mode == "아이템전":
        var_팀나누기.set(True)

def on_checkbox_change(selected_var):
    var_숫자뽑기.set(False)
    var_전설히든뽑기.set(False)
    var_필수상위.set(False)
    var_녜힁뽑기.set(False)
    var_팀나누기.set(False)

    if selected_var:
        selected_var.set(True)

전설히든뽑기_리스트 = [
    "레일리", "마르코", "샬롯크래커", "센고쿠", "스모커", "시저", "에이스", "울티", "카르가라", "킹", "흰수염",
    "히바리", "티치", "모리아", "나미", "네코마무시", "레이쥬", "루치", "로우", "루피개틀링", "루나메", "상디",
    "슈가", "시노부", "토키", "조로", "징베", "제파", "코비", "핸콕", "히루루크", "드래곤", "라분", "바르톨",
    "샹크스", "시키", "후지토라", "쿠마", "레드포스호", "모비딕호", "반더데켄", "발라티에", "방주맥심", "써니호",
    "레베카", "료쿠큐", "미호크", "베르고", "사보", "코알라", "킬러", "퀸", "류마", "시류", "아카이누", "캐럿",
    "키쿠", "스튜시", "페로나", "봉쿠레", "아오키지", "이완코브", "피셔타이거"
]

필수상위_리스트 = [
    "에넬", "레드필드", "레베카", "알비다", "시노부", "아인", "카타쿠리", "크로커다일", "킹", "도플라밍고", "로빈", "보니", "로쿠규",
    "루피", "바질호킨스", "사보", "야마토", "우솝", "조로", "징베", "쵸파", "후지토라", "검은수염", "나미", "로우", "루치",
    "루피기어포스", "브룩", "상디", "샹크스", "시라호시", "아오키지", "아카이누", "타시기", "코비", "키드", "키자루", "프랑키", "거프",
    "레일리", "로져", "스코퍼가반", "카이도", "흰수염", "드래곤", "빅맘", "센고쿠", "제트", "버기", "카벤딧슈", "에이스", "핸콕",
    "오뎅", "류마", "미호크", "비비", "우타", "니카", "마르코"
]

# 가로 정렬 함수
def format_horizontal(items, items_per_line=4):
    lines = []
    for i in range(0, len(items), items_per_line):
        line = "".join(items[i:i + items_per_line])
        lines.append(line)
    return lines

def generate_random_result():
    results = []
    try:
        num_players = int(player_count_entry.get())
        if num_players <= 0:
            num_players = 4
    except ValueError:
        num_players = 4

    if var_숫자뽑기.get():
        try:
            max_value = int(entry_max_value.get())
            results.append((""))
            for _ in range(num_players):
                results.append((f"  {random.randint(1, max_value)}"))
        except ValueError:
            results.append(("숫자 뽑기: 최대값 오류"))

    if var_전설히든뽑기.get():
        results.append((""))
        for _ in range(num_players):
            results.append((f"  {random.choice(전설히든뽑기_리스트)}"))

    if var_필수상위.get():
        results.append((""))
        for _ in range(num_players):
            results.append((f"  {random.choice(필수상위_리스트)}"))

    if var_녜힁뽑기.get():
        results.append((""))

        consonants = ['도', '라', '고', '로', '보', '니', '로', '쿠', '규', '루', '피', '바', '호', '스', '사', '야', '마',
                      '토', '우', '조', '베', '쵸', '파', '후', '지', '수', '나', '미', '치', '기', '어', '포', '브', '디',
                      '크', '시', '아', '오', '키', '카', '이', '누', '타', '코', '비', '드', '자', '프', '거', '레', '리',
                      '져', '퍼', '래', '제', '트', '초', '버', '슈', '에', '류', '르', '다', '노', '부', '커']
        selected = random.sample(consonants, 2)

        results.append(("  " + " | ".join(selected)))

        matching_items = set()
        for item in 필수상위_리스트:
            for con in selected:
                if con in item:
                    matching_items.add(item)
                    break

        if matching_items:
            results.append((""))
            sorted_items = sorted(matching_items)
            result_line = " ".join(sorted_items)  # 그냥 공백으로만 연결
            results.append(result_line)

    if var_팀나누기.get():
        results.append((""))
        team_colors = ['빨', '파', '보', '노']
        random.shuffle(team_colors)
        teams = [team_colors[i % len(team_colors)] for i in range(num_players)]
        for i in range(0, num_players - 1, 2):
            results.append((f"  {teams[i]}, {teams[i + 1]}"))
        if num_players % 2 == 1:
            results.append((f"  {teams[-1]} (왕따 ㅋㅋ)",))

    return results

    if var_팀나누기.get():
        results.append("")
        team_colors = ['빨', '파', '보', '노']
        random.shuffle(team_colors)
        teams = [team_colors[i % len(team_colors)] for i in range(num_players)]
        team_pairs = [f"  {teams[i]}, {teams[i + 1]}" for i in range(0, num_players - 1, 2)]
        if num_players % 2 == 1:
            team_pairs.append(f"  {teams[-1]} (왕따 ㅋㅋ)")
        results.extend(team_pairs)

    return results

def update_random_result():
    if not updating:
        return

    results = generate_random_result()

    # 모든 항목을 str로 변환해서 join
    result_label.config(
        text="\n".join(str(line) for line in results),
        justify="center"
    )
    root.after(50, update_random_result)

def copy_to_clipboard():
    result = result_label.cget("text").strip()
    root.clipboard_clear()
    root.clipboard_append(result)
    root.update()  # 클립보드 업데이트 보장

def show_final_result():
    global updating
    updating = False
    update_random_result()

def run_program():
    global updating
    updating = True
    update_random_result()
    root.after(2000, show_final_result)

root = tk.Tk()
root.title("원랜디 룰렛 v1.3")
root.geometry("400x850")
root.configure(bg="black")

# 창 크기 고정
root.resizable(False, False)  # Disable resizing in both horizontal and vertical directions

# Info Button
info_button = tk.Button(root, text="?", command=show_info, bg="black", fg="white", font=("맑은 고딕", 15),
                        width=1, height=1, relief="flat")
info_button.place(x=370, y=10)

# Game Mode Button
선택된_모드 = tk.StringVar()
mode_button = tk.Button(root, text="게임 모드 뽑기", command=뽑기_모드_애니메이션, bg="black", fg="white", font=("맑은 고딕", 15),
                        width=13, height=1)
mode_button.pack(pady=10)

mode_label = tk.Label(root, textvariable=선택된_모드, font=("맑은 고딕", 21), bg="black", fg="white")
mode_label.pack(pady=5)

frame = tk.Frame(root, bg="black")
frame.pack(pady=10)

# Player Count
player_count_label = tk.Label(root, text="플레이 인원 수", font=("맑은 고딕", 15), bg="black", fg="white")
player_count_label.pack(pady=5)

player_count_entry = tk.Entry(root, width=5, font=("맑은 고딕", 15))
player_count_entry.insert(0, "4")
player_count_entry.pack(pady=10)

# Checkboxes and Inputs
var_숫자뽑기 = tk.BooleanVar()
숫자뽑기_checkbox = tk.Checkbutton(frame, text="숫자 뽑기", variable=var_숫자뽑기, bg="black", fg="white", selectcolor="black",
                               font=("맑은 고딕", 18), command=lambda: on_checkbox_change(var_숫자뽑기))
숫자뽑기_checkbox.grid(row=0, column=0, columnspan=2)
entry_max_value = tk.Entry(frame, width=7, bg="white", fg="black", font=("맑은 고딕", 18))
entry_max_value.grid(row=1, column=0, columnspan=2, pady=5)

var_전설히든뽑기 = tk.BooleanVar()
전설히든뽑기_checkbox = tk.Checkbutton(frame, text="전설히든뽑기", variable=var_전설히든뽑기, bg="black", fg="white", selectcolor="black",
                             font=("맑은 고딕", 18), command=lambda: on_checkbox_change(var_전설히든뽑기))
전설히든뽑기_checkbox.grid(row=2, column=0)

var_필수상위 = tk.BooleanVar()
필수상위_checkbox = tk.Checkbutton(frame, text="필수상위", variable=var_필수상위, bg="black", fg="white", selectcolor="black",
                               font=("맑은 고딕", 18), command=lambda: on_checkbox_change(var_필수상위))
필수상위_checkbox.grid(row=3, column=0)

var_녜힁뽑기 = tk.BooleanVar()
녜힁뽑기_checkbox = tk.Checkbutton(
    frame, text="녜힁뽑기", variable=var_녜힁뽑기, bg="black", fg="white",
    selectcolor="black", font=("맑은 고딕", 18),
    command=lambda: on_checkbox_change(var_녜힁뽑기)
)
녜힁뽑기_checkbox.grid(row=4, column=0, pady=5)

var_팀나누기 = tk.BooleanVar()
팀나누기_checkbox = tk.Checkbutton(frame, text="팀 나누기", variable=var_팀나누기, bg="black", fg="white", selectcolor="black",
                               font=("맑은 고딕", 18), command=lambda: on_checkbox_change(var_팀나누기))
팀나누기_checkbox.grid(row=5, column=0)

# Result Button
result_button = tk.Button(root, text="결과 보기", command=run_program, bg="black", fg="white", font=("맑은 고딕", 15), width=10,
                          height=1)
result_button.pack(pady=1)

# ✅ Result Label (중앙 정렬 개선!)
result_label = tk.Label(
    root,
    text="",
    font=("맑은 고딕", 16),  # 고정폭 폰트 사용
    bg="black",
    fg="white",
    justify="center",      # 줄 내 중앙 정렬
    anchor="center",        # 전체 텍스트 중앙 정렬
    wraplength=360         # 픽셀 단위로 줄바꿈 너비 설정
)
result_label.pack(pady=10, fill="both", expand=True)  # 공간 내에서 가운데 정렬

# Copy Button
copy_button = tk.Button(root, text="결과 복사하기", command=copy_to_clipboard, bg="black", fg="white", font=("맑은 고딕", 15), width=12, height=1)
copy_button.pack(pady=10)

root.mainloop()