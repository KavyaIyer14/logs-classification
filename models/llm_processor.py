from google.colab import userdata
import os
from groq import Groq

api_key = os.environ.get('GROQ_API_KEY')

client = Groq()
def classify_with_llm(log_msg):
  prompt = f'''Classify the log message into one of these categories:
    (1) Workflow Error, (2) Deprecation Warning.
    If you can't figure out a category, return "Unclassified".
    Only return the category name. No preamble.
    Log message: {log_msg}'!!'''
  completion = client.chat.completions.create(
      model="llama-3.3-70b-versatile",
      messages=[
        {
          "role": "user",
          "content": prompt
        }
      ],
  )

  return completion.choices[0].message.content 


if __name__ == "__main__":
    print(classify_with_llm(
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classify_with_llm(
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
    print(classify_with_llm("System reboot initiated by user 12345."))
