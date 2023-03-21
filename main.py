import streamlit as st
from langchain.llms import OpenAI



# Set up OpenAI API credentials
st.set_option('deprecation.showfileUploaderEncoding', False)
openai_api_key = st.text_input('Enter your OpenAI API Key')

# Define Streamlit app
def app():
    # Title and description
    st.title('OpenAI Q&A')
    st.write('Upload a file and ask questions to get answers from OpenAI!')

    # File uploader
    file = st.file_uploader('Upload file', type=['txt', 'pdf'])

    # Question input
    question = st.text_input('Question')

    # Submit button
    if st.button('Get Answer'):
        # Check if file and question are provided
        if not file:
            st.warning('Please upload a file!')
        elif not question:
            st.warning('Please enter a question!')
        else:
            # Read uploaded file and convert to string
            file_content = ''
            if file.type == 'text/plain':
                file_content = file.read().decode('utf-8')
            elif file.type == 'application/pdf':
                file_content = convert_pdf_to_text(file)
            
            # Call OpenAI's API to get answer
            answer = openai.Completion.create(
                engine='davinci',
                prompt=f'Q: {question}\nA:',
                max_tokens=1024,
                temperature=0.5,
                n=1,
                stop=None,
                prompt_prefix=f'{file_content}\nQ&A:',
            )
            st.write(answer.choices[0].text.strip())

# Run Streamlit app
if __name__ == '__main__':
    app()
