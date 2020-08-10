from deeppavlov import build_model, configs
import pandas as pd
def build_ner_model ():
    model = build_model(configs. ner.ner_ontonotes_bert_mult, download=True)
    return model

test_input = ['HCL Technologies Limited, is an Indian multinational information technology (IT) service']

ner_model = build_ner_model()
results = ner_model(test_input)
results = pd.DataFrame(zip(results[0][0],results[1][0]), columns=['Word','Entity'])
print(results)
