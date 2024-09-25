from fetch_scheme_details import fetch_scheme_details
from save_argument import save_argument
from openai import OpenAI
import openai
import os
# os.environ['OPENAI_API_KEY'] =
client = OpenAI()
client.api_key = os.getenv('API_KEY')


def generateWithChatGPT(topic, stance, scheme):
    scheme_details = fetch_scheme_details(scheme)

    # Pretext
    pretext = ("You are an expert in Argumentation Theory. You know about so-called Walton argumentation schemes. "
               "These schemes consist of premises, a conclusion and critical questions the argument has to provide answers for. You are given either 1, 2 or 3 premises. Make sure to only use the premises explicitly specified."
               "In the following you are given a stance, and topic and a Walton scheme. Generate an argument according to the specified scheme."
               "Placeholder variables are delimited by $. Clarify which concrete instances these placeholders represent in your specific argument. "
               "The generated argument will be used in a realistic context, therefore it shall have no artificial placeholders."
               "Provide your comprehensive argument following the given scheme and analyze it carefully. "
               "Explain your way of reasoning precisely. Also clarify the used premises and the conclusion separately: "
               "Why are you using the specific premise(s) and why do they lead to the conclusion? "
               "Follow the structure 1. Premise(s) and conclusion, 2. Argument, 3. Answers to the critical questions: how does the generated argument provide these answers?, 4. Analysis explaining for each premise how it is connected to the Walton scheme and the conclusion.")

    # Construct the prompt
    prompt = (f"{pretext} "
              f"Generate an argument that discusses the topic {topic}, taking the stance {stance}. "
              f"The argument should be structured according to the Walton-scheme {scheme}. Variables are delimited by $. Name the concrete instances of these variables in the generated argument"
              f"The premise(s) is/are {scheme_details['premises']} and the conclusion is {scheme_details['conclusion']}. "
              f"The critical questions are {scheme_details['critical_questions']}."
              f"Also give a second version of the generated argument how it would be presented in a blog post, only consisting at most of 3 sentences and focussing on the most important aspects. Take your time to think before starting to generate.")

    print("enter response")

    response = client.chat.completions.create(
        # model="gpt-3.5-turbo",
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=1,  # Controls randomness. Lower is more deterministic, higher is more random.
        top_p=0.95
    )

    print("enter argument")
    argument = response.choices[0].message.content
    print("saving argument")
    save_argument(topic, stance, scheme, argument)
    # print(argument)
    # return argument
