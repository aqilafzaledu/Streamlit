import openai
import streamlit as st
import os

# Load OpenAI API key from environment variables
my_secret = os.environ.get('OPENAI_API_KEY')
openai.api_key = my_secret

# Story generator method
def story_gen(prompt):
    system_prompt = """
    You are a world-renowned storyteller with 50 years of experience in children's stories.
    Generate a story suitable for ages 5 to 7 based on the given concept.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=1.3,
        max_tokens=100
    )
    return response['choices'][0]['message']['content']

# Cover prompt generator method
def cover_gen(prompt):
    system_prompt = """
    You will be given a children's storybook.
    Generate a prompt for cover art that is suitable and represents the story themes.
    This prompt will be used for DALL·E 2.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=1.3,
        max_tokens=100
    )
    return response['choices'][0]['message']['content']

# Image generator method
def image_gen(prompt):
    response = openai.Image.create(
        prompt=prompt,
        size='256x256',
        n=1
    )
    return response['data'][0]['url']

# Storybook method
def storybook(prompt):
    story = story_gen(prompt)
    cover_prompt = cover_gen(story)
    image_url = image_gen(cover_prompt)

    # Display the generated image and story
    st.image(image_url, caption="Story Cover Art")
    st.write(story)

# Streamlit app UI
st.title("Storybook Generator for Awesome Kids")
st.divider()

prompt = st.text_area("Enter your story idea here:")

if st.button("Generate Storybook"):
    storybook(prompt)
