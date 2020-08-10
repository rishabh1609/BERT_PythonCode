from deeppavlov import build_model, configs

def qa_deeppavlov(question, context):
    model = build_model(configs.squad.squad_bert, download=True)
    result = model([context], [question])
    return result

context="Super Bowl 50 was an American football game to determine the champion of the National Football League (NFL) for the 2015 season. The American Football Conference (AFC) champion Denver Broncos defeated the National Football Conference (NFC) champion Carolina Panthers 24–10 to earn their third Super Bowl title. The game was played on February 7, 2016, at Levi's Stadium in the San Francisco Bay Area at Santa Clara, California. As this was the 50th Super Bowl, the league emphasized the 'golden anniversary' with various gold-themed initiatives, as well as temporarily suspending the tradition of naming each Super Bowl game with Roman numerals (under which the game would have been known as 'Super Bowl L'), so that the logo could prominently feature the Arabic numerals 50."

question="Which NFL team represented the AFC at Super Bowl 50?"

answers = qa_deeppavlov (context, question)
print(answers)