PUBLISHED = False
# APP_URL = "N / A"
# APP_IMAGE = "msct_tutor_flat.webp"

APP_TITLE = "Endicott Nursing Tutor"
APP_INTRO = """This is an AI tutor that presents interactive medical case studies for nursing students. 
"""

APP_HOW_IT_WORKS = """
 This is an **AI-Tutored Rubric exercise** that acts as a tutor guiding a student through a shared asset, like an article. It uses the OpenAI Assistants API with GPT-4. The **questions and rubric** are defined by a **faculty**. The **feedback and the score** are generarated by the **AI**. 

It can:

1. provide feedback on a student's answers to questions about an asset
2. roughly "score" a student to determine if they can move on to the next section.  

Scoring is based on a faculty-defined rubric on the backend. These rubrics can be simple (i.e. "full points if the student gives a thoughtful answer") or specific with different criteria and point thresholds. The faculty also defines a minimum pass threshold for each question. The threshold could be as low as zero points to pass any answer, or it could be higher. 

Using AI to provide feedback and score like this is a very experimental process. Some things to note: 

 - AIs make mistakes. Users are encourage to skip a question if the AI is not understanding them or giving good feedback. 
 - The AI might say things that it can't do, like "Ask me anything about the article". I presume further refinement can reduce these kinds of responses. 
 - Scoring is highly experimental. At this point, it should mainly be used to gauge if a user gave an approximately close answer to what the rubric suggests. It is not recommended to show the user the numeric score. 

 """

SHARED_ASSET = {
}

HTML_BUTTON = {
    
}

SYSTEM_PROMPT = """You are an assistant that helps nursing students explore patient case studies. \
Allow students to make mistakes. Do not merely correct students.  
"""


