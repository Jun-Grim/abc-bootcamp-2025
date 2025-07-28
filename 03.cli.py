from dotenv import load_dotenv
from ai import get_personality_analysis

load_dotenv()

print("AI 관상가입니다. 얼굴 특징을 입력해수지면, 성격과 미래를 전망해 드릴게요 ")
line = input("얼굴특징 : ").strip()



if not line:
    print("error, 특징이 입력되지 않았습니다.")
else:
    print("입력하신 얼굴 특징:",line)
    print("분석중.....")
    result = get_personality_analysis(line)
    print("분석완료")
    print(result)
# print(repr(line))



# get_personality_analysis()
