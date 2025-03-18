import streamlit as st

def main():
    st.set_page_config(page_title="Mad Libs Game", page_icon="📖")
    st.title("🎉 Fun Mad Libs Game")
    st.write("Fill in the blanks and generate a hilarious story!")

    # Input fields
    noun = st.text_input("Enter a Noun")
    adjective = st.text_input("Enter an Adjective")
    verb = st.text_input("Enter a Verb")
    place = st.text_input("Enter a Place")
    plural_noun = st.text_input("Enter a Plural Noun")

    if st.button("Generate Story"):
        if noun and adjective and verb and place and plural_noun:
            # Generating the story
            story = f"Once upon a time, in a {adjective} {place}, there lived a {noun}. Every day, it would {verb} with the {plural_noun}."
            st.subheader("Here's Your Story:")
            st.write(story)
        else:
            st.warning("Please fill out all the fields before generating the story.")


if __name__ == "__main__":
    main()
