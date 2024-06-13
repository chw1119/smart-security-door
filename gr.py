import matplotlib.pyplot as plt

# 데이터 정의
labels = ['asan::Allocator', 'asan::callback', 'asan::threadLocalStorage', 'Other sanitizer overhead']
sizes = [25.5, 12.8, 10.5, 51.2]
colors = ['#80B1D3', '#8DD3C7', '#FDB462', '#FB8072']

# 그래프 그리기
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#0D3E66')
ax.set_facecolor('#0D3E66')

wedges, texts, autotexts = ax.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=140, textprops={'color': 'white'})

# 타이틀 설정
plt.title('Google Sanitizer Overhead', color='white', fontsize=16, weight='bold')

# 텍스트 색상 설정
for text in texts:
    text.set_color('white')
for autotext in autotexts:
    autotext.set_color('white')

# 저장
plt.savefig("sanitizer_overhead_high_res.png", format='png', facecolor='#0D3E66', dpi=900)
# 그래프 표시
plt.show()