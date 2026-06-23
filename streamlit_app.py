import streamlit as st
import time
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
            if naive_matches:
                st.write(f"Positions: {naive_matches}")
        with col2:
            st.metric("KMP", f"{len(kmp_matches)} matches")
            st.write(f"Comparisons: {kmp_comps:,}")
            st.write(f"Time: {kmp_time:.6f}s")
            if kmp_matches:
                st.write(f"Positions: {kmp_matches}")
        with col3:
            st.metric("Rabin-Karp", f"{len(rk_matches)} matches")
            st.write(f"Comparisons: {rk_comps:,}")
            st.write(f"Time: {rk_time:.6f}s")
            if rk_matches:
                st.write(f"Positions: {rk_matches}")
        
        # Performance comparison chart
        st.subheader("📈 Performance Comparison")
        
        # Create DataFrame for comparison
        df = pd.DataFrame({
            'Algorithm': ['Naive', 'KMP', 'Rabin-Karp'],
            'Comparisons': [naive_comps, kmp_comps, rk_comps],
            'Time (ms)': [naive_time * 1000, kmp_time * 1000, rk_time * 1000]
        })
        
        col1, col2 = st.columns(2)
        with col1:
            st.bar_chart(df.set_index('Algorithm')['Comparisons'])
            st.caption("Number of character comparisons")
        with col2:
            st.bar_chart(df.set_index('Algorithm')['Time (ms)'])
            st.caption("Execution time in milliseconds")
        
        # Algorithm complexity information
        with st.expander("ℹ️ Algorithm Complexity"):
            st.markdown("""
            ### Time Complexities
            
            | Algorithm | Best Case | Average Case | Worst Case |
            |-----------|-----------|--------------|------------|
            | **Naive** | O(n) | O(n*m) | O(n*m) |
            | **KMP** | O(n) | O(n+m) | O(n+m) |
            | **Rabin-Karp** | O(n+m) | O(n+m) | O(n*m) |
            
            Where:
            - n = length of text
            - m = length of pattern
            
            ### Space Complexities
            - Naive: O(1)
            - KMP: O(m)
            - Rabin-Karp: O(1)
            """)
