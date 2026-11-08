# Pepkio Biostat Test Navigator

Run the Pepkio biostat-test-navigator CLI in Docker to automate statistical test selection, distribution assumption diagnostics, post-hoc pairwise comparisons, and effect size calculations without a local Python setup.

# What It Does

The image runs `pepkio-biostat-test-navigator`, a command-line client for the Pepkio Biostat Test Navigator REST API. It evaluates experimental design metadata (sample size, continuous vs. categorical outcomes, group counts, paired observations, and factor levels) and performs automated distribution diagnostics (Shapiro-Wilk normality and Levene's homoscedasticity) to select and execute the most appropriate parametric or non-parametric statistical test. Calculations, multiple testing corrections (FDR and Bonferroni), and effect size estimations run remotely on Pepkio servers; provide a network connection and API key for `run` commands.

# Features

- Automated statistical test recommendation based on experimental design and distribution testing
- Automated assumption checks: Shapiro-Wilk normality and Levene's homoscedasticity
- Comprehensive test coverage: Student's t-test, Welch's t-test, Paired t-test, Mann-Whitney U, Wilcoxon signed-rank, One-Way ANOVA, Kruskal-Wallis, Two-Way ANOVA, Repeated Measures ANOVA, Friedman, Chi-Square, and Fisher's Exact test
- Post-hoc pairwise comparisons: Tukey's HSD, Games-Howell, and Dunn's test with FDR/Bonferroni corrections
- Effect sizes and 95% confidence intervals (Cohen's d, Hedges' g, Eta-squared, Rank-Biserial correlation)
- Manifest inspection and example listing without an API key

# Quick Start

```bash
docker pull pepkio/biostat-test-navigator:0.1.0
docker run --rm -e PEPKIO_API_KEY="your-key" pepkio/biostat-test-navigator:0.1.0 \
  run --example qpcr_two_group_mann_whitney
```

Manifest only (no API key):

```bash
docker run --rm pepkio/biostat-test-navigator:0.1.0 \
  manifest --examples
```

Set `PEPKIO_API_BASE_URL` to override the API host (default: `https://tools.pepkio.com`). Create an API key with **tools:run** scope at https://www.pepkio.com/account/api-keys.

# Quick Example

```bash
docker run --rm -e PEPKIO_API_KEY="$PEPKIO_API_KEY" pepkio/biostat-test-navigator:0.1.0 \
  run --input-json \
  '{"template_id":"qpcr","outcome_type":"continuous","comparison_type":"two_groups","group_count":2,"paired":false,"groups":[{"name":"Control","values":[1.02,0.98,1.05,1.01]},{"name":"Treatment","values":[2.45,2.51,2.38,2.62]}]}'
```

# Typical Use Cases

- qPCR relative gene expression analysis ($\Delta\Delta Ct$): selecting between Student's t-test, Welch's t-test, and Mann-Whitney U for small replicate cohorts
- Western blot densitometry: choosing between One-Way ANOVA with Tukey HSD and Kruskal-Wallis with Dunn post-hoc test
- Cell viability and drug response screens: evaluating main effects and drug interactions across concentration levels using Two-Way ANOVA
- Preclinical animal models: analyzing longitudinal biomarker measurements with Repeated Measures ANOVA or the Friedman test
- Categorical histology scoring or responder gating: evaluating contingency tables with Fisher's Exact or Chi-Square tests
- Automated containerized pipelines: embedding reproducible statistical test selection into Nextflow, Snakemake, or Docker pipelines

# Scientific Background

In biomedical and life science research, defaulting to parametric tests (such as Student's t-test or ANOVA) without verifying assumptions can lead to inflated Type I errors (false positives) or diminished statistical power (Type II errors). Many laboratory assays feature small sample sizes ($n < 5$), skewed distributions, or heteroscedastic variances. Automated evaluation of sample size limits, Shapiro-Wilk normality statistics ($W$), and Levene's variance ratio test ($F$) ensures objective selection between parametric and non-parametric methodologies, while post-hoc multiple testing adjustments maintain family-wise error or false discovery rates.

# Web Application

For researchers who prefer a graphical interface, an interactive web version is available.

Web Application: https://www.pepkio.com/tools/biostat-test-navigator

The web interface features visual decision trees, distribution density plots, interactive data entry tables, exportable reports, and shareable permalinks.

# Documentation and Resources

GitHub Repository (source and Dockerfile): https://github.com/pepkio/pepkio-biostat-test-navigator

PyPI Package: https://pypi.org/project/pepkio-biostat-test-navigator/

Web Application: https://www.pepkio.com/tools/biostat-test-navigator

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and analysis services (https://www.pepkio.com/cro).

A semantic, AI-native version of this document in the K2F format is available at https://k2f.dev (https://k2f.dev/v/efed39d108253b81e82ce229825aac712a2196058d011799988936063de377df)
