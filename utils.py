import openai
import json


# Take in an input of "ingredients" and send them with pre-existing format to OpenAI's API
def grabRecipe(message, api_key):
    openai.api_key = api_key
    recipe_prompt = (
        "Here is a list of ingredients: \n\n"
        + message
        + "\n\n"
        + "Give me a list of 5 recipes that use these ingredients. Use ONLY the ingredients listed above. \n\n"
    )
    response = openai.Completion.create(
        engine="text-curie-001",  # using ada for now because of costs - we'll see how it goes
        prompt=recipe_prompt,
        temperature=0.5,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    first_generation = response.choices[0].text
    return first_generation


def grabInstructions(message, ingredients, api_key):
    openai.api_key = api_key
    ingredient_str = "\n".join(ingredients)
    instruction_prompt = (
        "Here is a recipe name: \n\n"
        + message
        + "\n\n"
        + "Give me a short, brief list of instructions for this recipe, with each instruction on a new line, and complete it within 250 tokens or less. \n\n"
        + "Here are the ingredients: \n\n"
        + ingredient_str
        + "\n\n"
        + "The recipe is considered completed when the final instruction is sent. Generate no more after that. \n\n"
    )
    response = openai.Completion.create(
        engine="text-curie-001",  # using ada for now because of costs - we'll see how it goes
        prompt=instruction_prompt,
        temperature=0.5,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    first_generation = response.choices[0].text
    return first_generation
