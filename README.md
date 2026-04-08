# Lens Idea Ranking System

## Overview

This project is a command-line tool that helps evaluate and rank augmented reality (AR) lens ideas.

The goal was to simulate how a real product or engineering team might decide which ideas are worth building. Instead of guessing, the system uses a structured scoring approach based on multiple factors like creativity, engagement, and trend relevance.

## Features

- Add custom AR lens ideas through user input
- Interactive menu system for navigating the application
- Weighted scoring system
- Ranking using sorting algorithms
- Search functionality
- Filter high-scoring ideas
- Explainable insights for each idea

## How It Works

Each idea is evaluated across four categories:

- Creativity (1–10)
- Trend Relevance (1–10)
- Ease of Build (1–10)
- Engagement Potential (1–10)

Each category contributes differently to the final score:

- Engagement is weighted the highest
- Trend relevance is also important
- Creativity has moderate impact
- Ease of build has the least weight

This helps balance ideas that are exciting with ones that are actually realistic to build.

## User Flow

The program runs through a simple interactive menu system.

Users can:

1. Add new lens ideas by entering scores for each category
2. View ranked ideas based on the scoring system
3. Search for specific ideas by name
4. Filter ideas to see only high-scoring results
5. Exit the program

## Example Output

Idea: Focus Lens, Score: 83 → high engagement, strong trend relevance | Insight: High potential viral lens
