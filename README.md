# 🔐 Managing Pipeline Secrets and Environment Variables

> **Task 14 — Secure Secret Management using GitHub Actions**

---

## 👥 Team Members

| Sl. No. | Name | SRN |
|:---:|---|---|
| 1 | **Nakshathira** | `PES2UG24AM096` |
| 2 | **Sharanya N.** | `PES2UG24AM150` |
| 3 | **Poojitha P.** | `PES2UG24AM112` |
| 4 | **Rahul Rajkumar S.** | `PES2UG24AM128` |

---

## 🎯 Objective

The objective of this task is to demonstrate how sensitive information such as API keys and access tokens can be securely injected into automated runtimes using **GitHub Repository Secrets** and **environment variables**, without exposing the sensitive information in plaintext code or workflow logs.

---

## 📌 Problem Statement

Sensitive credentials such as API keys, passwords, and access tokens should never be hard-coded inside source code or workflow files.

This project demonstrates the secure handling of a mock API key using:

- GitHub Repository Secrets
- GitHub Actions
- Environment Variables
- Python

The workflow retrieves the encrypted secret and makes it available to a Python script as an environment variable.

The Python script only checks whether the secret is present and **does not print the actual secret value**.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **GitHub** | Repository and secret management |
| **GitHub Actions** | Automated workflow execution |
| **YAML** | Workflow configuration |
| **Python** | Secret presence verification |
| **Environment Variables** | Securely passing the secret to the script |

---

## 📁 Project Structure

```text
github-secrets-demo/
│
├── .github/
│   └── workflows/
│       └── secret-check.yml
│
├── check_secret.py
│
└── README.md
