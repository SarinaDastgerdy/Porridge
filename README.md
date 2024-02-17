# Porridge

## Introduction

In the domain of computer security, safeguarding sensitive information against various forms of intrusion, including side-channel attacks, is paramount. Side-channel attacks exploit supplementary information obtained during the execution of computer protocols or algorithms, rather than inherent design flaws or implementation errors. Examples of such attacks include timing attacks and power-differential attacks, which capitalize on timing data and patterns of power consumption, respectively.

Porridge is an open-source library that offers two crucial functionalities: storing server-side secrets securely and providing an interface to the Argon2 password-hashing algorithm. One significant advantage of using Porridge is its ability to customize the time-cost parameter of Argon2. This feature allows developers to adjust the computational cost of hashing passwords, enhancing resistance against timing attacks. By fine-tuning the time-cost parameter, developers can mitigate the risk of adversaries exploiting timing discrepancies to deduce sensitive information.

## Description
This repository contains a Python script that leverages the capabilities of the Porridge library to facilitate secure password storage and verification. The script integrates seamlessly with Porridge, offering a user-friendly interface for storing and verifying passwords.

This code is written in Python and utilizes the Porridge library available at https://github.com/thusoy/porridge.

## Features
Secure Password Storage: Utilize Porridge to securely store passwords in a designated text file.
Password Verification: Verify stored passwords securely using Porridge.
Error Handling: Robust error handling mechanisms provide clear feedback and guidance in case of input format issues.
User-Friendly Interface: Intuitive commands and feedback messages ensure a smooth user experience.
