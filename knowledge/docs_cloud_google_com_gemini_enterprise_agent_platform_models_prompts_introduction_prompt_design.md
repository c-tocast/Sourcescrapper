# Fuente original: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/introduction-prompt-design

Introduction to prompting  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation
Skip to main content
/
Console
English
Deutsch
Español – América Latina
Français
Indonesia
Italiano
Português – Brasil
עברית
中文 – 简体
中文 – 繁體
日本語
한국어
Sign in
Gemini Enterprise Agent Platform
Start free
Home
Documentation
AI and ML
Gemini Enterprise Agent Platform
Models
Send feedback
Introduction to prompting
Stay organized with collections
Save and categorize content based on your preferences.
This page introduces some basic concepts to get you started in designing prompts. A prompt is a
natural language request submitted to a language model to receive a response back. Prompts can
contain questions, instructions, contextual information, few-shot examples, and partial input for
the model to complete or continue. After the model receives a prompt, depending on the type of model
being used, it can generate text, embeddings, code, images, videos, music, and more.
What is prompt design and prompt engineering
Prompt design
is the process of creating prompts that elicit the desired response from
language models. Writing well structured prompts can be an essential part of ensuring accurate, high
quality responses from a language model. The iterative process of repeatedly updating prompts and
assessing the model's responses is sometimes called
prompt engineering
.
Gemini models often perform well without the need for prompt engineering, especially for
straightforward tasks. However, for complex tasks, effective prompt engineering still plays an
important role.
Components of a prompt
You can include whatever information you want in a prompt that you think is important for the
task at hand. Generally, prompt content fall within one of the following components:
Task (required)
System instructions (optional)
Few-shot examples (optional)
Contextual information (optional)
Task
A task is the text in the prompt that you want the model to provide a response for. Tasks are
generally provided by a user and can be a question or some instructions on what to do.
Example question task:
Prompt:
What are the colors in the rainbow?
Response:
A rainbow has seven colors: red, orange, yellow, green, blue, indigo, and violet. These colors
are always in the same order, which is determined by the way light is refracted and dispersed
by water droplets in the air. This order is sometimes remembered by the acronym ROYGBIV. The
wavelengths of the colors in a rainbow range from the longest (red) to the shortest (violet).
Example instruction task:
Prompt:
Write a one-stanza poem about Captain Barktholomew, the most feared pirate dog of the seven seas.
Response:
Captain Barktholomew, with patch and with peg,
The terror of parrots, the bane of each keg.
His bark is a cutlass, his bite is a storm,
He'll plunder your biscuits and leave you forlorn.
System instructions
System instructions are instructions that get passed to the model before any
user input in the prompt. You can add system instructions in the dedicated
systemInstruction
parameter.
In the following example, system instructions are used to dictate the style and tone of the
model, while adding constraints to what it can and can't talk about:
System:
You are Captain Barktholomew, the most feared pirate dog of the seven seas. You are from the
1700s and have no knowledge of anything after that time. You only talk about topics related to
being a pirate. End every message with "woof!"
Prompt:
Hello! Who might you be?
Response:
Avast there! You can call me Captain Barktholomew, the scourge of the seven seas!
I'm a terror to landlubbers, a plunderer of the highest order, and a fearsome pirate of the
deepest blue! I sail the seas in search of treasure and adventure, leaving a trail of
laughter and dog biscuits in my wake! Don't let my fuzzy exterior fool you - I'm a cunning
captain with a nose for treasure and a heart for adventure!
Now, if you'll excuse me, I must away! There's a ship on the horizon, and it looks like they're
carrying a chest full of dubloons! Yo ho ho, and a bottle of rum! Woof!
To learn more about configuring system instructions, see
System instructions
.
Few-shot examples
Few-shot examples are examples that you include in a prompt to show the model what getting it
right looks like. Few-shot examples are especially effective at dictating the style and tone of the
response and for customizing the model's behavior.
Prompt:
Classify the following as red wine or white wine:
<examples>
Name: Chardonnay
Type: White wine
Name: Cabernet
Type: Red wine
Name: Moscato
Type: White wine
</examples>
Name: Riesling
Type:
Response:
White wine
Contextual information
Contextual information, or context, is information that you include in the prompt that the model
uses or references when generating a response. You can include contextual information in different
formats, like tables or text.
Prompt:
| Marble color | Number of marbles |
| ------------ | ----------------- |
| Red          | 12                |
| Blue         | 28                |
| Yellow       | 15                |
| Green        | 17                |
How many green marbles are there?
Response:
There are 17 green marbles.
Safety and fallback responses
There are a few use cases where the model is not expected to fulfill the user's requests.
Particularly, when the prompt is encouraging a response that is not aligned with Google's values or
policies, the model might refuse to respond and provide a fallback response.
Here are a few cases where the model is likely to refuse to respond:
Hate Speech:
Prompts with negative or harmful content targeting identity and/or protected attributes.
Harassment:
Malicious, intimidating, bullying, or abusive prompts targeting another individual.
Sexually Explicit:
Prompts that contains references to sexual acts or other lewd content.
Dangerous Content:
Prompts that promote or enable access to harmful goods, services, and activities.
Task-specific guidance
To learn about task-specific guidance for common use cases check out the
following pages:
Multimodal prompts
Overview of prompting strategies
Chat prompts
What's next
Learn about
prompting strategies
.
Explore more examples of prompts in the
Prompt gallery
.
Learn how to optimize prompts for use with
Google models
by using the
Gemini Enterprise Agent Platform prompt optimizer (Preview)
.
Learn about
saving and sharing prompts
Send feedback
Except as otherwise noted, the content of this page is licensed under the
Creative Commons Attribution 4.0 License
, and code samples are licensed under the
Apache 2.0 License
. For details, see the
Google Developers Site Policies
. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-07-28 UTC.