# 🎬 Movie Recommendation System
Link : https://movie-recommendation-system-elkholy.streamlit.app/
<img width="1914" height="991" alt="image" src="https://github.com/user-attachments/assets/59208f54-f273-4197-b8cd-e1292fbffd5e" />

## 📌 Project Overview

This project is a **Content-Based Movie Recommendation System** developed using Python and Streamlit. Given a selected movie, the system recommends similar movies based on several metadata features such as:

- Overview
- Genres
- Cast
- Director
- Keywords

The model uses **Natural Language Processing (NLP)** techniques combined with **cosine similarity** to identify similar movies based on their textual features.

---

## 🚀 Features

- Select a movie from a dropdown list
- Get 5 visually rich movie recommendations with posters
- Intuitive and responsive UI using Streamlit
- TMDb API integration to fetch movie posters

---

## 🧠 Methodology

1. **Data Cleaning and Merging**:
    - Combined `movies` and `credits` datasets using the title field.
    - Retained only important columns (`genres`, `keywords`, `cast`, `crew`, `overview`, `movie_id`, `title`).

2. **Feature Engineering**:
    - Extracted top 3 cast members and the director.
    - Removed spaces and lowercased all features for uniformity.
    - Combined all the information into a single `tags` column.

3. **Text Vectorization & Similarity**:
    - Used `CountVectorizer` with a max of 5000 features and English stopwords.
    - Applied `PorterStemmer` for stemming words.
    - Calculated pairwise similarity using **cosine similarity**.

4. **Recommendation Logic**:
    - For a given movie, retrieve the most similar movies by similarity scores.
    - Display the movie posters using the **TMDb API**.

---

## 🔥 Challenges Faced & Solutions

| Challenge | Solution |
|----------|----------|
| Extracting meaningful metadata (cast, crew, genres) | Used `ast.literal_eval` to parse stringified JSON and selected only relevant people like director and top 3 actors |
| Redundancy in tags and noisy text | Cleaned and normalized tags using lowercase and stemming |
| Missing poster paths from TMDb API | Added error handling and fallback logic for broken API calls |
| UI display with Streamlit columns | Divided recommendation section into 5 equal columns using `st.columns(5)` for cleaner layout |

---

## 📂 Files

- `app.py`: Main application script.
- `movies.pkl`: Serialized movie features and tags dictionary.
- `similarity.pkl`: Cosine similarity matrix.
- `README.md`: Project description.
- `requirements.txt`: Python dependencies.

---

## 🛠️ How to Run Locally

```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt
streamlit run app.py
```

---

## 📸 Sample Output

The app interface lets you choose a movie and returns the top 5 recommendations with their posters and titles.

---

---

*Last updated: 2025-07-26*
