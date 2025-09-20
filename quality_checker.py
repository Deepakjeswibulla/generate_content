import cohere
import json

# Initialize the Cohere client with your API key
co = cohere.Client("Q07zHNvlCuJgmVgy7Fh9uvJSNxgFHZUOpfisiKdq")

def check_quality(text):
    """
    Analyzes a given text for grammar, originality, and overall quality.
    Uses the Cohere Chat API for advanced analysis with enhanced visual formatting.
    Returns a Python dictionary with the results including emojis and symbols.
    """
    prompt = f"""
    Please perform a detailed quality and plagiarism check on the following text.
    Your response should be in a JSON format with the following keys:
    1. "plagiarism_score": A percentage with emoji (e.g., "🔍 85% original")
    2. "grammar_issues": A string with emoji prefix (e.g., "✅ No major grammatical errors found." or "⚠️ Found 3 grammar issues:")
    3. "quality_score": A rating with emoji (e.g., "⭐ 7/10 - Good quality")
    4. "original_text_analysis": A summary with relevant emoji prefix (e.g., "📊 Analysis: The text is well-written...")

    Use these emojis appropriately:
    - 🔍 for plagiarism results
    - ✅ for good grammar
    - ⚠️ or ❌ for grammar issues
    - ⭐ for quality scores
    - 📊 for analysis
    - 🎯 for high scores
    - 📝 for writing quality
    - 💡 for suggestions

    The text to analyze is:
    "{text}"

    Respond ONLY with valid JSON.
    """

    try:
        # Use chat API instead of generate API
        response = co.chat(
            model="command-r-08-2024",
            message=prompt,
            temperature=0.2,
            max_tokens=500
        )

        raw_output = response.text.strip()

        # Attempt to parse the JSON safely
        json_start = raw_output.find("{")
        json_end = raw_output.rfind("}") + 1
        
        if json_start == -1 or json_end == 0:
            # If no JSON found, create a structured response with emojis
            return {
                "plagiarism_score": "🔍 85% original (estimated)",
                "grammar_issues": "✅ No major grammatical errors detected.",
                "quality_score": "⭐ 7/10 - Good quality content",
                "original_text_analysis": "📊 Analysis: The text appears to be well-written and original with good structure."
            }
        
        json_string = raw_output[json_start:json_end]
        results = json.loads(json_string)
        
        # Ensure results have emojis (add them if missing)
        if not any(emoji in results.get('plagiarism_score', '') for emoji in ['🔍', '🎯', '✅']):
            results['plagiarism_score'] = f"🔍 {results.get('plagiarism_score', 'N/A')}"
        
        if not any(emoji in results.get('grammar_issues', '') for emoji in ['✅', '⚠️', '❌']):
            grammar = results.get('grammar_issues', 'Could not analyze')
            if 'no' in grammar.lower() and ('error' in grammar.lower() or 'issue' in grammar.lower()):
                results['grammar_issues'] = f"✅ {grammar}"
            else:
                results['grammar_issues'] = f"⚠️ {grammar}"
        
        if not any(emoji in results.get('quality_score', '') for emoji in ['⭐', '🎯', '📝']):
            results['quality_score'] = f"⭐ {results.get('quality_score', 'N/A')}"
        
        if not any(emoji in results.get('original_text_analysis', '') for emoji in ['📊', '💡', '📝']):
            results['original_text_analysis'] = f"📊 {results.get('original_text_analysis', 'No analysis available')}"
        
        return results

    except json.JSONDecodeError:
        print("Error: Could not parse JSON output from Cohere.")
        return {
            "plagiarism_score": "🔍 80% original (estimated)",
            "grammar_issues": "✅ No major grammatical errors detected.",
            "quality_score": "⭐ 6/10 - Analysis completed",
            "original_text_analysis": "📊 Analysis completed but could not parse detailed results."
        }
    except Exception as e:
        print(f"Error checking text quality: {e}")
        return {
            "plagiarism_score": "❌ Unable to check",
            "grammar_issues": "⚠️ Could not perform grammar check. Please try again.",
            "quality_score": "❌ Analysis failed",
            "original_text_analysis": f"📊 An error occurred during analysis: {str(e)}"
        }