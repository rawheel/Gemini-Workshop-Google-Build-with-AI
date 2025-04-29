# Getting a Gemini API Key

To use this application, you'll need a Google API key that has access to the Gemini API. Follow these steps to get your key:

## Step 1: Go to Google AI Studio

Visit [Google AI Studio](https://makersuite.google.com/) and sign in with your Google account.

## Step 2: Get an API Key

1. In the left sidebar, click on "Get API key"
2. If you already have an API key, it will be displayed
3. If not, click "Create API key" to generate a new one
4. Copy your API key to use in the application

## Step 3: Add the API Key to Your Project

1. Create a file named `.env` in the root directory of this project
2. Add your API key to the file:

```
GOOGLE_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

## Step 4: Keep Your API Key Safe

- Never commit your `.env` file to version control
- Don't share your API key publicly
- If you suspect your key has been compromised, generate a new one in the Google AI Studio

## API Quotas and Limitations

- The Gemini API has usage quotas based on your Google account
- Free tier users have limited requests per minute and per day
- Monitor your usage in the Google AI Studio dashboard
- For production use, consider upgrading to a paid tier

## Troubleshooting

If you encounter errors like "API key not valid" or "Quota exceeded", try the following:

1. Verify your API key is correct in the `.env` file
2. Check your API quota usage in the Google AI Studio
3. Generate a new API key if necessary 