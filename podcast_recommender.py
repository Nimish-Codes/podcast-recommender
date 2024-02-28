import streamlit as st
import random

# Define a dictionary of podcasts with categories
podcasts = {
    "Select category": ["", "", ""],
    "Technology": ["The Vergecast", "Reply All", "Syntax", "TED Radio Hour"],
    "Comedy": ["The Joe Rogan Experience", "My Dad Wrote A Poem", "Conan O'Brien Needs A Friend"],
    "True Crime": ["Serial", "Crime Junkie", "My Favorite Murder"],
    "Science": ["Science Vs", "Stuff You Should Know", "Radiolab"],
    "Business": ["How I Built This", "The Indicator from Planet Money", "Freakonomics Radio"],
    "News": ["The Daily", "Up First", "Today, Explained", "BBC Global News Podcast"],
    "History": ["Hardcore History", "The History of Rome", "Stuff You Missed in History Class"],
    "Health & Fitness": ["The Tim Ferriss Show", "The Model Health Show", "FoundMyFitness"],
    "Education": ["TED Talks Daily", "Stuff You Should Know", "The Great Courses"],
    "Sports": ["The Bill Simmons Podcast", "The Woj Pod", "Pardon My Take"],
    "Arts": ["ArtCurious Podcast", "99% Invisible", "The Art History Babes"],
    "Music": ["Song Exploder", "Dissect", "Switched on Pop"],
    "Food": ["The Sporkful", "Gastropod", "Home Cooking"],
    "Self-Improvement": ["The Tony Robbins Podcast", "The School of Greatness", "Optimal Living Daily"],
    "Science Fiction": ["Welcome to Night Vale", "The Twilight Zone Podcast", "StarTalk Radio"],
    "Interviews": ["Armchair Expert with Dax Shepard", "The Tim Ferriss Show", "The Joe Rogan Experience"],
    "Politics": ["Pod Save America", "The Rachel Maddow Show", "The Ben Shapiro Show"],
    "Travel": ["The Travel Diaries", "Zero to Travel", "Amateur Traveler Podcast"],
    "Parenting": ["The Longest Shortest Time", "The Modern Dads Podcast", "Spawned with Kristen and Liz"],
    "Storytelling": ["This American Life", "The Moth", "Snap Judgment"],
    "Movies & TV": ["Scriptnotes", "The Rewatchables", "Buffering the Vampire Slayer"],
    "Science & Medicine": ["Sawbones: A Marital Tour of Misguided Medicine", "Science Vs", "The Skeptics' Guide to the Universe"],
    "Relationships": ["Where Should We Begin? with Esther Perel", "Dear Sugars", "Modern Love"],
    "Fantasy & Fiction": ["The Adventure Zone", "Welcome to Night Vale", "LeVar Burton Reads"],
    "Motivation & Inspiration": ["The Daily Boost", "The Mindset Mentor", "The GaryVee Audio Experience"],
    "Documentaries": ["Serial", "The Documentary Podcast", "Criminal"]
}

# Streamlit app title
st.title("Podcast Recommender")

# Dropdown menu for selecting podcast category
selected_category = st.selectbox("Select a podcast category", list(podcasts.keys()))

# Display randomly recommended two podcasts from the selected category
if selected_category in podcasts:
    recommended_podcasts = random.sample(podcasts[selected_category], 2)
    st.write(f"Recommended podcasts from the {selected_category} category:")
    for podcast in recommended_podcasts:
        st.success("-", podcast)
else:
    st.error("Sorry, the category you selected is not available.")
