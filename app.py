import warnings
import io
import zipfile
from datetime import datetime

warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from matplotlib.ticker import FuncFormatter
from scipy import stats

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="Seaborn & Matplotlib Visual Lab",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==================== GLOBAL STYLE ====================
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

    * {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: radial-gradient(circle at 0% 0%, #020617 0, #020617 45%, #020617 100%);
        color: #e5e7eb;
    }

    .block-container {
        padding-top: 1.4rem;
        padding-bottom: 3rem;
    }

    .main-header {
        font-size: 3.1rem;
        font-weight: 800;
        background: linear-gradient(135deg, #38bdf8 0%, #6366f1 40%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        font-size: 1.05rem;
        color: #9ca3af;
        margin-bottom: 1.1rem;
    }

    .metric-row {
        display: flex;
        flex-wrap: wrap;
        gap: 0.9rem;
        margin-top: 0.3rem;
        margin-bottom: 1.0rem;
    }

    .metric-card {
        background: radial-gradient(circle at 0% 0%, rgba(56, 189, 248, 0.18), rgba(15, 23, 42, 0.96));
        padding: 0.9rem 1.2rem;
        border-radius: 14px;
        color: #e5e7eb;
        box-shadow:
            0 14px 40px rgba(15, 23, 42, 0.9),
            0 0 0 1px rgba(148, 163, 184, 0.45);
        min-width: 160px;
    }

    .metric-card-label {
        font-size: 0.75rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #9ca3af;
    }

    .metric-card-value {
        font-size: 1.45rem;
        font-weight: 700;
        margin-top: 0.15rem;
    }

    .info-box {
        background: radial-gradient(circle at 0% 0%, rgba(45, 212, 191, 0.25), rgba(56, 189, 248, 0.10));
        padding: 0.9rem 1.2rem;
        border-radius: 14px;
        border-left: 4px solid #22d3ee;
        margin: 0.7rem 0 1.0rem 0;
        color: #e0f2fe;
        box-shadow: 0 16px 40px rgba(15, 23, 42, 0.9);
        backdrop-filter: blur(18px);
    }

    .tip-box {
        background: linear-gradient(135deg, rgba(250, 204, 21, 0.12), rgba(251, 191, 36, 0.04));
        padding: 0.75rem 1rem;
        border-radius: 10px;
        border-left: 3px solid rgba(250, 204, 21, 0.7);
        margin: 0.4rem 0;
        font-size: 0.9rem;
        color: #facc15;
    }

    .code-box {
        background: #020617;
        color: #e5e7eb;
        padding: 0.9rem 1rem;
        border-radius: 12px;
        border: 1px solid rgba(148, 163, 184, 0.5);
        margin: 0.5rem 0;
        font-size: 0.9rem;
        box-shadow: 0 14px 36px rgba(15, 23, 42, 0.9);
    }

    .plot-container {
        background: radial-gradient(circle at 0% 0%, rgba(148, 163, 184, 0.16), rgba(15, 23, 42, 0.96));
        padding: 1.4rem 1.5rem;
        border-radius: 18px;
        box-shadow:
            0 20px 50px rgba(15, 23, 42, 0.95),
            0 0 0 1px rgba(148, 163, 184, 0.4);
        margin: 1.0rem 0 1.4rem 0;
        border: 1px solid rgba(148, 163, 184, 0.35);
    }

    .control-panel {
        background: linear-gradient(145deg, rgba(15, 23, 42, 0.98), rgba(30, 64, 175, 0.85));
        padding: 0.8rem 1.1rem;
        border-radius: 999px;
        box-shadow:
            0 16px 40px rgba(15, 23, 42, 0.9),
            0 0 0 1px rgba(129, 140, 248, 0.7);
        color: #e5e7eb;
        margin-bottom: 0.7rem;
    }

    .control-panel-header {
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin: 0;
        color: #e5e7eb;
        opacity: 0.98;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 0.7rem;
        background: transparent;
        padding: 0.4rem 0 0.8rem 0;
        border-radius: 0;
        border-bottom: 1px solid rgba(148, 163, 184, 0.35);
    }

    .stTabs [data-baseweb="tab"] {
        height: 3.3rem;
        padding: 0 1.8rem;
        font-weight: 600;
        border-radius: 999px;
        background: rgba(15, 23, 42, 0.86);
        border: 1px solid rgba(148, 163, 184, 0.5);
        color: #e5e7eb;
        transition: transform 0.18s ease, background 0.18s ease,
                    border-color 0.18s ease, box-shadow 0.18s ease;
    }

    .stTabs [data-baseweb="tab"]:hover {
        transform: translateY(-1px);
        border-color: rgba(129, 140, 248, 0.9);
        box-shadow: 0 10px 22px rgba(15, 23, 42, 0.85);
    }

    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, #6366f1, #ec4899);
        color: #ffffff;
        border-color: transparent;
        box-shadow:
            0 0 0 1px rgba(15, 23, 42, 0.9),
            0 14px 30px rgba(15, 23, 42, 0.95);
    }
</style>
""",
    unsafe_allow_html=True,
)

# ==================== SESSION STATE ====================
if "gallery" not in st.session_state:
    st.session_state["gallery"] = []

if "export_dpi" not in st.session_state:
    st.session_state["export_dpi"] = 300

# ==================== HELPERS ====================
def use_theme(context: str = "notebook", style: str = "whitegrid", palette: str = "deep") -> None:
    sns.set_theme(context=context, style=style)
    sns.set_palette(palette)
    plt.rcParams.update(
        {
            "figure.figsize": (10, 6),
            "savefig.dpi": 300,
            "figure.dpi": 150,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "figure.autolayout": True,
            "grid.alpha": 0.3,
            "grid.linestyle": "--",
            "font.size": 10,
            "axes.labelsize": 11,
            "axes.titlesize": 13,
            "legend.fontsize": 9,
        }
    )


def apply_dark(fig: plt.Figure, dark: bool = False) -> None:
    if not dark:
        return
    fig.patch.set_facecolor("#020617")
    for ax in fig.get_axes():
        ax.set_facecolor("#020617")
        ax.tick_params(colors="#e5e7eb")
        for spine in ax.spines.values():
            spine.set_color("#4b5563")
        for item in [ax.title, ax.xaxis.label, ax.yaxis.label]:
            if item:
                item.set_color("#e5e7eb")
        for t in ax.get_xticklabels() + ax.get_yticklabels():
            t.set_color("#e5e7eb")
        legend = ax.get_legend()
        if legend:
            legend.get_frame().set_facecolor("#020617")
            for text in legend.get_texts():
                text.set_color("#e5e7eb")


@st.cache_data
def load_builtin_data() -> dict:
    return {
        "Tips": sns.load_dataset("tips"),
        "Penguins": sns.load_dataset("penguins").dropna(),
        "Flights": sns.load_dataset("flights"),
        "Iris": sns.load_dataset("iris"),
        "Diamonds (1K sample)": sns.load_dataset("diamonds").sample(1000, random_state=42),
        "Titanic": sns.load_dataset("titanic"),
        "Car Crashes": sns.load_dataset("car_crashes"),
    }


def save_to_gallery(fig: plt.Figure, name: str, description: str) -> None:
    buf = io.BytesIO()
    dpi = st.session_state.get("export_dpi", 300)
    fig.savefig(
        buf,
        dpi=dpi,
        bbox_inches="tight",
        format="png",
        facecolor=fig.get_facecolor(),
    )
    buf.seek(0)
    st.session_state["gallery"].append(
        {
            "name": name,
            "description": description,
            "image": buf.getvalue(),
            "timestamp": datetime.now(),
        }
    )


def show_code_example(code: str, description: str = "") -> None:
    if description:
        st.markdown(
            f'<div class="tip-box"><strong>Tip:</strong> {description}</div>',
            unsafe_allow_html=True,
        )
    st.markdown('<div class="code-box">', unsafe_allow_html=True)
    st.code(code, language="python")
    st.markdown("</div>", unsafe_allow_html=True)

# ==================== HEADER ====================
st.markdown(
    '<h1 class="main-header">Seaborn & Matplotlib Visual Lab</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="subtitle">Interactive environment to explore, compare, and export visualizations with Seaborn and Matplotlib.</p>',
    unsafe_allow_html=True,
)

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("### Data settings")

    # Built-in datasets only
    builtin = load_builtin_data()
    dataset_label = st.selectbox(
        "Built-in only",
        list(builtin.keys()),
        key="sb_dataset",
    )
    df = builtin[dataset_label]

    st.markdown("---")

    with st.expander("Visual theme", expanded=False):
        context = st.selectbox(
            "Seaborn context",
            ["notebook", "paper", "talk", "poster"],
            index=0,
            key="sb_context",
        )
        style = st.selectbox(
            "Seaborn style",
            ["whitegrid", "darkgrid", "white", "dark", "ticks"],
            index=0,
            key="sb_style",
        )
        palette = st.selectbox(
            "Color palette",
            ["deep", "muted", "bright", "pastel", "dark", "colorblind", "Set2", "husl"],
            index=0,
            key="sb_palette",
        )
        use_theme(context, style, palette)

        theme_mode = st.radio(
            "Figure mode",
            ["Light", "Dark"],
            index=1,
            horizontal=True,
            key="sb_theme_mode",
        )
        DARK = theme_mode == "Dark"

    st.markdown("---")

    st.markdown("### Export settings")
    dpi = st.slider(
        "Image quality (DPI)",
        72,
        600,
        300,
        step=50,
        key="sb_dpi",
    )
    st.session_state["export_dpi"] = dpi

    if st.session_state["gallery"]:
        st.success(f"{len(st.session_state['gallery'])} plots in gallery")
        if st.button("Clear gallery", key="sb_clear_gallery"):
            st.session_state["gallery"] = []
            st.rerun()

# fallback
if df is None:
    df = builtin["Tips"]
    dataset_label = "Tips"

numeric_cols_all = df.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols_all = df.select_dtypes(include=["object", "category"]).columns.tolist()
missing_ratio = float(df.isna().mean().mean() * 100)

# ==================== TOP METRICS ====================
st.markdown(
    f"""
<div class="metric-row">
  <div class="metric-card">
    <div class="metric-card-label">Dataset</div>
    <div class="metric-card-value">{dataset_label}</div>
  </div>
  <div class="metric-card">
    <div class="metric-card-label">Rows</div>
    <div class="metric-card-value">{len(df):,}</div>
  </div>
  <div class="metric-card">
    <div class="metric-card-label">Columns</div>
    <div class="metric-card-value">{len(df.columns):,}</div>
  </div>
  <div class="metric-card">
    <div class="metric-card-label">Numeric features</div>
    <div class="metric-card-value">{len(numeric_cols_all)}</div>
  </div>
  <div class="metric-card">
    <div class="metric-card-label">Categorical features</div>
    <div class="metric-card-value">{len(categorical_cols_all)}</div>
  </div>
  <div class="metric-card">
    <div class="metric-card-label">Missing ratio</div>
    <div class="metric-card-value">{missing_ratio:.1f}%</div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ==================== TABS ====================
tab_overview, tab_seaborn, tab_mpl, tab_compare, tab_gallery = st.tabs(
    [
        "Overview",
        "Seaborn builder",
        "Matplotlib builder",
        "Compare",
        "Gallery",
    ]
)

# ==================== TAB: OVERVIEW ====================
with tab_overview:
    st.markdown("## Overview")
    st.markdown(
        '<div class="info-box"><strong>Goal:</strong> Quick health check of the current dataset and a first look at its distributions.</div>',
        unsafe_allow_html=True,
    )

    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.markdown("### Sample")
        st.dataframe(df.head(10), use_container_width=True)

        if numeric_cols_all:
            st.markdown("### Quick distribution")
            dist_col = st.selectbox(
                "Numeric column",
                numeric_cols_all,
                key="ov_dist_col",
            )
            fig, ax = plt.subplots(figsize=(10, 4))
            sns.histplot(df, x=dist_col, bins=30, kde=True, ax=ax)
            ax.set_title(f"{dist_col} distribution", fontsize=13, fontweight="bold")
            apply_dark(fig, DARK)
            st.pyplot(fig)

    with col_right:
        st.markdown("### Types & missing")
        schema_data = {
            "column": df.columns,
            "dtype": df.dtypes.astype(str),
            "missing_%": (df.isna().mean() * 100).round(1),
        }
        schema_df = pd.DataFrame(schema_data)
        st.dataframe(schema_df, height=260, use_container_width=True)

        if len(numeric_cols_all) >= 2:
            st.markdown("### Small correlation view")
            cols_small = numeric_cols_all[: min(4, len(numeric_cols_all))]
            corr = df[cols_small].corr()
            fig2, ax2 = plt.subplots(figsize=(4, 4))
            sns.heatmap(
                corr,
                annot=True,
                fmt=".2f",
                cmap="vlag",
                center=0,
                square=True,
                cbar=False,
                ax=ax2,
            )
            ax2.set_title("Correlation (subset)", fontsize=11, fontweight="bold")
            apply_dark(fig2, DARK)
            st.pyplot(fig2)

# ==================== TAB: SEABORN BUILDER ====================
with tab_seaborn:
    st.markdown("## Seaborn builder")
    st.markdown(
        '<div class="info-box"><strong>Goal:</strong> Build Seaborn plots by selecting columns and options. The code snippet updates automatically.</div>',
        unsafe_allow_html=True,
    )

    if df.empty:
        st.warning("No data loaded.")
    else:
        col_plot, col_ctrl = st.columns([7, 3])

        with col_ctrl:
            # Pill with header INSIDE
            st.markdown(
                """
<div class="control-panel">
  <div class="control-panel-header">PLOT SETUP</div>
</div>
""",
                unsafe_allow_html=True,
            )

            family = st.selectbox(
                "Plot family",
                [
                    "Distribution",
                    "Relationship",
                    "Category",
                    "Matrix / Heatmap",
                    "Multi-variable",
                ],
                key="sb_family",
            )

            code_str = ""
            description = ""
            fig_seaborn = None

            if family == "Distribution":
                kind = st.selectbox(
                    "Plot type",
                    [
                        "Histogram",
                        "KDE",
                        "Histogram + KDE",
                        "Box",
                        "Violin",
                        "ECDF",
                    ],
                    key="sb_dist_kind",
                )
                if not numeric_cols_all:
                    num_col = None
                    st.error("No numeric columns in this dataset.")
                else:
                    num_col = st.selectbox(
                        "Numeric column",
                        numeric_cols_all,
                        key="sb_dist_num",
                    )

                hue_col = None
                if categorical_cols_all and kind in ["Histogram", "KDE", "Histogram + KDE", "ECDF"]:
                    use_hue_dist = st.checkbox(
                        "Color by category",
                        value=False,
                        key="sb_dist_use_hue",
                    )
                    if use_hue_dist:
                        hue_col = st.selectbox(
                            "Hue",
                            categorical_cols_all,
                            key="sb_dist_hue",
                        )
                bins = st.slider(
                    "Bins (for histogram)",
                    5,
                    80,
                    30,
                    key="sb_dist_bins",
                )
                log_scale = st.checkbox(
                    "Log scale on x",
                    value=False,
                    key="sb_dist_log",
                )

            elif family == "Relationship":
                rel_kind = st.selectbox(
                    "Plot type",
                    [
                        "Scatter",
                        "Regression",
                        "Line",
                    ],
                    key="sb_rel_kind",
                )
                if len(numeric_cols_all) < 2:
                    x_rel = y_rel = None
                    st.error("Need at least two numeric columns.")
                else:
                    x_rel = st.selectbox(
                        "X variable",
                        numeric_cols_all,
                        key="sb_rel_x",
                    )
                    y_rel = st.selectbox(
                        "Y variable",
                        [c for c in numeric_cols_all if c != x_rel],
                        key="sb_rel_y",
                    )
                hue_rel = None
                if categorical_cols_all and rel_kind in ["Scatter", "Line"]:
                    use_hue_rel = st.checkbox(
                        "Color by category",
                        value=False,
                        key="sb_rel_use_hue",
                    )
                    if use_hue_rel:
                        hue_rel = st.selectbox(
                            "Hue",
                            categorical_cols_all,
                            key="sb_rel_hue",
                        )
                alpha_rel = st.slider(
                    "Point transparency",
                    0.1,
                    1.0,
                    0.7,
                    0.05,
                    key="sb_rel_alpha",
                )

            elif family == "Category":
                if not categorical_cols_all:
                    st.error("No categorical columns in this dataset.")
                    cat_var = num_cat = None
                else:
                    cat_var = st.selectbox(
                        "Category",
                        categorical_cols_all,
                        key="sb_cat_var",
                    )
                cat_kind = st.selectbox(
                    "Plot type",
                    [
                        "Count",
                        "Bar (mean)",
                        "Box",
                        "Violin",
                    ],
                    key="sb_cat_kind",
                )
                num_cat = None
                if cat_kind in ["Bar (mean)", "Box", "Violin"]:
                    if not numeric_cols_all:
                        st.error("No numeric columns for this plot type.")
                    else:
                        num_cat = st.selectbox(
                            "Numeric column",
                            numeric_cols_all,
                            key="sb_cat_num",
                        )

                if cat_var is not None:
                    order_top = st.slider(
                        "Top categories",
                        3,
                        min(15, df[cat_var].nunique()),
                        min(8, df[cat_var].nunique()),
                        key="sb_cat_top",
                    )

            elif family == "Matrix / Heatmap":
                if len(numeric_cols_all) < 2:
                    st.error("Need at least two numeric columns.")
                    selected_hm = []
                else:
                    selected_hm = st.multiselect(
                        "Numeric variables",
                        numeric_cols_all,
                        default=numeric_cols_all[: min(6, len(numeric_cols_all))],
                        key="sb_hm_vars",
                    )
                annot_hm = st.checkbox(
                    "Show values",
                    value=True,
                    key="sb_hm_annot",
                )
                center_zero = st.checkbox(
                    "Center at zero",
                    value=True,
                    key="sb_hm_center",
                )

            else:  # Multi-variable
                if len(numeric_cols_all) < 2:
                    st.error("Need at least two numeric columns.")
                    multi_vars = []
                else:
                    multi_vars = st.multiselect(
                        "Numeric variables",
                        numeric_cols_all,
                        default=numeric_cols_all[: min(4, len(numeric_cols_all))],
                        key="sb_multi_vars",
                    )
                sample_n = st.slider(
                    "Sample rows",
                    100,
                    min(len(df), 1000),
                    min(400, len(df)),
                    key="sb_multi_sample",
                )
                hue_multi = None
                if categorical_cols_all:
                    use_hue_multi = st.checkbox(
                        "Color by category",
                        value=False,
                        key="sb_multi_use_hue",
                    )
                    if use_hue_multi:
                        hue_multi = st.selectbox(
                            "Hue",
                            categorical_cols_all,
                            key="sb_multi_hue",
                        )

        with col_plot:
            st.markdown('<div class="plot-container">', unsafe_allow_html=True)

            # ------- Distribution -------
            if family == "Distribution" and numeric_cols_all and num_col is not None:
                fig_seaborn, ax = plt.subplots(figsize=(10, 5))

                if kind == "Histogram":
                    sns.histplot(
                        data=df,
                        x=num_col,
                        bins=bins,
                        hue=hue_col,
                        kde=False,
                        ax=ax,
                        log_scale=log_scale,
                    )
                elif kind == "KDE":
                    sns.kdeplot(
                        data=df,
                        x=num_col,
                        hue=hue_col,
                        fill=True,
                        ax=ax,
                        log_scale=log_scale,
                    )
                elif kind == "Histogram + KDE":
                    sns.histplot(
                        data=df,
                        x=num_col,
                        bins=bins,
                        hue=hue_col,
                        kde=True,
                        ax=ax,
                        log_scale=log_scale,
                    )
                elif kind == "Box":
                    sns.boxplot(
                        data=df,
                        x=num_col,
                        ax=ax,
                    )
                elif kind == "Violin":
                    sns.violinplot(
                        data=df,
                        x=num_col,
                        ax=ax,
                    )
                else:  # ECDF
                    sns.ecdfplot(
                        data=df,
                        x=num_col,
                        hue=hue_col,
                        ax=ax,
                    )
                    ax.yaxis.set_major_formatter(
                        FuncFormatter(lambda y, _: f"{y:.0%}")
                    )

                ax.set_title(f"{kind} for {num_col}", fontsize=13, fontweight="bold")
                apply_dark(fig_seaborn, DARK)
                st.pyplot(fig_seaborn)

                hue_part = f', hue="{hue_col}"' if hue_col else ""
                extra_kwargs = ""
                if kind in ["Histogram", "Histogram + KDE"]:
                    extra_kwargs = f", bins={bins}"
                    if log_scale:
                        extra_kwargs += ", log_scale=True"
                if kind in ["KDE", "ECDF"] and log_scale:
                    extra_kwargs = ", log_scale=True"
                if kind == "Histogram + KDE":
                    fn = "histplot"
                    extra_kwargs = f", bins={bins}, kde=True"
                elif kind == "Histogram":
                    fn = "histplot"
                elif kind == "KDE":
                    fn = "kdeplot"
                elif kind == "Box":
                    fn = "boxplot"
                elif kind == "Violin":
                    fn = "violinplot"
                else:
                    fn = "ecdfplot"

                code_str = f"""fig, ax = plt.subplots(figsize=(10, 5))
sns.{fn}(data=df, x="{num_col}"{hue_part}{extra_kwargs}, ax=ax)
ax.set_title("{kind} for {num_col}")
plt.show()"""
                description = "Distribution pattern: shape, spread, and tails of a single numeric column."

            # ------- Relationship -------
            elif family == "Relationship" and len(numeric_cols_all) >= 2 and x_rel is not None:
                fig_seaborn, ax = plt.subplots(figsize=(10, 5))

                if rel_kind == "Scatter":
                    sns.scatterplot(
                        data=df,
                        x=x_rel,
                        y=y_rel,
                        hue=hue_rel,
                        alpha=alpha_rel,
                        s=70,
                        ax=ax,
                    )
                elif rel_kind == "Line":
                    sns.lineplot(
                        data=df,
                        x=x_rel,
                        y=y_rel,
                        hue=hue_rel,
                        ax=ax,
                    )
                else:  # Regression
                    sns.regplot(
                        data=df,
                        x=x_rel,
                        y=y_rel,
                        ax=ax,
                        scatter_kws={"alpha": alpha_rel, "s": 60},
                        line_kws={"linewidth": 2},
                    )

                ax.set_title(
                    f"{rel_kind}: {y_rel} vs {x_rel}",
                    fontsize=13,
                    fontweight="bold",
                )
                apply_dark(fig_seaborn, DARK)
                st.pyplot(fig_seaborn)

                if rel_kind == "Scatter":
                    hue_part = f', hue="{hue_rel}"' if hue_rel else ""
                    code_str = f"""fig, ax = plt.subplots(figsize=(10, 5))
sns.scatterplot(
    data=df,
    x="{x_rel}",
    y="{y_rel}"{hue_part},
    alpha=0.7,
    s=70,
    ax=ax,
)
ax.set_title("Scatter: {y_rel} vs {x_rel}")
plt.show()"""
                elif rel_kind == "Line":
                    hue_part = f', hue="{hue_rel}"' if hue_rel else ""
                    code_str = f"""fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(
    data=df,
    x="{x_rel}",
    y="{y_rel}"{hue_part},
    ax=ax,
)
ax.set_title("Line: {y_rel} vs {x_rel}")
plt.show()"""
                else:
                    code_str = f"""fig, ax = plt.subplots(figsize=(10, 5))
sns.regplot(
    data=df,
    x="{x_rel}",
    y="{y_rel}",
    scatter_kws={{"alpha": 0.7, "s": 60}},
    line_kws={{"linewidth": 2}},
    ax=ax,
)
ax.set_title("Regression: {y_rel} vs {x_rel}")
plt.show()"""
                description = "Relationship pattern: how two numeric variables move together."

            # ------- Category -------
            elif family == "Category" and categorical_cols_all and cat_var is not None:
                fig_seaborn, ax = plt.subplots(figsize=(10, 5))

                df_tmp = df.copy()
                top_cats = (
                    df_tmp[cat_var]
                    .value_counts()
                    .head(order_top)
                    .index
                )
                df_tmp = df_tmp[df_tmp[cat_var].isin(top_cats)]

                if cat_kind == "Count":
                    sns.countplot(
                        data=df_tmp,
                        y=cat_var,
                        order=top_cats,
                        ax=ax,
                    )
                    for container in ax.containers:
                        ax.bar_label(container, padding=3)
                elif cat_kind == "Bar (mean)":
                    sns.barplot(
                        data=df_tmp,
                        y=cat_var,
                        x=num_cat,
                        order=top_cats,
                        ax=ax,
                        ci=95,
                    )
                elif cat_kind == "Box":
                    sns.boxplot(
                        data=df_tmp,
                        y=cat_var,
                        x=num_cat,
                        order=top_cats,
                        ax=ax,
                    )
                else:  # Violin
                    sns.violinplot(
                        data=df_tmp,
                        y=cat_var,
                        x=num_cat,
                        order=top_cats,
                        ax=ax,
                    )

                ax.set_title(
                    f"{cat_kind} for {cat_var}",
                    fontsize=13,
                    fontweight="bold",
                )
                apply_dark(fig_seaborn, DARK)
                st.pyplot(fig_seaborn)

                if cat_kind == "Count":
                    code_str = f"""fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(
    data=df,
    y="{cat_var}",
    ax=ax,
)
ax.set_title("Count for {cat_var}")
plt.show()"""
                elif cat_kind == "Bar (mean)":
                    code_str = f"""fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    data=df,
    y="{cat_var}",
    x="{num_cat}",
    ci=95,
    ax=ax,
)
ax.set_title("Mean {num_cat} by {cat_var}")
plt.show()"""
                elif cat_kind == "Box":
                    code_str = f"""fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(
    data=df,
    y="{cat_var}",
    x="{num_cat}",
    ax=ax,
)
ax.set_title("Box: {num_cat} by {cat_var}")
plt.show()"""
                else:
                    code_str = f"""fig, ax = plt.subplots(figsize=(10, 5))
sns.violinplot(
    data=df,
    y="{cat_var}",
    x="{num_cat}",
    ax=ax,
)
ax.set_title("Violin: {num_cat} by {cat_var}")
plt.show()"""
                description = "Category pattern: compare distributions or means across groups."

            # ------- Matrix / Heatmap -------
            elif family == "Matrix / Heatmap" and selected_hm:
                corr = df[selected_hm].corr()
                fig_seaborn, ax = plt.subplots(figsize=(7, 6))
                sns.heatmap(
                    corr,
                    annot=annot_hm,
                    fmt=".2f",
                    cmap="vlag",
                    center=0 if center_zero else None,
                    square=True,
                    linewidths=1,
                    cbar_kws={"shrink": 0.8},
                    ax=ax,
                )
                ax.set_title("Correlation heatmap", fontsize=13, fontweight="bold")
                apply_dark(fig_seaborn, DARK)
                st.pyplot(fig_seaborn)

                center_value = "0" if center_zero else "None"
                code_str = f"""corr = df[{selected_hm}].corr()
fig, ax = plt.subplots(figsize=(7, 6))
sns.heatmap(
    corr,
    annot={annot_hm},
    fmt=".2f",
    cmap="vlag",
    center={center_value},
    square=True,
    linewidths=1,
    cbar_kws={{"shrink": 0.8}},
    ax=ax,
)
ax.set_title("Correlation heatmap")
plt.show()"""
                description = "Matrix pattern: scan many pairwise relationships at once."

            # ------- Multi-variable (pairplot) -------
            elif family == "Multi-variable" and multi_vars:
                sample_size = min(sample_n, len(df))
                cols_to_use = multi_vars + ([hue_multi] if hue_multi else [])
                df_sample = df[cols_to_use].dropna().sample(sample_size, random_state=42)

                with st.spinner("Building pairplot..."):
                    g = sns.pairplot(
                        df_sample,
                        vars=multi_vars,
                        hue=hue_multi,
                        corner=True,
                        diag_kind="kde",
                        plot_kws={"alpha": 0.6},
                        diag_kws={"alpha": 0.7},
                    )
                    g.fig.suptitle("Pairplot", y=1.01, fontweight="bold")
                    fig_seaborn = g.fig
                    apply_dark(fig_seaborn, DARK)
                    st.pyplot(fig_seaborn)

                code_str = f"""sample = df[{multi_vars + ([hue_multi] if hue_multi else [])}].dropna().sample({sample_n}, random_state=42)
g = sns.pairplot(
    sample,
    vars={multi_vars},
    hue={repr(hue_multi)},
    corner=True,
    diag_kind="kde",
    plot_kws={{"alpha": 0.6}},
)
g.fig.suptitle("Pairplot", y=1.01)
plt.show()"""
                description = "Multi-variable view: every pair of variables in one grid."

            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("### Code preview")
        if code_str:
            show_code_example(code_str, description)

        if "fig_seaborn" in locals() and fig_seaborn is not None:
            if st.button("Save last Seaborn plot to gallery", key="sb_save_gallery"):
                save_to_gallery(fig_seaborn, f"Seaborn: {family}", "Seaborn builder plot")
                st.success("Saved to gallery.")

# ==================== TAB: MATPLOTLIB BUILDER ====================
with tab_mpl:
    st.markdown("## Matplotlib builder")
    st.markdown(
        '<div class="info-box"><strong>Goal:</strong> Build Matplotlib plots with fine-grained control on axes and layouts.</div>',
        unsafe_allow_html=True,
    )

    if df.empty:
        st.warning("No data loaded.")
    else:
        col_plot, col_ctrl = st.columns([7, 3])

        with col_ctrl:
            st.markdown(
                """
<div class="control-panel">
  <div class="control-panel-header">PLOT SETUP</div>
</div>
""",
                unsafe_allow_html=True,
            )

            mpl_type = st.selectbox(
                "Plot type",
                [
                    "Line",
                    "Scatter",
                    "Bar",
                    "Histogram",
                    "Box",
                    "Subplots overview",
                ],
                key="mpl_type",
            )

            code_mpl = ""
            fig_mpl = None

            if mpl_type == "Line":
                x_line = st.selectbox(
                    "X (numeric or index)",
                    ["index"] + numeric_cols_all,
                    key="mpl_line_x",
                )
                y_line = st.selectbox(
                    "Y (numeric)",
                    numeric_cols_all,
                    key="mpl_line_y",
                )
                marker = st.selectbox(
                    "Marker",
                    ["o", "s", "None"],
                    index=0,
                    key="mpl_line_marker",
                )
                use_grid = st.checkbox(
                    "Show grid",
                    value=True,
                    key="mpl_line_grid",
                )

            elif mpl_type == "Scatter":
                if len(numeric_cols_all) < 2:
                    st.error("Need at least two numeric columns for scatter.")
                x_sc = st.selectbox(
                    "X (numeric)",
                    numeric_cols_all,
                    key="mpl_sc_x",
                )
                y_sc = st.selectbox(
                    "Y (numeric)",
                    [c for c in numeric_cols_all if c != x_sc],
                    key="mpl_sc_y",
                )
                color_by = None
                if categorical_cols_all:
                    use_color = st.checkbox(
                        "Color by category",
                        value=False,
                        key="mpl_sc_use_color",
                    )
                    if use_color:
                        color_by = st.selectbox(
                            "Category",
                            categorical_cols_all,
                            key="mpl_sc_color_by",
                        )
                alpha_sc = st.slider(
                    "Point transparency",
                    0.1,
                    1.0,
                    0.7,
                    0.05,
                    key="mpl_sc_alpha",
                )
                size_sc = st.slider(
                    "Point size",
                    20,
                    200,
                    70,
                    key="mpl_sc_size",
                )

            elif mpl_type == "Bar":
                cat_for_bar = None
                if categorical_cols_all:
                    cat_for_bar = st.selectbox(
                        "Category",
                        categorical_cols_all,
                        key="mpl_bar_cat",
                    )
                else:
                    st.error("Need a categorical column for bar plot.")
                num_for_bar = st.selectbox(
                    "Value",
                    numeric_cols_all,
                    key="mpl_bar_num",
                )
                agg_bar = st.selectbox(
                    "Aggregation",
                    ["mean", "sum", "count"],
                    key="mpl_bar_agg",
                )
                horiz = st.checkbox(
                    "Horizontal bars",
                    value=True,
                    key="mpl_bar_horiz",
                )

            elif mpl_type == "Histogram":
                num_hist = st.selectbox(
                    "Numeric column",
                    numeric_cols_all,
                    key="mpl_hist_num",
                )
                bins_hist = st.slider(
                    "Bins",
                    5,
                    80,
                    30,
                    key="mpl_hist_bins",
                )
                density_hist = st.checkbox(
                    "Show density instead of counts",
                    value=False,
                    key="mpl_hist_density",
                )

            elif mpl_type == "Box":
                nums_box = st.multiselect(
                    "Numeric columns",
                    numeric_cols_all,
                    default=numeric_cols_all[: min(4, len(numeric_cols_all))],
                    key="mpl_box_nums",
                )

            else:  # Subplots overview
                nums_over = st.multiselect(
                    "Numeric columns",
                    numeric_cols_all,
                    default=numeric_cols_all[: min(3, len(numeric_cols_all))],
                    key="mpl_over_nums",
                )
                use_kde = st.checkbox(
                    "Overlay KDE on histograms",
                    value=True,
                    key="mpl_over_kde",
                )

        with col_plot:
            st.markdown('<div class="plot-container">', unsafe_allow_html=True)

            if mpl_type == "Line":
                if not numeric_cols_all:
                    st.error("No numeric columns for line plot.")
                else:
                    if x_line == "index":
                        x_vals = np.arange(len(df))
                        x_label = "Index"
                    else:
                        x_vals = df[x_line].values
                        x_label = x_line
                    y_vals = df[y_line].values

                    fig_mpl, ax = plt.subplots(figsize=(10, 5))
                    line_marker = None if marker == "None" else marker
                    ax.plot(x_vals, y_vals, marker=line_marker, lw=2)
                    ax.set_title(f"Line: {y_line} over {x_label}", fontsize=13, fontweight="bold")
                    ax.set_xlabel(x_label)
                    ax.set_ylabel(y_line)
                    if use_grid:
                        ax.grid(alpha=0.3)
                    apply_dark(fig_mpl, DARK)
                    st.pyplot(fig_mpl)

                    code_mpl = f"""fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(
    { 'np.arange(len(df))' if x_line == "index" else f'df["{x_line}"]' },
    df["{y_line}"],
    marker={'None' if marker == "None" else repr(marker)},
    lw=2,
)
ax.set_title("Line: {y_line} over {x_label}")
ax.set_xlabel("{x_label}")
ax.set_ylabel("{y_line}")
ax.grid(alpha=0.3)
plt.show()"""

            elif mpl_type == "Scatter":
                if len(numeric_cols_all) < 2:
                    st.error("No numeric columns for scatter plot.")
                else:
                    fig_mpl, ax = plt.subplots(figsize=(10, 5))
                    if color_by:
                        unique_vals = df[color_by].dropna().unique()
                        cmap = plt.get_cmap("tab10")
                        for idx, val in enumerate(unique_vals):
                            mask = df[color_by] == val
                            ax.scatter(
                                df.loc[mask, x_sc],
                                df.loc[mask, y_sc],
                                alpha=alpha_sc,
                                s=size_sc,
                                label=str(val),
                                color=cmap(idx % 10),
                            )
                        ax.legend(title=color_by)
                    else:
                        ax.scatter(
                            df[x_sc],
                            df[y_sc],
                            alpha=alpha_sc,
                            s=size_sc,
                        )
                    ax.set_title(f"Scatter: {y_sc} vs {x_sc}", fontsize=13, fontweight="bold")
                    ax.set_xlabel(x_sc)
                    ax.set_ylabel(y_sc)
                    ax.grid(alpha=0.3)
                    apply_dark(fig_mpl, DARK)
                    st.pyplot(fig_mpl)

                    code_mpl = f"""fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(
    df["{x_sc}"],
    df["{y_sc}"],
    alpha={alpha_sc},
    s={size_sc},
)
ax.set_title("Scatter: {y_sc} vs {x_sc}")
ax.set_xlabel("{x_sc}")
ax.set_ylabel("{y_sc}")
ax.grid(alpha=0.3)
plt.show()"""

            elif mpl_type == "Bar":
                if cat_for_bar is None:
                    st.error("Select a categorical column for the bar plot.")
                else:
                    grouped = getattr(df.groupby(cat_for_bar)[num_for_bar], agg_bar)()
                    grouped = grouped.sort_values(ascending=True)
                    fig_mpl, ax = plt.subplots(figsize=(9, 5))
                    if horiz:
                        ax.barh(grouped.index, grouped.values)
                        ax.set_xlabel(num_for_bar)
                        ax.set_ylabel(cat_for_bar)
                    else:
                        ax.bar(grouped.index, grouped.values)
                        ax.set_ylabel(num_for_bar)
                        ax.set_xlabel(cat_for_bar)
                        plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
                    ax.set_title(f"{agg_bar} of {num_for_bar} by {cat_for_bar}", fontsize=13, fontweight="bold")
                    ax.grid(axis="x" if horiz else "y", alpha=0.3)
                    apply_dark(fig_mpl, DARK)
                    st.pyplot(fig_mpl)

                    code_mpl = f"""grouped = df.groupby("{cat_for_bar}")["{num_for_bar}"].{agg_bar}().sort_values()
fig, ax = plt.subplots(figsize=(9, 5))
ax.barh(grouped.index, grouped.values) if {horiz} else ax.bar(grouped.index, grouped.values)
ax.set_title("{agg_bar} of {num_for_bar} by {cat_for_bar}")
plt.show()"""

            elif mpl_type == "Histogram":
                fig_mpl, ax = plt.subplots(figsize=(9, 5))
                ax.hist(
                    df[num_hist].dropna().values,
                    bins=bins_hist,
                    density=density_hist,
                    alpha=0.85,
                )
                ax.set_title(f"Histogram of {num_hist}", fontsize=13, fontweight="bold")
                ax.set_xlabel(num_hist)
                ax.set_ylabel("Density" if density_hist else "Count")
                ax.grid(alpha=0.3)
                apply_dark(fig_mpl, DARK)
                st.pyplot(fig_mpl)

                code_mpl = f"""fig, ax = plt.subplots(figsize=(9, 5))
ax.hist(
    df["{num_hist}"].dropna().values,
    bins={bins_hist},
    density={density_hist},
    alpha=0.85,
)
ax.set_title("Histogram of {num_hist}")
ax.set_xlabel("{num_hist}")
ax.set_ylabel("{'Density' if density_hist else 'Count'}")
ax.grid(alpha=0.3)
plt.show()"""

            elif mpl_type == "Box":
                if not nums_box:
                    st.warning("Select at least one numeric column.")
                else:
                    fig_mpl, ax = plt.subplots(figsize=(10, 5))
                    ax.boxplot(
                        [df[c].dropna().values for c in nums_box],
                        labels=nums_box,
                        vert=True,
                    )
                    ax.set_title("Box plots", fontsize=13, fontweight="bold")
                    ax.grid(alpha=0.3)
                    apply_dark(fig_mpl, DARK)
                    st.pyplot(fig_mpl)

                    code_mpl = f"""fig, ax = plt.subplots(figsize=(10, 5))
ax.boxplot(
    [{', '.join([f'df["{c}"].dropna().values' for c in nums_box])}],
    labels={nums_box},
)
ax.set_title("Box plots")
ax.grid(alpha=0.3)
plt.show()"""

            else:  # Subplots overview
                if not nums_over:
                    st.warning("Select at least one numeric column.")
                else:
                    k = len(nums_over)
                    fig_mpl, axes = plt.subplots(
                        1,
                        k,
                        figsize=(4 * k, 4),
                        squeeze=False,
                    )
                    for idx, col_name in enumerate(nums_over):
                        ax = axes[0, idx]
                        data = df[col_name].dropna().values
                        ax.hist(data, bins=30, alpha=0.8, density=True)
                        if use_kde and len(data) > 10:
                            x_vals = np.linspace(data.min(), data.max(), 200)
                            kde = stats.gaussian_kde(data)
                            ax.plot(x_vals, kde(x_vals), lw=2)
                        ax.set_title(col_name)
                        ax.grid(alpha=0.3)
                    fig_mpl.suptitle("Numeric overview", fontsize=13, fontweight="bold")
                    plt.tight_layout()
                    apply_dark(fig_mpl, DARK)
                    st.pyplot(fig_mpl)

                    code_mpl = """cols = {cols}
fig, axes = plt.subplots(1, len(cols), figsize=(4 * len(cols), 4), squeeze=False)
for idx, name in enumerate(cols):
    ax = axes[0, idx]
    data = df[name].dropna().values
    ax.hist(data, bins=30, density=True, alpha=0.8)
    ax.set_title(name)
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()""".format(
                        cols=nums_over
                    )

            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("### Code preview")
        if code_mpl:
            show_code_example(code_mpl, "Matplotlib commands that reproduce the current plot.")

        if fig_mpl is not None:
            if st.button("Save last Matplotlib plot to gallery", key="mpl_save_gallery"):
                save_to_gallery(fig_mpl, f"Matplotlib: {mpl_type}", "Matplotlib builder plot")
                st.success("Saved to gallery.")

# ==================== TAB: COMPARE ====================
with tab_compare:
    st.markdown("## Compare Seaborn and Matplotlib")
    st.markdown(
        '<div class="info-box"><strong>Goal:</strong> See the same idea expressed once with Seaborn and once with Matplotlib.</div>',
        unsafe_allow_html=True,
    )

    if df.empty or not numeric_cols_all:
        st.warning("Need at least one numeric column in the dataset.")
    else:
        compare_kind = st.selectbox(
            "Comparison pattern",
            [
                "Distribution (histogram + KDE)",
                "Relationship (scatter)",
            ],
            key="cmp_kind",
        )

        if compare_kind == "Distribution (histogram + KDE)":
            num_cmp = st.selectbox(
                "Numeric column",
                numeric_cols_all,
                key="cmp_dist_num",
            )
            hue_cmp = None
            if categorical_cols_all:
                use_hue_cmp = st.checkbox(
                    "Color by category (Seaborn only)",
                    value=False,
                    key="cmp_dist_use_hue",
                )
                if use_hue_cmp:
                    hue_cmp = st.selectbox(
                        "Hue",
                        categorical_cols_all,
                        key="cmp_dist_hue",
                    )

            col_s, col_m = st.columns(2)

            with col_s:
                st.markdown("### Seaborn view")
                fig_s, ax_s = plt.subplots(figsize=(7, 4))
                sns.histplot(
                    data=df,
                    x=num_cmp,
                    hue=hue_cmp,
                    kde=True,
                    bins=30,
                    ax=ax_s,
                )
                ax_s.set_title("Seaborn: histogram + KDE", fontsize=12, fontweight="bold")
                apply_dark(fig_s, DARK)
                st.pyplot(fig_s)

            with col_m:
                st.markdown("### Matplotlib view")
                fig_m, ax_m = plt.subplots(figsize=(7, 4))
                values = df[num_cmp].dropna().values
                ax_m.hist(values, bins=30, alpha=0.85, density=True)
                x_vals = np.linspace(values.min(), values.max(), 200)
                kde = stats.gaussian_kde(values)
                ax_m.plot(x_vals, kde(x_vals), lw=2)
                ax_m.set_title("Matplotlib: histogram + KDE", fontsize=12, fontweight="bold")
                ax_m.set_xlabel(num_cmp)
                ax_m.set_ylabel("Density")
                ax_m.grid(alpha=0.3)
                apply_dark(fig_m, DARK)
                st.pyplot(fig_m)

            if st.button("Save Seaborn comparison plot to gallery", key="cmp_dist_save"):
                save_to_gallery(fig_s, "Compare: Distribution", "Seaborn vs Matplotlib distribution")
                st.success("Saved Seaborn figure to gallery.")

        else:  # Relationship (scatter)
            if len(numeric_cols_all) < 2:
                st.warning("Need at least two numeric columns.")
            else:
                x_cmp = st.selectbox(
                    "X",
                    numeric_cols_all,
                    key="cmp_rel_x",
                )
                y_cmp = st.selectbox(
                    "Y",
                    [c for c in numeric_cols_all if c != x_cmp],
                    key="cmp_rel_y",
                )
                hue_cmp_rel = None
                if categorical_cols_all:
                    use_hue_cmp_rel = st.checkbox(
                        "Color by category (Seaborn only)",
                        value=False,
                        key="cmp_rel_use_hue",
                    )
                    if use_hue_cmp_rel:
                        hue_cmp_rel = st.selectbox(
                            "Hue",
                            categorical_cols_all,
                            key="cmp_rel_hue",
                        )

                col_s2, col_m2 = st.columns(2)

                with col_s2:
                    st.markdown("### Seaborn view")
                    fig_s2, ax_s2 = plt.subplots(figsize=(7, 4))
                    sns.scatterplot(
                        data=df,
                        x=x_cmp,
                        y=y_cmp,
                        hue=hue_cmp_rel,
                        alpha=0.7,
                        s=70,
                        ax=ax_s2,
                    )
                    ax_s2.set_title("Seaborn: scatterplot", fontsize=12, fontweight="bold")
                    apply_dark(fig_s2, DARK)
                    st.pyplot(fig_s2)

                with col_m2:
                    st.markdown("### Matplotlib view")
                    fig_m2, ax_m2 = plt.subplots(figsize=(7, 4))
                    ax_m2.scatter(df[x_cmp], df[y_cmp], alpha=0.7)
                    ax_m2.set_title("Matplotlib: scatter", fontsize=12, fontweight="bold")
                    ax_m2.set_xlabel(x_cmp)
                    ax_m2.set_ylabel(y_cmp)
                    ax_m2.grid(alpha=0.3)
                    apply_dark(fig_m2, DARK)
                    st.pyplot(fig_m2)

                if st.button("Save Seaborn comparison plot to gallery", key="cmp_rel_save"):
                    save_to_gallery(fig_s2, "Compare: Relationship", "Seaborn vs Matplotlib scatter")
                    st.success("Saved Seaborn figure to gallery.")

# ==================== TAB: GALLERY ====================
with tab_gallery:
    st.markdown("## Gallery")

    if not st.session_state["gallery"]:
        st.info("Gallery is empty. Build a plot in any tab and save it here.")
        st.markdown(
            """
**How this gallery works**

1. Create a visualization in one of the tabs
2. Click the **Save to gallery** button
3. Return here to review the saved visuals
4. Download individual PNG files or a ZIP archive
"""
        )
    else:
        st.success(f"{len(st.session_state['gallery'])} visualizations stored.")

        col_zip, col_clear, _ = st.columns([2, 2, 1])

        with col_zip:
            if st.button("Prepare ZIP archive", key="gal_zip_btn", use_container_width=True):
                zip_buf = io.BytesIO()
                with zipfile.ZipFile(zip_buf, "w", zipfile.ZIP_DEFLATED) as zf:
                    for idx, item in enumerate(st.session_state["gallery"]):
                        filename = f"{idx+1:02d}_{item['name'].replace(' ', '_')}.png"
                        zf.writestr(filename, item["image"])

                st.download_button(
                    "Download ZIP",
                    data=zip_buf.getvalue(),
                    file_name=f"visual_lab_gallery_{datetime.now():%Y%m%d_%H%M%S}.zip",
                    mime="application/zip",
                    use_container_width=True,
                    key="gal_zip_dl",
                )

        with col_clear:
            if st.button("Clear gallery", key="gal_clear_btn", use_container_width=True):
                st.session_state["gallery"] = []
                st.rerun()

        st.markdown("---")

        cols_per_row = 2
        for i in range(0, len(st.session_state["gallery"]), cols_per_row):
            cols = st.columns(cols_per_row)
            for j, c in enumerate(cols):
                item_idx = i + j
                if item_idx < len(st.session_state["gallery"]):
                    item = st.session_state["gallery"][item_idx]
                    with c:
                        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
                        st.image(item["image"], use_container_width=True)
                        st.markdown(f"**{item['name']}**")
                        st.caption(item["description"])
                        st.caption(
                            f"Saved at {item['timestamp'].strftime('%Y-%m-%d %H:%M')}"
                        )
                        st.download_button(
                            "Download PNG",
                            data=item["image"],
                            file_name=f"{item['name'].replace(' ', '_')}.png",
                            mime="image/png",
                            key=f"gal_dl_{item_idx}",
                            use_container_width=True,
                        )
                        st.markdown("</div>", unsafe_allow_html=True)

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("### Quick reference")

col_f1, col_f2, col_f3 = st.columns(3)
with col_f1:
    st.markdown(
        """
**Distribution**
- Histogram / KDE / ECDF
- Box / Violin
"""
    )
with col_f2:
    st.markdown(
        """
**Relationships & groups**
- Scatter / Regression / Line
- Category summaries
"""
    )
with col_f3:
    st.markdown(
        """
**Matrix & multi-view**
- Correlation heatmaps
- Pairplot grids
"""
    )
