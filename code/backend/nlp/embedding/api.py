import torch
from transformers import BertTokenizer
from keras.preprocessing.sequence import pad_sequences
from transformers import BertModel
import os
BASE_PATH = os.path.dirname(__file__)


class BertEmbedding():
    def __init__(self) -> None:
        self.tokenizer = BertTokenizer.from_pretrained(
            os.path.join(BASE_PATH, './models/bert-chinese'))
        self.device = torch.device(
            "cuda:0" if torch.cuda.is_available() else "cpu")
        self.MAX_LEN = 128
        self.model = BertModel.from_pretrained(
            os.path.join(BASE_PATH, './models/bert-chinese'),
            num_labels=2,
            output_attentions=False,
            output_hidden_states=True,
        )
        self.model.eval()

    def bert_embedding(self, sent):
        encoded_sent = [self.tokenizer.encode(sent, add_special_tokens=True)]
        input_ids = pad_sequences(encoded_sent, maxlen=self.MAX_LEN, dtype="long",
                                  value=0, truncating="post", padding="post")
        attention_masks = [[int(token_id > 0) for token_id in input_ids[0]]]
        input_ids = torch.tensor(input_ids).to(self.device)
        attention_masks = torch.tensor(attention_masks).to(self.device)
        outputs = self.model(input_ids, token_type_ids=None,
                             attention_mask=attention_masks)
        return outputs.pooler_output


if __name__ == '__main__':
    b = BertEmbedding()
    sentence = "我来测试一下这个能不能用!"
    print(b.bert_embedding(sentence).shape)
