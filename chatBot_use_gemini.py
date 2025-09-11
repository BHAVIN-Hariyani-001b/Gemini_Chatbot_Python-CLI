from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="GEMINI_API_KEY")

while True:
    user = input("You : ")

    if user.lower() in ["exit","quit"]:
        print(": Goodbye!")
        break

    try:    
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=user
        )
    except Exception as e:
        print(f"Error : {e}")

    print(f"Gemini : {response.text}\n")