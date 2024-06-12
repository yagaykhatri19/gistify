from flask import Flask, render_template, redirect, request
from extractive import extractive_summarize_text
from abstractive import abstractive_summarize_text

app = Flask(__name__)

#ENDPOINTS
@app.route('/')
def main():
    return render_template('dashboard.html')

@app.route('/info')
def information():
    return render_template('information.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/summary', methods=['GET','POST'])
def summary():
    # print(request.form)
    text = request.form['text']
    if (len(text)==0):
        return render_template('dashboard.html', error='Enter text.')
    # text = text.strip()
    
    summary = extractive_summarize_text(text)
    summary_ = abstractive_summarize_text(text)

    return render_template('summarize.html', text=text, summary_=summary_, summary=summary,)
#ENDPOINTS

if (__name__=='__main__'):
    app.run(debug=True)