import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="AI Text Generator",
    page_icon="🤖"
)

st.title("🤖 AI Text Generator")
st.write("✨ Enter a prompt and let AI generate text for you!")

prompt = st.text_area(
    "✍️ Enter your prompt:",
    placeholder="Artificial Intelligence is..."
)

if st.button("✨ Generate Text"):

    if not prompt.strip():
        st.warning("⚠️ Please enter a prompt first!")

    else:
        st.info("🔄 Loading GPT-Neo model...")

        try:
            generator = pipeline(
                "text-generation",
                model="EleutherAI/gpt-neo-125M"
            )

            st.success("✅ Model loaded successfully!")

            st.info("🤖 Generating text...")

            result = generator(
                prompt,
                max_new_tokens=400,
                num_return_sequences=1,
                do_sample=True,
                temperature=0.7,
                top_p=0.9
            )

            generated_text = result[0]["generated_text"]

            st.subheader("📝 Generated Text")
            st.write(generated_text)

        except Exception as e:
            st.error("❌ Something went wrong:")
            st.exception(e)
