---
title: BubbleSortCISC121
colorFrom: green
colorTo: yellow
sdk: gradio
sdk_version: 6.0.2
app_file: app.py
pinned: false
short_description: bubble sort
emoji: 📊
---
This project is a simple web app that shows the step-by-step process of the Bubble Sort algorithm.
It takes a list of numbers and displays each step of the sorting process so users can clearly inderstand how the algorithm works.

# How it works: 
1. User enters numbers separated by commas
2. The app runs Bubble Sort on provided numbers.
3. Every time two numbers are compared and swapped, the step is saved.
4. All steps are shown in the output box.

# Computational Thinking Breakdown
1. Decomposition:
   - input numbers
   - compare and swap
   - Save each step
   - Display result
2. Pattern Recognition:
   - Repeated comparison of adjacent values
   - Swapping when left > right
   - Fewer comparisons on each pass
3. Abstraction:
   - The user does not need to know how sorting works internally
   - They only provide input. The algorithm handles everything
4. Algorithm Design:
   - User enter numbers
   - Turn into a list of integers
   - Perform bubble Sort
   - Save the list after each pass
   - Display every step

# Steps to Run
Local Run: 
1. pip install gradio (to install gradio)
2. python app.py (to run the app)
3. A browse window will open automatically.

Using the app:
1. Type numbers separated by commas
2. Click "Run Sort"
3. The app will show each Bubble Sort step

# Hugging face link
https://huggingface.co/spaces/Seun1358/Bubble_Sort
# Author & Acknowledgment
Author: Saeeun Park
This project was created for the CISC121 Final Project.
