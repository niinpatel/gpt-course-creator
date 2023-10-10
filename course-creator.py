import json
import shutil
import openai
import os
import argparse


openai.api_key = os.getenv("OPENAI_API_KEY")

model = "gpt-3.5-turbo-16k"  # I still don't have GPT-4 API 😭😭


parser = argparse.ArgumentParser(description="Create a course outline.")
parser.add_argument("--topic", type=str, required=True, help="The topic of the course.")
parser.add_argument(
    "--guidelines", type=str, required=True, help="The guidelines for the course."
)
parser.add_argument(
    "--prior_knowledge_assumed",
    type=str,
    required=True,
    help="The prior knowledge assumed for the course.",
)

args = parser.parse_args()

topic = args.topic
guidelines = args.guidelines
prior_knowledge_assumed = args.prior_knowledge_assumed


def create_course_outline(topic, guidelines, prior_knowledge_assumed):
    systemPrompt = f"""
    Create a course outline for the topic given to you based on the provided guidelines. 

    Output format must be a json format. It contains, course title, course summary, modules, submodules & word count. 
    Note that the course can contain code examples & word count is excluding the code examples. 

    [
        "course_title": <course title>,
        "course_summary": <course summary>,
        "prior_knowledge_assumed": <prior knowledge assumed>,
        "modules": [
            {{"module_title": <module_title>, 
            "submodules": [
                {{"submodule_title": <submodule_title>, "submodule_summary": <submodule_summary>, "word_count": <word count num>}},
                {{"submodule_title": <submodule_title>, "submodule_summary": <submodule_summary>, "word_count": <word count num>}}
            ]}},
            {{...}},
            {{...}}
        ]
    ]
    """

    userPrompt = f"""
    Topic: {topic}. 

    Guidelines: {guidelines}

    Prior knowledge assumed: {prior_knowledge_assumed}.
    """

    print("Creating course outline...")

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": systemPrompt},
            {"role": "user", "content": userPrompt},
        ],
        temperature=1,
        max_tokens=8191,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    course_outline_string = response["choices"][0]["message"]["content"]

    print("Course outline created: ")
    print(course_outline_string)

    course_outline_json = json.loads(course_outline_string)

    try:
        assert "course_title" in course_outline_json
        assert "course_summary" in course_outline_json
        assert "prior_knowledge_assumed" in course_outline_json
        assert "modules" in course_outline_json
        for module in course_outline_json["modules"]:
            assert "module_title" in module
            assert "submodules" in module
            for submodule in module["submodules"]:
                assert "submodule_title" in submodule
                assert "submodule_summary" in submodule
                assert "word_count" in submodule
                assert isinstance(submodule["word_count"], int)
    except AssertionError:
        print("Invalid output_json format")
        exit(1)

    return course_outline_json


def save_course_outline(course_outline_json):
    with open("course_outline.json", "w") as json_file:
        json.dump(course_outline_json, json_file)

    print("Course outline successfully saved to course_outline.json")


def create_course(course_outline_json):
    systemPrompt = f"""
    Course outline: 
    ```
    {json.dumps(course_outline_json)}
    ```

    From the above course outline, you will be given a single submodule title. 

    You will generate the content for that submodule that will fit inside the course. 

    Try to follow the word count mentioned in the course outline. The content may contain code examples. The word count is excluding any code examples the content may generate.

    Output will be the content in markdown format.
    """

    for module_index, module in enumerate(course_outline_json["modules"]):
        for submodule_index, submodule in enumerate(module["submodules"]):
            print(f"Generating content for submodule: {submodule['submodule_title']}")
            userPrompt = submodule["submodule_title"]
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": systemPrompt},
                    {"role": "user", "content": userPrompt},
                ],
                temperature=1,
                max_tokens=8191,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            submodule_content = response["choices"][0]["message"]["content"]

            module["submodules"][submodule_index]["content"] = submodule_content

    submodule_count = 0
    try:
        for module in course_outline_json["modules"]:
            for submodule in module["submodules"]:
                assert "content" in submodule
                submodule_count += 1
    except AssertionError:
        print("Content missing in one or more submodules")
        exit(1)

    print(f"Content generated for {submodule_count} submodules.")


def save_course_to_files(course_outline_json):
    print("Now saving the content to individual markdown files...")

    if os.path.exists("outputs"):
        shutil.rmtree("outputs")

    for module_index, module in enumerate(course_outline_json["modules"]):
        for submodule_index, submodule in enumerate(module["submodules"]):
            directory = f"outputs/{module_index} {module['module_title']}"
            os.makedirs(directory, exist_ok=True)
            with open(
                f"{directory}/{submodule_index} {submodule['submodule_title']}.md", "w"
            ) as md_file:
                md_file.write(submodule["content"])

    print("Markdown files successfully created.")


course_outline_json = create_course_outline(topic, guidelines, prior_knowledge_assumed)
save_course_outline(course_outline_json)
create_course(course_outline_json)
save_course_to_files(course_outline_json)
