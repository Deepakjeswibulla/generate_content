import cohere

co = cohere.Client("Replace with your cohere api key") 

def build_prompt(topic, format, length="medium", audience="general"):
    if format == "Blog":
        return f"Write a '{length}' blog post on '{topic}' for a '{audience}' audience in a attractive tone. Include subheadings and a conclusion clear instruction and clear information.use effective active symbols which are relavent insteead and in place of bullets,hastags if and only required.give only in html format to show in web page."
    elif format == "Notes":
        return f"Summarize and crete notes for topic '{topic}' into bullet-point or any special symbols if rewired study '{length}' notes for '{audience}' depends and topic in a informative+helping tone in more effective way.if required use different kind of bullet points like attractive relavent symbols at different places.try to give in some paragraphs format.use symbols compulsory.give it onlyy in html format to show in web page."
    elif format == "Post":
        return f"Create a engaging attractive, catchy social media post about '{topic}' for '{audience}'. Use a informative,friendly according to '{audience}' tone and include emojis and hashtags and also considering present conditions related to the {topic} .give in html format to show in web page."
    elif format == "Letter":
        return f"write a body letter and format on  '{topic}' of size  '{length}' in  '{audience}' purpose .the letter created should be more effective.give in html format to show in web page."
    elif format == "Email":
        return f"write an email subject and body and end part of email on '{topic}' in '{audience}' of size '{length}'. in an very effective manner .give in html format to show in web page,"
    else:
        return "on ai theme."

def gen_content(topic, format="notes", tone="neutral", audience="students"):
    prompt = build_prompt(topic, format, tone, audience)
    response = co.chat(
        model="command-r-08-2024", 
        message=prompt,
        temperature=0.7,
        max_tokens=500
    )


    return response.text
