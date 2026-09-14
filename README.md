# Cloud-Native Fraud Detection Analytics Pipeline

## Project Overview

This project demonstrates an end-to-end **cloud-native fraud detection analytics pipeline** for analyzing financial transaction data.

The pipeline takes transaction data through multiple stages:

**Raw CSV → Python/Pandas → Data Cleaning → BigQuery → SQL Analysis → Power BI Dashboard → Business Insights**

The objective is to identify transaction patterns, analyze potentially fraudulent transactions, and provide actionable insights through an interactive dashboard.

---

## Architecture

```text
Financial Transaction Data
          ↓
       Raw CSV
          ↓
    Python + Pandas
          ↓
     Data Cleaning
          ↓
     Cleaned CSV
          ↓
     Google BigQuery
          ↓
      GoogleSQL
          ↓
   Power BI Dashboard
          ↓
   Business Insights