PHASES = {
    "About": {
        "name": "About",
        "fields": {
            "markdown": {
                "type": "markdown",
                "body": """In this case you will be caring for Bellie B. Hertin. \
                She comes into the hospital with her daughter and son-in-law, Leia and Lou Stewel.""",
                "unsafe_allow_html": True
            },
            "markdown": {
                "type": "markdown",
                "body": """This client is an 82 year old woman with a 3 day history 
                of intermittent abdominal pain, abdominal bloating, nausea and vomiting. 
                She recently moved from Italy to join her daughter and her family only two months ago 
                and she speaks very little English. All information was obtained through her daughter 
                who is here with her. Her medical history includes a colectomy for colon cancer 
                6 years ago and hiatal hernia repair two years ago. She has a history of CAD and diabetes 
                but no evidence of any pulmonary disease. She takes only Ibuprofen (Motrin) 
                occasionally for mild arthritis and metformin for her diabetes. 
                She has an allergy to sulfa drugs and she reports that she has an aunt 
                who died having a surgical procedure many years ago.
                
                """,
                "unsafe_allow_html": True
            }
        },
        "no_submission": True
    },
    "Phase 1" : {
        "name" : "Peptic Ulcer Disease Differential",
         "fields" : {
             "user_response_1" : {
                 "type" : "text_input",
                 "label" : """Ms. Hertin complains of pain in the mid epigastric area. \
                You know that this pain could be a sign of Peptic Ulcer Disease. \
                List some additional questions that you would ask Betty to further investigate \
                if her symptoms might be related to PUD?
                """,
                "value" : "Enter your response here."
             }
        },
        "phase_instructions" : """The user will input a set of diagnostic questions to ask the patient \
        to assess whether the patient suffers from  Peptic Ulcer Disease (PUD).
        Do not provide feedback. Do not ask follow-up questions.""",
        "user_prompt" : "{user_response_1}",
        "scored_phase" : True,
        "rubric": """
            1. Diagnostic Questions
                1 point - The user asks appropriate questions to diagnose the patient.
                0 points - The user asks impertinent or unhelpful questions. 
        """,
        "minimum_score" : 0
    },
    "Phase 2" : {
        "name" : "Bowel Obstruction Tentative Diagnosis",
        "fields" : {
             "user_response_2" : {
                 "type" : "text_input",
                 "label" : """Bellie's tentative diagnosis is a small bowel obstruction (SBO)
                 secondary to adhesions. She is being admitted to your floor for a diagnostic workup. 
                Her vital signs are stable, she is receiving an infusion of D5 ½ NS 
                with 20mEq KCl at 100 ml/hr and 2L oxygen by nasal cannula. 
                Based on the report you received so far, what signs of bowel obstruction does Bellie have?
                """,
                "value" : "Enter your response here."
             }
        },
        "phase_instructions" : """The user will input symptoms of bowel obstruction. The patient in question 
        has intermittent abdominal pain, abdominal bloating, nausea and vomiting.
        Do not provide feedback. Do not ask follow-up questions.""",
        "user_prompt" : "{user_response_2}",
        "scored_phase" : True,
        "rubric": """
            1. Symptom Assessment
                2 points - The user lists multiple symptoms this patient exhibits.
                1 point - The user lists only one relevant symptom this patient exhibits.
                0 points - The user lists no relevant symptoms this patient exhibits.  
        """,
        "minimum_score" : 0
    },
    "Phase 3" : {
        "name" : "Interpreter Services",
        "fields" : {
             "user_response_3" : {
                 "type" : "text_input",
                 "label" : """As you are assessing Ms. Hertin, the interpreter you requested arrives. 
                Leia, her daughter, tells you that Bellie would prefer that she do the interpreting.  
                How should you proceed?
                """,
                "value" : "Enter your response here."
             }
        },
        "phase_instructions" : """The user will describe their approach to handling the offer of \
        the patient's daughter Bellie to serve as an interpreter rather than the hospital interpreter. \
        The patient has an Italian background. Remind the user of the patient's rights in this situation.
        Do not provide feedback. Do not ask follow-up questions.""",
        "user_prompt" : "{user_response_3}",
        "scored_phase" : True,
        "rubric": """
            1. Interpreter Services
                1 point - The user has the interpreter ask the patient directly if they \
                would like to use interpretation services while in hospital.
                0 points - The user does not have the interpreter ask the patient directly if they \
                would like to use interpretation services while in hospital.
        """,
        "minimum_score" : 0
    },
    "Phase 4" : {
        "name" : "Key Questions",
        "fields" : {
             "user_response_4" : {
                 "type" : "text_input",
                 "label" : """What key questions must you ask this patient while you have the use of an interpreter?
                """,
                "value" : "Enter your response here."
             }
        },
        "phase_instructions" : """The user should provide variations of the following questions. \
        - What is your code status? \
        - Who is your healthcare proxy? \
        - What allergies do you have? \
        - What exacerbates your symptoms? \
        - Do you know where you are right now? \
        - What is the date today? \
        Do not provide feedback. Do not ask follow-up questions.
        """,
        "user_prompt" : "{user_response_4}",
        "scored_phase" : True,
        "rubric": """
            1. Key Questions
                2 points - The user provides several appropriate questions to ask the patient. 
                1 point - The user provides one or two appropriate questions to ask the patient. 
                0 points - The user provides one or no appropriate questions to ask the patient.
        """,
        "minimum_score" : 0
    },
    "Phase 5" : {
        "name" : "Nasogastric Tube Inserted",
        "fields" : {
             "user_response_5" : {
                 "type" : "text_input",
                 "label" : """Following the doctor's orders, you prepare to insert a nasogastric tube (NGT) 
                for the patient. What nursing actions should you take after insertion to secure the NGT 
                and care for the patient?
                """,
                "value" : "Enter your response here."
             }
        },
        "phase_instructions" : """The user should provide variations of the following actions. 
        - Provide frequent oral care 
        - Check the nares around the tube for signs of irritation 
        - Tape the tube to the nose so it does not pull on the nares or cause ulceration 
        - Obtain an order for a topical antiseptic spray if she has a sore throat 
        Do not provide feedback. Do not ask follow-up questions.
        """,
        "user_prompt" : "{user_response_5}",
        "scored_phase" : True,
        "rubric": """
            1. Nursing actions
                2 points - The user provides several appropriate actions for NGT care. 
                1 point - The user provides one or two appropriate actions for NGT care. 
                0 points - The user provides no appropriate actions for NGT care.
        """,
        "minimum_score" : 0
    },
    "Phase 6": {
        "name": "Labs",
        "fields": {
            "markdown": {
                "type": "markdown",
                "body": """In this case you will be caring for Bellie B. Hertin. 
                She comes into the hospital with her daughter and son-in-law, Leia and Lou Stewel.""",
                "unsafe_allow_html": True
            },
            "markdown": {
                "type": "markdown",
                "body": """
                After 24 hours, Ms. Hertin's symptoms are unrelieved. 
                She reports continued nausea, cramps, and sometimes strong abdominal pain. 
                Her hand grips are weaker and she seems to be increasingly lethargic. 
                You look up her latest lab values and compare them with the admission data.

                | Test | Admission | Hospital Day 3 |
                | -------- | ------- | | ------- |
                | Sodium | 136 mEq/L | 130 mEq/L |
                | Potassium | 3.7 mEq/L | 2.5 mEq/L |
                | Chloride | 108 mEq/L | 97 mEq/L |
                | Carbon dioxide | 25 mEq/L | 31 mEq/L |
                | BUN | 19 mg/dL | 38 mg/dL |
                | Creatinine | 1 mg/dL | 2.2 mg/dL |
                | Glucose | 126 mg/dL | 65 mg/dL |
                | Albumin | 3.0 g/dL | 3.1 g/dL |
                | Protein | 6.8 g/dL | 4/9 g/dL |

                """,
                "unsafe_allow_html": True
            }
        },
        "no_submission": True
    },
     "Phase 7" : {
        "name" : "Interpreting the Labs",
        "fields" : {
             "user_response_7" : {
                 "type" : "text_input",
                 "label" : """Which lab results raise the most concern? Explain your rationale. 
                What interventions would you suggest?
                """,
                "value" : "Enter your response here."
             }
        },
        "phase_instructions" : """The user should provide variations of the following observations. 
        - Low sodium/hyponatremia 
        - Low potassium/hypokalemia
        - Elevated BUN and Creatinine
        The best answers will note the presence of hypovolemia, evidenced by low electrolytes, and impaired
        kidney function, evidenced by the elevated BUN and Creatinine levels. Users should develop a plan 
        that replaces the patient's electrolytes via food and drink. The patient should be put on telemetry 
        monitoring. Patient's diabetes should also be closely monitored (hypoglycemic).
        Do not provide feedback. Do not ask follow-up questions.
        """,
        "user_prompt" : "{user_response_7}",
        "scored_phase" : True,
        "rubric": """
            1. Identifying lab abnormalities
                2 points - The user identifies all lab abnormalities and accurately describes 
                their causes.
                1 point - The user identifies some of the lab anormalities and/or incorrectly
                assigns their causes. 
                0 points - The user does not identify abnormalities or correctly describe their causes.
            2. Suggesting corrective actions
                2 points - The user's plan addresses electrolyte imbalance, kidney function, and diabetes. 
                1 point - The user's plan only addresses some of the patient's ailments. 
                0 points - The user's plan does not address patient's condition, may be detrimental.
        """,
        "minimum_score" : 0
    },
    
}
    

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end of this tutoring exercise! Thank you for your hard work."
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "Endicott Nursing Tutor",
    "page_icon": "️🧑‍🏫",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())