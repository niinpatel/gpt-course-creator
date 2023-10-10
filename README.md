# Course Creator

This project is about creating a course on any topic using OpenAI's GPT-3.5-turbo model. The course creation process is designed to be dynamic and adaptable to various topics. For example, you can create a course on "Building a GPT model from scratch". The course assumes prior knowledge of Python, data structures, and algorithms.

## Getting Started

To get started with this project, you need to have Python installed on your machine. You also need to install the OpenAI API. You can install it using pip:

```bash
pip install openai
```

## Usage

1. Set your OpenAI API key as an environment variable. You can do this in the terminal like so:

```bash
export OPENAI_API_KEY='your-api-key'
```

2. Run the `course-creator.py` script. You will need to provide the topic, guidelines, and prior knowledge assumed as inputs to the program. For example:

```bash
python course-creator.py --topic "Building a GPT model from scratch" --guidelines "A mostly hands on course where throughout the course ideally we work towards building something useful constantly & we learn concepts that help us build it." --prior_knowledge "Python, Data structures & algorithms"
```

3. The script will generate a `course_outline.json` file with the course outline. The course outline will be saved in the `outputs` directory.

## Generated Output

You can view a sample generated output [here](https://three-olive-ba9.notion.site/GPT-course-c1b150f7b5cd47c88c76bb883f94d5e8).

You can also see a different sample output in the repository in the [sample_outputs](./sample_outputs) directory.
