import openai, os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('API_KEY')


def generate_keywords(summary: str, rule: str):
    prompt = f"You're this person {summary}, Generate keywords to add in the last page of your resume to prevent being excluded from filtering algorithms for a rule of {rule}. exclude company names and focus in your skills."
    chat = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0,
        stop=None,
        n=1,
    )
    return chat.choices[0].text.strip()

# # Example usage
summary = "Experienced Software Developer with skills in Full-Stack development, Automation, AI, and UI/UX Design. Proven track record with companies like Jobati, Kr8vSolutions, My Karaj, Syara Finder, River Blood, and Junky Helmets. Specialized in Fullstack and UI/UX. Established Taskure, a startup providing digital solutions with a track record of multiple projects. Ready to enhance your team with versatile expertise."
rule = "python developer"
for i in range(15):
    keywords = generate_keywords(summary, rule)
    print(keywords)

