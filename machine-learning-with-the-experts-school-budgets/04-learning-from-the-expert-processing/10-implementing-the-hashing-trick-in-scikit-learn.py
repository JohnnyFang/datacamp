"""
Implementing the hashing trick in scikit-learn

In this exercise you will check out the scikit-learn implementation of HashingVectorizer before adding it to your pipeline later.

As you saw in the video, HashingVectorizer acts just like CountVectorizer in that it can accept token_pattern and ngram_range parameters. The important difference is that it creates hash values from the text, so that we get all the computational advantages of hashing!
Instructions
100 XP

    Import HashingVectorizer from sklearn.feature_extraction.text.
    Instantiate the HashingVectorizer as hashing_vec using the TOKENS_ALPHANUMERIC pattern.
    Fit and transform hashing_vec using text_data. Save the result as hashed_text.
    Hit 'Submit Answer' to see some of the resulting hash values.
"""
fit_transform
