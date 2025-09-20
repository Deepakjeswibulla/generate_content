from flask import Flask, render_template, request, jsonify
from quality_checker import check_quality
from genei import gen_content
content_history = []
app = Flask(__name__)

@app.route('/')
def content_page():
    return render_template('main.html')
@app.route('/check_quality', methods=['POST'])
def check_text_quality():
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        if not text:
            return jsonify({
                'plagiarism_score': 'N/A',
                'grammar_issues': 'No text provided',
                'quality_score': 'N/A',
                'original_text_analysis': 'Please enter text to analyze'
            })
        
        # Use your existing quality checker
        results = check_quality(text)
        
        return jsonify({
            'plagiarism_score': results.get('plagiarism_score', 'N/A'),
            'grammar_issues': results.get('grammar_issues', 'Could not analyze'),
            'quality_score': results.get('quality_score', 'N/A'),
            'original_text_analysis': results.get('original_text_analysis', 'No analysis')
        })
        
    except Exception as e:
        return jsonify({
            'plagiarism_score': 'Error',
            'grammar_issues': f'Error: {str(e)}',
            'quality_score': 'Error',
            'original_text_analysis': 'Analysis failed'
        })
@app.route('/quality_check')
def check_page():
    return render_template('quality_check.html')

@app.route('/history')
def history_page():
    return render_template('history.html', history=content_history)

@app.route('/feedback')
def feedback_page():
    return "Feedback page will be here."

@app.route('/generate', methods=['POST'])
def generate_content():
    data = request.get_json()
    topic = data.get('topic', 'A default topic')
    content_type = data.get('content_type', 'Blog')
    length = data.get('length', 'Short')
    audience = data.get('audience', 'General')

    generated_text = gen_content(topic,content_type,length,audience)
    print(generated_text)
    content_history.append({
        'topic': topic,
        'content_type': content_type,
        'length': length,
        'audience': audience,
        'content': generated_text
    })
    return jsonify({
        'success': True,
        'content': generated_text
    })
if __name__ == '__main__':
    app.run(debug=True)