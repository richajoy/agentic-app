# Wikipedia Researcher Agent

This project defines a Researcher Agent that uses Wikipedia to look up information and report on the results. The agent is built using the `crew.ai` library and utilizes the `wikipedia-api` package to fetch data from Wikipedia.

## Prerequisites
- Python 3.6 or higher
- Conda (recommended for managing dependencies)

## Installation
1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
2. **Create and activate a Conda environment**:
   ```sh
    conda create --name wikipedia_agent python=3.8
    conda activate wikipedia_agent
3. **Install the required packages**:
   ```sh
   pip install crewai wikipedia-api

## Usage
1. **Set up the environment variable: Ensure you have your OpenAI API key set up in the environment variable OPENAI_API_KEY. You can set it in the script or export it in your terminal**:
   ```sh
   export OPENAI_API_KEY="your-openai-api-key"

2. **Run the script: Execute the script to start the agent**:
   ```sh
   python wikipedia.py

3. **Enter a query: When prompted, enter a query for the agent to look up on Wikipedia.**
   ```sh
   Enter a query: What's moore's law?

The agent will fetch the summary of the Wikipedia page for "Python programming language" and display it.
