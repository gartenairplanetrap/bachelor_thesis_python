from fetch_scheme_details import fetch_scheme_details
from save_argument import save_argument
import google.generativeai as genai
from dotenv import load_dotenv
import os

APIKEY = os.getenv('API_KEY')

# os.environ['GOOGLE_API_KEY'] =
genai.configure(api_key=APIKEY)


def generateWithGemini(topic, stance, scheme):
    scheme_details = fetch_scheme_details(scheme)
    model = genai.GenerativeModel("gemini-1.5-pro")

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

    response = model.generate_content(prompt)

    argument = response.text

    print(argument)

    save_argument(topic, stance, scheme, argument)
