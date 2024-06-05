# Project Plan

## Title
<!-- Give your project a short title. -->
Correlation Analysis between Deforestation and CO2 Emissions by Country

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. How do deforestation rates (Net forest conversion) correlate with CO2 emissions in various countries?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Understanding the relationship between deforestation and CO2 emissions is critical for developing effective climate policies and mitigating climate change impacts. This project aims to analyze the correlation between net forest conversion (deforestation rates) and CO2 emissions by country.

We will use two comprehensive datasets for this analysis. The first dataset provides information on the net change in forest area, which measures forest expansion minus deforestation, for various countries over the years 1990, 2000, 2010, and 2015. The second dataset offers a detailed overview of CO2 emissions by country from 1960 to the present day, covering data from multiple sources such as the UNFCCC and the IEA.

By leveraging statistical techniques, we aim to uncover significant relationships between deforestation rates and CO2 emissions. The findings will provide valuable insights for researchers, policymakers, and environmentalists working on climate action and forest conservation.

## Datasources

<!-- Describe each datasource you plan to use in a section. Use the prefix "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Deforestation and Forest Loss
* Metadata URL: [https://www.kaggle.com/datasets/chiticariucristian/deforestation-and-forest-loss]
* Data URL: [Kaggle](https://www.kaggle.com/datasets/chiticariucristian/deforestation-and-forest-loss)
* Data Type: CSV

#### Description:
Net change in forest area measures forest expansion (either through afforestation or natural expansion) minus deforestation. The dataset includes the following features:
- Entity (Country)
- Code (Country Code)
- Year (4 unique values for each country: 1990, 2000, 2010, 2015)
- Net forest conversion (Net change in forest area measures forest expansion)

### Datasource2: CO2 Emissions by Country
* Metadata URL: [https://www.kaggle.com/datasets/ulrikthygepedersen/co2-emissions-by-country]
* Data URL: [Kaggle](https://www.kaggle.com/datasets/ulrikthygepedersen/co2-emissions-by-country)
* Data Type: CSV

#### Description:
The CO2 emissions dataset provides a comprehensive overview of the amount of CO2 emitted by each country. It includes information on CO2 emissions by country from 1960 to the present day. The dataset covers all countries in the world and is compiled from various sources, including the United Nations Framework Convention on Climate Change (UNFCCC) and the International Energy Agency (IEA).

This dataset can be used to monitor changes in emissions over time and to assess the effectiveness of climate policies.

## Work Packages

1. Data Acquisition and Cleaning [#1][i1]
2. Exploratory Data Analysis [#2][i2]
3. Data Integration [#3][i3]
4. Conclusion and Insights [#4][i4]
5. Report Writing and Visualization [#5][i5]

[i1]: https://github.com/Nasimattar/made-ns/issues/1
[i2]: https://github.com/Nasimattar/made-ns/issues/2
[i3]: https://github.com/Nasimattar/made-ns/issues/3
[i4]: https://github.com/Nasimattar/made-ns/issues/4
[i5]: https://github.com/Nasimattar/made-ns/issues/5
