import streamlit as st
import string
from streamlit_extras.switch_page_button import switch_page

st.title("Terms Of Service")



st.subheader("Use")
use_text = """
        Use of Our Hosted Services GPT Lab LLC provides a user-friendly platform for creating and interacting with AI Assistants powered by OpenAI's GPT language model. These terms apply specifically to the use of our hosted version of this platform. By using our hosted services, you agree to use them only for lawful purposes and in a manner that does not infringe the rights of or restrict or inhibit the use and enjoyment of our services by any third party. We reserve the right to terminate your access to our hosted services at any time if we reasonably believe that you have breached any of these terms of service.
        """
st.write(use_text)


st.subheader("Eligibility")
eligibility_text = """
        To use the hosted services provided by GPT Lab, you must be at least 18 years of age or the legal age of majority in your jurisdiction (if different). You must also have an OpenAI API Key to access the AI models used by GPT Lab.
        """
st.write(eligibility_text)


st.subheader("Usage Policy")
usage_policy_text = """
        "OpenAI wants everyone to use their tools safely and responsibly. That’s why OpenAI has created usage policies that apply to all users of their models, tools, and services. By following these policies, users will ensure that OpenAI's technology is used for good. If OpenAI discovers that a user's product or usage doesn't follow these policies, they may ask the user to make necessary changes. Repeated or serious violations may result in further action, including suspending or terminating the user's account. OpenAI's policies may change as they learn more about use and abuse of their models. To learn more about OpenAI's usage policy, please visit https://platform.openai.com/docs/usage-policies.
        """
st.write(usage_policy_text)


st.subheader("Privacy Policy")
privacy_policy_text = """
        At GPT Lab, we take your privacy very seriously. Our application only uses your OpenAI API Key during sessions to interact with the AI models. To ensure your confidentiality and security, we use a one-way hashing algorithm on your OpenAI Key to generate your unique user identity rather than collecting or storing Personal-Identifiable-Information (PII). We also use a symmetric AES-128 encryption algorithm, with a unique key for each user, to encrypt your chat transcripts with the AI Assistants. Lastly, we do store the AI assistant prompts, which can be reviewed and audited periodically to ensure no misuse. For more information about our privacy practices, please visit our privacy policy.
        """
st.write(privacy_policy_text)


st.subheader("User Conduct")
user_conduct_text = """
        You agree to use GPT Lab only for lawful purposes and in accordance with these Terms of Service. Specifically, you agree not to: (a) violate any applicable law or regulation; (b) maliciously try to hack or break AI Assistants by using Prompt Injection techniques; (c) share bots that do not meet our user content standard; (d) break the system in any way. You also agree to use GPT Lab in a responsible and ethical manner and to contribute to an overall positive environment for all users. This includes refraining from any behavior that promotes, incites, or engages in hate speech, discriminatory behavior, or harassment of any kind based on race, gender, sexual orientation, religion, nationality, or any other personal characteristics. This also includes creating and using AI responsibly and ethically.
        """
st.write(user_conduct_text)

container = st.container()
col1, col2, col3 = container.columns(3)

# Add buttons to each column
with col2:
    if st.button("return to Home", type="primary"):
        switch_page("Home")
