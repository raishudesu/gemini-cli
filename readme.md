# Gemini CLI Documentation

Welcome to the Gemini CLI! This documentation will guide you through the setup process to get started with the Gemini AI command line interface.

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.6 or higher installed on your machine.
- Basic knowledge of using the command line.

## Step 1: Clone the GitHub Repository

You can clone the Gemini CLI repository using the following command. Choose the appropriate repository based on your needs. Here are a couple of options:

### Clone from `raishudesu/gemini-cli`

```bash
git clone https://github.com/raishudesu/gemini-cli
```

## Step 2: Set Up a Python Environment

1. **Create a Virtual Environment** (optional but recommended):
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to create your project.
   - Run the following command to create a virtual environment:
     ```bash
     python -m venv gemini_cli_env
     ```
   - Activate the virtual environment:
     - On **Unix or MacOS**:
       ```bash
       source gemini_cli_env/bin/activate
       ```
     - On **Windows**:
       ```bash
       gemini_cli_env\Scripts\activate
       ```

## Step 3: Install Required Packages

1. **Install the packages** listed in `requirements.txt` by running:
   ```bash
   pip install -r requirements.txt
   ```

## Step 4: Set Up Your Gemini API Key

1. Obtain your Gemini API key from the [Google Cloud Console](https://console.cloud.google.com/).
2. Set the API key as an environment variable:
   - On **Unix or MacOS**:
     ```bash
     export GEMINI_API_KEY='your_api_key_here'
     ```
   - On **Windows**:
     ```bash
     set GEMINI_API_KEY='your_api_key_here'
     ```

## Step 5: Run the Gemini CLI

1. Make sure you are in the directory where your `gemini_cli.py` script is located.
2. Run the Python script using the following command:

   ```bash
   python gemini_cli.py
   ```

3. Start chatting with Gemini AI! Type your messages and press Enter. Type `exit` to end the conversation.

## Troubleshooting

- If you encounter any errors related to package installations, ensure that your Python and pip versions are up to date.
- If the API key is not recognized, double-check that you have set the environment variable correctly.

## Conclusion

You are now ready to use the Gemini CLI! Enjoy your conversations with Gemini AI. If you have any questions or need further assistance, feel free to reach out.
