import streamlit as st
import random
import string
import pandas as pd
from string_matching import naive_search, kmp_search, rabin_karp

st.set_page_config(page_title="String Matching Algorithms", layout="wide")

st.title("🔍 String Matching Algorithm Visualizer")
st.markdown("Compare Naive, KMP, and Rabin-Karp algorithms for pattern matching")

# Input section
col1, col2 = st.columns(2)
with col1:
    text = st.text_area("Enter text:", value="AABAACAADAABAABA", height=150)
with col2:
    pattern = st.text_input("Enter pattern:", value="AABA")

if st.button("🔍 Run Search", type="primary"):
    if text and pattern:
        with st.spinner("Running algorithms..."):
            # Run algorithms
            start = time.time()
            naive_matches, naive_comps = naive_search(text, pattern)
            naive_time = time.time() - start
            
            start = time.time()
            kmp_matches, kmp_comps = kmp_search(text, pattern)
            kmp_time = time.time() - start
            
            start = time.time()
            rk_matches, rk_comps = rabin_karp(text, pattern)
            rk_time = time.time() - start
        
        # Display results
        st.subheader("📊 Results")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Naive", f"{len(naive_matches)} matches")
            st.write(f"Comparisons: {naive_comps:,}")
            st.write(f"Time: {naive_time:.6f}s")
        with col2:
            st.metric("KMP", f"{len(kmp_matches)} matches")
            st.write(f"Comparisons: {kmp_comps:,}")
            st.write(f"Time: {kmp_time:.6f}s")
        with col3:
            st.metric("Rabin-Karp", f"{len(rk_matches)} matches")
            st.write(f"Comparisons: {rk_comps:,}")
            st.write(f"Time: {rk_time:.6f}s")
        
        # Show match positions
        if naive_matches:
            st.success(f"Pattern found at positions: {naive_matches}")
