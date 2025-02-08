import openai

# OpenAI API 키 설정
API_KEY = "sk-proj-a3HxB..." # 여기에 OpenAI API 키 입력

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 또는 "gpt-4"
        # model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,  # 응답의 창의성 조절
        max_tokens=200  # 응답 길이 제한
    )
    return response["choices"][0]["message"]["content"]

# 실행 예제
if __name__ == "__main__":
    user_input = input("ChatGPT에게 물어볼 내용을 입력하세요: ")
    response = chat_with_gpt(user_input)
    print("\nChatGPT 응답:", response)
