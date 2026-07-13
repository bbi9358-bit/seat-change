import random

# 학생 번호 생성 (1번 ~ 20번)
students = list(range(1, 21))

# 랜덤으로 섞기
random.shuffle(students)

# 자리 배치 (4행 × 5열)
rows = 4
cols = 5

print("=" * 35)
print("      랜덤 자리 배치")
print("=" * 35)

index = 0
for r in range(rows):
    for c in range(cols):
        print(f"{students[index]:>2}번", end="\t")
        index += 1
    print()

print("=" * 35)
