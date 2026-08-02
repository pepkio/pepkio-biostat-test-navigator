# Pepkio Biostat Test Navigator

Execute automated statistical test selection, distribution assumption diagnostics, post-hoc pairwise comparisons, and effect size calculations for biological research data via Python or REST API.

# What It Does

Selecting the appropriate statistical test for biological and biomedical data is critical to avoid false positives (Type I errors) or lost statistical power (Type II errors). Datasets from real-time PCR, Western blots, cell viability assays, and flow cytometry often have small sample sizes ($n < 5$), non-normal distributions, or unequal group variances that violate standard parametric assumptions.

The `pepkio-biostat-test-navigator` package connects your Python workflows directly to the Pepkio Biostat Test Navigator calculation engine. It evaluates experimental design metadata—such as group counts, continuous vs. categorical outcomes, and paired observations—and runs distribution diagnostics (Shapiro-Wilk normality and Levene's homoscedasticity) to select and execute the most appropriate parametric or non-parametric statistical test.

# Features

- **Automated Test Recommendation**: Recommends optimal parametric or non-parametric tests based on sample size, experimental design, and distribution assumption testing.
- **Assumption Diagnostics**: Performs automated Shapiro-Wilk normality tests and Levene's homoscedasticity tests on input group data.
- **Comprehensive Test Suite**: Supports Student's t-test, Welch's t-test, Paired t-test, Mann-Whitney U test, Wilcoxon signed-rank test, One-Way ANOVA, Welch ANOVA, Kruskal-Wallis, Two-Way ANOVA, Repeated Measures ANOVA, Friedman test, Chi-Square, and Fisher's Exact test.
- **Post-Hoc Pairwise Testing**: Executes appropriate post-hoc tests (Tukey's HSD, Games-Howell, Dunn's test) with Bonferroni or Benjamini-Hochberg False Discovery Rate (FDR) adjustments.
- **Effect Size & Confidence Intervals**: Calculates standardized effect sizes (Cohen's $d$, Hedges' $g$, Eta-squared $\eta^2$, Rank-Biserial correlation, Odds Ratio) with 95% confidence intervals.
- **Power & Sample Size Analysis**: Provides post-hoc statistical power analysis and prospective sample size estimation.
- **CLI & Python API**: Provides both a programmatic Python client and a command-line interface for batch processing and workflow automation.

# Installation

Install the package via `pip`:

```bash
pip install pepkio-biostat-test-navigator
```

Set your Pepkio API key as an environment variable before running calculations:

```bash
export PEPKIO_API_KEY="your-api-key"
```

# Quick Example

```python
from pepkio_biostat_test_navigator import PepkioClient

with PepkioClient() as client:
    qpcr_input = {
        "template_id": "qpcr",
        "outcome_type": "continuous",
        "comparison_type": "two_groups",
        "group_count": 2,
        "paired": False,
        "groups": [
            {"name": "Control", "values": [1.02, 0.98, 1.05, 1.01]},
            {"name": "Treatment", "values": [2.45, 2.51, 2.38, 2.62]},
        ],
    }

    result = client.run(qpcr_input)
    print("Recommended Test:", result.result["primary_test"])
    print("Rationale:", result.result["rationale"])
    print("Permalink:", result.permalink)
```

Command-line interface usage:

```bash
pepkio-biostat-test-navigator manifest
pepkio-biostat-test-navigator run --example qpcr_two_group_mann_whitney
```

# Typical Use Cases

- **qPCR Relative Gene Expression ($\Delta\Delta Ct$)**: Choosing between Student's t-test, Welch's t-test, and Mann-Whitney U test when comparing fold-change values across small replicate cohorts.
- **Western Blot Densitometry**: Selecting between One-Way ANOVA with Tukey HSD and Kruskal-Wallis with Dunn's post-hoc test for normalized protein optical densities.
- **Cell Viability Assays**: Evaluating main treatment effects and compound-concentration interactions across dose response levels using Two-Way ANOVA.
- **Preclinical Animal Studies**: Analyzing longitudinal biomarkers or tumor volumes in paired animal groups using Repeated Measures ANOVA or the Friedman test.
- **Flow Cytometry & Histopathology Gating**: Assessing responder frequencies or categorical marker staining intensities using Fisher's Exact test or Chi-Square tests of independence.

# Scientific Background

Parametric statistical tests assume normally distributed data and equal group variances, while non-parametric tests operate on rank orders without distributional assumptions. When sample sizes are small ($n < 5$), formal normality tests have low statistical power, making decision rules based on sample size thresholds, Shapiro-Wilk test statistics ($W$), and Levene's variance ratio test ($F$) critical for preventing inflated Type I error rates. Post-hoc multi-group comparisons apply family-wise error rate corrections (Bonferroni) or False Discovery Rate control (Benjamini-Hochberg) to ensure statistical validity across multiple testing steps.

# Web Application

For researchers who prefer a graphical interface, an interactive web version is available.

Web Application: https://www.pepkio.com/tools/biostat-test-navigator

The web interface offers visual decision flowcharts, interactive data entry tables, graphical distribution plots, one-click PDF/CSV export, and shareable permalinks for manuscript peer review.

# Documentation and Resources

GitHub Repository: https://github.com/pepkio/pepkio-biostat-test-navigator

Web Application: https://www.pepkio.com/tools/biostat-test-navigator

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and analysis services (https://www.pepkio.com/cro).

# Keywords

biostatistics test navigator, statistical test selector, biological hypothesis testing, qPCR statistical analysis, parametric vs non-parametric test chooser, Student's t-test vs Mann-Whitney U, One-Way ANOVA decision tree, Shapiro-Wilk normality diagnostic, Levene's test homoscedasticity, Welch's t-test calculator, Kruskal-Wallis post-hoc Dunn test, Tukey HSD pairwise comparison, Benjamini-Hochberg FDR correction, Bonferroni adjusted p-value, Cohen's d effect size calculator, Hedges' g small sample correction, statistical power calculator biology, Fisher's exact test contingency table, Wilcoxon signed-rank test paired data, Two-Way ANOVA interaction effect, Repeated Measures ANOVA, Friedman test non-parametric, biological replicate statistics, pepkio-biostat-test-navigator, Python biostatistics package, automated hypothesis testing API, REST API statistical decision engine, how to choose statistical test for qPCR, post-hoc pairwise testing with FDR correction, automate biostatistical assumption checking Python, determine parametric or non-parametric test for small sample size, calculate Cohen's d and Hedges' g effect size with confidence intervals, perform Shapiro-Wilk and Levene's test automatically in Python, select between Student's t-test and Welch's t-test for unequal variances, evaluate Western blot densitometry with ANOVA and Tukey HSD, run Fisher's exact test on small sample contingency tables programmatically, batch statistical test navigation via Python client and CLI
