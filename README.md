# AI Text Generator

## Overview

AI Text Generator is a web-based text generation application built using Streamlit and Hugging Face Transformers. The application uses the EleutherAI GPT-Neo 125M pre-trained language model to generate meaningful text based on a user-provided prompt.

Users can enter a sentence or short prompt, and the application generates a continuation using natural language generation techniques.

## Features

* Simple and interactive web interface
* AI-based text generation
* Prompt-based text completion
* Uses a pre-trained GPT-Neo language model
* Adjustable text generation parameters
* Real-time text generation
* Built with Streamlit

## Technologies Used

* Python
* Streamlit
* Hugging Face Transformers
* PyTorch
* GPT-Neo 125M

## Model

The project uses:

**EleutherAI/gpt-neo-125M**

GPT-Neo is a transformer-based language model developed by EleutherAI and is designed for natural language generation tasks.

## Project Structure

```text
AI-Text-Generator/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd AI-Text-Generator
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install the dependencies manually:

```bash
pip install streamlit transformers torch
```

## Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your default web browser.

## Usage

1. Enter a sentence or prompt in the text input area.
2. Click the Generate Text button.
3. The GPT-Neo model processes the prompt.
4. The generated continuation is displayed on the application.

### Example

**Input:**

```text
Artificial Intelligence is
```

**Output:**

```text
Artificial Intelligence is transforming the way people interact with
technology by enabling machines to learn from data and perform
complex tasks efficiently.
```

The generated output may vary because the model uses probabilistic text generation.

## Generation Parameters

The application uses the following parameters:

| Parameter            | Value | Purpose                                    |
| -------------------- | ----: | ------------------------------------------ |
| max_new_tokens       |   400 | Maximum number of new tokens generated     |
| temperature          |   0.7 | Controls randomness                        |
| top_p                |   0.9 | Controls probability-based token selection |
| do_sample            |  True | Enables sampling-based generation          |
| num_return_sequences |     1 | Generates one output sequence              |

## Requirements

Create a `requirements.txt` file with:

```text
streamlit
transformers
torch
```

## Future Enhancements

* Add multiple language models
* Allow users to select generation length
* Add temperature and creativity controls
* Add text download functionality
* Add conversation history
* Improve user interface and accessibility
* Deploy the application using Streamlit Community Cloud

## Conclusion

This project demonstrates the implementation of an AI-powered text generation application using a pre-trained transformer language model. It provides a simple interface for understanding prompt-based text generation and integrating Hugging Face models with Streamlit.

## Author

Varalakshmi K
