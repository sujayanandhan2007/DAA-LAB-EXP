import streamlit as st
import pandas as pd


# ---------- Core DP algorithm (unchanged logic from the original script) ----------

def matrix_chain_order(dims):
    n = len(dims) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_optimal_parens(s, i, j):
    if i == j:
        return f'A{i}'
    k = s[i][j]
    left = print_optimal_parens(s, i, k)
    right = print_optimal_parens(s, k + 1, j)
    return f'({left} x {right})'


def build_cost_dataframe(m, n):
    cols = [f'A{j}' for j in range(1, n + 1)]
    rows = [f'A{i}' for i in range(1, n + 1)]
    data = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append('—' if j < i else int(m[i][j]))
        data.append(row)
    return pd.DataFrame(data, index=rows, columns=cols)


def build_split_dataframe(s, n):
    cols = [f'A{j}' for j in range(1, n + 1)]
    rows = [f'A{i}' for i in range(1, n + 1)]
    data = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            if j <= i:
                row.append('—')
            else:
                row.append(f'k={s[i][j]}')
        data.append(row)
    return pd.DataFrame(data, index=rows, columns=cols)


# ---------- Streamlit UI ----------

st.set_page_config(page_title="Matrix Chain Multiplication", page_icon="🔗", layout="centered")

st.title("🔗 Matrix Chain Multiplication")
st.caption("Dynamic programming visualizer — finds the optimal way to parenthesize a chain of matrix multiplications.")

st.markdown("### Input")
default_dims = "10, 30, 5, 60, 10"
dims_input = st.text_input(
    "Matrix dimensions (comma-separated)",
    value=default_dims,
    help="For matrices A1..An, enter p0, p1, ..., pn where Ai has dimensions p(i-1) x p(i)."
)

try:
    dims = [int(x.strip()) for x in dims_input.split(",") if x.strip() != ""]
except ValueError:
    st.error("Please enter only integers separated by commas.")
    st.stop()

if len(dims) < 2:
    st.warning("Enter at least 2 numbers (for at least 1 matrix).")
    st.stop()

n = len(dims) - 1

st.markdown("### Matrix Dimensions")
dim_table = pd.DataFrame(
    {"Matrix": [f"A{i+1}" for i in range(n)],
     "Rows": dims[:-1],
     "Cols": dims[1:]}
)
st.dataframe(dim_table, hide_index=True, use_container_width=True)

if n == 1:
    st.info("Only one matrix — no multiplication needed.")
    st.stop()

m, s = matrix_chain_order(dims)

st.markdown("### Result")
col1, col2 = st.columns(2)
col1.metric("Minimum scalar multiplications", f"{m[1][n]:.0f}")
col2.markdown("**Optimal parenthesization**")
col2.code(print_optimal_parens(s, 1, n), language=None)

st.markdown("### DP Cost Table `m[i][j]`")
st.dataframe(build_cost_dataframe(m, n), use_container_width=True)

with st.expander("Show split table (`s[i][j]` — where each optimal split occurs)"):
    st.dataframe(build_split_dataframe(s, n), use_container_width=True)

with st.expander("What's happening here?"):
    st.markdown(
        """
Matrix chain multiplication finds the cheapest order to multiply a chain of matrices
(matrix multiplication is associative, so the order affects total scalar multiplications
but not the result).

- **Brute force:** trying every parenthesization is exponential — O(4ⁿ / n^1.5).
- **This DP approach:** builds up the answer using optimal substructure, running in **O(n³)** time and O(n²) space.
- `m[i][j]` = minimum cost to multiply matrices Aᵢ..Aⱼ.
- `s[i][j]` = the split point k that achieves that minimum, used to reconstruct the parenthesization.
        """
    )

st.markdown("---")
st.caption("Deployed with Streamlit · DP core adapted from exp06_matrix_chain_multiplication.py")
