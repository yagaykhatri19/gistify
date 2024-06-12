import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import warnings

warnings.filterwarnings("ignore")

nltk.download('punkt')

def extractive_summarize_text(text, min_words=120, max_words=180):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    
    summarizer = TextRankSummarizer()
    
    summary = summarizer(parser.document, 10)
    
    summary_sentences = [str(sentence) for sentence in summary]
    
    summary_text = ""
    for sentence in summary_sentences:
        if len(summary_text.split()) + len(sentence.split()) <= max_words:
            summary_text += " " + sentence
        else:
            break
    
    if len(summary_text.split()) < min_words:
        summary_text = " ".join(summary_sentences)
    
    return summary_text.strip()