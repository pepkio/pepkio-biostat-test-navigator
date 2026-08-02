# Pepkio Biostat Test Navigator

Automate statistical test selection, assumption checking, power calculations, and hypothesis testing for life science research data using Python and web interfaces.

# Overview

Selecting the correct statistical test is one of the most critical and error-prone steps in biological, biomedical, and bioinformatic research. Life science experiments—ranging from quantitative real-time PCR (qPCR) relative gene expression assays and Western blot densitometry to flow cytometry marker intensity comparisons, cell viability screens, animal cohort survival studies, and high-throughput RNA sequencing—produce diverse data structures. Researchers must choose between parametric tests (such as Student's t-test, Welch's t-test, one-way ANOVA, two-way ANOVA, and repeated measures ANOVA) and non-parametric tests (such as the Mann-Whitney U test, Wilcoxon signed-rank test, Kruskal-Wallis test, and Friedman test) based on sample sizes, data normality, variance homogeneity, paired design structures, and categorical frequency tables.

Selecting an inappropriate statistical test can yield invalid $p$-values, inflated false positive rates (Type I errors), or loss of statistical power (Type II errors). Standard software packages often require manual specification of test types without evaluating distribution assumptions or accounting for small biological sample sizes ($n < 5$). Manual selection and calculation in spreadsheets can lead to unvetted assumptions, missing post-hoc adjustments (e.g., Tukey HSD, Dunn's test, or Benjamini-Hochberg FDR correction), and unstandardized statistical reporting.

The **Pepkio Biostat Test Navigator** solves these challenges by providing an automated, rule-based decision engine and calculation framework for biostatistical hypothesis testing. It evaluates dataset characteristics—including sample size per group, distributional normality via Shapiro-Wilk testing, homoscedasticity via Levene's test, experimental pairing, factor levels, and outcome variable types—to select, execute, and report the most statistically appropriate test.

Researchers can run automated statistical test selection and hypothesis evaluation directly in their web browser via the [Pepkio Biostat Test Navigator](https://www.pepkio.com/tools/biostat-test-navigator) web application. A programmatic Python client and command-line interface (CLI) are also available for batch evaluation, workflow integration, and reproducible data pipelines.

Common search terms and alternative terminology for this tool include biostatistics test navigator, statistical test selector for biology, biostatistical decision tree, qPCR statistical analysis tool, parametric vs non-parametric test chooser, biological hypothesis test calculator, Mann-Whitney vs t-test guide, ANOVA decision tree for wet lab research, and False Discovery Rate (FDR) correction calculator.

# Features

- **Automated Statistical Test Selection**: Evaluates experimental design metadata (sample size, continuous vs categorical outcome, group count, paired vs unpaired observations, factor counts) and underlying data distributions to automatically recommend the optimal statistical test.
- **Assumption Diagnostics**: Performs automated Shapiro-Wilk normality testing and Levene's or Bartlett's homoscedasticity testing to verify whether parametric test assumptions are met before analysis.
- **Comprehensive Parametric & Non-Parametric Library**: Supports Student's t-test, Welch's t-test, Paired t-test, Mann-Whitney U test, Wilcoxon signed-rank test, One-Way ANOVA, Welch ANOVA, Kruskal-Wallis test, Two-Way ANOVA, Repeated Measures ANOVA, Friedman test, Chi-Square test, and Fisher's Exact test.
- **Post-Hoc Pairwise Comparisons**: Automatically performs appropriate post-hoc tests for multi-group comparisons, including Tukey's HSD for equal-variance ANOVA, Games-Howell for unequal variance, and Dunn's test with Bonferroni or Benjamini-Hochberg FDR adjustments for non-parametric data.
- **Multiple Testing Correction**: Integrates False Discovery Rate (FDR) control methods (Benjamini-Hochberg, Benjamini-Yekutieli) and Family-Wise Error Rate (FWER) controls (Bonferroni, Holm-Bonferroni) for high-throughput screening and multi-target assays.
- **Effect Size Calculation**: Computes standardized effect sizes—including Cohen's $d$, Hedges' $g$ (for small sample correction), Eta-squared ($\eta^2$), Partial Eta-squared ($\eta_p^2$), Rank-Biserial correlation, and Odds Ratios—alongside $95\%$ confidence intervals.
- **Power & Sample Size Estimation**: Provides post-hoc statistical power calculations and prospective sample size determinations based on user-defined significance thresholds ($\alpha$), target power ($1-\beta$), and expected effect size.
- **Python API & CLI**: Programmatic Python package and command-line client supporting JSON input/output, manifest auto-discovery, batch dataset processing, and programmatic pipeline integration.
- **Reproducible Permalinks**: Generates unique permanent URLs for sharing test selections, assumptions diagnostics, raw data, and statistical outputs with collaborators or in manuscript peer review.

# Common Use Cases

- **qPCR Relative Fold Change ($\Delta\Delta Ct$) Analysis**: Determine whether to use an unpaired Student's t-test, Welch's t-test, or Mann-Whitney U test when comparing $2^{-\Delta\Delta Ct}$ gene expression fold-changes between control and gene knockout cell lines across small sample replicates ($n = 3 \text{ to } 6$).
- **Western Blot Protein Densitometry**: Evaluate normalized optical density measurements across multiple experimental treatment conditions to decide between One-Way ANOVA with Tukey post-hoc test or Kruskal-Wallis with Dunn post-hoc test when sample normality cannot be assumed.
- **Pre-clinical Animal Drug Efficacy Screens**: Compare tumor volume trajectories or physiological biomarkers over time in paired animal cohorts using Repeated Measures ANOVA or the non-parametric Friedman test.
- **Cell Viability & Cytotoxicity Assays**: Assess dose-response cell viability percentages across multiple compound concentrations and control vehicles using Two-Way ANOVA to inspect main effects and compound-dose interaction terms.
- **Categorical Histopathology & Flow Cytometry Gating**: Analyze responder vs non-responder cell populations or tissue staining severity categories across treatment arms using Chi-Square tests of independence or Fisher's Exact test for small sample contingency tables.
- **High-Throughput Biomarker Screening**: Apply multiple testing corrections (Benjamini-Hochberg FDR) across dozens of protein analyte ELISA panels or multiplex cytokine arrays to control false discovery rates without over-conservative Bonferroni penalties.

# Why This Tool Exists

In biological and biomedical research, statistical test selection is frequently dictated by legacy laboratory habits rather than objective diagnostic evaluation of data properties. Researchers commonly default to standard two-sample Student's t-tests or One-Way ANOVA regardless of whether their sample sizes violate normality assumptions or whether variances are severely unequal across treatment groups.

Spreadsheet applications (such as Microsoft Excel or Google Sheets) compound this issue by offering built-in functions for basic t-tests and ANOVA while omitting built-in normality tests (like Shapiro-Wilk), variance homogeneity diagnostics (like Levene's test), and non-parametric rank-based alternatives (like Mann-Whitney U or Kruskal-Wallis). Moreover, spreadsheets do not provide post-hoc pairwise comparison algorithms with appropriate family-wise error or FDR corrections, leading researchers to perform unadjusted multiple pairwise t-tests that artificially inflate Type I error rates.

General-purpose statistical software platforms (such as R, Prism, or SAS) provide comprehensive statistical routines but require researchers to manually check assumptions, navigate complex parameter menus, and select the correct test independently. For wet-lab scientists without advanced biostatistical training, interpreting diagnostic outputs to choose between competing tests remains a significant bottleneck.

The **Pepkio Biostat Test Navigator** fills this gap by implementing an automated biological decision engine. By evaluating dataset dimensionality, outcome types, sample size constraints, normality test statistics, and variance ratios in a single unified execution, it eliminates subjective decision biases and automates rigorous hypothesis testing. Researchers can access these decision algorithms online via the [biostat test navigator web tool](https://www.pepkio.com/tools/biostat-test-navigator) or programmatically via the Python API package.

# Installation

Install the Python client package from PyPI using `pip`:

```bash
pip install pepkio-biostat-test-navigator
```

Or using `uv`:

```bash
uv add pepkio-biostat-test-navigator
```

Package distribution details and version releases are indexed on [PyPI](https://pypi.org/project/pepkio-biostat-test-navigator/).

# Quick Start

### Python API Usage

Set your API key as an environment variable:

```bash
export PEPKIO_API_KEY="your_pepkio_api_key"
```

Run automated statistical test navigation and hypothesis evaluation in Python:

```python
from pepkio_biostat_test_navigator import PepkioClient

# Initialize client
with PepkioClient() as client:
    # 1. Unpaired two-group qPCR data comparison with automated test selection
    qpcr_input = {
        "template_id": "qpcr",
        "outcome_type": "continuous",
        "comparison_type": "two_groups",
        "group_count": 2,
        "paired": False,
        "groups": [
            {"name": "Control", "values": [1.02, 0.98, 1.05, 1.01]},
            {"name": "Treatment", "values": [2.45, 2.51, 2.38, 2.62]}
        ]
    }
    qpcr_result = client.run(qpcr_input)
    print("Primary Test Selected:", qpcr_result.result["primary_test"])
    print("Rationale:", qpcr_result.result["rationale"])
    print("Permalink:", qpcr_result.permalink)

    # 2. Small sample contingency table analysis (Fisher's Exact Test)
    fisher_input = {
        "outcome_type": "categorical",
        "comparison_type": "two_groups",
        "categorical_table": [[8, 2], [3, 12]]
    }
    fisher_result = client.run(fisher_input)
    print("Fisher Test Selected:", fisher_result.result["primary_test"])
```

### Command Line Interface (CLI)

The package includes a built-in CLI executable `pepkio-biostat-test-navigator`:

```bash
# List example manifest templates
pepkio-biostat-test-navigator manifest --examples

# Run a pre-configured example by name
pepkio-biostat-test-navigator run --example qpcr_two_group_mann_whitney

# Run custom inline JSON input
pepkio-biostat-test-navigator run --input-json '{
  "template_id": "qpcr",
  "outcome_type": "continuous",
  "comparison_type": "two_groups",
  "group_count": 2,
  "paired": false,
  "groups": [
    {"name": "WildType", "values": [12.1, 11.8, 12.5, 12.0]},
    {"name": "Knockout", "values": [4.2, 4.5, 3.9, 4.1]}
  ]
}'
```

# Example Output

Executing the biostat test navigator tool yields a structured JSON response containing the selected primary test, assumption diagnostic results, detailed rationale, test statistics, $p$-values, effect sizes, and permalink:

```json
{
  "run_id": "run_biostat_98765",
  "status": "completed",
  "result": {
    "ready": true,
    "preliminary": false,
    "primary_test": "Mann-Whitney U test",
    "primary_test_key": "mann_whitney",
    "rationale": "Group sample sizes are small (n = 4 per group), making Shapiro-Wilk normality testing low in power. Non-parametric rank summation (Mann-Whitney U) is recommended to prevent invalid Gaussian assumptions.",
    "diagnostics": {
      "normality_test": "Shapiro-Wilk",
      "control_normality_p": 0.432,
      "treatment_normality_p": 0.189,
      "homoscedasticity_test": "Levene",
      "homoscedasticity_p": 0.654,
      "equal_variance_assumed": true
    },
    "statistics": {
      "test_statistic": 0.0,
      "p_value": 0.0286,
      "significance_alpha_0_05": true,
      "effect_size": {
        "metric": "Rank-Biserial Correlation",
        "value": 1.0,
        "ci_95": [0.38, 1.0]
      }
    },
    "post_hoc": null
  },
  "error": null,
  "result_url": "https://tools.pepkio.com/api/tools/v1/runs/run_biostat_98765",
  "permalink": "https://tools.pepkio.com/r/run_biostat_98765"
}
```

# Scientific Background

### Parametric vs. Non-Parametric Statistical Inference

Hypothesis testing evaluates whether observed differences between biological groups reflect true underlying biological effects or random sampling variation. Statistical tests fall into two major paradigms:

1. **Parametric Tests**: Assume that the data follow a specified parametric probability distribution (typically a normal or Gaussian distribution $N(\mu, \sigma^2)$). Key parametric tests include:
   - **Student's $t$-test**: Compares means between two independent groups assuming equal variances. The test statistic is calculated as:
     $$t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}$$
     where $s_p = \sqrt{\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}}$ is the pooled sample standard deviation.
   - **Welch's $t$-test**: Compares means between two independent groups without assuming equal variances ($\sigma_1^2 \neq \sigma_2^2$). The statistic uses unequal variance estimates:
     $$t_{Welch} = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$
     with degrees of freedom adjusted via the Welch-Satterthwaite equation.
   - **One-Way Analysis of Variance (ANOVA)**: Tests for differences across $k \ge 3$ independent group means by partitioning total variance into between-group variance ($MS_{between}$) and within-group residual variance ($MS_{within}$):
     $$F = \frac{MS_{between}}{MS_{within}}$$

2. **Non-Parametric Tests**: Do not assume a underlying Gaussian distribution. They convert raw measurement values into ordinal ranks, making them robust against outliers, skewed distributions, and ordinal scale data:
   - **Mann-Whitney U Test (Wilcoxon Rank-Sum Test)**: Evaluates whether the distributions of two independent groups differ. The test ranks all combined observations $R_i$ and calculates $U$:
     $$U_1 = n_1 n_2 + \frac{n_1(n_1 + 1)}{2} - R_1$$
   - **Wilcoxon Signed-Rank Test**: Non-parametric counterpart to the paired $t$-test for dependent paired measurements (e.g., pre-treatment vs post-treatment in the same cell culture batch).
   - **Kruskal-Wallis Test**: Non-parametric alternative to One-Way ANOVA for comparing $k \ge 3$ independent groups using rank sums.
   - **Friedman Test**: Non-parametric alternative to Repeated Measures ANOVA for complete block designs.

### Assumption Diagnostics: Normality and Homoscedasticity

Valid application of parametric statistics requires verifying underlying mathematical assumptions:

- **Normality Testing (Shapiro-Wilk Test)**: Tests the null hypothesis ($H_0$) that data are drawn from a normally distributed population. The Shapiro-Wilk statistic $W$ measures the correlation between ordered sample values and normal quantiles:
  $$W = \frac{\left( \sum_{i=1}^n a_i x_{(i)} \right)^2}{\sum_{i=1}^n (x_i - \bar{x})^2}$$
  A significant result ($p < 0.05$) indicates deviation from normality, necessitating a non-parametric test or data transformation (e.g., $\log_{10}$ transformation).
- **Homoscedasticity Testing (Levene's & Bartlett's Tests)**: Verifies equal group variances ($\sigma_1^2 = \sigma_2^2 = \dots = \sigma_k^2$). Levene's test evaluates absolute deviations from group medians, making it robust against non-normality. If $p < 0.05$, equal variance is rejected, indicating the use of Welch's $t$-test or Welch ANOVA instead of standard Student's $t$-test or classic ANOVA.

### Multiple Testing Correction and False Discovery Rate (FDR)

When conducting $m$ simultaneous hypothesis tests (such as screening multiple genes or cytokines), the overall probability of at least one false positive (Family-Wise Error Rate, FWER) accumulates exponentially: FWER $= 1 - (1 - \alpha)^m$.

To prevent false discovery inflation:
- **Bonferroni Adjustment**: Adjusts the significance threshold $\alpha_{adj} = \alpha / m$. While controlling FWER, Bonferroni is highly conservative and increases Type II errors in high-throughput screening.
- **Benjamini-Hochberg (BH) FDR Procedure**: Controls the expected proportion of false discoveries among rejected null hypotheses. Raw $p$-values are sorted in ascending order $p_{(1)} \le p_{(2)} \le \dots \le p_{(m)}$, and the maximum rank $k$ is identified satisfying:
  $$p_{(k)} \le \frac{k}{m} Q$$
  where $Q$ is the chosen false discovery rate threshold (e.g., $Q = 0.05$).

### Effect Size Estimation

Reporting $p$-values alone is insufficient for scientific interpretation because $p$-values depend on both effect magnitude and sample size. Standardized effect sizes quantify the magnitude of biological effects:
- **Cohen's $d$**: Difference between two means divided by pooled standard deviation: $d = \frac{\bar{x}_1 - \bar{x}_2}{s_p}$.
- **Hedges' $g$**: Applies a small-sample bias correction factor $J(df) \approx 1 - \frac{3}{4(n_1+n_2)-9}$ to Cohen's $d$: $g = d \times J(df)$.
- **Eta-Squared ($\eta^2$)**: Proportion of total variance explained by a factor in ANOVA: $\eta^2 = \frac{SS_{effect}}{SS_{total}}$.

# Frequently Asked Questions

### 1. How do I choose between a parametric and a non-parametric statistical test?
Choose a parametric test (such as Student's t-test or One-Way ANOVA) when your continuous data follow a normal (Gaussian) distribution, group variances are relatively homogenous, and your sample size per group is sufficiently large ($n \ge 30$). Choose a non-parametric test (such as Mann-Whitney U or Kruskal-Wallis) when sample sizes are small ($n < 10$), data are severely skewed, outliers are present, or outcome variables are ordinal ratings.

### 2. What statistical test should I use for qPCR relative gene expression ($\Delta\Delta Ct$) data?
For qPCR $2^{-\Delta\Delta Ct}$ fold-change data comparing two independent experimental groups, first test for normality using the Shapiro-Wilk test on $\Delta Ct$ or $\log_2(\text{fold change})$ values. If data are normally distributed with equal variances, use an unpaired Student's t-test. If variances are unequal, use Welch's t-test. If sample size is small ($n = 3 \text{ to } 5$) or non-normal, use the non-parametric Mann-Whitney U test.

### 3. When should I use Welch's t-test instead of Student's t-test?
Use Welch's t-test whenever sample variances between two groups are unequal ($\sigma_1^2 \neq \sigma_2^2$), or when sample sizes between the two groups are unequal ($n_1 \neq n_2$). Welch's t-test maintains accurate Type I error rates without losing statistical power, making it a safer default choice than standard Student's t-test for most wet-lab biological experiments.

### 4. How do I test for normal distribution in small biological sample sizes ($n < 10$)?
Use the Shapiro-Wilk test for sample sizes between $n = 3$ and $n = 50$. However, note that statistical tests for normality have low statistical power when $n < 10$, meaning they may fail to reject normality even in non-normal datasets. In very small biological replicates ($n = 3 \text{ or } 4$), non-parametric tests or log-transformations are often recommended unless prior historical data establishes Gaussian distribution.

### 5. What is the difference between the Mann-Whitney U test and the Wilcoxon signed-rank test?
The Mann-Whitney U test (also called the Wilcoxon rank-sum test) compares two **independent (unpaired)** experimental groups (e.g., wild-type vs knockout mice). The Wilcoxon signed-rank test compares two **dependent (paired)** samples measured on the same experimental units (e.g., cell cultures measured before and after drug treatment).

### 6. When should I use One-Way ANOVA versus Two-Way ANOVA?
Use One-Way ANOVA when comparing continuous outcome measurements across three or more levels of a **single independent variable** (e.g., comparing protein expression across Control, Vehicle, and Treatment groups). Use Two-Way ANOVA when examining the effect of **two independent variables** simultaneously (e.g., Genotype [WildType vs Knockout] and Drug Treatment [Dose 0, Dose 10, Dose 50]) to evaluate main effects and interaction terms.

### 7. What is the difference between One-Way ANOVA and Kruskal-Wallis test?
One-Way ANOVA is a parametric test that compares the means of three or more independent groups, assuming normal distributions and equal variances. The Kruskal-Wallis test is the non-parametric equivalent that compares group medians by evaluating the distribution of ranks across three or more independent groups without requiring normality.

### 8. What is False Discovery Rate (FDR) and why is Benjamini-Hochberg correction used?
False Discovery Rate (FDR) is the expected proportion of false positive results (Type I errors) among all tests declared statistically significant. When running dozens or thousands of statistical tests simultaneously (e.g., RNA-seq differential expression or multi-analyte cytokine screens), applying Benjamini-Hochberg (BH) FDR correction controls false positives while preserving significantly higher statistical power compared to conservative Bonferroni correction.

### 9. What is the difference between paired and unpaired t-tests in laboratory experiments?
An unpaired (independent) t-test compares two separate, randomized experimental groups (e.g., biological samples from distinct animals). A paired t-test compares matched or related pairs of observations, such as technical replicates from the same microtiter plate row, or cells from the same patient split into vehicle control and drug-treated channels.

### 10. How do I calculate effect size like Cohen's d or Hedges' g for small sample sizes?
Cohen's $d$ measures the standardized difference between two means: $d = (\bar{x}_1 - \bar{x}_2) / s_p$. For small sample sizes ($n < 20$), Cohen's $d$ systematically overestimates the population effect size. Hedges' $g$ applies a bias correction factor $J(df) \approx 1 - 3/(4(n_1+n_2)-9)$ to adjust Cohen's $d$, providing an unbiased effect size estimate for small biological replicates.

### 11. When should I use Fisher's Exact test instead of a Chi-Square test?
Use Fisher's Exact test when analyzing categorical contingency tables ($2 \times 2$) where sample sizes are small and any expected cell count is less than 5. Use the Chi-Square ($\chi^2$) test of independence when analyzing larger sample sizes where all expected cell counts in the contingency table exceed 5.

### 12. What is a post-hoc test in ANOVA and why is Tukey's HSD used?
An ANOVA test evaluates whether at least one group mean differs from the others ($H_0: \mu_1 = \mu_2 = \dots = \mu_k$), but it does not specify which specific groups differ. A post-hoc test performs pairwise group comparisons after a significant ANOVA result. Tukey's Honestly Significant Difference (HSD) test compares all possible pair combinations while controlling the overall Family-Wise Error Rate (FWER) at $\alpha = 0.05$.

### 13. How does the Biostat Test Navigator handle repeated measures data over time?
When continuous biological parameters are measured across multiple time points within the same experimental subjects (e.g., mouse body weight tracked over 14 days), the tool selects Repeated Measures ANOVA for normal distributions or the non-parametric Friedman test when normality assumptions are violated.

### 14. What is Levene's test for equality of variances?
Levene's test assesses whether $k$ independent groups have equal variances (homoscedasticity). Unlike Bartlett's test, which is sensitive to deviations from normality, Levene's test evaluates absolute deviations from group medians, making it robust for assessing variance homogeneity in biological datasets prior to running parametric ANOVA or t-tests.

### 15. Can I use a t-test if my sample size per group is only n = 3?
Yes, a Student's or Welch's t-test can theoretically be calculated for $n = 3$, provided the underlying population is normally distributed. However, testing for normality with $n = 3$ is mathematically underpowered. If normality cannot be verified, researchers should report non-parametric Mann-Whitney U test statistics, log-transform the raw data, or report exact individual data points alongside median and interquartile ranges.

### 16. How does the tool determine sample size requirements for power analysis?
The tool uses post-hoc and prospective power analysis algorithms based on non-central $t$, $F$, or $\chi^2$ distributions. Given a target significance level ($\alpha = 0.05$), desired statistical power ($1 - \beta = 0.80$), and anticipated effect size (e.g., Cohen's $d = 0.8$), it calculates the minimum sample size ($n$) required per group to detect biological differences reliably.

# Web Application

The hosted version of the tool is available at the [Pepkio Biostat Test Navigator](https://www.pepkio.com/tools/biostat-test-navigator) web application.

The web version provides an interactive interface, shareable links, protocol generation, printable worksheets, and visualization tools. It allows researchers to upload dataset files (CSV, TSV, or Excel format), run interactive decision wizards, visualize normality Q-Q plots and boxplots, export formatted statistical reporting tables, and generate permanent permalinks for manuscript submission without requiring local installation or command-line experience.

# Related Resources

- **GitHub Repository**: [https://github.com/pepkio/pepkio-biostat-test-navigator](https://github.com/pepkio/pepkio-biostat-test-navigator)
- **PyPI Package**: [https://pypi.org/project/pepkio-biostat-test-navigator/](https://pypi.org/project/pepkio-biostat-test-navigator/)
- **Web Application**: [https://www.pepkio.com/tools/biostat-test-navigator](https://www.pepkio.com/tools/biostat-test-navigator)

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and analysis services (https://www.pepkio.com/cro).

Pepkio's scientific capabilities include:
- RNA-seq analysis
- Single-cell RNA-seq analysis
- Spatial transcriptomics analysis
- Functional enrichment analysis
- Custom bioinformatics workflows

Website: https://www.pepkio.com/

# Citation

If you use the Pepkio Biostat Test Navigator in your research, software pipelines, or scientific publications, please cite it as follows:

```bibtex
@software{pepkio_biostat_test_navigator,
  author       = {{Pepkio Team}},
  title        = {Pepkio Biostat Test Navigator: Automated Statistical Test Selection and Hypothesis Evaluation for Life Sciences},
  year         = {2026},
  url          = {https://www.pepkio.com/tools/biostat-test-navigator},
  publisher    = {Pepkio}
}
```

Plain text:
Pepkio Team. (2026). Pepkio Biostat Test Navigator: Automated Statistical Test Selection and Hypothesis Evaluation for Life Sciences. Pepkio. Available at: https://www.pepkio.com/tools/biostat-test-navigator

# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Keywords

biostat-test-navigator, biostatistics test navigator, statistical test selector, biological hypothesis testing, qPCR statistical analysis, parametric vs non-parametric tests, t-test vs Mann-Whitney, ANOVA decision tree, Shapiro-Wilk normality test, Levene homoscedasticity test, Welch t-test calculator, Kruskal-Wallis test, Wilcoxon signed-rank test, Friedman test, Fisher exact test, Chi-square test of independence, Tukey HSD post-hoc test, Dunn test with FDR, Benjamini-Hochberg correction, False Discovery Rate calculator, Cohen d effect size, Hedges g small sample correction, Eta-squared calculator, biological sample size power analysis, two-group comparison biology, multi-group ANOVA selector, paired vs unpaired t-test, repeated measures ANOVA, rank-biserial correlation, molecular biology statistics, bioinformatics statistical pipeline, Pepkio biostat navigator

biostatistics statistical test decision tree, how to choose statistical test for biology experiment, qPCR gene expression statistical significance test, non-parametric test for small sample size biology, Welch t-test vs Student t-test equal variance, automated assumption checking statistical software, Benjamini-Hochberg FDR correction calculator online, post-hoc pairwise comparison after ANOVA, effect size calculation for small biological replicates, Fisher exact test small cell count contingency table, repeated measures vs friedman test time series biological data, normality test for qPCR fold change data, how to calculate sample size for animal study power analysis
