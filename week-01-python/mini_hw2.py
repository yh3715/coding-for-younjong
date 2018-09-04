
class 학교:
    def __init__(self, 이름, 설립연도, 주소):
        self.이름 = 이름
        self.설립연도 = 설립연도
        self.주소 = 주소

school = 학교("중앙", "1960", "동작구")

print(school.이름)
print(school.주소)
print(school.설립연도)
